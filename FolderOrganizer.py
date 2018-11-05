import os
import sys
import shutil
import tkinter

from tkinter import filedialog

# Go to the Folder Mentioned.
# Organize the PDF's, Docs, Spreadsheets into the Documents Folder.
# Organize any Movies into the Videos Folder.
# Organize any Audio files into the Audio Folder.
# Organize any other Files into Unsorted Folder.
class FolderOrganizer:

    folderPath = "Dummy"

    # Function to Open a Folder and store the data.
    def openFolder(self):
        self.folderPath = tkinter.filedialog.askdirectory()
        self.folderPath = self.folderPath.replace("//banner.main.ad.rit.edu/students/skk7174/", "Z:/")

    def listFiles(self):
        for f in os.listdir(self.folderPath):
            print(f)

    def organizeToSeparateFolders(self):

        location = self.folderPath

        os.chdir(location);

        documents_init = False
        videos_init = False
        icloud_init = False
        app_init = False
        images_init = False

        documents_dir = location + "/Documents/"
        videos_dir = location + "/Videos/"
        icloud_dir = location + "/iCloud/"
        app_dir = location + "/Applications/"
        images_dir = location + "/Images/"


        for f in os.listdir(location):

            file_name, file_extension = os.path.splitext(f)

            if ( file_extension in [".pdf", ".docx", ".xls", ".pages", ".xlsx", ".txt", ".csv", ".epub", ".log"] ):

                if not documents_init:

                    if not (os.path.isdir(location + "/Documents")):

                        os.makedirs(location + "/Documents")

                    documents_init = True

                shutil.move(f, documents_dir + f)

            elif ( file_extension in [".mov", ".mp4", ] ):

                if not videos_init:

                    if not (os.path.isdir(location + "/Videos")):
                        os.makedirs(location + "/Videos")

                    videos_init = True

                shutil.move(f, videos_dir + f )

            elif file_extension in [".icloud"] :

                if not icloud_init:

                    if not (os.path.isdir(location + "/iCloud")):
                        os.makedirs(location + "/iCloud")

                    icloud_init = True

                shutil.move(f, icloud_dir + f)

            elif file_extension in [".app", ".exe", ".msi"]:

                if not app_init:

                    if not (os.path.isdir(location + "/Applications")):
                        os.makedirs(location + "/Applications")

                    app_init = True

                shutil.move(f, app_dir + f)

            elif file_extension in [".png", ".psd"]:

                if not images_init:

                    if not (os.path.isdir(location + "/Images")):
                        os.makedirs(location + "/Images")

                    images_init = True

                shutil.move(f, images_dir + f)

            else:

                print(file_extension)

    def consolidateFolders(self):
        print("Consolidate Folders Called")
#   We should have a Button to Add Folders to the Consolidation List.
#   We should ask for input as to where to Output all the Files.
#   Once we add all the folders, we should be able to press a different button, that would merge those folders, into a single Folder.


# We need a folder consolidator, which would combine 'n' different folders into one, and then Organize it.

def main():

    organizer = FolderOrganizer()

    rootWindow = tkinter.Tk()
    rootWindow.geometry("500x500")
    topFrame = tkinter.Frame(rootWindow)
    topFrame.pack()

    bottomFrame = tkinter.Frame(rootWindow)
    bottomFrame.pack(side=tkinter.BOTTOM)

    folderChoseButton = tkinter.Button(topFrame, text="Choose Folder", fg="green", command= lambda : organizer.openFolder())

    listFilesButton = tkinter.Button(topFrame, text="List all the Files in that Folder", fg='green', command = organizer.listFiles)

    organizeButton = tkinter.Button(topFrame, text="Organize into Folders", fg="cyan", command=organizer.organizeToSeparateFolders)

    consolidateButton = tkinter.Button(bottomFrame, text="Consolidate Folders", fg="red", command=organizer.consolidateFolders)


    folderChoseButton.pack(side=tkinter.LEFT)
    listFilesButton.pack(side=tkinter.LEFT)
    organizeButton.pack(side=tkinter.LEFT)

    consolidateButton.pack(side=tkinter.BOTTOM)

    rootWindow.mainloop()

if __name__ == "__main__":
    main()

