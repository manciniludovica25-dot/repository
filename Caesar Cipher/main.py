import alphabet

def encrypt(original_text, shift_amount):

    frase_criptata=[]
    lunghezza_lista = len(alphabet.alphabet)

    for letter in original_text:
        if letter in alphabet:
            posizione_variata = (alphabet.index(letter) + shift_amount) % lunghezza_lista
            lettera_criptata=alphabet[posizione_variata]
            frase_criptata.append(lettera_criptata)

    testo_criptato = "".join(frase_criptata)
    print(f"Here is the encode result: {testo_criptato}")


def decrypt (original_text, shift_amount):

    frase_decriptata=[]
    lunghezza_lista = len(alphabet.alphabet)

    for letter in original_text:
        if letter in alphabet:
            posizione_variata = (alphabet.index(letter) - shift_amount) % lunghezza_lista
            lettera_decriptata=alphabet[posizione_variata]
            frase_decriptata.append(lettera_decriptata)

    testo_decriptato = "".join(frase_decriptata)
    print(f"Here is the decode result: {testo_decriptato}")



def caesar(scelta, original_text, shift_amount):
    if scelta == "encode":
        encrypt(original_text, shift_amount)
    elif scelta == "decode":
        decrypt(original_text, shift_amount)

def continua():
    end = "y"
    while end == "y":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(direction, text, shift)

        end = input("Vuoi continuare? (y/n): ").lower()

continua()