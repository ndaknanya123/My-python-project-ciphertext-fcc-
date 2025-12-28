
def cipher(text, shift, encrypt = True):
    if not encrypt:
        shift = - shift

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:]+alphabet[:shift]
    table_translate = str.maketrans(alphabet,shifted_alphabet)
    encrypted_text = text.translate(table_translate)
    return encrypted_text

def encrypt(text, shift):
    return cipher(text, shift)

def decrypt(text, shift):
    return cipher(text, shift, encrypt = False)

text = input("Berikan teks : ")
shift = int(input("jumlah shift : "))

encrypted_text = encrypt(text,shift)
decrypted_text = decrypt(encrypted_text,shift)
print(encrypted_text)
print(decrypted_text)

