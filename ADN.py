def valide(ADN):
    isok = True
    for lettre in ADN:
        if lettre not in ["a", "t", "g", "c"]:
            isok = False

    return isok


def saisie():
    chaine = input("saisir ADN")

    if valide(chaine):
        return chaine

    else:
        print("Chane ADN non vlaide")
        return None


def proportion(c, ADN):
    nb = ADN.count(c)
    tot = len(ADN)/len(c)

    return "il y a {} % de séquence '{}' dans votre chaîne".format((nb / tot)*100, c)


if __name__ == "__main__":
    a = "atgctga"
    b = "az"

    print(valide(a))
    print(valide(b))
    #    saisie()
    print(proportion("ca","caagcatca"))
    print(proportion("ca", saisie()))
