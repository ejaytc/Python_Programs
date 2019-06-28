#!/usr/bin/env python3 
#Renamer.py 01 - Rename videos
#reference directory:/home/jay/Desktop/Workspace/Python_Workspace/samplevid
import shutil, os, re

epID = re.compile(r'\d{1,4}(.*?)$')

file_path = input("Input target directory: \t")
vidMainName  = input("Input new name: \t")
target = os.path.basename(file_path)
curDir = os.getcwd()

for list_file in os.listdir(target):
    vidEpisodes = epID.search(list_file)
    dirPath = os.path.join(curDir, target, list_file)
    newVideoName = "Inuyasha" + r" s1_Episode_" + vidEpisodes.group()
    shutil.move(dirPath, newVideoName)
    print(newVideoName)
    print(vidEpisodes.group())