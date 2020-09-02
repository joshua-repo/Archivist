import os
import sqlite3
import rawpy
import tifffile
import exifread
import taglib #支持任意类型的文件标记
import tinytag #目前作用是提取音乐的专辑封面
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

#这个模块已经使用
def ReadExif(path, filename):
    f = open(path+ "\\" + filename, 'rb')
    #可以直接读NEF格式
    tags = exifread.process_file(f)
    f.close()
    return tags

def SearchSelectedPath(path,picFiles = [], musicFiles = [], docFiles = []):
    for fileName in os.listdir(path):
        suffixName = os.path.splitext(fileName)[-1]
        # 搜索图片
        # 读取EXIF信息并生成缩略图保存在backups/thumbnail
        if suffixName in picFiles:
            print("Found Picture {}".format(fileName))
        # 搜索音乐
        if suffixName in musicFiles:
            print("Found Music {}".format(fileName))
        if suffixName in docFiles:
            print("Found Document {}".format(fileName))
        # if suffixName in costumeFiles:
        #     print("Found costume type file {}".format(fileName))
        if os.path.isdir(path + '/' + fileName):
            SearchSelectedPath(path + '/' + fileName)

# def crateDB():
#     db = QSqlDatabase.addDatabase('QSQLITE')
#     db.setDatabaseName('./backups/Archivies.db')
#     with db.open():
#         return False
#     query = QSqlQuery()
#     query.exec('''CREATE TABLE IF NOT EXISTS METADATE(
#         VERSION     TEXT    PRIMARY KEY NOT NULL ,
#         HOSTEDIR    TEXT    NULT
#     );''')
#
#     query.exec('''CREATE TABLE IF NOT EXISTS PICTURES(
#         PATH        TEXT    PRIMARY KEY NOT NULL ,
#         FILENAME    TEXT    NOT NULL ,
#         EXIF        TEXT    NOT NULL ,
#         USERTAGS    TEXT    NOT NULL
#     );''')
#
#     query.exec('''CREATE TABLE IF NOT EXISTS PDFDOC(
#         PATH        TEXT    PRIMARY KEY ,
#         FILENAME    TEXT    NOT NULL ,
#         ARRAGE      TEXT    NOT NULL ,
#         USERTAGS    TEXT    NOT NULL ,
#     );''')
#
#     query.exec('''CREATE TABLE IF NOT EXISTS MUSIC(
#         PATH        TEXT    PRIMARY KEY ,
#         FILENAME    TEXT    NOT NULL ,
#         METADATA    TEXT    NOT NULL ,
#         THUMBNAIL   TEXT    NOT NULL ,
#         ALBUM       TEXT    NOT NULL ,
#         USERTAGS    TEXT    NOT NULL ,
#         STYLE       TEXT    NOT NULL
#     );''')
#     conn.close()


#     self.cur.execute('''CREATE TABLE IF NOT EXISTS MUSIC(
#     PATH        TEXT PRIMARY KEY NOT NULL ,
#     INFO        TEXT    NOT NULL ,
#     ALMBU       TEXT    NOT NULL ,
#     USERTAGS    TEXT    NOT NULL );''')
#
#     self.cur.execute('''CREATE TABLE IF NOT EXISTS DOC(
#     PATH    TEXT    PRIMARY KEY NOT NULL
#     );''')
#
#     self.conn.commit()
#
#     self.picFiles = ['.JPGE', '.JPG', '.jpg', '.jpge', '.raw', '.tiff', '.NEF']
#     self.musicFiles = ['.MP3', '.mp3']
#     self.docFiles = ['.pdf', '.doc', '.docx']
#     self.costumeFiles = []



#这个模块还没有验证,也许有更好的办法
#这里使用绝对路径，path这个参数直接传入os.getcwd()
# def ExtractPreviewImage(path, filename, workPath):
#     raw = rawpy.imread(path+ '\\' + filename)
#     thumb = raw.extract_thumb()
#     #如果是JPGE格式，就直接创建缩略图
#     if thumb.format == rawpy.ThumbFormat.JPGE:
#         f = open(workPath + "\\backups\\thumbnail" + filename + "_thumb.jpg", 'wb')
#         f.write(thumb.data)
#     #非JPGE格式生成缩略图
#     else:
#         imageio.imsave(workPath + "\\backups\\thumbnail" + filename + '_thumb.jpeg,', thumb.data)