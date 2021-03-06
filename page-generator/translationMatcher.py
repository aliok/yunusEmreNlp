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

from dictionary import dictionary
from nlpToolAdapter import NlpToolAdapter


class Match:
    def __init__(self, start, end, root, translation):
        self.start = start
        self.end = end
        self.root = root
        self.translation = translation

class TranslationMatcher:
    def __init__(self):
        self._dictionary = dict(dictionary.entries)
        self._nlpToolAdapter = NlpToolAdapter()

    def getMatchForWord(self, word):
        if not word:
            return None

        word = word.lower()

        directMatch = self._searchDirectMatch(word)

        if directMatch:
            return directMatch
        else:
            resolutions = self._nlpToolAdapter.resolveWord(word)

            for resolution in resolutions:
                if resolution.rootIsVerb:
                    rootInfinitive = self._nlpToolAdapter.getVerbInfinitive(resolution.root)
                    if self._dictionary.has_key(rootInfinitive):
                        translation = self._dictionary[rootInfinitive]

                        return Match(0, len(resolution.rootContent), rootInfinitive, translation)

                else:
                    if self._dictionary.has_key(resolution.rootContent):
                        return self._searchDirectMatch(resolution.rootContent)

        return None


    def _searchDirectMatch(self, word):
        if not word:
            return None

        if self._dictionary.has_key(word):
            translation = self._dictionary[word]

            return Match(0, len(word), word, translation)
        else:
            return None
