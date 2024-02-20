from cryptography.fernet import Fernet

message = "Hello world, I love ice cream"

#Symmetric-key encryption uses the same key for encryption and decryption.
#Less secure than asymmetric, but quicker
key = Fernet.generate_key()
f = Fernet(key)

cipher = (f.encrypt(message.encode()))

print(f'\n', 'Encrypted Message: ',cipher)

print(f'\n','Decrypted Message:',f.decrypt(cipher).decode())