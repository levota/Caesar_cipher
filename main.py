#def fnkce

def caesar(zprava) -> str:
    k_zasifrovani = zprava
    k_zasifrovani = k_zasifrovani.replace(" ", "")
    print(k_zasifrovani)
    posun = int(input("Zadej číslem posun: "))
    print(posun)
    sifra = ""
    for znak in k_zasifrovani:
        i = ord(znak)
        i = i + posun
        if (i > ord("z")):
            i = i - 26
        znak = chr(i)
        sifra = sifra + znak
    return print(sifra)


# Zprava
zprava = input("Zadej zprávu : ").lower().strip("?!.,)(")

# Zavolani fce
caesar(zprava)