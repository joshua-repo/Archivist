import os
import imageio
import rawpy
import tifffile
import exifread
import taglib #支持任意类型的文件标记
import tinytag #目前作用是提取音乐的专辑封面

def RawToTiff(path, filename):
    raw = rawpy.imread(path + filename)
    # use_camera_wb 是否执行自动白平衡，如果不执行白平衡，一般图像会偏色
    # half_size 是否图像减半
    # no_auto_bright 不自动调整亮度
    # output_bps bit数据 可选8或16
    img = raw.postprocess(
        use_camera_wb=True,
        half_size=False,
        no_auto_bright=True,
        output_bps=16
    )
    tifffile.imwrite('{}.tiff'.format(filename), data=img)

def ReadExif(path, filename):
    f = open(path + filename, 'rb')
    #注意，exifread只支持jpg或者tiff格式的输入
    tags = exifread.process_file(f)
    f.close()
    '''
    if FIELD in tags:
        #获取照片的时间
        time = str(tags[FIELD])
        #获取照片的格式
        file_suffix = os.path.splitext(filename)[-1]
    '''
    return tags

def ExtractPreviewImage(path, filename):
    raw = rawpy.imread(path + filename)
    thumb = raw.extract_thumb()
    if thumb.format == rawpy.ThumbFormat.JPGE:
        f = open(path + filename, 'wb')
        f.write(thumb.data)
    else:
        imageio.imsave(filename + '_thumb.jpeg,', thumb.data)