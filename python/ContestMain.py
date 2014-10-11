import os
from filecmp import cmp

from ContestCode import dummy_message


PATH = "."
FOLDER_PREFIX = "level";
DEFAULT_FOLDDER = PATH + '/' + FOLDER_PREFIX


def write_result(someResultValue, outputLocation, outputFileName):
    """ Writes a result value to the given file at the given location!"""
    with open(outputLocation + '/' + outputFileName, 'w') as content_file:
        content_file.write(someResultValue)


def read_input_file_from_location(inputLocation, inputFileName):
    """ Reads an input file and returns it contents as a String"""
    return read_input_file(inputLocation + '/' + inputFileName)


def read_input_file(inputFileWithPath):
    with open(inputFileWithPath, 'r') as content_file:
        return content_file.read()


def create_folder(folderToCreate):
    """ Creates a folder if it does not exist """
    if not os.path.exists(folderToCreate):
        os.makedirs(folderToCreate)
    return folderToCreate


def create_default_folder(folderPostfix):
    return create_folder(DEFAULT_FOLDDER + folderPostfix)


def compare_file_contents(fileWithPath1, fileWithPath2):
    """ compares two files and return true if they have the same content, false if not """
    return cmp(fileWithPath1, fileWithPath2)


def compare_file_with_content(fileWithPath, expectedContent):
    """ looks if a file contains the expectedContent """
    return expectedContent == read_input_file(fileWithPath)


def do_setup_testing():
    """ tests the setup of the notebook """
    folderName = create_default_folder('0')
    write_result("foo", folderName, 'testInput.txt')
    input_content = read_input_file_from_location(folderName, 'testInput.txt')
    write_result(dummy_message(input_content), folderName, 'testOutput.txt')
    print compare_file_contents(folderName + '/testInput.txt', folderName + '/testOutput.txt')
    print compare_file_with_content(folderName + '/testOutput.txt', dummy_message(input_content))


def do_level_1():
    """ Calls the required methods for level 1 of the contest. It should stay the same along the later levels. """
    folderName = create_default_folder('1')


def do_level_2():
    """ Calls the required methods for level 2 of the contest. It should stay the same along the later levels. """
    folderName = create_default_folder('2')


def do_level_3():
    """ Calls the required methods for level 3 of the contest. It should stay the same along the later levels. """
    folderName = create_default_folder('3')


def do_level_4():
    """ Calls the required methods for level 4 of the contest. It should stay the same along the later levels. """
    folderName = create_default_folder('4')


if __name__ == '__main__':
    do_setup_testing()
    do_level_1()
    do_level_2()
    do_level_3()
    do_level_4()
