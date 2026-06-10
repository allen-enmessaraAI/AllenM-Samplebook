#!/usr/bin/env python3
"""
Script-to-Video Pipeline
Usage:
  python3 main.py <google_doc_url_or_txt_file> [project_name]

Examples:
  python3 main.py "https://docs.google.com/document/d/XXXX/edit" "Lesson 1"
  python3 main.py my_script.txt "Promo Video"
"""

import os
import sys
import subprocess
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

from chunker import chunk_script
from elevenlabs_client import generate_audio
from heygen_client import upload_audio, generate_video, wait_for_video, download_video
from gdocs_client import fetch_script

OUTPUT_BASE = os.getenv("OUTPUT_DIR", str(Path.home() / "HeyGen Automations"))


def stitch_videos(video_paths: list[str], output_path: str):
    """Concatenate video clips into a single final video using ffmpeg."""
    list_file = output_path.replace(".mp4", "_list.txt")
    with open(list_file, "w") as f:
        for p in video_paths:
            f.write(f"file '{p}'\n")
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file, "-c", "copy", output_path],
        check=True, capture_output=True
    )
    os.remove(list_file)
    print(f"\n[Done] Final video: {output_path}")


def run(source: str, project_name: str):
    project_dir = Path(OUTPUT_BASE) / project_name
    audio_dir = project_dir / "audio"
    video_dir = project_dir / "clips"
    audio_dir.mkdir(parents=True, exist_ok=True)
    video_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n=== Script-to-Video: {project_name} ===\n")

    # 1. Fetch script
    print(f"[1/4] Fetching script from: {source}")
    script = fetch_script(source)
    (project_dir / "script.txt").write_text(script)
    print(f"      {len(script.split())} words total")

    # 2. Chunk script
    print("\n[2/4] Chunking script...")
    chunks = chunk_script(script)
    print(f"      {len(chunks)} chunks created")
    for i, chunk in enumerate(chunks, 1):
        print(f"      Chunk {i}: {len(chunk.split())} words")

    # 3. Generate audio (ElevenLabs) + video (HeyGen) per chunk
    print("\n[3/4] Generating audio and avatar videos...")
    video_paths = []
    video_ids = []

    # Submit all jobs first, then wait — faster overall
    jobs = []
    for i, chunk in enumerate(chunks, 1):
        print(f"\n  --- Chunk {i}/{len(chunks)} ---")
        audio_path = str(audio_dir / f"chunk_{i:03d}.mp3")
        generate_audio(chunk, audio_path)
        asset_id = upload_audio(audio_path)
        video_id = generate_video(asset_id)
        video_path = str(video_dir / f"clip_{i:03d}.mp4")
        jobs.append((video_id, video_path))

    print("\n  Waiting for all HeyGen renders to complete...")
    for video_id, video_path in jobs:
        video_url = wait_for_video(video_id)
        download_video(video_url, video_path)
        video_paths.append(video_path)

    # 4. Stitch everything together
    print("\n[4/4] Stitching clips into final video...")
    final_path = str(project_dir / f"{project_name}.mp4")
    stitch_videos(video_paths, final_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    source = sys.argv[1]
    project_name = sys.argv[2] if len(sys.argv) > 2 else Path(source).stem

    run(source, project_name)
