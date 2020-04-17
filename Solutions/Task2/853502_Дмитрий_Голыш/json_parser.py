nested_types = [
        '<class \'dict\'>',
        '<class \'list\'>',
        '<class \'tuple\'>',
    ]


def python_object_to_json(obj, indent=0, flag=False):
    json_string = ''
    obj_type = str(type(obj))

    basic_types = [
        '<class \'dict\'>',
        '<class \'list\'>',
        '<class \'tuple\'>',
        '<class \'set\'>',
        '<class \'str\'>',
        '<class \'int\'>',
        '<class \'float\'>',
        '<class \'bool\'>',
        '<class \'NoneType\'>',
    ]

    if obj_type not in basic_types:
        json_string = dict_to_json(obj.__dict__, indent)

    elif obj_type == '<class \'dict\'>':
        json_string = dict_to_json(obj, indent)

    elif obj_type == '<class \'list\'>' or obj_type == '<class \'tuple\'>':
        json_string = arr_to_json(obj, indent)

    elif obj_type == '<class \'set\'>':
        json_string = set_to_json(obj, indent)

    elif obj_type == '<class \'str\'>':
        json_string = str_to_json(obj, flag)

    elif obj_type == '<class \'int\'>' or obj_type == '<class \'float\'>':
        json_string = num_to_json(obj)

    elif obj_type == '<class \'bool\'>':
        json_string = bool_to_json(obj)

    elif obj_type == '<class \'NoneType\'>':
        json_string = none_to_json()

    return json_string


def dict_to_json(obj, indent):
    json_string = ''
    k = 1
    flag = False
    spaces = '    ' * indent

    if indent != 0:
        bracket_spaces = '    ' * (indent - 1)
        json_string += '{\n'
        for i in obj:
            if str(type(obj[i])) == '<class \'str\'>' or str(type(i)) == '<class \'str\'>':
                flag = True
            if str(type(obj[i])) not in nested_types:
                if k < len(obj):
                    json_string += f'{spaces}"{python_object_to_json(i, flag=flag)}": "{python_object_to_json(obj[i], flag=flag)}",\n'
                else:
                    json_string += f'{spaces}"{python_object_to_json(i, flag=flag)}": "{python_object_to_json(obj[i], flag=flag)}"\n'
            else:
                if k < len(obj):
                    json_string += f'{spaces}"{python_object_to_json(i, flag=flag)}": {python_object_to_json(obj[i], flag=flag, indent=indent+1)},\n'
                else:
                    json_string += f'{spaces}"{python_object_to_json(i, flag=flag)}": {python_object_to_json(obj[i], flag=flag, indent=indent+1)}\n'
            k += 1
        json_string += bracket_spaces + '}'
    else:
        json_string += '{'
        for i in obj:
            if str(type(obj[i])) == '<class \'str\'>' or str(type(i)) == '<class \'str\'>':
                flag = True
            if str(type(obj[i])) not in nested_types:
                if k < len(obj):
                    json_string += f'"{python_object_to_json(i, flag=flag)}": "{python_object_to_json(obj[i], flag=flag)}", '
                else:
                    json_string += f'"{python_object_to_json(i, flag=flag)}": "{python_object_to_json(obj[i], flag=flag)}"'
            else:
                if k < len(obj):
                    json_string += f'"{python_object_to_json(i, flag=flag)}": {python_object_to_json(obj[i], flag=flag)}, '
                else:
                    json_string += f'"{python_object_to_json(i, flag=flag)}": {python_object_to_json(obj[i], flag=flag)}'
            k += 1
        json_string += '}'

    return json_string


def arr_to_json(obj, indent):
    json_string = ''
    k = 1
    spaces = '    ' * indent

    if indent != 0:
        bracket_spaces = '    ' * (indent - 1)
        json_string += '[\n'
        for i in obj:
            if k < len(obj):
                json_string += f'{spaces}{python_object_to_json(i, indent=indent+1)},\n'
            else:
                json_string += f'{spaces}{python_object_to_json(i, indent=indent+1)}\n'
            k += 1
        json_string += bracket_spaces + ']'
    else:
        json_string += '['
        for i in obj:
            if k < len(obj):
                json_string += f'{python_object_to_json(i)}, '
            else:
                json_string += f'{python_object_to_json(i)}'
            k += 1
        json_string += ']'

    return json_string


def set_to_json(obj, indent):
    json_string = ''
    spaces = '    ' * indent
    k = 1

    if indent != 0:
        bracket_spaces = '    ' * (indent - 1)
        json_string += '{\n'
        for i in obj:
            if k < len(obj):
                json_string += f'{spaces}{python_object_to_json(i)},\n'
            else:
                json_string += f'{spaces}{python_object_to_json(i)}\n'
            k += 1
        json_string += bracket_spaces + '}'

    else:
        json_string += '{'
        for i in obj:
            if k < len(obj):
                json_string += f'{python_object_to_json(i)}, '
            else:
                json_string += f'{python_object_to_json(i)}'
            k += 1
        json_string += '}'

    return json_string


def str_to_json(obj, flag):
    if flag:
        return obj
    return '"' + obj + '"'


def num_to_json(obj):
    return obj


def bool_to_json(obj):
    return str(obj).lower()


def none_to_json():
    return 'null'

