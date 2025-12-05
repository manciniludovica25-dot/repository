import random
import elenco_parole
import immagini_impiccato


print(immagini_impiccato.logo)

parola_scelta=random.choice(elenco_parole.word_list)

print(parola_scelta)
display = ["_"] * len(parola_scelta)
lista_lettere = []

vite = 6
print("".join(display))

game_over=False

while game_over == False :
    print(f"vite: {vite}")
    scelta = input("scegli la lettera\n").lower()

    if scelta in lista_lettere:
        print("lettera già scelta")
        continue

    lista_lettere.append(scelta)

    trovata = False

    for index, letter in enumerate(parola_scelta):
        if letter == scelta:
            display[index] = letter
            trovata = True

    if trovata == True:
        print("".join(display))
        if "_" not in display:
            print("".join(display))
            print("Hai Vinto!")
            game_over = True
    else:
        vite -=1
        print(immagini_impiccato.stages[vite])
        if vite == 0:
            game_over =True
            print("Hai Perso!")




