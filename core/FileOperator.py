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
                   "PATH, FILENAME, SUFFIX, ROOT, FILETYPE, USERTAGS, RATING, KEYWORDS"
                   ") VALUES ('{}', '{}', '{}', '{}','{}', '{}', '{}', '{}')".format(
            PATH, FILENAME, SUFFIX, ROOT, FILETYPE, USERTAG, RATING, KEYWORD
        ))
        print(PATH, FILENAME, SUFFIX)
        if os.path.isdir(path + '/' + fileName):
            query.exec("INSERT INTO HostedDirectory (LOCATION) VALUES ('{}')".format(path + '/' + fileName))
            searchPath(path + '/' + fileName, query)

def sortFiles(query):
    pass

def ReadExif(path):
    f = open(path, 'rb')
    tags = exifread.process_file(f)
    f.close()
    return tags

def unionQuery(query, tagsList, ratingsList, keywordsList):
    sql = ""
    if tagsList == []:
        pass
    elif len(tagsList) == 1:
        sql = "SELECT FILENAME FROM FileLibrary WHERE USERTAGS == '{}'".format(tagsList[0])
    else:
        sql = "SELECT FILENAME FROM FileLibrary WHERE USERTAGS == '{}'".format(tagsList[0])
        for i in range(1, len(tagsList)):
            print(tagsList[i])
            sql += "UNION SELECT FILENAME FROM FileLibrary WHERE USERTAGS == '{}'".format(tagsList[i])

    if ratingsList == []:
        pass
    elif len(ratingsList) == 1:
        if sql == "":
            sql = "SELECT FILENAME FROM FileLibrary WHERE RATING == '{}'".format(ratingsList[0])
        else:
            sql += "UNION SELECT FILENAME FROM FileLibrary WHERE RATING == '{}'".format(ratingsList[0])
    else:
        if sql == "":
            sql = "SELECT FILENAME FROM FileLibrary WHERE RATING == '{}'".format(ratingsList[0])
            for i in range(1, len(ratingsList)):
                sql += "UNION SELECT FILENAME FROM FileLibrary WHERE RATING == '{}'".format(ratingsList[i])
        else:
            for i in range(0, len(ratingsList)):
                sql += "UNION SELECT FILENAME FROM FileLibrary WHERE RATING == '{}'".format(ratingsList[i])

    if keywordsList == []:
        pass
    elif len(keywordsList) == 1:
        if sql == "":
            sql = "SELECT FILENAME FROM FileLibrary WHERE KEYWORDS == '{}'".format(keywordsList[0])
        else:
            sql += "UNION SELECT FILENAME FROM FileLibrary WHERE KEYWORDS == '{}'".format(keywordsList[0])
    else:
        if sql == "":
            sql = "SELECT FILENAME FROM FileLibrary WHERE KEYWORDS == '{}'".format(keywordsList[0])
            for i in range(1, len(keywordsList)):
                sql += "UNION SELECT FILENAME FROM FileLibrary WHERE KEYWORDS == '{}'".format(keywordsList[i])
        else:
            for i in range (0, len(ratingsList)):
                sql += "UNION SELECT FILENAME FROM FileLibrary WHERE KEYWORDS == '{}'".format(keywordsList[i])
    query.exec(sql)
