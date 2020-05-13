import requests
import re
def download_remote_file(url):
    """Download files from link
    Args:
        url: file location
    Returns:
        File object
        -1 : unexpected url 
        -2 : download failed
    """
    #检验url的合法性
    if re.match(r'^https?:/{2}\w.+$', url):
        try:
            f = requests.get(url) 
        except BaseException:
            return -2
        return f  
    else:
        return -1

def check_remote_file(url):
    """
    判断远程文件的类型 大小
    大小<2M 保存在内存中，直接返回文件
    大小2M-20M 保存在硬盘中，等待下载完成 跳转并在包含文件地址的网页
    >20M 在网页中显示下载进度 下载完成后生成下载链接
    模式0 直接返回文件，服务器下载并实时返回给客户端
    Args:
        url: file location
    Returns:
        dict:{'size':file-size,'accept':request type} 
    """
    ret = {}
    if re.match(r'^https?:/{2}\w.+$', url) is None:  #检验url合法性
        return None
    try:
        r = requests.head(url)
    except BaseException:
        ret['size'] = -2
        ret['accept'] = None
    else:
        size = r.headers.get('content-length', None)
        accept = r.headers.get('Accept-Ranges', None)
        if size:
            size = int(size)
            ret['size'] = size/(1048576.0)
        else:
            ret['size'] = -1 
        ret['accept'] = accept
    return ret


def get_remote_file_name(url):
    """Create a file name from the url
    Args:
        url: file location
    Returns:
        String representing the filename
    """
    array = url.split('/')
    name = url
    if len(array) > 0:
        name = array[-1]
    return name


"""Python下载文件并返回实施进度
"""
