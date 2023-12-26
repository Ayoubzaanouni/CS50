substitution = {'a': '#', 'b': '@', 'c': '$', 'd': '%', 'e': '^',
                'f': '&', 'g': '*', 'h': '(', 'i': ')', 'j': '-',
                'k': '+', 'l': '=', 'm': '[', 'n': ']', 'o': '{',
                'p': '}', 'q': ';', 'r': ':', 's': ',', 't': '.',
                'u': '<', 'v': '>', 'w': '/', 'x': '?', 'y': '|',
                'z': '~'}

def encrypt(text, shift, substitution_key):
    text= text.lower()
    text = [substitution_key[char] if char in substitution_key else char for char in text]
    text = "".join(text)

    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_char = chr((ord(char.upper()) - 65 + shift) % 26 + 65)
            if char.islower():
                shift_char = shift_char.lower()
            encrypted_text += shift_char
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(encrypted_text, shift, substitution_key):
    substitution_key_inv = {v: k for k, v in substitution_key.items()}
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift_char = chr((ord(char.upper()) - 65 - shift + 26) % 26 + 65)
            if char.islower():
                shift_char = shift_char.lower()
            decrypted_text += shift_char
        else:
            decrypted_text += char

    decrypted_text = [substitution_key_inv[char] if char in substitution_key_inv else char for char in decrypted_text]
    decrypted_text = "".join(decrypted_text)

    return decrypted_text

def main():
    plaintext = input("Enter the plaintext message: ")

    shift = int(input("Enter the shift amount: "))

    encoded_message = encrypt(plaintext, shift, substitution)
    print("Encoded message: ", encoded_message)


    decoded_message = decrypt(encoded_message, shift, substitution)
    print("Decoded message: ", decoded_message)

if __name__ == "__main__":
    main()