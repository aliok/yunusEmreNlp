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

from net.zemberek.yapi.ek import Ek
from net.zemberek.tr.yapi import TurkiyeTurkcesi
from net.zemberek.erisim import Zemberek
from net.zemberek.tr.yapi.ek import TurkceEkAdlari
from net.zemberek.yapi import KelimeTipi

class NlpToolAdapter:
    def __init__(self):
        languageSettings = TurkiyeTurkcesi()
        zemberek = Zemberek(languageSettings)

        grammar = zemberek.dilBilgisi()
        suffixManager = grammar.ekler()
        alphabet = grammar.alfabe()
        suffixGenerator = languageSettings.ekUretici(alphabet)

        infinitiveSuffix = suffixManager.ek(TurkceEkAdlari.FIIL_MASTAR_MEK)

        # an empty suffix (workaroundSuffix here) is required to be added when creating the infinitive
        # form of the verb. See http://code.google.com/p/zemberek/issues/detail?id=117
        workaroundSuffix = Ek("WORKAROUND")
        workaroundSuffix.setUretimBilesenleri([])
        workaroundSuffix.setEkKuralCozumleyici(suffixGenerator)
        infinitiveSuffix.ardisilEkler().add(workaroundSuffix)

        self._zemberek = zemberek
        self._infinitiveSuffix = infinitiveSuffix
        self._workaroundSuffix = workaroundSuffix

    def resolveWord(self, word):
        resolutions = self._zemberek.kelimeCozumle(word)
        resolutions = sorted(resolutions, key=lambda (s): len(s.kok().icerik()), reverse=True)

        return [self._adaptResolution(resolution) for resolution in resolutions]

    def getVerbInfinitive(self, root):
        # an empty suffix (workaroundSuffix here) is required to be added when creating the infinitive
        # form of the verb. See http://code.google.com/p/zemberek/issues/detail?id=117
        return self._zemberek.kelimeUret(root, [self._infinitiveSuffix, self._workaroundSuffix])

    def _adaptResolution(self, resolution):
        newResolution = Resolution()
        newResolution.root = resolution.kok()
        newResolution.rootContent = resolution.kok().icerik()
        newResolution.rootIsVerb = resolution.kok().tip() == KelimeTipi.FIIL
        newResolution.rootIsProperNoun = resolution.kok().tip() == KelimeTipi.OZEL
        return newResolution

    def isProperNoun(self, word):
    # TR: ozel isim mi diye bakar
    # See http://en.wikipedia.org/wiki/Proper_noun

        resolutions = self.resolveWord(word)
        for resolution in resolutions:
            if resolution.rootIsProperNoun:
                return True

        return False


class Resolution:
    def __init__(self):
        self.root = None
        self.rootContent = None
        self.rootIsVerb = False
        self.rootIsProperNoun = False