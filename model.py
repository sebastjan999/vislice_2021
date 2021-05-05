# 2.)
import random
STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'w'
PORAZ = 'x'

# 3.)


class Igra:
    # 1.

    def __init__(self, geslo, crke):
        self.geslo = geslo
        # ce tko zapisemo crke[:] to uresnic pol nardimo kopijo, to je ce nocmo da se nm un seznam crke k je v funk init spreminja
        self.crke = crke[:]
# 2.

    def napacne_crke(self):
        # napcne crke so une k so v seznamu crke in niso v seznamu geslo
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        # pravilne crke so une k so v seznamu crke in hkrati tudi v seznamu geslo
        return [crka for crka in self.crke if crka in self.geslo]
# 3.

    def stevilo_napak(self):
        return len(self.napacne_crke())
# 4.

    def zmaga(self):
        vse_crke = True
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                pass
            else:
                vse_crke = False
                break
        return STEVILO_DOVOLJENIH_NAPAK >= self.stevilo_napak() and vse_crke

    def poraz(self):
        return STEVILO_DOVOLJENIH_NAPAK < self.stevilo_napak()
        # za vse_crke bi lahk tut z izpeljanim sez v eni vrstici sprogramiral
        # vse_crke = all(crka in self.crke for crka in self.geslo)

# 5.

    def pravilni_del_gesla(self):
        delni = ''
        ugibanje = [crka.upper() for crka in self.crke]
        for crka in self.geslo:
            if crka.upper() in ugibanje:
                delni += crka + ' '
            else:
                delni += '_'
        return delni.strip()


# 6.

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

# 7.

    def ugibaj(self,crka):
        velika_crka = crka.upper()
        self.crke.append(velika_crka)
        if self.zmaga():
            return ZMAGA
        elif self.poraz():
            return PORAZ
        else:
            if velika_crka in self.pravilne_crke():
                return PRAVILNA_CRKA
            elif velika_crka in self.napacne_crke():
                return NAPACNA_CRKA
            elif velika_crka in self.crke:
                return PONOVLJENA_CRKA
 
# 4.)


with open('vislice_2021/besede.txt', 'r', encoding='utf-8') as f:
    bazen_besed = [beseda.strip().upper() for beseda in f.readlines()]

random.choice(bazen_besed)
# 5.)


def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])



#dod iz git repozitorija
class Vislice:

    def __init__(self):
        self.igre = {}
 
    def prost_id_igre(self): # id igralca, ce slovar prazn vrnemo 0,
        if len(self.igre) == 0: # ce pa smo ze mel kksn kljuc je pa nou id najlazi nardit tko, 
            return 0 #da vrnemo najvecji kljuc + 1 :), torej ce mamo 10 igralcev bojo njihovi idji: 1,2,3,4,5,6,7,8,9,10 :)
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = nova_igra() # igra je funkcija, ki ni definirana znotraj nobenga classa tko da ns ne napisemo spredi(glej 95 vrstico)
        self.igre[id_igre] = (igra, ZACETEK)
        return id_igre

    def ugibaj(self,id_igre,crka): #ko ugibamo crko mormo vedt katero igro igramo pa kero crko smo zbrali
        igra = self.igre[id_igre]
        poskus = igra.ugibaj(crka)
        self.igre[id_igre] = (igra,poskus)






# testi :)
# _____________________________________________________________________________________________
testno_geslo = 'DEŽUJE'
testne_crke = ['A', 'E', 'I', 'O', 'U', 'D', 'J', 'K', 'Ž']
igra = Igra(testno_geslo, testne_crke)
print(testno_geslo)

igra.zmaga()
igra.stevilo_napak()
igra.napacne_crke()
igra.pravilne_crke()
igra.geslo
# __________________________________________________________________________________________________
igra = nova_igra()
igra.ugibaj('e')
igra.ugibaj('i')
igra.ugibaj('o')
igra.pravilni_del_gesla()
igra.ugibaj('k')
igra.ugibaj('l')
igra.stevilo_napak()
igra.ugibaj('a')
igra.napacne_crke()
igra.pravilni_del_gesla()
