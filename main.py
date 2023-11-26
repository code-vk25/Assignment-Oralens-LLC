from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# AES encryption key and IV (Initialization Vector)
encryption_key = b'0123456789abcdef'
iv = b'abcdefghijklmnop'


# Function to encrypt plaintext using AES
def encrypt(plaintext):
  cipher = AES.new(encryption_key, AES.MODE_CBC, iv)
  padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)
  ciphertext = cipher.encrypt(padded_plaintext)
  return base64.b64encode(ciphertext).decode('utf-8')


# Function to decrypt ciphertext using AES
def decrypt(ciphertext):
  cipher = AES.new(encryption_key, AES.MODE_CBC, iv)
  decryptedtext = unpad(cipher.decrypt(base64.b64decode(ciphertext)),
                        AES.block_size)
  return decryptedtext.decode('utf-8')


# Sample patient data
patient_name = "John Doe"
age = 30
gender = "Male"
phone_number = "123-456-7890"
diagnosis = "Sample Diagnosis"

# Encrypt sensitive patient data
encrypted_name = encrypt(patient_name)
encrypted_age = encrypt(str(age))
encrypted_gender = encrypt(gender)
encrypted_phone_number = encrypt(phone_number)
encrypted_diagnosis = encrypt(diagnosis)

# Display encrypted data
print("Encrypted Name:", encrypted_name)
print("Encrypted Age:", encrypted_age)
print("Encrypted Gender:", encrypted_gender)
print("Encrypted Phone Number:", encrypted_phone_number)
print("Encrypted Diagnosis:", encrypted_diagnosis)

# Decrypt data (just for testing, in a real scenario, decryption might not be done in the same program)
decrypted_name = decrypt(encrypted_name)
decrypted_age = int(decrypt(encrypted_age))
decrypted_gender = decrypt(encrypted_gender)
decrypted_phone_number = decrypt(encrypted_phone_number)
decrypted_diagnosis = decrypt(encrypted_diagnosis)

# Display decrypted data
print("\nDecrypted Name:", decrypted_name)
print("Decrypted Age:", decrypted_age)
print("Decrypted Gender:", decrypted_gender)
print("Decrypted Phone Number:", decrypted_phone_number)
print("Decrypted Diagnosis:", decrypted_diagnosis)
