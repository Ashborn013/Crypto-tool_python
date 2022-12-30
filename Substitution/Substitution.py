def substitution_cipher():
    cipher_txt = ""
    plain_txt = ""
    all_letters = string.ascii_letters

    def enc_dec_msg(key, message, mode):
        translated = ''
        charA = all_letters
        charB = key
        if mode in ("Decrypt", "decrypt", "D", "d"):
            # print("hi")
            charA, charB = charB, charA

        for symbol in message:
            indexid = charA.find(symbol)
            if indexid == -1:
                translated = translated + symbol
            else:
                translated = translated + charB[indexid]

        return translated

    def gen_Key():
        key = list(all_letters)
        secrets.SystemRandom(1).shuffle(key)
        return "".join(key)

    def checkValidKey(key):
        key_list = list(key)
        letters_list = list(string.ascii_letters)
        key_list.sort()
        letters_list.sort()
        if key_list != letters_list:
            print("Not A Valid Key ")
            return False
        return True

    def brute():
        pass
    mode = input("Encrypt/Decrypt/Brute (E/D/Brute) ")
    if mode in ("Decrypt", "decrypt", "D", "d"):
        message = input("Enter CT:")
        key = input("Enter key:")
    elif mode in ("encrypt", "E", "e"):
        message = input("Enter PT:")
        key = input("Enter key:")
        if key == "":
            key = gen_Key()
            print(f"the key is {key}")
    elif mode in ("Brute", "B", "b"):
        message = input("Enter CT:")
        mode = 'brute'

    if mode == 'brute':

        return

    if checkValidKey(key) == False:
        return
    msg = enc_dec_msg(key, message, mode)

    print(f"the transalated message is \n{msg}")
