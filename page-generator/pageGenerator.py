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
    return lines[0]


def main():
    dataFolder = '../data/'
    dataFileExtension = '.txt'
    destinationFolderName = '../generated-pages/pages/'

    if os.path.exists(destinationFolderName):
        shutil.rmtree(destinationFolderName)
        os.makedirs(destinationFolderName)

    pageTemplateFile = open('templates/pageTemplate.html')
    template = pageTemplateFile.read()

    dataFileNameList = getDataFileNameList(dataFolder, dataFileExtension)

#    for i in range(0, 1):
    ##TODO: revert
    for i in range(0, len(dataFileNameList)):
        dataFileName = dataFileNameList[i]
        index = i+1
        nextPageHref = ''
        if i < len(dataFileNameList)-1: #not the last element
            nextPageHref = getPageHref(dataFileNameList[i+1])

        outputFileName = getPageHref(dataFileName)

        ##TODO: try catch!
        dataFile = open(dataFolder + dataFileName)
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

        outputFilePath = destinationFolderName + outputFileName
        outputFile = open(outputFilePath, 'w')
        outputFile.write(html)


if __name__ == "__main__":
    sys.exit(main())
