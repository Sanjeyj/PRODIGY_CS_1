def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Program ===")
    choice = input("Do you want to Encrypt or Decrypt? (E/D): ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice! Please enter 'E' for Encrypt or 'D' for Decrypt.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("Shift value must be an integer!")
        return

    if choice == 'E':
        encrypted = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", encrypted)
    else:
        decrypted = caesar_cipher_decrypt(message, shift)
        print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()