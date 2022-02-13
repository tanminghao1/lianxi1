from configparser import ConfigParser

import yaml


class ConfigHandler(ConfigParser):
    def __init__(self,file,encoding='utf-8'):
        """
        参数：
        file:配置文件的路径名
        :param file:
        """
        # config =ConfigParser()
        super().__init__()
        self.read(file,encoding)
def read_yaml(file,encoding='utf-8'):
    with open(file,encoding=encoding) as f:
        return yaml.load(f.read(),Loader=yaml.FullLoader)

def write_yaml(file,data,encoding='utf-8'):
    """
    写入yaml
    中文如何处理？用allow_unicode=True
    """
    with open(file,encoding=encoding,mode='w') as f:
         yaml.dump(data,stream=f,allow_unicode=True)


if __name__ == '__main__':
    # config = ConfigHandler('D:\pythonProject\python1\class_21_logger封装\python25.ini')
    # a= config.get('teachers','name')
    # print(a)

    # print(read_yaml('D:\pythonProject\python1\class_21_logger封装\python25.yaml'))

    #先读取yaml数据
    data= read_yaml('D:\pythonProject\python1\class_21_logger封装\python25.yaml')
    write_yaml('python_26.yaml',data)