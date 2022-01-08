teks = open("test.txt", "r")

posisii = []

for i in teks:
    posisii.append(i.split())
# print(posisii)

kombinasi_menang = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def isi_papan():

    posisi = posisii[0] + posisii[1] + posisii[2]

    print()
    print(posisi[0] + " " + posisi[1] + " " + posisi[2])
    print(posisi[3] + " " + posisi[4] + " " + posisi[5])
    print(posisi[6] + " " + posisi[7] + " " + posisi[8])
    print()


def siapa_menang(posisi):

    posisi = posisii[0] + posisii[1] + posisii[2]

    count = 0
    for a in kombinasi_menang:
            if posisi[a[0]] == posisi[a[1]] == posisi[a[2]] == "0":
                print("0 menang")
                return True

            if posisi[a[0]] == posisi[a[1]] == posisi[a[2]] == "x":
                print("x menang")
                return True
                
    for a in range(9):
            if posisi[a] == "0" or posisi[a] == "x" or posisi[a] == "_":
                count += 1


def siapa_hampir_menang(posisi):

    posisi = posisii[0] + posisii[1] + posisii[2]

    count = 0
    for b in kombinasi_menang:
        if posisi[b[0]] == '_' or posisi[b[1]] == '_' or posisi[b[2]] == '_':

            #gabisa masuk di kondisi if yg ini
            if (posisi[b[0]] == posisi[b[1]] == "0" or posisi[b[0]] == posisi[b[2]] == "0" or posisi[b[1]] == posisi[b[2]] == "0") and (posisi[b[0]] == posisi[b[1]] == "x" or posisi[b[0]] == posisi[b[2]] == "x" or posisi[b[1]] == posisi[b[2]] == "x"):
                print("0 dan x hampir menang")
                return True
            #---------------------------------

            elif posisi[b[0]] == posisi[b[1]] == "0" or posisi[b[0]] == posisi[b[2]] == "0" or posisi[b[1]] == posisi[b[2]] == "0":
                print("0 hampir menang")
                return True

            elif posisi[b[0]] == posisi[b[1]] == "x" or posisi[b[0]] == posisi[b[2]] == "x" or posisi[b[1]] == posisi[b[2]] == "x":
                print("x hampir menang")
                return True
                
    for b in range(9):
            if posisi[b] == "0" or posisi[b] == "x" or posisi[b] == "_":
                count += 1

isi_papan()

hasil = []

siapa_menang(hasil)
siapa_hampir_menang(hasil)

# if siapa_menang(hasil) != None:
#     siapa_menang
# elif siapa_hampir_menang(hasil) != None:
#     siapa_hampir_menang
# else:
#     print('none')

print()

teks.close()