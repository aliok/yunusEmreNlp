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
