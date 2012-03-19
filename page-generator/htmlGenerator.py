from translationMatcher import TranslationMatcher

translationMatcher = TranslationMatcher()

def getHtmlForWord(word):
    match = translationMatcher.getMatchForWord(word)
    if match:
        return word[0:match.start] + u'<a href="#" class="tip" title="' + match.root + ' : ' + match.translation + u'">' + word[match.start:match.end] + u'</a>' + word[match.end:]
    else:
        return word

def getHtmlForLine(line):
    ##TODO: comma, dot, etc in line??

    words = line.split(u' ')
    lineContent = ' '.join([getHtmlForWord(word) for word in words])
    return u'<p class="line"><a class="lineTipToggler" href="#"><img src="../resources/img/lineTip.png"/></a>' + lineContent + u'</p>'



