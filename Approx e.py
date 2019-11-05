def fact(i):
    if i < 2:
        return 1
    else:
        return i * fact(i - 1)


if __name__ == "__main__":
    e = 0
    n = int(input("valeur de n ?"))
    for i in range(n):
        e += 1 / fact(i)

    print(e)
