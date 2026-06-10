---
name: heygen-video
description: >
  Runs the HeyGen Avatar Automation pipeline to produce a finished avatar video from a script.
  Use this skill any time the user wants to generate an avatar video, turn a script into a video,
  run the video pipeline, produce course content or training videos, or mentions HeyGen, ElevenLabs,
  or the script-to-video workflow. Trigger even if the user phrases it casually — e.g. "make a video
  from this", "run the pipeline on my script", "generate a video for lesson 3", or "process this doc".
---

# HeyGen Avatar Automation

## What this does
Takes a script (from a Google Doc URL or a local `.txt` file) and runs it through a three-stage pipeline:
1. **ElevenLabs** — clones your voice and generates audio for each ~45–55 second chunk
2. **HeyGen** — renders avatar video for each audio chunk
3. **ffmpeg** — stitches all clips into one final `.mp4`

Output lands in: `<OUTPUT_DIR>/<project_name>/`

## Pipeline location
```
./main.py
```

## How to run

### Step 1 — Collect inputs
You need two things from the user:
- **source**: a Google Doc URL *or* a local `.txt` file path
  - Google Doc must be shared as "Anyone with the link can view"
  - Local file can be any plain text file with the script content
- **project_name**: a short descriptive name for this video (used for the output folder and final filename)

If either is missing from the user's message, ask for it before proceeding.

### Step 2 — Run the pipeline
```bash
cd "<repo>/HeyGen-Avatar-Automation" && \
python3 main.py "<source>" "<project_name>"
```

Stream the output so the user can see progress. The pipeline prints stage-by-stage updates:
- Chunk count and word counts
- ElevenLabs audio generation per chunk
- HeyGen job submission and polling
- Final stitch confirmation with output path

### Step 3 — Report completion
When done, tell the user:
- The final video path: `<OUTPUT_DIR>/<project_name>/<project_name>.mp4`
- How many chunks were processed
- Any errors encountered

## Handling errors

| Error | Fix |
|-------|-----|
| Google Doc returns 403 | Ask user to set sharing to "Anyone with the link can view" |
| ElevenLabs 401/403 | API key may be expired — check `.env` |
| HeyGen job fails | Check HeyGen dashboard for quota; Avatar API generation may be rate-limited |
| ffmpeg not found | Run `brew install ffmpeg` |

## Notes
- Each ~10-minute script generates roughly 10–12 chunks and takes 5–15 minutes end-to-end
- HeyGen renders run in parallel (all jobs submitted first, then polled together)
- The `.env` file at the pipeline root holds all API keys — never expose it
