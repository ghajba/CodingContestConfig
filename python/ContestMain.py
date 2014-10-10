import io, os, sys
from ContestCode import dummy_message
from filecmp import cmp

PATH = "."
FOLDER_PREFIX = "level";
DEFAULT_FOLDDER = PATH+'/'+FOLDER_PREFIX

def writeResult(someResultValue, outputLocation, outputFileName):
    """ Writes a result value to the given file at the given location!"""
    with open(outputLocation+'/'+outputFileName, 'w') as content_file:
         content_file.write(someResultValue)

def readInputFileFromLocation(inputLocation, inputFileName):
    """ Reads an input file and returns it contents as a String"""
    return readInputFile(inputLocation+'/'+inputFileName)
    
def readInputFile(inputFileWithPath):
    with open(inputFileWithPath, 'r') as content_file:
        return content_file.read()

def createFolder(folderToCreate):
    """ Creates a folder if it does not exist """
    if not os.path.exists(folderToCreate):
        os.makedirs(folderToCreate)
    return folderToCreate

def createDefaultFolder(folderPostfix):
    return createFolder(DEFAULT_FOLDDER+folderPostfix)
        
def compareFileContents(fileWithPath1, fileWithPath2):
    """ compares two files and return true if they have the same content, false if not """
    return cmp(fileWithPath1, fileWithPath2)

def compareFileWithContent(fileWithPath, expectedContent):
    """ looks if a file contains the expectedContent """
    return expectedContent == readInputFile(fileWithPath)


def do_setup_testing():
    """ tests the setup of the notebook """
    folderName = createDefaultFolder('0')
    writeResult("foo", folderName, 'testInput.txt')
    input_content = readInputFileFromLocation(folderName, 'testInput.txt')
    writeResult(dummy_message(input_content), folderName, 'testOutput.txt')
    print compareFileContents(folderName+'/testInput.txt', folderName+'/testOutput.txt')
    print compareFileWithContent(folderName+'/testOutput.txt',dummy_message(input_content))

def do_level_1():
    """ Calls the required methods for level 1 of the contest. It should stay the same along the later levels. """
    folderName = createDefaultFolder('1')

def do_level_2():
    """ Calls the required methods for level 2 of the contest. It should stay the same along the later levels. """
    folderName = createDefaultFolder('2')

def do_level_3():
    """ Calls the required methods for level 3 of the contest. It should stay the same along the later levels. """
    folderName = createDefaultFolder('3')

def do_level_4():
    """ Calls the required methods for level 4 of the contest. It should stay the same along the later levels. """
    folderName = createDefaultFolder('4')

if __name__ == '__main__':
    do_setup_testing()
    do_level_1()
    do_level_2()
    do_level_3()
    do_level_4()
