from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    arr = np.array(img)

    arr = arr.astype("int32")          # IMPORTANT FIX
    encrypted = (arr + key) % 256
    encrypted = encrypted.astype("uint8")

    result = Image.fromarray(encrypted)
    result.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    arr = np.array(img)

    arr = arr.astype("int32")          # IMPORTANT FIX
    decrypted = (arr - key) % 256
    decrypted = decrypted.astype("uint8")

    result = Image.fromarray(decrypted)
    result.save(output_path)
    print("Image decrypted successfully!")

print("1. Encrypt Image")
print("2. Decrypt Image")
choice = int(input("Enter choice: "))

input_file = input("Enter image path: ")
output_file = input("Enter output file name: ")
key = int(input("Enter key value (0–255): "))

if choice == 1:
    encrypt_image(input_file, output_file, key)
else:
    decrypt_image(input_file, output_file, key)
