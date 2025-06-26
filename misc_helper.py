import subprocess


def remove_widgets(layout):
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)

def parse_command_string(command, percent_u=None):
    parsed_array = []
    pre_parsed_array = command.split(' ')
    is_string = False
    buffer_string = ""
    if percent_u is not None:
        percent_u = False

    for segment in pre_parsed_array:
        if segment == "%u" or segment == "%U":
            continue
        if is_string:
            buffer_string += segment
        else:
            parsed_array.append(segment)
        if segment[0] == '"':
            is_string = True
            buffer_string += segment
        elif segment[-1] == '"':
            is_string = False
    return parsed_array

def run_command(command):
    subprocess.run(parse_command_string(command))
