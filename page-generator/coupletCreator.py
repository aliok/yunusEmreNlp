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

from nlpToolAdapter import NlpToolAdapter

nlpToolAdapter = NlpToolAdapter()

def createCouplets(lines):
    coupletSize = _getCoupletSize(lines)

    _verifyCoupletSize(lines, coupletSize)

    lines = _removeEmptyLines(lines)

    couplets = _createCoupletsList(lines, coupletSize)

    #Some hardcoded stuff, I feel sorry :(
    if coupletSize == 4:
        couplets = _changeCoupletSizeToTwo(couplets)

    return couplets


def _getCoupletSize(lines):
    """
    Returns the couplet (TR: beyit) length. Generally 2 or 4.
    See http://en.wikipedia.org/wiki/Couplet
    """
    index = 0
    for line in lines:
        if line == '':
            break
        index += 1

    return index


def _verifyCoupletSize(lines, coupletSize):
    # check if the couplet size is same for all couplets
    if len(lines) % (coupletSize + 1):
        raise repr('Couplet size ' + str(coupletSize) + ' cannot be verified for title : ' + lines[0])
    for i in range(coupletSize, len(lines), (coupletSize + 1)):
        if lines[i] != '':
            raise repr('Couplet size ' + str(coupletSize) + ' cannot be verified for title : ' + lines[0])


def _removeEmptyLines(lines):
    return filter(lambda (s): s != '', lines)

def _createCoupletsList(lines, coupletSize):
    couplets = []
    for i in range(0, len(lines) / coupletSize):
        couplet = []
        for j in range(0, coupletSize):
            couplet.append(lines[coupletSize * i + j])
        couplets.append(couplet)

    return couplets

def _mergeLines(firstLine, secondLine):
    if not firstLine[-1].isalpha():
        firstLine = firstLine[:-1]

    indexOfFirstSpaceInSecondLine = secondLine.find(' ')
    if indexOfFirstSpaceInSecondLine != -1:
        firstWordOfSecondLine = secondLine[0:indexOfFirstSpaceInSecondLine]
        if firstWordOfSecondLine[0].isupper() and not nlpToolAdapter.isProperNoun(firstWordOfSecondLine):
            secondLine = secondLine[0].lower() + secondLine[1:]

    return firstLine + ', ' + secondLine


def _changeCoupletSizeToTwo(couplets):
    #Some hardcoded stuff, I feel sorry :(

    newCouplets = []
    for couplet in couplets:
        newCouplet = [_mergeLines(couplet[0], couplet[1]), _mergeLines(couplet[2], couplet[3])]
        newCouplets.append(newCouplet)

    return newCouplets
