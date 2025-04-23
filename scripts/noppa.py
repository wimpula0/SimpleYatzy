# R3
# Väyrynen Vilma
"""Täällä funktio, joka arpoo noppien silmäluvut ja heittää valitut nopat uudelleen"""

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

    for i in vaihdettavat_nopat:
        if 1 <= i <= len(nopat):
            nopat[i - 1] = random.randint(1,6)
    
    print("Uudet nopat: ", nopat)
    return nopat
            
