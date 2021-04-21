import model


def izpis_igre(igra):
    tekst = f"""########################\n
    Pravilni del gesla: {igra.pravilni_del_gesla()}\n
    Število poskusov: {model.STEVILO_DOVOLJENIH_NAPAK + 1 - igra.stevilo_napak()} \n
    Nepravilne črke: {igra.nepravilni_ugibi()}
    ########################\n
    """
    return tekst


def izpiz_zmage(igra):
    tekst = f"""########################\n
    Bravo! Zmagali ste!\n
    Uganili ste geslo: {igra.pravilni_del_gesla()}\n
    ########################\n"""
    return tekst


def izpis_poraza(igra):

    tekst = f"""########################\n
    Porabili ste vse poskuse.\n
    Pravilno geslo: {igra.geslo}\n
    ########################\n"""
    return tekst


def zahtevaj_vnos():
    return input('Vnesite črko:')

#def zahtevaj_moznost():
 #   return input('zahtevaj')

#def ponudi_moznosti():
 #   tekst = f""" Vpišite črko za izbor naslednjih možnosti:\n
  #  p : ponovni zagon igre\n
   # i : izhod\n
    #"""
    #return tekst

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        stanje = igra.ugibaj(crka)
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break
        
pozeni_vmesnik()

#testne_crke = ['A', 'I', "O", "U", "D", "J" ]
#testna_igra = model.igra()
# print(izpis_igre(testna_igra))

#5)  nadgradnja vmesnika

