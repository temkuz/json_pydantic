from jinja2 import Environment, FileSystemLoader

from .classes import ClassStruct
from .functions import get_type, load_json, save_models
from .variables import models_template_name, templates_path


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


def parse_classes(data: dict[str, ...] | list, name: str = 'Root') -> list[ClassStruct]:
    result_classes: list[ClassStruct] = []

    buffer: ClassStruct = {'name': name, 'args': {}}
    if not isinstance(data, dict):
        return get_type(data)

    for key, value in data.items():
        class_name = key.title().replace('_', '')
        if isinstance(value, dict):
            if value:
                new_classes = parse_classes(value, class_name)
                result_classes = new_classes + result_classes
                buffer['args'][key] = class_name
            else:
                buffer['args'][key] = 'dict'
        elif isinstance(value, list):
            if value:
                if value:
                    new_classes = parse_classes(value[0], class_name)
                    result_classes = new_classes + result_classes
                    buffer['args'][key] = f'list[{class_name}]'
                else:
                    buffer['args'][key] = 'list'
        else:
            buffer['args'][key] = value
    result_classes.append(buffer)

    return result_classes


def generate_models(classes: list[ClassStruct]):
    environment = Environment(loader=FileSystemLoader(templates_path))
    models_template = environment.get_template(models_template_name)
    return models_template.render(classes=classes)


def run(input_file: str, output_file: str, first_class_name: str):
    input_json = load_json(input_file)
    parsed_types = parse_types(input_json)
    class_struct = parse_classes(parsed_types, first_class_name)
    models = generate_models(class_struct)
    save_models(output_file, models)
