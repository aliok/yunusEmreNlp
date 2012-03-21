#
# Copyright [2012] [Ali Ok - aliok@apache.org]
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

import os
import shutil
import sys
import codecs

entrySplitChar = ':'
synonymSplitChar = ','

def getEntries(line):
    line = line.strip()
    line = line.lower()
    if line.endswith('.'):
        line = line[:len(line) - 1]

    (word, translation) = line.split(entrySplitChar, 2)

    word = word.strip()
    translation = translation.strip()

    entries = []

    commaIndex = word.find(synonymSplitChar)
    if commaIndex != -1:
        synonyms = word.split(synonymSplitChar)
        for synonym in synonyms:
            entries.append((synonym.strip(), translation))
    else:
        entries.append((word, translation))

    return entries


def readEntries(srcFileName):
    allEntries = []
    with codecs.open(srcFileName, 'r', 'utf-8') as srcFile:
        for line in srcFile:
            allEntries += getEntries(line)

    return allEntries


def calculateFileCount(allEntries, entriesInOneFile):
    fileCount = len(allEntries) / entriesInOneFile
    if len(allEntries) % entriesInOneFile != 0:
        fileCount += 1
    return fileCount


def deleteAndRecreateFolder(destinationFolderName):
    if os.path.exists(destinationFolderName):
        shutil.rmtree(destinationFolderName)
    os.makedirs(destinationFolderName)


def createDictionaryFile(entriesToWrite, dictionaryFileName):
    print 'Creating dictionary file {0}'.format(dictionaryFileName)
    with open(dictionaryFileName, 'w') as destinationFile:
        #manual work to have a better file layout
        destinationFile.write('entries = [')
        destinationFile.write(',\n'.join([repr(entry) for entry in entriesToWrite]))
        destinationFile.write(']')


def createDictionaryImportFile(dictionaryImportFileName, fileCount):
    with open(dictionaryImportFileName, 'w') as dictionaryImportFile:
        for i in range(0, fileCount):
            dictionaryImportFile.write('import dictionary{0}\n'.format(i))

        dictionaryImportFile.write(
            '\nentries = ' + '+'.join(['dictionary{0}.entries '.format(i) for i in range(0, fileCount)]))


def createModuleFile(destinationFolderName):
    with open(destinationFolderName + '__init__.py', 'w'):
        pass


def main():
    entriesInOneFile = 500
    destinationFolderName = '../page-generator/dictionary/'

    allEntries = readEntries('wordSrc.txt')
    print 'Found {0} entries'.format(len(allEntries))

    fileCount = calculateFileCount(allEntries, entriesInOneFile)
    print 'Writing entries in {0} files to {1}'.format(fileCount, destinationFolderName)

    print 'Deleting and recreating destination folder "{0}"'.format(destinationFolderName)
    deleteAndRecreateFolder(destinationFolderName)

    # since page-generator runs in Jython and Jython has a max
    # code-file limitation, divide result to entriesInOneFile entries

    for i in range(0, fileCount):
        entriesToWrite = allEntries[i * entriesInOneFile: (i + 1) * entriesInOneFile]
        dictionaryFileName = destinationFolderName + 'dictionary{0}.py'.format(i)
        createDictionaryFile(entriesToWrite, dictionaryFileName)

    dictionaryImportFileName = destinationFolderName + 'dictionary.py'
    print 'Creating dictionary import file {0}'.format(dictionaryImportFileName)
    createDictionaryImportFile(dictionaryImportFileName, fileCount)

    print 'Creating __init__.py file'
    createModuleFile(destinationFolderName)

if __name__ == "__main__":
    sys.exit(main())
