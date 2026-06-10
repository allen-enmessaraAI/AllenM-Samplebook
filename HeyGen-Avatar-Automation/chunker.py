import re

WORDS_PER_CHUNK = 120  # ~50-55 seconds at ~130 wpm average speaking pace


def chunk_script(text: str) -> list[str]:
    """Split script into sentence-boundary chunks of ~120 words each."""
    text = text.strip()
    sentences = re.split(r'(?<=[.!?])\s+', text)

    chunks = []
    current_chunk = []
    current_word_count = 0

    for sentence in sentences:
        word_count = len(sentence.split())
        if current_word_count + word_count > WORDS_PER_CHUNK and current_chunk:
            chunks.append(' '.join(current_chunk))
            current_chunk = [sentence]
            current_word_count = word_count
        else:
            current_chunk.append(sentence)
            current_word_count += word_count

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
