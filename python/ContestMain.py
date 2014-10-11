import os
from glob import glob
from filecmp import cmp

from ContestCode import dummy_message
from ContestCode import do_level_1
from ContestCode import do_level_2
from ContestCode import do_level_3
from ContestCode import do_level_4


PATH = "."
FOLDER_PREFIX = "level"
DEFAULT_FOLDER = PATH + '/' + FOLDER_PREFIX


def write_result_to_location(some_result_value, output_location, output_file_name):
    """ Writes a result value to the given file at the given location!"""
    write_result(some_result_value, output_location + '/' + output_file_name)


def write_result(result_value, output_file_name):
    with open(output_file_name, 'w') as content_file:
        content_file.write(result_value)


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
    write_result_to_location("foo", folder_name, 'testInput.txt')
    input_content = read_input_file_from_location(folder_name, 'testInput.txt')
    write_result_to_location(dummy_message(input_content), folder_name, 'testOutput.txt')
    print compare_file_contents(folder_name + '/testInput.txt', folder_name + '/testOutput.txt')
    print compare_file_with_content(folder_name + '/testOutput.txt', dummy_message(input_content))
    do_it_nasty(folder_name, False, dummy_message)
    do_it_nasty(folder_name, True, dummy_message)


def do_it_nasty(folder_name, level_completed, level_function):
    create_folder(folder_name)
    for content_file in glob(folder_name + '/' + "*.in"):
        input_content = read_input_file(content_file)
        result = level_function(input_content)
        out_file_name = content_file.replace(".in", ".out")
        if not level_completed:
            write_result(result, out_file_name)
        else:
            expected = read_input_file(out_file_name)
            assert expected == result, "Actual result [%s] is not as expected [%s]!" % (result, expected)


if __name__ == '__main__':
    do_setup_testing()
    do_it_nasty("level1", False, do_level_1)
    do_it_nasty("level2", False, do_level_2)
    do_it_nasty("level3", False, do_level_3)
    do_it_nasty("level4", False, do_level_4)
