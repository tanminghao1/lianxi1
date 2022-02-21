import yaml


def yaml_read(yaml_file,encoding="utf-8"):
    with open(yaml_file,encoding=encoding) as y:
        return yaml.load(y.read(),Loader=yaml.FullLoader)


def yaml_writer(yaml_file,data,encoding="utf-8"):
    with open(yaml_file,mode="w",encoding=encoding) as f:
        yaml.dump(data,f,allow_unicode=True)


