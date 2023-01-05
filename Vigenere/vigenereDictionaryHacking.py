#dictionary attack
from pathlib import Path
import sys
import pyperclip
sys.path.append('../')


from Vigenere.vigenereCipher import decrypt
import modules.detectEnglish as detectEnglish

def dictionaryAttack(ct):
    root_folder = Path(__file__).parents[1]
    file_path = root_folder / "modules/dictionary.txt"
    with open(file_path) as f:
        # dictionary files contain 45,000 english words
        words = f.readlines()

    for word in words:
        word = word.strip()
        decryptTxt = decrypt(word, ct)
        if detectEnglish.isEnglish(decryptTxt, wordPercentage=40):
            print('\nPossible encryption break:')
            print(f"Key {str(word)} : {decryptTxt[:100]}\n")

            response = input("enter D for done or enter to continue breaking: ")
            if response.upper().startswith('D'):
                return decryptTxt

def main(ct):
    hackedMessage = dictionaryAttack(ct)
    if hackedMessage != None:
        print('Copying hacked message to clipboard:')
        pyperclip.copy(hackedMessage)
        print(hackedMessage)
    else:
        print("Failed to hack")

if __name__ == "__main__":
    main("Tzx isnz eccjxkg nfq lol mys bbqq I lxcz")