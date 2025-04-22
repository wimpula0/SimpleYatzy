"""Tänne funktio, joka laskee pisteet yhteen sekä funktio, joka tarkistaa nopat"""


def noppien_tarkistus(nopat):
    pisteet = 0
    kombinaatiot = {
        'yatzy': False,
        'mokki': False,
        'p_suora': False,
        'i_suora': False,
        'neljä_samaa': False,
        'kolme_samaa': False,
        'pari': False,
        'kaksi_paria': False
    }

    silmaluvut = [0] * 7  
    for noppa in nopat:
        silmaluvut[noppa] += 1

    parit = [i for i, count in enumerate(silmaluvut) if count >= 2]

    if 5 in silmaluvut:
        kombinaatiot['yatzy'] = True
        pisteet += 50
    elif 3 in silmaluvut and 2 in silmaluvut:
        kombinaatiot['mokki'] = True
        pisteet += 25
    elif sorted(nopat) == [1, 2, 3, 4, 5]:
        kombinaatiot['p_suora'] = True
        pisteet += 15
    elif sorted(nopat) == [2, 3, 4, 5, 6]:
        kombinaatiot['i_suora'] = True
        pisteet += 20
    elif 4 in silmaluvut:
        kombinaatiot['neljä_samaa'] = True
        pisteet += sum(nopat)
    elif 3 in silmaluvut:
        kombinaatiot['kolme_samaa'] = True
        pisteet += sum(nopat)
    else:
        if len(parit) >= 2:
            kombinaatiot['kaksi_paria'] = True
            pisteet += sum(p * 2 for p in parit[-2:])
        elif len(parit) == 1:
            kombinaatiot['pari'] = True
            pisteet += parit[0] * 2


    for nimi, löytyi in kombinaatiot.items():
        if löytyi:
            print(nimi.upper())

    return pisteet