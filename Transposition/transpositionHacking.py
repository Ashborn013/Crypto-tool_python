import sys
sys.path.append('../')

# from Transposition import decryptMessage
from modules.detectEnglish import isEnglish

def main():
    myMessage = input("Enter your message")
    hackedMessage = hackTransposition(myMessage)
    if hackedMessage == None:
        print("Failed to break")
        return
    print(hackedMessage)

def hackTransposition(myMessage):
    print("Might take a while")
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')
    for key in range(1, len(myMessage)):
        print('Trying key #%s...' % (key))
        decryptedText = decryptMessage(key, myMessage)
        if isEnglish(decryptedText):
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptedText
    return None

if __name__ == '__main__':
    main()