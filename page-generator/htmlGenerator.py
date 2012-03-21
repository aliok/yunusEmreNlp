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

import re
from translationMatcher import TranslationMatcher

translationMatcher = TranslationMatcher()

def getHtmlForWord(word):
    stripped = word.strip()

    if stripped=='' or not stripped.isalpha():
        return word

    match = translationMatcher.getMatchForWord(word)
    if match:
        return word[0:match.start] + u'<a href="#" class="tip" title="' + match.root + ' : ' + match.translation + u'">' + word[match.start:match.end] + u'</a>' + word[match.end:]
    else:
        return word


WORD_SPLIT_PATTERN = re.compile(ur"(\W)", re.UNICODE | re.IGNORECASE)

def splitLine(line):
    return WORD_SPLIT_PATTERN.split(line)

def getHtmlForLine(line):
    words = splitLine(line)
    lineContent = ''.join([getHtmlForWord(word) for word in words])
    return u'<p class="line"><a class="lineTipToggler" href="#"><img src="../resources/img/lineTip.png"/></a>' + lineContent + u'</p>'

def getHtmlForCouplet(couplet):
    return u'\n'.join([getHtmlForLine(line) for line in couplet])

def getHtmlForCouplets(couplets):
    return u'\n</br>'.join([getHtmlForCouplet(couplet) for couplet in couplets])
