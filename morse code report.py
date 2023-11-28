# Morse code dictionary
morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-', 'D': '-..', 'E': '.', 'F': '..-.',
                   'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                   'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..',
                   '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                   '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
                   '/': '-..-.','(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
                   ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
                   '"': '.-..-.', '$': '...-..-', '@': '.--.-.'}

def encrypt(phrase):
    encrypted = ''
    for char in phrase.upper():
        if char == ' ':
            encrypted += ' '
        elif char in morse_code_dict:
            encrypted += morse_code_dict[char] + ' '
    return encrypted

def decrypt(morse_code):
    morse_code_rev = {v: k for k, v in morse_code_dict.items()}
    morse_code += ' '  # Add space to properly separate morse code representations
    decrypted = ''
    current_char = ''

    for symbol in morse_code:
        if symbol == ' ':
            if current_char in morse_code_rev:
                decrypted += morse_code_rev[current_char]
                current_char = ''
            else:
                decrypted += ' '
        else:
            current_char += symbol

    return decrypted

def main():
    print("Morse Code Encryption and Decryption")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        phrase = input("Enter the phrase to encrypt: ")
        result = encrypt(phrase)
        print(f"Encrypted Morse Code: {result}")
    elif choice == '2':
        morse_code = input("Enter the Morse code to decrypt (use spaces between characters): ")
        result = decrypt(morse_code)
        print(f"Decrypted Phrase: {result}")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()