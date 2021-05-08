import dynamic_yaml

config = ...

with open('config.yaml', 'r') as config_file:
    config = dynamic_yaml.load(config_file)


def to_tuple(config_entry):
    return [x for x in config_entry.values()]
