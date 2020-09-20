import os
import sqlite3
import json

import exifread

import tools.Utilities

def searchPath(path, query):
    for fileName in os.listdir(path):
        PATH = path + '/' + fileName
        FILENAME = fileName
        SUFFIX = os.path.splitext(fileName)[-1]
        ROOT = path
        FILETYPE = ""
        USERTAG = ""
        RATING = ""
        KEYWORD = ""
        query.exec("INSERT INTO FileLibrary ("
                   "PATH, FILENAME, SUFFIX, ROOT, FILETYPE, USERTAGS, RATING, KEYWORD"
                   ") VALUES ('{}', '{}', '{}', '{}','{}', '{}', '{}', '{}')".format(
            PATH, FILENAME, SUFFIX, ROOT, FILETYPE, USERTAG, RATING, KEYWORD
        ))
        print(PATH, FILENAME, SUFFIX)
        if os.path.isdir(path + '/' + fileName):
            query.exec("INSERT INTO HostedDirectory (LOCATION) VALUES ('{}')".format(path + '/' + fileName))
            searchPath(path + '/' + fileName, query)

def sortFiles(path):
    pass

def ReadExif(path, filename):
    f = open(path+ "\\" + filename, 'rb')
    tags = exifread.process_file(f)
    f.close()
    return tags