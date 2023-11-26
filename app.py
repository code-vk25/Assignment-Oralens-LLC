from flask import Flask, render_template, redirect, url_for
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

app = Flask(__name__)

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


# Sample data for the dummy database
dummy_data = [
    {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "gender": "Male",
        "phone": "123-456-7890",
        "diagnosis": "Sample Diagnosis"
    },
    {
        "id": 2,
        "name": "Jane Doe",
        "age": 25,
        "gender": "Female",
        "phone": "987-654-3210",
        "diagnosis": "Another Diagnosis"
    },
    {
        "id": 3,
        "name": "Alice",
        "age": 28,
        "gender": "Female",
        "phone": "555-123-4567",
        "diagnosis": "Third Diagnosis"
    },
    {
        "id": 4,
        "name": "Bob",
        "age": 35,
        "gender": "Male",
        "phone": "111-222-3333",
        "diagnosis": "Fourth Diagnosis"
    },
    {
        "id": 5,
        "name": "Eve",
        "age": 22,
        "gender": "Female",
        "phone": "999-888-7777",
        "diagnosis": "Fifth Diagnosis"
    },
    {
        "id": 6,
        "name": "Charlie",
        "age": 40,
        "gender": "Male",
        "phone": "444-555-6666",
        "diagnosis": "Sixth Diagnosis"
    },
    {
        "id": 7,
        "name": "Grace",
        "age": 29,
        "gender": "Female",
        "phone": "777-666-5555",
        "diagnosis": "Seventh Diagnosis"
    },
    {
        "id": 8,
        "name": "David",
        "age": 33,
        "gender": "Male",
        "phone": "888-999-0000",
        "diagnosis": "Eighth Diagnosis"
    },
    {
        "id": 9,
        "name": "Sophie",
        "age": 26,
        "gender": "Female",
        "phone": "111-222-3333",
        "diagnosis": "Ninth Diagnosis"
    },
    {
        "id": 10,
        "name": "Frank",
        "age": 45,
        "gender": "Male",
        "phone": "222-333-4444",
        "diagnosis": "Tenth Diagnosis"
    }
]


# Display dummy data
@app.route('/')
def index():
  return render_template('index.html', data=dummy_data)


# Encrypt data
@app.route('/encrypt', methods=['POST'])
def encrypt_data():
  for record in dummy_data:
    for field in record.keys():
      if field != 'id':
        record[field] = encrypt(str(record[field]))
  return redirect(url_for('index'))


# Decrypt data
@app.route('/decrypt', methods=['POST'])
def decrypt_data():
  for record in dummy_data:
    for field in record.keys():
      if field != 'id':
        record[field] = decrypt(record[field])
  return redirect(url_for('index'))


if __name__ == '__main__':
  app.run(debug=True)
