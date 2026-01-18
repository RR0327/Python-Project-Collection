import os
import shutil
from datetime import datetime

# ==========================
# CONFIGURATION
# ==========================
DOWNLOADS_DIR = os.path.join(os.path.expanduser("~"), "Downloads")
LOG_FILE = "organizer.log"

# File categories
FILE_TYPES = {
    "PDF": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "ZIP": [".zip", ".rar", ".7z"],
    "Documents": [".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
}


# ==========================
# LOGGING FUNCTION
# ==========================
def log_activity(message):
    with open(LOG_FILE, "a") as log:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{time}] {message}\n")


# ==========================
# ORGANIZER FUNCTION
# ==========================
def organize_downloads():
    if not os.path.exists(DOWNLOADS_DIR):
        print("Downloads folder not found.")
        return

    for file in os.listdir(DOWNLOADS_DIR):
        file_path = os.path.join(DOWNLOADS_DIR, file)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()

            for folder, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    target_folder = os.path.join(DOWNLOADS_DIR, folder)

                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, target_folder)

                    log_activity(f"Moved '{file}' to '{folder}' folder")
                    break


# ==========================
# MAIN EXECUTION
# ==========================
if __name__ == "__main__":
    organize_downloads()
    print("Downloads folder organized successfully.")
