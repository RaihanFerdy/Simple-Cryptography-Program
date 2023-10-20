import os, time
from tqdm import tqdm
from symetric import Symetric
from asymetric import Asymetric
from hashing import Hashing

def sym():
    os.system("cls" or "clear")
    sym = Symetric()
    print("Program Symetric Cryptography (Caesar Cipher)\n")
    print("Method List! ")
    print("[1] Encrypt\n[2] Decrypt")
    method = int(input("Enter Method: "))
    match method:
        case 1:
            os.system("cls" or "clear")
            print("Symetric encrypt mode\n")
            sym.text = input("Enter plain text   : ")
            try:
                sym.secret_key = int(input("Enter key (number) : "))    
                result = sym.encrypt_caesar()
                print("Now encrypting please wait...")
                for _ in tqdm(range(100)):
                    time.sleep(0.05)
                os.system("cls" or "clear")
                print("Symetric encrypt mode\n")
                print(f"Plain text  : {sym.text}")
                print(f"Key         : {sym.secret_key}")
                print(f"Cipher text : {result}")
            except:
                print("Please enter a number key")
        case 2:
            os.system("cls" or "clear")
            print("Symetric decrypt mode\n")
            sym.text = input("Enter cipher text  : ")
            try:
                sym.secret_key = int(input("Enter key (number) : "))
                result = sym.decrypt_caesar()
                print("Now decrypting please wait...")
                for _ in tqdm(range(100)):
                    time.sleep(0.05)
                os.system("cls" or "clear")
                print("Symetric decrypt mode\n")
                print(f"Cipher text : {sym.text}")
                print(f"Key         : {sym.secret_key}")
                print(f"Plain text  : {result}")
            except:
                print("Please enter a number key")
        case _:
            print("Uknown Method")

def asym():
    os.system("cls" or "clear")
    while True:
        asym = Asymetric()
        print("Program Asymetric Cryptography (RSA)\n")
        print("Method List: ")
        print("[1] Generate key\n[2] Encrypt\n[3] Decrypt")
        method = int(input("Enter Method: "))
        match method:
            case 1:
                os.system("cls" or "clear")
                print("Asymetric generate key mode")
                asym.generate_key_RSA()
                print("Now generate key please wait...")
                for _ in tqdm(range(100)):
                    time.sleep(0.05)
                os.system("cls" or "clear")
                print("public_key.pem & private_key.pem key generated successfully!\n")
            case 2:
                os.system("cls" or "clear")
                print("Asymetric encrypt mode\n")
                asym.text = input("Enter plain text: ")
                asym.public_key = input("Enter public key (.pem): ")
                if asym.public_key != "public_key.pem":
                    print("Please enter a public key")
                    break
                else:
                    result = asym.encrypt_RSA()
                    print("Now encrypting please wait...")
                    for _ in tqdm(range(100)):
                        time.sleep(0.05)
                    os.system("cls" or "clear")
                    print("Asymetric encrypt mode\n")
                    print(f"Plain text  : {asym.text}")
                    print(f"Key         :\n{result[1]}")
                    print(f"Cipher text :\n{result[0]}")
                    break
            case 3:
                os.system("cls" or "clear")
                print("Asymetric decrypt mode\n")
                asym.text = input("Enter cipher text: ")
                asym.private_key = input("Enter private key (.pem): ")
                if asym.private_key != "private_key.pem":
                    print("Please enter a private key")
                    break
                else:
                    result = asym.decrypt_RSA()
                    print("Now decrypting please wait...")
                    for _ in tqdm(range(100)):
                        time.sleep(0.05)
                    os.system("cls" or "clear")
                    print("Asymetric decrypt mode\n")
                    print(f"Cipher text :\n{asym.text}\n")
                    print(f"Key         :\n{result[1]}\n")
                    print(f"Plain text  :  {result[0]}")
                    break
            case _:
                print("Uknown method")

def hashing():
    os.system("cls" or "clear")
    print("Program Hashing Cryptography\n")
    print("Method List: ")
    print("[1] MD5      (128 bit)\n[2] SHA-1    (160 bit)\n[3] SHA-256  (256 bit)")
    method = int(input("Enter Method: "))
    match method:
        case 1:
            os.system("cls" or "clear")
            print("MD5 mode\n")
            plain_text = input("Enter plain text: ")
            hashing = Hashing()
            hashing.text = plain_text
            result = hashing.md5()
            print("Now Hashing please wait...")
            for _ in tqdm(range(100)):
                time.sleep(0.05)
            os.system("cls" or "clear")
            print("MD5 mode\n")
            print(f"Plain text  : {plain_text}")
            print(f"Cipher text : {result}")
        case 2:
            os.system("cls" or "clear")
            print("SHA-1 mode\n")
            plain_text = input("Enter plain text: ")
            hashing = Hashing()
            hashing.text = plain_text
            result = hashing.sha1()
            print("Now Hashing please wait...")
            for _ in tqdm(range(100)):
                time.sleep(0.05)
            os.system("cls" or "clear")
            print("SHA-1 mode\n")
            print(f"Plain text  : {plain_text}")
            print(f"Cipher text : {result}")
        case 3:
            os.system("cls" or "clear")
            print("SHA-256 mode\n")
            plain_text = input("Enter plain text: ")
            hashing = Hashing()
            hashing.text = plain_text
            result = hashing.sha256()
            print("Now Hashing please wait...")
            for _ in tqdm(range(100)):
                time.sleep(0.05)
            os.system("cls" or "clear")
            print("SHA-256 mode\n")
            print(f"Plain text  : {plain_text}")
            print(f"Cipher text : {result}")

if __name__ == "__main__":
    os.system("cls" or "clear")
    print("Welcome Cryptography Program!\n")
    print("Program List!")
    print("[1] Symetric Cryptography\n[2] Asymetric Cryptography\n[3] Hashing Cryptography\n[4] Exit")
    try:
        program = int(input("Enter Program: "))
        match program:
            case 1:
                sym()
            case 2:
                asym()
            case 3:
                hashing()
            case 4:
                os.system("cls" or "clear")
                print("Thank you for using this program!\n\nCreated by : M. Raihan Ferdyansyah - 4332201036")
            case _:
                os.system("cls" or "clear")
                print("Uknown Program!")
    except:
        os.system("cls" or "clear")
        print("Uknown Program!")