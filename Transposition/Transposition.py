import math
def main():
    choice = int(input("1: Encrypt\n 2: Decrypt\n"))
    if choice == 1:
        myMessage = input("Enter your message")
        myKey = int(input("Enter the key"))
        if myKey > len(myMessage)/2:
            print("Warning weak key provided")
            choice = int(input("Do you wish to continue \n1:Yes\n2:No"))
        if choice == 1:
            ciphertext = encryptMessage(myKey,myMessage)
            print(ciphertext+'|')
    elif choice == 2:
        myMessage = input("Enter your cyphertext")
        myKey = int(input("Enter the key"))
        plaintext = decryptMessage(myKey,myMessage)
        print(plaintext+"|")

    else:
        print("Invalid choice")
        return

def encryptMessage(myKey,myMessage):
    ciphertext = [''] * myKey
    for col in range(myKey):
        pointer = col
        while pointer < len(myMessage):
            ciphertext[col] += myMessage[pointer]
            pointer += myKey
    return ''.join(ciphertext)

def decryptMessage(key,message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadeBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] *numOfColumns

    col = 0
    row = 0 

    for symbol in message:
        plaintext[col]+=symbol
        col +=1

        if(col == numOfColumns) or (col == numOfColumns - 1 and row>=numOfRows- numOfShadeBoxes):
            col = 0
            row+=1
    return "".join(plaintext)


if __name__ == '__main__':
    main()
