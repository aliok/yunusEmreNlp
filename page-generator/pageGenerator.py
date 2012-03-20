# coding=utf-8
import os
import shutil
import sys
import coupletCreator

import htmlGenerator

def getDataFileNameList(dataFolder, dataFileExtension):
    dataFiles = os.listdir(dataFolder)
    return filter(lambda fileName : fileName.endswith(dataFileExtension), dataFiles)


def getPageHref(dataFileName):
    return dataFileName + '.html'


def getTitle(lines):
    firstLine = lines[0]
    if not firstLine[-1].isalpha():
        firstLine = firstLine[:-1]
    return firstLine


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


def main():
    dataFolder = '../data/'
    dataFileExtension = '.txt'
    destinationFolderName = '../generated-pages/pages/'

    clearDestinationFolder(destinationFolderName)

    template = readPageTemplate()

    dataFileNameList = getDataFileNameList(dataFolder, dataFileExtension)

    indexContent = ''

    for i in range(0, len(dataFileNameList)):
        dataFileName = dataFileNameList[i]
        print 'Processing input file ' + dataFileName
        index = i+1
        nextPageHref = ''
        if i < len(dataFileNameList)-1: #not the last element
            nextPageHref = getPageHref(dataFileNameList[i+1])

        outputFileName = getPageHref(dataFileName)
        outputFilePath = destinationFolderName + outputFileName

        ##TODO: try catch!
        dataFile = open(dataFolder + dataFileName)
        outputFile = open(outputFilePath, 'w')
        try:
            lines = [line.decode('utf-8').strip() for line in dataFile.readlines()]    # we'll use lines more than once, so let's get them on memory
            title = str(index) + '. ' + getTitle(lines)
            couplets = coupletCreator.createCouplets(lines)

            htmlForFile = htmlGenerator.getHtmlForCouplets(couplets)

            html = template
            html = html.replace('#{title}', title.encode('utf-8'))
            html = html.replace('#{content}', htmlForFile.encode('utf-8'))
            html = html.replace('#{titleVar}', title.encode('utf-8'))
            html = html.replace('#{urlVar}', outputFileName)
            html = html.replace('#{nextPageUrl}', nextPageHref)

            outputFile.write(html)

            indexContent += '<li><a href="' + outputFileName + '">' + title + '</a></li>\n'
        finally:
            dataFile.close()
            outputFile.close()

    indexTemplateFile = open('templates/indexTemplate.html')
    indexOutputFile = open(destinationFolderName + 'index.html', 'w')

    try:
        indexTemplate = indexTemplateFile.read()
        html = indexTemplate.replace('#{index}', indexContent.encode('utf-8'))
        indexOutputFile.write(html)
    finally:
        indexOutputFile.close()
        indexTemplateFile.close()

if __name__ == "__main__":
    sys.exit(main())
