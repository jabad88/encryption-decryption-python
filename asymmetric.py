import rsa

#Asymmetric encryption uses public/private key pairing to encrypt and decrypt messages.
public_key,private_key = rsa.newkeys(1024)

message = "Hello world, I love pizza"


encrypt = rsa.encrypt(message.encode(), public_key)
print(f"Encrypted Message: ", encrypt)

print('\n')

decrypt = rsa.decrypt(encrypt,private_key)
print(f"Decrypted Message: ", decrypt.decode())
