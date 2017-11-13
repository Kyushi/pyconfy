import argparse
import os
import yaml


def add_root(path_from_here):
    wd = os.path.abspath(os.getcwd())
    root = os.path.join(wd, path_from_here)
    return f'import os\n\nROOT = {root}\n\n'

def load_yaml(yaml_file):
    with open(yaml_file, 'r') as stream:
        yaml_conf = yaml.load(stream)
    return yaml_conf


def create_class_str(class_name):
    return f"class {class_name}:\n"

def create_class_var_str(k, v):
    if isinstance(v, str):
        return f"{k} = '{v}'\n"
    else:
        return f"{k} = {v}\n"


def generate_classes(k, v, is_sub_n):
    out_str = is_sub_n * 4 * ' '
    if isinstance(v, dict):
        out_str += create_class_str(k)
        for sk, sv in v.items():
            out_str += generate_classes(sk, sv, is_sub_n + 1)
    else:
        out_str += create_class_var_str(k, v)
    return out_str


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "yaml",
        metavar='path/to/config.yaml',
        help="Path to your config yaml file"
    )
    parser.add_argument(
        "root",
        help="Add path to root dir"
    )
    args = parser.parse_args()
    class_str = '"""This is a file that was automatically generated using PyConfY"""\n\n'
    class_str += add_root(args.root)
    class_str += generate_classes('LolaConfig', load_yaml(args.yaml), 0)
    class_str += '\n'
    print(class_str)
