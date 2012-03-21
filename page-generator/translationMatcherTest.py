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

# coding=utf-8
import sys
import unittest
import translationMatcher

class TranslationMatcherTest(unittest.TestCase):

    def setUp(self):
        super(TranslationMatcherTest, self).setUp()
        self.translationMatcher = translationMatcher.TranslationMatcher()

    def testDirectMatch(self):
        word = u'Teferrüc'
        match = self.translationMatcher.getMatchForWord(word)

        assert match.start==0, match.start
        assert match.end==8, match.end
        assert match.root==u'teferrüc', match.root
        assert match.translation==u'gezinti', match.translation


    def testRootMatch(self):
        word = u'sinleri'
        match = self.translationMatcher.getMatchForWord(word)

        assert match.start==0, match.start
        assert match.end==3, match.end
        assert match.root==u'sin', match.root
        assert match.translation==u'mezar', match.translation

    def testRootMatch2(self):
        word = u'mihnette'
        match = self.translationMatcher.getMatchForWord(word)

        assert match.start==0, match.start
        assert match.end==6, match.end
        assert match.root==u'mihnet', match.root
        assert match.translation==u'zahmet, eziyet, gam, keder, sıkıntı, bela', match.translation

    def testVerbRootMatch(self):
        word = u'kılıp'
        match = self.translationMatcher.getMatchForWord(word)

        assert match.start==0, match.start
        assert match.end==3, match.end
        assert match.root==u'kılmak', match.root
        assert match.translation==u'etmek, eylemek, yapmak', match.translation

    def testVerbRootMatch2(self):
        word = u'kılanlara'
        match = self.translationMatcher.getMatchForWord(word)

        assert match.start==0, match.start
        assert match.end==3, match.end
        assert match.root==u'kılmak', match.root
        assert match.translation==u'etmek, eylemek, yapmak', match.translation



if __name__ == "__main__":
    unittest.main()
