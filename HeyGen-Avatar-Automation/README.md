# HeyGen Avatar Automation

Automated pipeline that takes a written script and produces a finished avatar video — no manual recording, no editing. Powered by ElevenLabs (voice cloning), HeyGen (avatar video generation), and ffmpeg (final stitch).

## How it works

1. **Fetch** — pulls script from a Google Doc URL or local `.txt` file
2. **Chunk** — splits the script at sentence boundaries into ~45–55 second segments (~120 words each)
3. **Audio** — sends each chunk to ElevenLabs for voice clone synthesis
4. **Avatar** — uploads each audio file to HeyGen, generates an avatar video per chunk
5. **Stitch** — concatenates all clips into one final `.mp4` via ffmpeg

## Prerequisites

- Python 3.10+
- ffmpeg installed (`brew install ffmpeg`)
- ElevenLabs account with a Professional Voice Clone
- HeyGen account with an Avatar created
- A `.env` file (see setup below)

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure environment

Copy the example below into a `.env` file in this directory:

```env
ELEVENLABS_API_KEY=your_elevenlabs_api_key
ELEVENLABS_VOICE_ID=your_voice_clone_id
HEYGEN_API_KEY=your_heygen_api_key
HEYGEN_AVATAR_ID=your_avatar_id
OUTPUT_DIR=/path/to/HeyGen Automations
```

To find your HeyGen Avatar ID, run:

```bash
curl -s -X GET "https://api.heygen.com/v2/avatars" \
  -H "X-Api-Key: YOUR_HEYGEN_API_KEY" | python3 -m json.tool | grep avatar_id
```

## Running the pipeline

```bash
# From a Google Doc (must be shared "Anyone with the link can view")
python3 main.py "https://docs.google.com/document/d/YOUR_DOC_ID/edit" "Project Name"

# From a local text file
python3 main.py my_script.txt "Project Name"
```

### Output

Each run creates a folder inside your configured `OUTPUT_DIR`:

```
HeyGen Automations/
└── Project Name/
    ├── script.txt         # raw fetched script
    ├── audio/
    │   ├── chunk_001.mp3
    │   ├── chunk_002.mp3
    │   └── ...
    ├── clips/
    │   ├── clip_001.mp4
    │   ├── clip_002.mp4
    │   └── ...
    └── Project Name.mp4   # final stitched video
```

## Project structure

| File | Purpose |
|------|---------|
| `main.py` | Orchestrates the full pipeline end-to-end |
| `chunker.py` | Splits script at sentence boundaries |
| `elevenlabs_client.py` | ElevenLabs TTS API wrapper |
| `heygen_client.py` | HeyGen upload, generate, poll, and download |
| `gdocs_client.py` | Fetches script from Google Doc URL or local file |
| `requirements.txt` | Python dependencies |

## Tuning

- **Chunk size** — adjust `WORDS_PER_CHUNK` in `chunker.py` (default: 120 words ≈ 50s)
- **Voice settings** — adjust `VOICE_SETTINGS` in `elevenlabs_client.py` (stability, similarity, style)
- **Video resolution** — adjust `dimension` in `heygen_client.py` (default: 1280×720)

---

## Next phase: End-to-end testing

The immediate next step is running the full pipeline against a real script to validate each stage:

- [ ] Test Google Doc fetch with a publicly shared doc
- [ ] Verify ElevenLabs audio quality and chunk timing (~45–55s per clip)
- [ ] Confirm HeyGen avatar generation completes successfully via API
- [ ] Validate final stitched video plays back seamlessly with no visible cut points
- [ ] Tune `VOICE_SETTINGS` and `WORDS_PER_CHUNK` based on output quality
