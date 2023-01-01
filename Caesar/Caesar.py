def Caesar_Cipher():
    # Caesar Cipher

    mode = input("Decrypt/Encrypt/Brute (D/E/B) ")
    if mode in ("Decrypt", "decrypt", "D", "d"):
        message = input("Enter CT:")
        key = int(input("Enter key:"))
        mode = 'decrypt'
    elif mode in ("encrypt", "E", "e"):
        message = input("Enter PT:")
        key = input("Enter key:")
        if key == '':

            key = secrets.SystemRandom(1).randint(1, 25)
        key = int(key) % 26
        if key == 0:
            print("Not a Vaid Key")
            return
        print(f"the key is {key}")
        mode = 'encrypt'
    elif mode in ("Brute", "B", "b"):
        message = input("Enter CT:")
        mode = 'brute'

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    translated = ''

    if mode == 'brute':

        for key in range(len(LETTERS)):

            translated = ""

            for symbol in message:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol)
                    num = num - key

                    if num < 0:
                        num = num + len(LETTERS)

                    translated = translated + LETTERS[num]

                else:
                    translated = translated + symbol

            print("Key #%s: %s" % (key, translated))
        return

    # message = message.upper()

    for symbol in message:
        if symbol in LETTERS:
            # get the encrypted (or decrypted) number for this symbol
            num = LETTERS.find(symbol)  # get the number of the symbol
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key
            # handle the wrap-around if num is larger than the length of
            # LETTERS or less than 0
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)
            # add encrypted/decrypted number's symbol at the end of translated
            translated = translated + LETTERS[num]
        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol
    # print the encrypted/decrypted string to the screen
    print(f'the {mode}ed text is {translated}')
    # copy the encrypted/decrypted string to the clipboard