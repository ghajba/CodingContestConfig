package hu.japy.dev.contestconfig;

import org.apache.commons.io.FileUtils;
import org.apache.commons.lang3.StringUtils;

import java.io.File;
import java.io.IOException;
import java.util.Collection;
import java.util.function.Function;

/**
 * Created by GHajba on 2014.10.10..
 */
public class Main {

    public static void main(String... args) throws IOException {
        Code code = new Code();

        //doItNasty("level0", false, code::doLevel0);
        //doItNasty("level0", true, code::doLevel0);
        
        doItNasty("level1", false, code::doLevel1);
        //doItNasty("level2", false, code::doLevel1);
        //doItNasty("level3", false, code::doLevel1);
        //doItNasty("level4", false, code::doLevel1);
    }

    private static void doItNasty(String folderName, boolean levelDone, Function<String,
            String> levelFunction) throws IOException {
        createFolder(folderName);
        for (File inputFile : listInputFiles(folderName)) {
            String input = readFile(inputFile);
            String result = levelFunction.apply(input);
            File outFile = new File(inputFile.getPath().replace(".in", ".out"));
            if (!levelDone) {
                writeFile(outFile, result);
            }
            else {
                String expected = readFile(outFile);
                if (!StringUtils.equals(result, expected)) {
                    throw new AssertionError(String.format("Expected and actual result are not the same!\nExpected: " +
                            "%s\nActual: %s", expected, result));
                }
            }
        }
    }

    private static void doLevel1(Code code) throws IOException {
        createFolder("level1");
        for (File inputFile : listInputFiles("level1")) {
            String input = readFile(inputFile);
            String result = code.doLevel1(input);
            String outFileName = inputFile.getName().replace(".in", ".out");
            writeFile(inputFile.getPath(), outFileName, result);
            //assert readFile(inputFile.getPath(), outFileName).equals(result);
        }

    }

    private static void doLevel2(Code code) throws IOException {
        createFolder("level2");
    }

    private static void doLevel3(Code code) throws IOException {
        createFolder("level3");
    }

    private static void doLevel4(Code code) throws IOException {
        createFolder("level4");
    }

    private static void createFolder(String folderName) throws IOException {
        FileUtils.forceMkdir(new File(folderName));
    }

    private static String readFile(String filePath, String fileName) throws IOException {
        return readFile(new File(filePath, fileName));
    }

    private static String readFile(File file) throws IOException {
        return FileUtils.readFileToString(file);
    }

    private static void writeFile(String filePath, String fileName, String content) throws IOException {
        writeFile(new File(filePath, fileName), content);
    }

    private static void writeFile(File file, String content) throws IOException {
        FileUtils.write(file, content);
    }

    private static Collection<File> listInputFiles(String folder) {
        return FileUtils.listFiles(new File(folder), new String[]{"in"}, false);
    }

}
