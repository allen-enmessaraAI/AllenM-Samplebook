import re
import requests


def _extract_doc_id(url: str) -> str:
    """Pull the document ID out of a Google Docs URL."""
    match = re.search(r'/document/d/([a-zA-Z0-9_-]+)', url)
    if not match:
        raise ValueError(f"Could not find document ID in URL: {url}")
    return match.group(1)


def fetch_script(source: str) -> str:
    """
    Fetch script text from a Google Docs URL or a local file path.
    Google Doc must be shared as 'Anyone with the link can view'.
    """
    if source.startswith("http"):
        doc_id = _extract_doc_id(source)
        export_url = f"https://docs.google.com/document/d/{doc_id}/export?format=txt"
        response = requests.get(export_url)
        if response.status_code == 403:
            raise PermissionError(
                "Google Doc is not publicly accessible. "
                "Share it with 'Anyone with the link can view' and try again."
            )
        response.raise_for_status()
        return response.text.strip()
    else:
        with open(source, "r") as f:
            return f.read().strip()
