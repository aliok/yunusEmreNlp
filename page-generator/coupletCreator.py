from net.zemberek.erisim import Zemberek
from net.zemberek.tr.yapi import TurkiyeTurkcesi
from net.zemberek.yapi import KelimeTipi

zemberek = Zemberek(TurkiyeTurkcesi())


def createCouplets(lines):
    coupletSize = getCoupletSize(lines)

    # first check if the couplet size is same for all couplets
    if len(lines) % (coupletSize + 1):
        raise repr('Couplet size ' + str(coupletSize) + ' cannot be verified for title : ' + lines[0])
    for i in range(coupletSize, len(lines), (coupletSize + 1)):
        if lines[i] != '':
            raise repr('Couplet size ' + str(coupletSize) + ' cannot be verified for title : ' + lines[0])

    # remove the empty lines from the lines list
    lines = filter(lambda (s): s != '', lines)

    couplets = []
    for i in range(0, len(lines) / coupletSize):
        couplet = []
        for j in range(0, coupletSize):
            couplet.append(lines[coupletSize * i + j])
        couplets.append(couplet)

    #Some hardcoded stuff, feeling sorry :(
    if coupletSize == 4:
        couplets = changeCoupletSizeToTwo(couplets)

    return couplets


def getCoupletSize(lines):
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


def isProperNoun(word):
    # TR: ozel isim mi diye bakar
    # See http://en.wikipedia.org/wiki/Proper_noun

    resolutions = zemberek.kelimeCozumle(word)
    resolutions = sorted(resolutions, key=lambda (s): len(s.kok().icerik()), reverse=True)
    for resolution in resolutions:
        root = resolution.kok()
        if KelimeTipi.OZEL == root.tip():
            return True

    return False


def mergeLines(firstLine, secondLine):
    if not firstLine[-1].isalpha():
        firstLine = firstLine[:-1]

    indexOfFirstSpaceInSecondLine = secondLine.find(' ')
    if indexOfFirstSpaceInSecondLine != -1:
        firstWordOfSecondLine = secondLine[0:indexOfFirstSpaceInSecondLine]
        if firstWordOfSecondLine[0].isupper() and not isProperNoun(firstWordOfSecondLine):
            secondLine = secondLine[0].lower() + secondLine[1:]

    return firstLine + ', ' + secondLine


def changeCoupletSizeToTwo(couplets):
    #Some hardcoded stuff, feeling sorry :(

    newCouplets = []
    for couplet in couplets:
        newCouplet = [mergeLines(couplet[0], couplet[1]), mergeLines(couplet[2], couplet[3])]
        newCouplets.append(newCouplet)

    return newCouplets
