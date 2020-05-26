class toimitus:
    """Luokka määrittelee toimitettavat esineet"""

    nimi = ""
    osoite = ""

def lisaa():
    asikas = input("Asikas nimi: ")
    paikka = input("Anna toimitusosoite: ")

    paketti = toimitus()
    paketti.nimi = asikas
    paketti.osoite = paikka
    return paketti

def main():
    kierros = []
    maara = int(input("Kuinka monta toimitusta?: "))
    for i in range(0,maara):
        toimitus = lisaa()
        kierros.append(toimitus)
    print("Vierailtavat paikat:")

    for i in range(0, maara):
        print(kierros[i].nimi + ":" + kierros[i].osoite)

if __name__ == "__main__":
    main()

