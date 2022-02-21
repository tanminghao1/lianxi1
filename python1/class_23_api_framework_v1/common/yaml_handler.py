import yaml


def yaml_read(file,encoding="utf-8"):
    with open(file,encoding=encoding) as f:
        return yaml.load(f.read(),Loader=yaml.FullLoader)

def yaml_write(file,data,encoding="utf-8"):
    with open(file,mode="a",encoding=encoding) as f:
        yaml.dump(data,stream=f,allow_unicode=True)