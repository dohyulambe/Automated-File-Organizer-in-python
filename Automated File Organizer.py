import os
import shutil

# Prompt the user to input the folder path
folder_path = input("Enter the path to the folder you want to organize: ").strip()

# Validate the input path
if not os.path.exists(folder_path):
    print("The provided path does not exist. Please check and try again.")
    exit()

# Proceed with the rest of the script
print(f"Organizing files in: {folder_path}")

# Dictionary of folder names and file extensions
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".exe", ".msi"],
    "Others": []
}

# Create folders if not exist
for folder in file_types:
    folder_name = os.path.join(folder_path, folder)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Move files to their respective folders
files_moved = 0
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Skip directories and hidden/system files
    if os.path.isdir(file_path) or filename.startswith('.'):
        continue

    file_ext = os.path.splitext(filename)[1].lower()
    file_moved = False

    for folder, extensions in file_types.items():
        if file_ext in extensions:
            src = file_path
            dest = os.path.join(folder_path, folder, filename)
            try:
                shutil.move(src, dest)
                files_moved += 1
                print(f"Moved: {filename} -> {folder}")
            except Exception as e:
                print(f"Error moving {filename}: {e}")
            file_moved = True
            break

    # Move unknown types to "Others"
    if not file_moved and os.path.isfile(file_path):
        try:
            shutil.move(file_path, os.path.join(folder_path, "Others", filename))
            files_moved += 1
            print(f"Moved: {filename} -> Others")
        except Exception as e:
            print(f"Error moving {filename}: {e}")

if files_moved == 0:
    print("No files were moved. The folder might be empty or contain unsupported file types.")
else:
    print(f"Files organized successfully! Total files moved: {files_moved}")