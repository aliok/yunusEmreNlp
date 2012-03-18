from net.zemberek.tr.yapi.ek import TurkceEkAdlari
from net.zemberek.yapi.ek import Ek
from net.zemberek.islemler import KelimeUretici
from dictionary import dictionary
from net.zemberek.erisim import Zemberek
from net.zemberek.tr.yapi import TurkiyeTurkcesi
from net.zemberek.yapi import KelimeTipi


class Match:
    pass

class TranslationMatcher:
    def __init__(self):
        languageSettings = TurkiyeTurkcesi()
        zemberek = Zemberek(languageSettings);

        grammar = zemberek.dilBilgisi()
        suffixManager = grammar.ekler()
        alphabet = grammar.alfabe()
        suffixGenerator = languageSettings.ekUretici(alphabet);

        infinitiveSuffix = suffixManager.ek(TurkceEkAdlari.FIIL_MASTAR_MEK)

        # an empty suffix (workaroundSuffix here) is required to be added when creating the infinitive
        # form of the verb. See http://code.google.com/p/zemberek/issues/detail?id=117
        workaroundSuffix = Ek("WORKAROUND")
        workaroundSuffix.setUretimBilesenleri([])
        workaroundSuffix.setEkKuralCozumleyici(suffixGenerator)
        infinitiveSuffix.ardisilEkler().add(workaroundSuffix)

        self.zemberek = zemberek
        self.dictionary = dict(dictionary.entries)
        self.infinitiveSuffix = infinitiveSuffix
        self.workaroundSuffix = workaroundSuffix

    def getMatchForWord(self, word):
        if not word:
            return None

        word = word.lower()

        ##TODO: extract to method, it used 3 times
        #first look for a direct match
        if self.dictionary.has_key(word):
            translation = self.dictionary[word]

            match = Match()

            match.start = 0
            match.end = len(word)
            match.root = word
            match.translation = translation

            return match

        else:
            parts = self.zemberek.kelimeCozumle(word)
            parts = sorted(parts, key=lambda (s): len(s.kok().icerik()), reverse=True)

            for part in parts:
                root = part.kok()
                rootContent = root.icerik()
                rootWordType = root.tip()

                if rootWordType==KelimeTipi.FIIL:
                    rootInfinitive = self.getVerbInfinitive(root)
                    if self.dictionary.has_key(rootInfinitive):
                        translation = self.dictionary[rootInfinitive]

                        match = Match()

                        match.start = 0
                        match.end = len(rootContent)
                        match.root = rootInfinitive
                        match.translation = translation

                        return match

                else:
                    if self.dictionary.has_key(rootContent):
                        translation = self.dictionary[rootContent]

                        match = Match()

                        match.start = 0
                        match.end = len(rootContent)
                        match.root = rootContent
                        match.translation = translation

                        return match

        return None


    def getVerbInfinitive(self, root):
        # an empty suffix (workaroundSuffix here) is required to be added when creating the infinitive
        # form of the verb. See http://code.google.com/p/zemberek/issues/detail?id=117
        return self.zemberek.kelimeUret(root, [self.infinitiveSuffix, self.workaroundSuffix])
