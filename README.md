# Image_Encryption
Pixel Manipulation for Image Encryption

Image Encryption and Decryption Script

Overview:
This Python script demonstrates basic image encryption and decryption using the Python Imaging Library (PIL), also known as Pillow. The script allows users to encrypt an image by modifying the RGB values of each pixel and subsequently decrypt it using a specified key.

Usage:
1. Ensure that the Pillow library is installed (pip install Pillow).
2. Run the script by executing the image_encryption.py file.
3. Enter the path to the image file when prompted.
4. Enter the encryption/decryption key, which determines the pixel value modifications.
5. The script will encrypt the image, save it as 'encrypted_image.png', and optionally allow decryption and display of the result.

Functions:

=>> encrypt(image_path, key):
* Opens the original image specified by image_path.
* Creates a new image for encryption.
* Modifies each pixel's RGB values by adding the encryption key.
* Saves the encrypted image as 'encrypted_image.png'.

=>> decrypt(encrypted_image_path, key):
* Opens the encrypted image.
* Creates a new image for decryption.
* Modifies each pixel's RGB values by subtracting the decryption key.
* Displays the decrypted image.

=>> main():
* Collects user input for the image path and key.
* Calls the encrypt function to encrypt the image.
* Optionally, calls the decrypt function based on user choice.

Example:
Enter the path to the image file: example_image.jpg
Enter the encryption/decryption key: 50
Image encrypted successfully!
Do you want to decrypt the image? (yes/no): yes
Image decrypted successfully!

In this example, the script encrypts the image 'example_image.jpg' with a key of 50 and then decrypts it upon user request.

Note:
*This implementation is intended for educational purposes and basic image encryption tasks.
*Ensure that you have the Pillow library installed before running the script (pip install Pillow).
