import yaml

from config.setting import config


class YamlHandler:
    def __init__(self,file):
        self.file = file
    def read(self,encoding='utf-8'):
        f = open(self.file,encoding=encoding)
        #   TODO:f.read()和f都可以作为参数
        data = yaml.load(f,yaml.FullLoader)
        f.close()
        return data

# 直接初始化，读取本项目中yaml配置项供其它模块调用，省去初始化
yaml_data = YamlHandler(config.yaml_config_path).read()
# print(yaml_data)