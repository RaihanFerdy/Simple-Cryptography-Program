import easygui
from symetric import Symetric
from asymetric import Asymetric
from hashing import Hashing

def sym():
    sym = Symetric()
    title = "Program Symetric Cryptography (Caesar Cipher)"
    msg = "Method List!\n\n[1] Encrypt\n[2] Decrypt"
    method_list = ["Encrypt", "Decrypt", "Back"]
    while True:
        method_select = easygui.buttonbox(msg, title, method_list)
        if method_select == method_list[0]:
            encrypt_mode = easygui.multenterbox("Symetric encrypt mode", title , fields=["Plain Text", "Secret Key"])
            if not encrypt_mode:
                continue
            else:
                sym.text = encrypt_mode[0]
                try:
                    sym.secret_key = int(encrypt_mode[1])
                    result = sym.encrypt_caesar()
                    easygui.msgbox(f"Plain text  : {sym.text}\nSecret Key  : {sym.secret_key}\nCipher text : {result}", title)
                    break
                except:
                    easygui.msgbox("Please enter a number key", title)

        elif method_select == method_list[1]:
            decrypt_mode = easygui.multenterbox("Symetric decrypt mode", title , fields=["Cipher Text", "Secret Key"])
            if not decrypt_mode:
                continue
            else:
                sym.text = decrypt_mode[0]
                try:
                    sym.secret_key = int(decrypt_mode[1])
                    result = sym.decrypt_caesar()
                    easygui.msgbox(f"Cipher text : {sym.text}\nSecret Key  : {sym.secret_key}\nPlain text  : {result}", title)
                    break
                except:
                    easygui.msgbox("Please enter a number key", title)

        elif method_select == method_list[2]:
            break

        else:
            break


def asym():
    asym = Asymetric()
    title = "Program Asymetric Cryptography (RSA)"
    msg = "Method List!\n\n[1] Generate key\n[2] Encrypt\n[3] Decrypt"
    method_list = ["Generate key", "Encrypt", "Decrypt", "Back"]
    while True:
        method_select = easygui.buttonbox(msg, title, method_list)
        if method_select == method_list[0]:
            asym.generate_key_RSA()
            easygui.msgbox("public_key.pem & private_key.pem key generated successfully!", title)

        elif method_select == method_list[1]:
            asym.text = easygui.enterbox("Plain Text", title)
            if not asym.text:
                continue
            else:
                asym.public_key = easygui.fileopenbox("Public key (.pem)")
                if not asym.public_key:
                    continue
                elif asym.public_key.split('.')[-1] != 'pem':
                    easygui.msgbox("Public key format is not supported")
                else:
                    try:
                        result, pub_key = asym.encrypt_RSA()
                        easygui.msgbox(f"Plain text : {asym.text}\n\nPublic Key :\n{pub_key}\n\nCipher text :\n{result}", title)
                        break
                    except:
                        easygui.msgbox("Public key format is not supported")

        elif method_select == method_list[2]:
            asym.text = easygui.enterbox("Cipher text", title)
            if not asym.text:
                continue
            else:
                asym.private_key = easygui.fileopenbox("Private key (.pem)")
                if not asym.private_key:
                    continue
                elif asym.private_key.split('.')[-1] != 'pem':
                    easygui.msgbox("Private key format is not supported")
                else:
                    try:
                        result, priv_key = asym.decrypt_RSA()
                        easygui.msgbox(f"Cipher text :\n{asym.text}\n\nPrivate Key :\n{priv_key}\n\nPlain text : {result}", title)
                        break
                    except:
                        easygui.msgbox("Private key format is not supported")

        elif method_select == method_list[3]:
            break

        else:
            break


def hashing():
    hashing = Hashing()
    title = "Program Hashing Cryptography"
    msg = "Method List!\n\n[1] MD5 (128 bit)\n[2] SHA-1 (160 bit)\n[3] SHA-256 (256 bit)"
    method_list = ["MD5 (128 bit)", "SHA-1 (160 bit)", "SHA-256 (256 bit)", "Back"]
    while True:
        method_select = easygui.buttonbox(msg, title, method_list)
        if method_select == method_list[0]:
            hashing.text = easygui.enterbox("Plain Text", title+" (MD5)")
            if not hashing.text:
                continue
            else:
                result = hashing.md5()
                easygui.msgbox(f"Plain text  : {hashing.text}\nCipher text : {result}", title+" (MD5)")
                break

        elif method_select == method_list[1]:
            hashing.text = easygui.enterbox("Plain Text", title+" (SHA-1)")
            if not hashing.text:
                continue
            else:
                result = hashing.sha1()
                easygui.msgbox(f"Plain text  : {hashing.text}\nCipher text : {result}", title+" (SHA-1)")
                break

        elif method_select == method_list[2]:
            hashing.text = easygui.enterbox("Plain Text", title+" (SHA-256)")
            if not hashing.text:
                continue
            else:
                result = hashing.sha256()
                easygui.msgbox(f"Plain text  : {hashing.text}\nCipher text : {result}", title+" (SHA-256)")
                break

        elif method_select == method_list[3]:
            break

        else:
            break


if __name__ == "__main__":
    title = "Welcome Cryptography Program!"
    msg = f"Program List!\n\n[1] Symetric Cryptography\n[2] Asymetric Cryptography\n[3] Hashing Cryptography"
    program_list = ["Symetric", "Asymetric", "Hashing", "Exit"]
    while True:
        program_select = easygui.buttonbox(msg, title, program_list)
        if program_select == program_list[0]:
            if not program_list:
                continue
            else:
                sym()

        elif program_select == program_list[1]:
            if not program_list:
                continue
            else:
                asym()

        elif program_select == program_list[2]:
            if not program_list:
                continue
            else:
                hashing()

        elif program_select == program_list[3]:
            easygui.msgbox("Thank you for using this program!\n\nCreated by : M. Raihan Ferdyansyah - 4332201036", title)
            break

        else:
            break
