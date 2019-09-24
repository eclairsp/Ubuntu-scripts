import os
import time
import magic

downloadPath = os.path.join(os.path.expanduser("~"), "Downloads")
wallpaperFolderPath = os.path.join(os.path.expanduser("~"), "Pictures", "Wallpapers-dl")
KEYWORDS = set(["wall", "unsplash", "Unsplash", "Wall"])

def checkImageAndMove(imageFiles):
    print(imageFiles)
    for file in imageFiles:
        if any(x in file for x in KEYWORDS):
            currentPath = os.path.join(downloadPath, file)
            destPath =  os.path.join(wallpaperFolderPath, file)
            os.rename(currentPath, destPath)


def getImageFilesWithKeywords():
    imageFiles = []
    downloadDir = os.listdir(downloadPath)
    for file in downloadDir:
        fileAddress = os.path.join(downloadPath, file)
        type = magic.from_file(fileAddress, mime=True)
        if "image" in type:
            imageFiles.append(file)
    checkImageAndMove(imageFiles)

def main():
    getImageFilesWithKeywords()

if __name__ == "__main__":
    main()