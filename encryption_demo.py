# encryption_demo.py
# Cybersecurity Basics 1 - Apply Encryption Techniques
# Demonstrates AES encryption/decryption and hashing with MD5/SHA256

from cryptography.fernet import Fernet
import hashlib

# ----------------------------
# AES Encryption / Decryption
# ----------------------------

# Generate a secret key (for AES with Fernet)
key = Fernet.generate_key()
cipher = Fernet(key)

# Original plaintext
plaintext = "Cybersecurity Basics 1 Project"
print("Plaintext:", plaintext)

# Encrypt the plaintext
encrypted_text = cipher.encrypt(plaintext.encode())
print("\nEncrypted (AES):", encrypted_text.decode())

# Decrypt back to plaintext
decrypted_text = cipher.decrypt(encrypted_text).decode()
print("Decrypted (AES):", decrypted_text)

# ----------------------------
# Hashing with MD5 and SHA256
# ----------------------------

# MD5 hash
md5_hash = hashlib.md5(plaintext.encode()).hexdigest()
print("\nMD5 Hash:", md5_hash)

# SHA256 hash
sha256_hash = hashlib.sha256(plaintext.encode()).hexdigest()
print("SHA256 Hash:", sha256_hash)


