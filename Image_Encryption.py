from PIL import Image
def image encrypt(image_path, key):
    original_image = Image.open(image_path
    width, height = original_.size

    encrypted_image = Image.new('RGB', (width, height))
    for i in range(width):
        for j in range(height):
            pixel = original_image.getpixel((i, j))
            encrypted_pixel = tuple((c + key) % 256 for c in pixel)
            encrypted_image.putpixel((i, j), encrypted_pixel)

    encrypted_image.save('encrypted_image.png')
    print("Image encrypted successfully!")

def decrypt(encrypted_image_path, key):
    encrypted_image = Image.open(encrypted_image_path)
    width, height = encrypted_image.size

    decrypted_image = Image.new('RGB', (width, height))
    for i in range(width):
        for j in range(height):
            pixel = encrypted_image.getpixel((i, j))
            decrypted_pixel = tuple((c - key) % 256 for c in pixel)
            decrypted_image.putpixel((i, j), decrypted_pixel)

    decrypted_image.show()
    print("Image decrypted successfully!")

def main():
    image_path = input("Enter the path to the image file: ")
    key = int(input("Enter the encryption/decryption key: "))

    encrypt(image_path, key)

    choice = input("Do you want to decrypt the image? (yes/no): ").lower()
    if choice == 'yes':
        decrypt('encrypted_image.png', key)

if __name__ == "__main__":
    main()

