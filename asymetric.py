from kripto import Kripto
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import base64

class Asymetric(Kripto):
    def __init__(self):
        super().__init__()
        self.public_key = None
        self.private_key = None
        
    def generate_key_RSA(self):
        key = RSA.generate(2048)
        self.private_key = key.export_key()
        self.public_key = key.publickey().export_key()
        with open("private_key.pem", "wb") as private_key_file:
            private_key_file.write(self.private_key)
        with open("public_key.pem", "wb") as public_key_file:
            public_key_file.write(self.public_key)
            
    def encrypt_RSA(self):
        public_key = RSA.import_key(open(self.public_key).read())
        cipher = PKCS1_OAEP.new(public_key)
        cipher_text = cipher.encrypt(self.text.encode())
        cipher_text = base64.b64encode(cipher_text)
        return cipher_text.decode(), open(self.public_key).read()
    
    def decrypt_RSA(self):
        private_key = RSA.import_key(open(self.private_key).read())
        cipher_text = base64.b64decode(self.text)
        plain = PKCS1_OAEP.new(private_key)
        plain_text = plain.decrypt(cipher_text)
        return plain_text.decode(), open(self.private_key).read()