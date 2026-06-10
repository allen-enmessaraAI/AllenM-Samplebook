import requests
import os


ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")

TTS_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"

VOICE_SETTINGS = {
    "stability": 0.5,
    "similarity_boost": 0.85,
    "style": 0.2,
    "use_speaker_boost": True
}


def generate_audio(text: str, output_path: str) -> str:
    """Generate audio from text via ElevenLabs and save to output_path. Returns path."""
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "model_id": "eleven_turbo_v2_5",
        "voice_settings": VOICE_SETTINGS
    }

    response = requests.post(TTS_URL, json=payload, headers=headers)
    response.raise_for_status()

    with open(output_path, "wb") as f:
        f.write(response.content)

    print(f"  [ElevenLabs] Saved audio: {os.path.basename(output_path)}")
    return output_path
