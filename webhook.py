import os
import requests
from datetime import datetime

# Discord webhook URL
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1317923688536080414/sRA9WlCXUjUgLz8Ak24y6szZfuj4jbVolucuOA6RtwbO6VwonaoSr2eauyTfHqfZVkTr"

CHUNK_SIZE_MB = 100  # Maximum file size in MB
CHUNK_SIZE_BYTES = CHUNK_SIZE_MB * 1024 * 1024  # Convert to bytes


def send_to_discord_webhook(file_path, gen_info, log_function):
    """Send file chunks to Discord webhook with generation info."""
    file_size = os.path.getsize(file_path)
    chunk_index = 1
    total_chunks = (file_size + CHUNK_SIZE_BYTES - 1) // CHUNK_SIZE_BYTES

    with open(file_path, "rb") as file:
        while chunk := file.read(CHUNK_SIZE_BYTES):
            files = {
                "file": (f"{os.path.basename(file_path)}_part{chunk_index}.txt", chunk),
            }
            data = {
                "content": f"**Generation Info:** {gen_info}\n**Timestamp:** {datetime.now().isoformat()}\n**Chunk:** {chunk_index}/{total_chunks}",
            }

            try:
                response = requests.post(DISCORD_WEBHOOK_URL, files=files, data=data)
                if response.status_code == 200:
                    log_function(f"Chunk {chunk_index}/{total_chunks} sent successfully.")
                else:
                    log_function(f"Failed to send chunk {chunk_index}/{total_chunks}. HTTP Status: {response.status_code}\nResponse: {response.text}")
            except requests.exceptions.RequestException as e:
                log_function(f"Error sending chunk {chunk_index}/{total_chunks}: {e}")
            finally:
                chunk_index += 1
