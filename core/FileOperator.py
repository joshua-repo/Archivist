import os
import sqlite3
import json
import tools.Utilities

'''
使用SQLite作为Archivist的数据库
在初始化过程中应先检查这个数据库
Archives.db为总数据库
图片、音乐、视频、文档（未来计划）
'''

class FileOperator(object):

    def __init__(self):
        print("Welcome to Archivisit!")
        print("Current working path {}".format(os.getcwd()))
        #生成当前工作路径，默认情况是软件所在位置
        self.workingDir = os.getcwd()

        self.conn = sqlite3.connect("backups/Archives.db")
        self.cur = self.conn.cursor()
        '''
        初始化用于管理图片的表
        key-路径
        value-EXIF信息，自定义名称，tags(用户自定）
        EXIF信息是一个字典，存入数据库之前需要序列化
        '''
        self.cur.execute('''CREATE TABLE IF NOT EXISTS PICTURES (
        PATH        TEXT    PRIMARY KEY NOT NULL ,
        FILENAME    TEXT    NOT NULL ,
        EXIF        TEXT    NOT NULL ,
        THUMBNAIL   TEXT    NOT NULL ,
        USERTAGS    TEXT    NOT NULL);''')
        print("Picture Library initialized successfully.")
        '''
        初始化用于管理音乐的表
        key-路径
        '''
        self.cur.execute('''CREATE TABLE IF NOT EXISTS MUSIC(
        PATH        TEXT PRIMARY KEY NOT NULL ,
        INFO        TEXT    NOT NULL ,
        ALMBU       TEXT    NOT NULL ,
        USERTAGS    TEXT    NOT NULL );''')
        print("Music Library initialized successfully.")
        '''
        初始化用于管理文档的表
        key-路径
        '''
        self.cur.execute('''CREATE TABLE IF NOT EXISTS DOC(
        PATH    TEXT    PRIMARY KEY NOT NULL 
        );''')
        print("Document Library initialized successfully.")

        self.conn.commit()

        self.picFiles = ['.JPGE', '.JPG', '.jpg', '.jpge', '.raw', '.tiff', '.NEF']
        self.musicFiles = ['.MP3', '.mp3']
        self.docFiles = ['.pdf', '.doc', '.docx']
        self.costumeFiles = []

    #重新定位Archivies数据库,同时生成备份
    # def RedirectLibrary(self, libPath):
    #     self.libPath = libPath

    #增加管理自定义类型文件
    def costumeSearch(self):
        print("What kind of files do you wish Archivist to manage?")
        costumeSuffix = input()
        self.costumeFiles.append(costumeSuffix)
        print("Now Archivist will serach files including {}.".format(self.costumeFiles))

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


    # def SetTag(self, path, tag):
    #     self.cur.execute('''(
    #     );''')

    def __del__(self):
        self.conn.commit()
        self.conn.close()
        print("Exit Archivist successfully.")