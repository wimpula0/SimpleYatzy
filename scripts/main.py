"""Tänne actual peli"""

from noppa import noppien_heitto, noppien_vaihto
from laskut import noppien_tarkistus


def pelaa_vuoro(pelaaja_numero):
    print(f"\nPelaajan {pelaaja_numero} vuoro:")
    nopat = noppien_heitto()
    
    # Mahdollisuus vaihtaa noppia kerran
    vaihto = input("Haluatko vaihtaa noppia? (k/e): ").lower()
    if vaihto == 'k':
        nopat = noppien_vaihto(nopat)
    
    pisteet = noppien_tarkistus(nopat)
    print(f"Sait {pisteet} pistettä!")
    return pisteet

def main():
    pelaajien_pisteet = [0, 0]
    
    print("-" * 80)
    title = "Y A T Z Y"
    txt = title.center(80)
    print(txt)
    print("-" * 80)
    print("")
    print("Ohjeet:")
    print(" Peliä pelaa kaksi pelaajaa vuorotellen")
    print("- Jokaisella vuorolla voit heittää noppia kerran")
    print("- Voit vaihtaa haluamasi nopat uudelleenheitolle")
    print("- Peli kestää 5 kierrosta")
    print("- Eniten pisteitä kerännyt voittaa\n")
    
    for kierros in range(1, 6):
        print(f"\n--- Kierros {kierros} ---")
        for pelaaja in range(2):
            pelaajien_pisteet[pelaaja] += pelaa_vuoro(pelaaja + 1)
    
    
    print("\n--- Peli ohi! ---")
    for i, pisteet in enumerate(pelaajien_pisteet):
        print(f"Pelaajan {i+1} kokonaispisteet: {pisteet}")
    
    if pelaajien_pisteet[0] > pelaajien_pisteet[1]:
        print("Pelaaja 1 voitti!")
    elif pelaajien_pisteet[1] > pelaajien_pisteet[0]:
        print("Pelaaja 2 voitti!")
    else:
        print("Tasapeli!")

if __name__ == "__main__":
    main()