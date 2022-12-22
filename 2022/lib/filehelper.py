def file_to_array(path):
    """Open file and return each line as a list of ints."""
    return [int(line.strip()) for line in open(path, "r")]

def file_to_bald_str_array(path):
    """Open file and return each line as a list of ints."""
    return [str(line.rstrip('\n')) for line in open(path, "r")]

def file_to_str_array(path):
    """Open file and return each line as a list of ints."""
    return [str(line.strip()) for line in open(path, "r")]

def get_number_list_from_file(path):
    """Return a list of numbers for each line in a file"""
    with open(path, "r") as numberlist_file:
        return [int(opcode) for opcode in numberlist_file.read().split(",")]


def get_numbers_from_string_from_file(path):
    res = []
    with open(path, "r") as f:
        for line in f.readlines():
            for letter in line:
                if letter != "\n":
                    res.append(int(letter))
        return res


def get_string_lists_from_file(path):
    res = []
    with open(path, "r") as f:
        for line in f.readlines():
            current_line = []
            for input in line.split(","):
                current_line.append(input.strip())
            res.append(current_line)
    return res


def get_map_from_file(path):
    res = []
    with open(path, "r") as f:
        for line in f.readlines():
            current_line = []
            for letter in line:
                if letter != "\n":
                    current_line.append(letter)
            res.append(current_line)
    return res


def get_string_list_from_file(path):
    return [line.strip() for line in open(path, "r")]

def get_bald_string_list_from_file(path):
    return [line.replace('\n','') for line in open(path, "r")]
