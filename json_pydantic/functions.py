from json import load, dump


def load_json(filename: str) -> dict:
    with open(filename, 'r', encoding='utf-8') as f:
        return load(f)


def save_json(filename: str, obj: dict):
    with open(filename, 'w', encoding='utf-8') as f:
        dump(obj, f, ensure_ascii=False, indent=2)


def save_models(filename: str, data: str):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)


def get_type(data):
    result = type(data).__name__
    if result == 'NoneType':
        result = 'None'
    return result
