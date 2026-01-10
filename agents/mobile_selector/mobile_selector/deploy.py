from huggingface_hub import HfApi
import os

# Initialize the API
api = HfApi()

repo_id = "alaa-gamal/mobile_selector"
print(f"Uploading to {repo_id}...")

try:
    api.upload_folder(
        folder_path=".",
        repo_id=repo_id,
        repo_type="space",
        # Explicitly ignore heavy folders
        ignore_patterns=["pyproject.toml",".venv", ".venv/*", "output", "output/*", "logs", "logs/*", "*.db", "chroma_db_data", "chroma_db_data/*", "models", "models/*", "__pycache__", "*.pyc", ".git", ".env"]
    )
    print("✅ Upload complete! Your Space should be building now.")
    print(f"View it here: https://huggingface.co/spaces/{repo_id}")
except Exception as e:
    print(f"❌ Upload failed: {e}")
