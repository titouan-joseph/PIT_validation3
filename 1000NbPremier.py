def ispremier(nb):
    for i in range(2, nb):
        if nb % i == 0:
            return False
    return True


f = open("premierspremiers.txt", "w")
count = 0
nb = 1

while count < 1000:
    if ispremier(nb):
        f.write(str(nb) + "\n")
        count += 1
    nb += 1

f.close()
f = open("premierspremiers.txt", "r")
sum = 0
for nb in f:
    sum += int(nb)
print(sum)
