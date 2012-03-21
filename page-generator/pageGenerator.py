# coding=utf-8
import os
import shutil
import sys
import coupletCreator

import htmlGenerator

def getDataFileNameList(dataFolder, dataFileExtension):
    dataFiles = os.listdir(dataFolder)
    return filter(lambda fileName: fileName.endswith(dataFileExtension), dataFiles)


def getPageHref(dataFileName):
    return dataFileName + '.html'


def getTitle(lines, fileIndex):
    firstLine = lines[0]
    if not firstLine[-1].isalpha():
        firstLine = firstLine[:-1]

    return str(fileIndex) + '. ' + firstLine


def clearDestinationFolder(destinationFolderName):
    if os.path.exists(destinationFolderName):
        shutil.rmtree(destinationFolderName)
        os.makedirs(destinationFolderName)


def readPageTemplate():
    pageTemplateFile = open('templates/pageTemplate.html')
    try:
        pageTemplateFile = open('templates/pageTemplate.html')
        template = pageTemplateFile.read()
        return template
    finally:
        pageTemplateFile.close()


def generatePageContent(template=None, lines=None, title=None, outputFileName=None, nextPageHref=None):
    couplets = coupletCreator.createCouplets(lines)

    htmlForFile = htmlGenerator.getHtmlForCouplets(couplets)

    html = template
    html = html.replace('#{title}', title.encode('utf-8'))
    html = html.replace('#{content}', htmlForFile.encode('utf-8'))
    html = html.replace('#{titleVar}', title.encode('utf-8'))
    html = html.replace('#{urlVar}', outputFileName)
    html = html.replace('#{nextPageUrl}', nextPageHref)

    return html


def writeToFile(outputFilePath, content):
    outputFile = open(outputFilePath, 'w')
    try:
        outputFile.write(content)
    finally:
        outputFile.close()


def readLines(dataFilePath):
    dataFile = open(dataFilePath)
    try:
        return [line.decode('utf-8').strip() for line in dataFile.readlines()]
    finally:
        dataFile.close()


def createIndexFile(indexContent, destinationFolderName):
    indexTemplateFile = open('templates/indexTemplate.html')
    indexOutputFile = open(destinationFolderName + 'index.html', 'w')

    try:
        indexTemplate = indexTemplateFile.read()
        html = indexTemplate.replace('#{index}', indexContent.encode('utf-8'))
        indexOutputFile.write(html)
    finally:
        indexOutputFile.close()
        indexTemplateFile.close()


def main():
    dataFolder = '../data/'
    dataFileExtension = '.txt'
    destinationFolderName = '../generated-pages/pages/'

    clearDestinationFolder(destinationFolderName)

    pageTemplate = readPageTemplate()

    dataFileNameList = getDataFileNameList(dataFolder, dataFileExtension)

    indexContent = ''

    for i in range(0, len(dataFileNameList)):
        dataFileName = dataFileNameList[i]
        print 'Processing input file ' + dataFileName

        fileIndex = i + 1

        nextPageHref = ''
        if i < len(dataFileNameList) - 1: #not the last element
            nextPageHref = getPageHref(dataFileNameList[i + 1])

        outputFileName = getPageHref(dataFileName)

        # we'll use lines more than once, so let's get them on memory
        lines = readLines(dataFolder + dataFileName)

        title = getTitle(lines, fileIndex)

        html = generatePageContent(pageTemplate, lines, title, outputFileName, nextPageHref)

        writeToFile(destinationFolderName + outputFileName, html)

        indexContent += '<li><a href="' + outputFileName + '">' + title + '</a></li>\n'


    createIndexFile(indexContent, destinationFolderName)

if __name__ == "__main__":
    sys.exit(main())
