import os
import sqlite3
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

        conn = sqlite3.connect("backups/Archives.db")
        cur = conn.cursor()
        '''
        初始化用于管理图片的表
        key-路径
        value-EXIF信息，自定义名称，tags(用户自定）
        EXIF信息是一个字典，存入数据库之前需要序列化
        '''
        cur.execute('''CREATE TABLE IF NOT EXISTS PICTURES (
        PATH    TEXT    PRIMARY KEY NOT NULL ,
        EXIF    TEXT    NOT NULL ,
        TAGS    TEXT    NOT NULL);''')
#        print("Picture Library initialized successfully.")
        '''
        初始化用于管理音乐的表
        key-路径
        '''
        cur.execute('''CREATE TABLE IF NOT EXISTS MUSIC(
        PATH    TEXT PRIMARY KEY NOT NULL ,
        INFO    TEXT    NOT NULL ,
        ALMBU   TEXT    NOT NULL ,
        TAGS    TEXT    NOT NULL );''')
#        print("Music Library initialized successfully.")
        '''
        初始化用于管理文档的表
        key-路径
        '''
        cur.execute('''CREATE TABLE IF NOT EXISTS DOC(
        PATH    TEXT    PRIMARY KEY NOT NULL 
        );''')
#        print("Document Library initialized successfully.")

        conn.commit()
        conn.close()

        self.suffixName = ['Anything']
        self.picFiles = ['JPGE', 'JPG', 'jpg', 'jpge', 'raw', 'tiff']
        self.musicFiles = ['MP3', 'mp3']
        self.docFiles = ['pdf', 'doc', 'docx']
        self.costumeFiles = []
        self.conn = sqlite3.connect("backups/Archives.db")
        self.cur = conn.cursor()

    def RedirectLibrary(self, libPath):
        self.libPath = libPath

    def costumeSearch(self, costumeSuffix):
        print("What kind of files do you wish Archivist to manage?")
        self.costumeFiles.insert(costumeSuffix)
        print("Now Archivist will serach files including {}.".format(self.suffixName))


    def SearchSelectedPath(self, path):
        for fileName in os.listdir(path):
            suffixName = os.path.splitext(fileName)[-1]
            if suffixName in self.picFiles:
                print("Found Picture {}".format(fileName))
                self.cur.execute('''(

                );''')
                self.conn.commit()
            elif suffixName in self.musicFiles:
                print("Found Music {}".format(fileName))
                self.cur.execute('''(

                );''')
            elif suffixName in self.docFiles:
                print("Found Document {}".format(fileName))
                self.cur.execute('''(

                );''')
            elif suffixName in self.costumeFiles:
                print("Found costume type file {}".format(fileName))
                self.cur.execute('''(

                );''')
            if os.path.isdir(path + "\\" + fileName):
                self.SearchSelectedPath(path + "\\" + fileName)

    def __del__(self):
        self.conn.commit()
        self.conn.close()
        print("Exit Archivist successfully.")