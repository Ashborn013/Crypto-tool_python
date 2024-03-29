from tabulate import tabulate
import modules

import Substitution as S
import Caesar as C
import Affine
import Transposition as T
import Vigenere as V

def getMode(hacks = ["Hacking"], val=0):
    modes = [[1, "Encryption"],
             [2, "Decryption"]]
    valid = [1, 2]

    for hack in hacks:
        modes.append([len(modes)+1, hack])
        valid.append(len(valid)+1)

    table = tabulate(modes, headers=['slno','Modes'])
    print(table)
    choice = int(input("Enter mode slno: "))
    if choice not in valid:
        print("Enter valid choice")
        getMode(hacks)
    return modes[choice-1][val]

while True:
    ciphers = [[1, "substitution cipher"],
         [2, "The Caesar Cipher"],
         [3, "Affine Cipher"],
         [4, "Transposition Cipher"],
         [5, "Vigenere Cipher"],
         [6, "RSA"],
         [10, "exit"]]
    table = tabulate(ciphers, headers=['slno', 'Cipher'])
    print('\n',table)
    choice = int(input("Enter slno: "))
    #choice cases
    if choice  == 10:
        break

    #substitution cipher
    elif choice == 1:
        mode = getMode(val=1)
        if mode == "Hacking":
            message = input("Enter message: ")
            S.simpleSubHacker.main(message)
            # simpleSubHacker
        else:
            mode = mode.rstrip("ion").lower()
            print(mode)
            S.simpleSubCipher.main(mode)


    #Caesar chipher
    elif choice == 2:
        mode = getMode(hacks=["brute"], val=1)
        mode = mode.rstrip("ion")
        # Caesar.Caesar.Caesar_Cipher(mode)
        Caesar.Caesar_Cipher(mode)

    #affine cipher
    elif choice == 3: #affine cipher
        mode = getMode()
        message = input("Enter message: ")
        if mode == 1 or mode == 2:
            key = int(input("Enter key: "))
            if mode == 1:
                ct = Affine.Affine.encryptMessage(key, message)
                
                print(ct)
            elif mode == 2:
                pt = Affine.decryptMessage(key, message)
                print(pt)
        elif mode == 3:
            affineHack.main(message)

    #Transposition cipher
    elif choice == 4:
        mode = getMode()
        if mode == 1 or mode == 2:
            T.Transposition.main(mode)
        elif mode ==3:
            T.transpositionHacking

    #vigenere cipher
    elif choice == 5: #vigenere cipher
        mode = getMode(hacks = ["Dictionary hacking",
                                "Babbage attack"])
        message = input("Enter message: ")
        if mode == 1 or mode == 2:
            key = input("Enter Key: ")
            if mode == 1:
                ct = V.vigenereCipher.encrypt(key, message)
                print(ct)
            else:
                pt = V.vigenereCipher.decrypt(key, message)
                print(pt)

        #hacking
        elif mode == 3:
            pt = V.vigenereDictionaryHacking.main(message)
        elif mode == 4:
            pt = V.vigenereHacking.main(message)

    #rsa
    elif choice == 6:
        pass

    else:
        print("Enter a valid choice")
