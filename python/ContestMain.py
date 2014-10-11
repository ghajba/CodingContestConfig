import os
from filecmp import cmp

from ContestCode import dummy_message


PATH = "."
FOLDER_PREFIX = "level"
DEFAULT_FOLDER = PATH + '/' + FOLDER_PREFIX


def write_result(some_result_value, output_location, output_file_name):
    """ Writes a result value to the given file at the given location!"""
    with open(output_location + '/' + output_file_name, 'w') as content_file:
        content_file.write(some_result_value)


def read_input_file_from_location(input_location, input_file_name):
    """ Reads an input file and returns it contents as a String"""
    return read_input_file(input_location + '/' + input_file_name)


def read_input_file(input_file_with_path):
    with open(input_file_with_path, 'r') as content_file:
        return content_file.read()


def create_folder(folder_to_create):
    """ Creates a folder if it does not exist """
    if not os.path.exists(folder_to_create):
        os.makedirs(folder_to_create)
    return folder_to_create


def create_default_folder(folder_postfix):
    return create_folder(DEFAULT_FOLDER + folder_postfix)


def compare_file_contents(file_with_path_1, file_with_path2):
    """ compares two files and return true if they have the same content, false if not """
    return cmp(file_with_path_1, file_with_path2)


def compare_file_with_content(file_with_path, expected_content):
    """ looks if a file contains the expectedContent """
    return expected_content == read_input_file(file_with_path)


def do_setup_testing():
    """ tests the setup of the notebook """
    folder_name = create_default_folder('0')
    write_result("foo", folder_name, 'testInput.txt')
    input_content = read_input_file_from_location(folder_name, 'testInput.txt')
    write_result(dummy_message(input_content), folder_name, 'testOutput.txt')
    print compare_file_contents(folder_name + '/testInput.txt', folder_name + '/testOutput.txt')
    print compare_file_with_content(folder_name + '/testOutput.txt', dummy_message(input_content))


def do_level_1():
    """ Calls the required methods for level 1 of the contest. It should stay the same along the later levels. """
    folder_name = create_default_folder('1')


def do_level_2():
    """ Calls the required methods for level 2 of the contest. It should stay the same along the later levels. """
    folder_name = create_default_folder('2')


def do_level_3():
    """ Calls the required methods for level 3 of the contest. It should stay the same along the later levels. """
    folder_name = create_default_folder('3')


def do_level_4():
    """ Calls the required methods for level 4 of the contest. It should stay the same along the later levels. """
    folder_name = create_default_folder('4')


if __name__ == '__main__':
    do_setup_testing()
    do_level_1()
    do_level_2()
    do_level_3()
    do_level_4()
