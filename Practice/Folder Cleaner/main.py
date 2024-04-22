import os

def createfNOtExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def movefiles(foldername, files):
    for file in files:
        os.replace(f"FolderCleaner/{file}", f"{foldername}/{file}")

folder_path = "FolderCleaner"

# Remove the main script file from the list
files = [file for file in os.listdir(folder_path) if file != "main.py"]

print(files)

# Create necessary folders inside "FolderCleaner"
createfNOtExist(f"{folder_path}/Images")
createfNOtExist(f"{folder_path}/Docs")
createfNOtExist(f"{folder_path}/Media")
createfNOtExist(f"{folder_path}/Others")

imgExts = [".png", ".jpg", ".jpeg"]
docExts = [".txt", ".doc", ".pdf"]
mediaExts = [".mp4", ".mp3", ".flv"]

images = []
docs = []
medias = []
others = []

for file in files:
    ext = os.path.splitext(file)[1].lower()
    if ext in imgExts:
        images.append(file)
    elif ext in docExts:
        docs.append(file)
    elif ext in mediaExts:
        medias.append(file)
    elif os.path.isfile(f"FolderCleaner/{file}"):  # Check if the item is a file
        others.append(file)

print(images)
print(docs)
print(medias)
print(others)

# Move files to appropriate folders inside "FolderCleaner"
movefiles(f"{folder_path}/Images", images)
movefiles(f"{folder_path}/Docs", docs)
movefiles(f"{folder_path}/Media", medias)
movefiles(f"{folder_path}/Others", others)
