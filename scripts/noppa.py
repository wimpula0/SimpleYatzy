"""Täällä funktio, joka arpoo noppien silmäluvut"""

import random

def noppien_heitto():
    """Arpoo 5 silmälukua."""

    nopat = []
    for _ in range(1, 6):
        nopat.append(random.randint(1,6))

    print(f"Heitetyt nopat: {nopat}")
    return nopat

def noppien_vaihto(nopat):
    """Heittää käyttäjän valitsemat nopat uudelleen."""
    vaihdettavat_nopat = []
    vaihto = input("Valitse nopat, jotka haluat vaihtaa (numerot 1-5): ")

    for i in vaihto:
        if i.isdigit():
            vaihdettavat_nopat.append(int(i))
    
    # Pitää vielä vaihtaa valitut nopat uusiin rand. lukuihin:
    # for i in vaihdettavat:
    #   nopat[vaihdettavat[i]] = rand.randint(1,6) or something??


    print(vaihdettavat_nopat)
    return nopat
            




noppien_vaihto(noppien_heitto())
