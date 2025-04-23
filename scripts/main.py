"""Tänne actual peli"""

from noppa import noppien_heitto, noppien_vaihto
from laskut import noppien_tarkistus


def pelaa_vuoro(pelaaja_numero):
    print(f"\nPelaajan {pelaaja_numero} vuoro:\n")
    nopat = noppien_heitto()
    a = 0
    
    while a < 2:
        vaihto = input("Haluatko vaihtaa noppia? (k/e): ").lower()
        if vaihto == 'k':
            nopat = noppien_vaihto(nopat)
        elif vaihto == 'e':
            break
        a += 1
    
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
    print("- Peliä pelaa kaksi pelaajaa vuorotellen")
    print("- Jokaisella vuorolla noppia voi heittää uudestaan kaksi kertaa")
    print("- Peli kestää 3 kierrosta")
    print("- Eniten pisteitä kerännyt voittaa! :)")
    print("")
    print("-" * 80)
    print("")

    for kierros in range(1, 4):
        kierros_title = f"--- KIERROS {kierros} ---"
        kier = kierros_title.center(80)
        print(kier)
        for pelaaja in range(2):
            pelaajien_pisteet[pelaaja] += pelaa_vuoro(pelaaja + 1)
    
    
    print("\n--- Peli ohi! ---")
    for i, pisteet in enumerate(pelaajien_pisteet):
        print(f"Pelaajan {i+1} kokonaispisteet: {pisteet}")
    
    if pelaajien_pisteet[0] > pelaajien_pisteet[1]:
        print("Pelaaja 1 voitti! :D")
    elif pelaajien_pisteet[1] > pelaajien_pisteet[0]:
        print("Pelaaja 2 voitti! :D")
    else:
        print("Tasapeli! :3")

if __name__ == "__main__":
    main()