from .classes import ClassStruct
from .variables import CLASS_TEMPLATE
from .functions import get_type, load_json, save_models


def parse_types(data: dict) -> dict[str, ...]:
    result = {}

    if isinstance(data, list) and len(data):
        result['content_list'] = [parse_types(data[0])]
        return result

    if not isinstance(data, dict):
        return get_type(data)
    for key, value in data.items():
        if isinstance(value, dict):
            result[key] = parse_types(value)
        elif isinstance(value, list):
            result[key] = [parse_types(i) if isinstance(i, dict) else get_type(i) for i in value]
        else:
            result[key] = get_type(value)
    return result


def parse_classes(data: dict[str, ...] | list, name: str = 'Root') -> ClassStruct:
    class_struct: ClassStruct = {
        'name': name,
        'args': {},
        'inner_classes': []
    }

    if not isinstance(data, dict):
        return get_type(data)

    for key, value in data.items():
        class_name = key.title().replace('_', '')
        if isinstance(value, dict):
            if len(value):
                class_struct['inner_classes'].append(parse_classes(value, class_name))
                class_struct['args'][key] = class_name
            else:
                class_struct['args'][key] = 'dict'
        elif isinstance(value, list):
            if len(value):
                class_struct['inner_classes'].append(parse_classes(value[0], class_name))
                class_struct['args'][key] = f'list[{class_name}]'
            else:
                class_struct['args'][key] = 'list'
        else:
            class_struct['args'][key] = value
    return class_struct


def _generate_models(class_struct: ClassStruct) -> str:
    inner = class_struct['inner_classes']
    result_string = ''
    if inner:
        for class_ in inner:
            result_string += _generate_models(class_)
    name = class_struct['name']
    args = class_struct['args']
    args = '\n\t'.join(f'{k}: {v}' for k, v in sorted(args.items()))
    result_string += CLASS_TEMPLATE.format(name=name, args=args)
    return result_string


def generate_models(class_struct: ClassStruct):
    return 'from pydantic import BaseModel\n\n\n' + _generate_models(class_struct)


def run(input_file: str, output_file: str, first_class_name: str):
    input_json = load_json(input_file)
    parsed_types = parse_types(input_json)
    class_struct = parse_classes(parsed_types, first_class_name)
    models = generate_models(class_struct)
    save_models(output_file, models)
