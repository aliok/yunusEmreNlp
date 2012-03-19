# coding=utf-8
import sys
import unittest
import htmlGenerator

class HtmlGeneratorTest(unittest.TestCase):

    def setUp(self):
        super(HtmlGeneratorTest, self).setUp()

    def testGetHtmlForWord_directMatch(self):
        word = u'Teferrüc'
        html = htmlGenerator.getHtmlForWord(word)
        assert html==u'<a href="#" class="tip" title="teferrüc : gezinti">Teferrüc</a>', html

    def testGetHtmlForWord_rootMatch(self):
        word = u'sinleri'
        html = htmlGenerator.getHtmlForWord(word)
        assert html==u'<a href="#" class="tip" title="sin : mezar">sin</a>leri', html

    def testGetHtmlForWord_rootMatch2(self):
        word = u'mihnette'
        html = htmlGenerator.getHtmlForWord(word)
        assert html==u'<a href="#" class="tip" title="mihnet : zahmet, eziyet, gam, keder, sıkıntı, bela">mihnet</a>te', html

    def testGetHtmlForWord_verbRootMatch(self):
        word = u'kılıp'
        html = htmlGenerator.getHtmlForWord(word)
        assert html==u'<a href="#" class="tip" title="kılmak : etmek, eylemek, yapmak">kıl</a>ıp', html

    def testGetHtmlForWord_verbRootMatch2(self):
        word = u'kılanlara'
        html = htmlGenerator.getHtmlForWord(word)
        assert html==u'<a href="#" class="tip" title="kılmak : etmek, eylemek, yapmak">kıl</a>anlara', html

    def testGetHtmlForLine_withoutPunctuation(self):
        line = u'Teferrüc sinlerine kılanlar iyi mi acaba?'      #sentence doesn't make any sense!
        html = htmlGenerator.getHtmlForLine(line)
        assert html==u'<p class="line"><a class="lineTipToggler" href="#"><img src="../resources/img/lineTip.png"/></a>' \
                     u'<a href="#" class="tip" title="teferrüc : gezinti">Teferrüc</a> <a href="#" class="tip" title="sin : mezar">sin</a>lerine ' \
                     u'<a href="#" class="tip" title="kılmak : etmek, eylemek, yapmak">kıl</a>anlar iyi mi acaba?</p>', html

    def testGetHtmlForLine_withPunctuation1(self):
        line = u'Teferrüc sinlerine , kılanlar iyi mi acaba?'      #sentence doesn't make any sense!
        html = htmlGenerator.getHtmlForLine(line)
        assert html==u'<p class="line"><a class="lineTipToggler" href="#"><img src="../resources/img/lineTip.png"/></a>'\
                     u'<a href="#" class="tip" title="teferrüc : gezinti">Teferrüc</a> <a href="#" class="tip" title="sin : mezar">sin</a>lerine , '\
                     u'<a href="#" class="tip" title="kılmak : etmek, eylemek, yapmak">kıl</a>anlar iyi mi acaba?</p>', html

    def testGetHtmlForLine_withPunctuation2(self):
        line = u'Teferrüc sinlerine, kılanlar iyi mi acaba?'      #sentence doesn't make any sense!
        html = htmlGenerator.getHtmlForLine(line)
        assert html==u'<p class="line"><a class="lineTipToggler" href="#"><img src="../resources/img/lineTip.png"/></a>'\
                     u'<a href="#" class="tip" title="teferrüc : gezinti">Teferrüc</a> <a href="#" class="tip" title="sin : mezar">sin</a>lerine, '\
                     u'<a href="#" class="tip" title="kılmak : etmek, eylemek, yapmak">kıl</a>anlar iyi mi acaba?</p>', html

if __name__ == "__main__":
    unittest.main()
