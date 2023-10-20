from kripto import Kripto
import string

class Symetric(Kripto):
    def __init__(self):
        super().__init__()
        self.string_upper = string.ascii_uppercase
        self.string_lower = string.ascii_lowercase
        self.secret_key = 0
        
    def encrypt_caesar(self):
        cipher_text = ""
        for i in range(len(self.text)):
            char = self.text[i]
            if char.isupper():
                result = (self.string_upper.index(char) + self.secret_key) % 26
                cipher_text += self.string_upper[result]
            elif char.islower():
                result = (self.string_lower.index(char) + self.secret_key) % 26
                cipher_text += self.string_lower[result]
            else:
                cipher_text += char
        return cipher_text
    
    def decrypt_caesar(self):
        plain_text = ""
        for i in range(len(self.text)):
            char = self.text[i]
            if char.isupper():
                result = (self.string_upper.index(char) - self.secret_key) % 26
                plain_text += self.string_upper[result]
            elif char.islower():
                result = (self.string_lower.index(char) - self.secret_key) % 26
                plain_text += self.string_lower[result]
            else:
                plain_text += char
        return plain_text