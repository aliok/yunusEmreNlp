# coding=utf-8
import os
import shutil
import sys
import codecs
import dictionary

#class Page:
#    def __init__(self, dataFileName, index, nextPageUrl):
#        self.dataFileName = dataFileName
#        self.index = index
#        self.nextPageUrl = nextPageUrl


def getDataFileNameList(dataFolder, dataFileExtension):
    dataFiles = os.listdir(dataFolder)
    return filter(lambda fileName : fileName.endswith(dataFileExtension), dataFiles)


#def createPageObjects(dataFileNameList):
#    pageObjects = []
#    for i in range(0, len(dataFileNameList)):
#        if i < len(dataFileNameList)-1: #not the last element
#            pageObjects.append(Page(dataFileNameList[0], i, ))


def getPageHref(dataFileName):
    return dataFileName + '.html'


def getTitle(dataFile):
    for line in dataFile:
        return line.strip()


def getHtmlForFile(dataFile):
    return '<br/>'.join(dataFile)


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

    for i in range(0, 1):
    ##TODO: revert
    #for i in range(0, len(dataFileNameList)):
        dataFileName = dataFileNameList[i]
        index = i+1
        nextPageHref = ''
        if i < len(dataFileNameList)-1: #not the last element
            nextPageHref = getPageHref(dataFileNameList[i+1])

        outputFileName = getPageHref(dataFileName)

        ##TODO: try catch!
        dataFile = open(dataFolder + dataFileName)
        title = str(index) + '. ' + getTitle(dataFile)
        htmlForFile = getHtmlForFile(dataFile)

        html = template
        html = html.replace('#{title}', title.encode('utf-8'))
        html = html.replace('#{content}', htmlForFile)
        html = html.replace('#{titleVar}', title.encode('utf-8'))
        html = html.replace('#{urlVar}', outputFileName)
        html = html.replace('#{nextPageUrl}', nextPageHref)

        outputFilePath = destinationFolderName + outputFileName
        outputFile = open(outputFilePath, 'w')
        outputFile.write(html)


if __name__ == "__main__":
    sys.exit(main())
