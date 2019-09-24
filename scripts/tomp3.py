import pydub
import magic
import os
import time 

pathToYoutube = os.path.join(os.path.expanduser("~"), "Music", "youtube")
allFilesinYoutube = os.listdir(pathToYoutube)

def removem4aFiles(m4aFiles):
    for file in m4aFiles:
        if os.path.isfile(file):
            os.remove(file)
        else:    ## Show an error ##
            print("Error: %s file not found" % file)

def convertTomp3(m4aFiles):
    for file in m4aFiles:
        filenameToSave = file.rsplit(".")[0] + ".mp3"
        try:
            if os.path.isfile(filenameToSave):
                print("file with name %s already exists" % filenameToSave)
                filenameToSave = file.rsplit(".")[0] + "-" + str(int(time.time())) + ".mp3"
                print("Saving as %s \n" % filenameToSave)                
            print("Converting: " + file + "\n")
            sound = pydub.AudioSegment.from_file(file)
            sound.export(filenameToSave, format="mp3")
        except:
            print("Error: While converting: %s" % file)
    removem4aFiles(m4aFiles)
    

def main():
    m4aFiles = []
    for file in allFilesinYoutube:
        filename = os.path.join(pathToYoutube, file)
        type = magic.from_file(filename, mime=True)
        if (type == "video/mp4"):
            m4aFiles.append(filename)
    convertTomp3(m4aFiles)

if __name__ == '__main__':
    main()