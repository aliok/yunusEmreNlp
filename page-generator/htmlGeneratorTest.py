# coding=utf-8
import sys
import unittest
import htmlGenerator

class HtmlGeneratorTest(unittest.TestCase):

    def setUp(self):
        super(HtmlGeneratorTest, self).setUp()

    def testSplitLine(self):
        splits = htmlGenerator.splitLine(u'Teferrüc eyleyi vardım')
        assert splits ==[u'Teferrüc', u' ', u'eyleyi', u' ' , u'vardım'], splits

        splits = htmlGenerator.splitLine(u'Teferrüc, eyleyi vardım')
        assert splits ==[u'Teferrüc', u',', u'', u' ', u'eyleyi', u' ' , u'vardım'], splits

        splits = htmlGenerator.splitLine(u'Teferrüc, ,eyleyi vardım')
        assert splits ==[u'Teferrüc', u',', u'', u' ', u'', u',', u'eyleyi', u' ' , u'vardım'], splits

        splits = htmlGenerator.splitLine(u'Teferrüc, ,eyleyi. vardım?')
        assert splits ==[u'Teferrüc', u',', u'', u' ', u'', u',', u'eyleyi', u'.', u'', u' ', u'vardım', u'?', u''], splits

        splits = htmlGenerator.splitLine(u'Teferrüc, ,eyleyi-vardım?')
        assert splits ==[u'Teferrüc', u',', u'', u' ', u'', u',', u'eyleyi', u'-', u'vardım', u'?', u''], splits

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

    def testGetHtmlForWord_empty(self):
        assert htmlGenerator.getHtmlForWord(u'') == u''
        assert htmlGenerator.getHtmlForWord(u' ') == u' '
        assert htmlGenerator.getHtmlForWord(u'  \t  ') == u'  \t  '
        assert htmlGenerator.getHtmlForWord(u'  \t , ') == u'  \t , '
        assert htmlGenerator.getHtmlForWord(u',  \t  ') == u',  \t  '
        assert htmlGenerator.getHtmlForWord(u', ,') == u', ,'
        assert htmlGenerator.getHtmlForWord(u', \t ,') == u', \t ,'

    def testGetHtmlForLine_withoutPunctuation(self):
        line = u'Teferrüc sinlerine kılanlar iyi mi acaba?'      #sentence doesn't make any sense!
        html = htmlGenerator.getHtmlForLine(line)
        assert html==u'<p class="line"><a class="lineTipToggler" href="#"><img src="../resources/img/lineTip.png"/></a>' \
                     u'<a href="#" class="tip" title="teferrüc : gezinti">Teferrüc</a> <a href="#" class="tip" title="sin : mezar">sin</a>lerine ' \
                     u'<a href="#" class="tip" title="kılmak : etmek, eylemek, yapmak">kıl</a>anlar iyi mi acaba?</p>', repr(html)

    def testGetHtmlForLine_withPunctuation1(self):
        line = u'Teferrüc sinlerine , kılanlar iyi mi acaba?'      #sentence doesn't make any sense!
        html = htmlGenerator.getHtmlForLine(line)
        assert html==u'<p class="line"><a class="lineTipToggler" href="#"><img src="../resources/img/lineTip.png"/></a>'\
                     u'<a href="#" class="tip" title="teferrüc : gezinti">Teferrüc</a> <a href="#" class="tip" title="sin : mezar">sin</a>lerine , '\
                     u'<a href="#" class="tip" title="kılmak : etmek, eylemek, yapmak">kıl</a>anlar iyi mi acaba?</p>', repr(html)

    def testGetHtmlForLine_withPunctuation2(self):
        line = u'Teferrüc sinlerine, kılanlar iyi mi acaba?'      #sentence doesn't make any sense!
        html = htmlGenerator.getHtmlForLine(line)
        assert html==u'<p class="line"><a class="lineTipToggler" href="#"><img src="../resources/img/lineTip.png"/></a>'\
                     u'<a href="#" class="tip" title="teferrüc : gezinti">Teferrüc</a> <a href="#" class="tip" title="sin : mezar">sin</a>lerine, '\
                     u'<a href="#" class="tip" title="kılmak : etmek, eylemek, yapmak">kıl</a>anlar iyi mi acaba?</p>', repr(html)

    def testGetHtmlForLine_withPunctuation3(self):
        line = u'Teferrüc ,sinlerine, kılanlar iyi mi acaba?'      #sentence doesn't make any sense!
        html = htmlGenerator.getHtmlForLine(line)
        assert html==u'<p class="line"><a class="lineTipToggler" href="#"><img src="../resources/img/lineTip.png"/></a>'\
                     u'<a href="#" class="tip" title="teferrüc : gezinti">Teferrüc</a> ,<a href="#" class="tip" title="sin : mezar">sin</a>lerine, '\
                     u'<a href="#" class="tip" title="kılmak : etmek, eylemek, yapmak">kıl</a>anlar iyi mi acaba?</p>', repr(html)

    def testGetHtmlForLine_withPunctuation3(self):
        line = u'Teferrüc,sinlerine, kılanlar iyi mi acaba?'      #sentence doesn't make any sense!
        html = htmlGenerator.getHtmlForLine(line)
        assert html==u'<p class="line"><a class="lineTipToggler" href="#"><img src="../resources/img/lineTip.png"/></a>'\
                     u'<a href="#" class="tip" title="teferrüc : gezinti">Teferrüc</a>,<a href="#" class="tip" title="sin : mezar">sin</a>lerine, '\
                     u'<a href="#" class="tip" title="kılmak : etmek, eylemek, yapmak">kıl</a>anlar iyi mi acaba?</p>', repr(html)

    def testGetHtmlCouplet(self):
        line1 = u'sinlerine,'      #sentence doesn't make any sense!
        line2 = u'sinlerini.'      #sentence doesn't make any sense!
        html = htmlGenerator.getHtmlForCouplet([line1, line2])
        assert html==u'<p class="line"><a class="lineTipToggler" href="#"><img src="../resources/img/lineTip.png"/></a>'\
                     u'<a href="#" class="tip" title="sin : mezar">sin</a>lerine,</p>'\
                     u'\n'\
                     u'<p class="line"><a class="lineTipToggler" href="#"><img src="../resources/img/lineTip.png"/></a>'\
                     u'<a href="#" class="tip" title="sin : mezar">sin</a>lerini.</p>' , repr(html)

if __name__ == "__main__":
    unittest.main()
