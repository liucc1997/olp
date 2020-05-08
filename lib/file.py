import requests
def download_remote_file(url):
    """Download files from link
    Args:
        url: file location
    Returns:
        File object
    """
    f = requests.get(url) 
    return f

def check_remote_file():
    """
    判断远程文件的类型 大小
    大小<2M 保存在内存中，直接返回文件
    大小2M-20M 保存在硬盘中，等待下载完成 跳转并在包含文件地址的网页
    >20M 在网页中显示下载进度 下载完成后生成下载链接
    模式0 直接返回文件，服务器下载并实时返回给客户端
    """
    pass

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
