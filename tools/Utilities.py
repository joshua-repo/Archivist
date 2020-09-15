import os
import http.client
import time
import sqlite3
import rawpy
import tifffile
import exifread
import taglib #支持任意类型的文件标记
import tinytag #目前作用是提取音乐的专辑封面
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# 可以直接读NEF格式
def ReadExif(path, filename):
    f = open(path+ "\\" + filename, 'rb')
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

#传入一个网址，来获得它的服务器时间
def getWebServerTime(host):
    conn = http.client.HTTPConnection(host)
    conn.request("GET", "/")
    r = conn.getresponse()
    ts = r.getheader('date')

    # 将GMT时间转换成北京时间
    # 以下这部分可能会用到
    ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    ttime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)
    dat = "%u-%02u-%02u" % (ttime.tm_year, ttime.tm_mon, ttime.tm_mday)
    tm = "%02u:%02u:%02u" % (ttime.tm_hour, ttime.tm_min, ttime.tm_sec)
    return tm

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