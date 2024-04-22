import os

def createfNOtExist(folder):

    if not os.path.exists(folder):
        os.makedirs(folder)

def movefiles (foldername,files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")



files = os.listdir()
createfNOtExist("Docs")
createfNOtExist("Media")
createfNOtExist("Others")

imgExts =[ ".png",".jpg",".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
print(images)


docExts =[ ".txt",".doc",".pdf"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
print(docs)

mediaExts =[ ".mp4" , ".mp3",".flv"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
print(medias)

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts):
        others.append(file)
print(others)


movefiles("Images",images)
movefiles("Docs",docs)
movefiles('Media',medias)





