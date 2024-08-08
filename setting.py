import yaml

setting = {}
with open("settings.yaml", "r", encoding="utf-8") as f:
    setting = yaml.safe_load(f)


def load(k, default=None):
    if default is None:return setting.setdefault(k,default)
    else:return setting[k]


def save(k, v):
    setting[k] = v
    yaml.safe_dump(v)
