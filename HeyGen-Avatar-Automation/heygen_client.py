import requests
import time
import os


HEYGEN_API_KEY = os.getenv("HEYGEN_API_KEY")
HEYGEN_AVATAR_ID = os.getenv("HEYGEN_AVATAR_ID")

UPLOAD_URL = "https://upload.heygen.com/v1/asset"
GENERATE_URL = "https://api.heygen.com/v2/video/generate"
STATUS_URL = "https://api.heygen.com/v1/video_status.get"

POLL_INTERVAL = 15  # seconds between status checks


def upload_audio(audio_path: str) -> str:
    """Upload an audio file to HeyGen and return the asset ID."""
    headers = {
        "X-Api-Key": HEYGEN_API_KEY,
        "Content-Type": "audio/mpeg"
    }
    with open(audio_path, "rb") as f:
        response = requests.post(UPLOAD_URL, data=f, headers=headers)
    response.raise_for_status()
    asset_id = response.json()["data"]["id"]
    print(f"  [HeyGen] Uploaded audio asset: {asset_id}")
    return asset_id


def generate_video(audio_asset_id: str) -> str:
    """Submit a video generation job and return the video ID."""
    headers = {
        "X-Api-Key": HEYGEN_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "video_inputs": [{
            "character": {
                "type": "avatar",
                "avatar_id": HEYGEN_AVATAR_ID,
                "avatar_style": "normal"
            },
            "voice": {
                "type": "audio",
                "audio_asset_id": audio_asset_id
            }
        }],
        "dimension": {"width": 1280, "height": 720}
    }
    response = requests.post(GENERATE_URL, json=payload, headers=headers)
    response.raise_for_status()
    video_id = response.json()["data"]["video_id"]
    print(f"  [HeyGen] Video job submitted: {video_id}")
    return video_id


def wait_for_video(video_id: str) -> str:
    """Poll until video is ready, then return the download URL."""
    headers = {"X-Api-Key": HEYGEN_API_KEY}
    print(f"  [HeyGen] Waiting for video {video_id}...", end="", flush=True)
    while True:
        response = requests.get(f"{STATUS_URL}?video_id={video_id}", headers=headers)
        response.raise_for_status()
        data = response.json()["data"]
        status = data["status"]
        if status == "completed":
            print(" done.")
            return data["video_url"]
        elif status == "failed":
            raise RuntimeError(f"HeyGen video generation failed: {data.get('error')}")
        print(".", end="", flush=True)
        time.sleep(POLL_INTERVAL)


def download_video(video_url: str, output_path: str) -> str:
    """Download a video from URL to output_path. Returns path."""
    response = requests.get(video_url, stream=True)
    response.raise_for_status()
    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"  [HeyGen] Downloaded: {os.path.basename(output_path)}")
    return output_path
