import os
import sqlite3
import json
import tools.Utilities

'''
使用SQLite作为Archivist的数据库
在初始化过程中应先检查这个数据库
Archives.db为总数据库
图片、pdf（阅读管理）、音乐、视频、文档（未来计划）
'''

class FileOperator(object):

    #搜索目标路径的所有文件
    def SearchSelectedPath(self, path):
        for fileName in os.listdir(path):
            suffixName = os.path.splitext(fileName)[-1]
            #搜索图片
            #读取EXIF信息并生成缩略图保存在backups/thumbnail
            if suffixName in self.picFiles:
                print("Found Picture {}".format(fileName))
                EXIF = tools.Utilities.ReadExif(path, fileName)
                self.cur.execute('''
                
                ''')
            #搜索音乐
            if suffixName in self.musicFiles:
                print("Found Music {}".format(fileName))
            if suffixName in self.docFiles:
                print("Found Document {}".format(fileName))
            if suffixName in self.costumeFiles:
                print("Found costume type file {}".format(fileName))
            if os.path.isdir(path + '/' + fileName):
                self.SearchSelectedPath(path + '/' + fileName)
