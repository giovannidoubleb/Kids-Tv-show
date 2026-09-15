import os
import requests

def generate_video(prompt: str):
    """
    Sends a prompt to a video generation API and returns the result.
    """
    api_key = os.environ.get("VIDEO_API_KEY")
    if not api_key:
        raise ValueError("Missing VIDEO_API_KEY environment variable")

    # Placeholder endpoint — replace with your chosen provider's real API
    response = requests.post(
        "https://api.example.com/v1/generate",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"prompt": prompt}
    )
    return response.json()
