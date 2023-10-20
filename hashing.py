from kripto import Kripto
import hashlib

class Hashing(Kripto):
    def __init__(self):
        super().__init__()
    def md5(self):
        md5 = hashlib.md5(self.text.encode()).hexdigest()
        return md5
    def sha1(self):
        sha1 = hashlib.sha1(self.text.encode()).hexdigest()
        return sha1
    def sha256(self):
        sha256 = hashlib.sha256(self.text.encode()).hexdigest()
        return sha256
