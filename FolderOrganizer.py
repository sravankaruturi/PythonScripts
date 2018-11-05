import os
import sys
import shutil

# Go to the Folder Mentioned.
# Organize the PDF's, Docs, Spreadsheets into the Documents Folder.
# Organize any Movies into the Videos Folder.
# Organize any Audio files into the Audio Folder.
# Organize any other Files into Unsorted Folder.

# We can run this script once every couple of days on most of our folders to keep ourselves organized.

location = sys.argv[1];

print(location);

os.chdir(location);

# Make all the necessary Directories.

# All the booleans to make sure the directories are created and initialized.

documents_init = False
videos_init = False
icloud_init = False
app_init = False

documents_dir = location + "/Documents/"
videos_dir = location + "/Videos/"
icloud_dir = location + "/iCloud/"
app_dir = location + "/Applications/"
        

for f in os.listdir(location):

    file_name, file_extension = os.path.splitext(f)

    if ( file_extension in [".pdf", ".docx", ".xls", ".pages", ".xlsx"] ):

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

    elif file_extension in [".app", ".exe"]:

        if not app_init:

            if not (os.path.isdir(location + "/Applications")):
                os.makedirs(location + "/Applications")

            app_init = True

        shutil.move(f, app_dir + f)

    else:

        print(file_extension)
