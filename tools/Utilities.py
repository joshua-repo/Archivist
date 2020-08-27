import os
import rawpy
import tifffile
import exifread
import taglib #支持任意类型的文件标记
import tinytag #目前作用是提取音乐的专辑封面

#这个模块已经使用
def ReadExif(path, filename):
    f = open(path+ "\\" + filename, 'rb')
    #可以直接读NEF格式
    tags = exifread.process_file(f)
    f.close()
    return tags

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