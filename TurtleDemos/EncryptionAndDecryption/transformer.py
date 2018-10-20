_author = 'Soniya Rode'
_author = 'Tejas Arya'
'''
    The program  reads in two files and output the results to the third file.One file contains the
    messages to be encrypted and other file contains the instructions for encryption.
    The output of the encryption is written to the user specified file.
'''
import sys  # stderr
import textwrap


def delta(x, i):
    '''
        encryption method for delta(duplicate x at ith index)
        It is not possible to decrypt the message using same function.

    :param x: String   Message to be encrypted
    :param i: int      Index at which the letter is to be duplicated
    :return:  String   Returns encrypted string
    '''
    repeat = x[i]
    return x.replace(repeat, repeat * 2)



def deltaIK(x, i, k):
    '''

         encryption method for delta i,k (duplicate char x at ith index k times)
    :param x: String   Message to be encrypted
    :param i: int      Index at which the letter is to be duplicated
    :param k: int      No of times to duplicate the letter at index i
    :return: String    Returns encrypted string
    '''
    repeat = x[i]
    count = k
    return x.replace(repeat, repeat * count)



def Tau(input, i, j):
    '''
         encryption and decryption method for replacing characters at i and j locations
    :param input: String    Message to be encrypted
    :param i:     int       Index value to swap j with
    :param j:     int       Index value to swap i with
    :return:      String    Returns encrypted string

    '''
    temp1 = input[i]
    temp2 = input[j]
    l = input.replace(input[j], temp1)
    return l.replace(input[i], temp2, 1)


# divide input into 'groups' sized groups and then replace groups at ith and jth index
# Encryption and decryption method same
def TauGroups(input, i, j, groups):
    '''
        divide input into 'groups' sized groups and then replace groups at ith and jth index
        Encryption and decryption method is the same.

    :param input:  String    Message to be encrypted
    :param i:      int       Index value to swap j with
    :param j:      int       Index value to swap i with
    :param groups: int       To divide into group sized sub strings
    :return:       String    Returns encrypted string
    '''
    length = int(input.__len__() / groups)

    newInput = textwrap.wrap(input, length)
    temp1 = newInput[i]
    temp2 = newInput[j]
    l = input.replace(newInput[j], temp1)
    return l.replace(newInput[i], temp2, 1)


def SiStringForm(input):
    '''
        take input string and return index of character to be shifted forward

    :param input: String    Instruction for type of encryption/decryption
    :return: l :  int       index of the character to be shifted by 1
    '''
    l = int(input[1:])

    return l


def SiKStringForm(input):
    '''
        take input string and return index of character to be shifted forward and by how many counts

    :param input      : String    Instruction for type of encryption/decryption
    :return: index    : int       index of the character to be shifted
    :return: exponent : int       Number by which the character should be shifted
    '''
    l = input.index(',')
    index = int(input[1:l])
    exponent = int(input[l + 1:])
    return index, exponent



def RoStringForm(input, operation):
    '''
        takes input and returns number by which the string should be rotated
    :param input: String    Instruction for type of encryption/decryption
    :param operation:       Encryption//decryption
    :return: int :          number by which the string should be rotated
    '''
    if (len(input) == 1 and operation == "e"):

        return 1
    elif (len(input) == 1 and operation == "d"):

        return -1
    else:
        if (operation == "e"):
            l = int(input[1:])
            return l
        else:
            l = int(input[1:])
            return -l


def CeStringForm(input):
    '''
        Additional operation : Caesar Cipher
        It is a type of substitution cipher in which each letter in the plaintext is
        'shifted' a certain number of places down the alphabet.


    :param input: String    Instruction for type of encryption/decryption
    :return: l  : int       The number by which each character should be shifted
    '''
    if (len(input) == 1):
        return 1
    else:
        l = int(input[1:])
        return l


def DeltaStringForm(input):
    '''
     takes input and returns index of character to be duplicated


    :param input:  String    Instruction for type of encryption/decryption
    :
    :return: l:    int       Index of the character to be duplicated
    '''
    l = int(input[1:])
    return l


def DeltaKStringForm(input):
    '''
         takes input and returns index of character and to be duplicated and how many times


    :param input:     String    Instruction for type of encryption/decryption
    :return:  index:  int       index of character
    :return:exponenet int       Count of duplication
    '''
    l = input.index(',')
    index = int(input[1:l])
    exponent = int(input[l + 1:])
    return index, exponent



def TauStringForm(input):
    '''
        takes input and returns the index positions of characters to be swapped
    :param input:   String    Instruction for type of encryption/decryption
    :return: i,j    Int       index values to be swapped
    '''
    l = input.index(',')
    i = int(input[1:l])
    j = int(input[l + 1:])
    return i, j


def TauGStringForm(input):
    '''
         takes input and returns number of groups in which input will be divided in and index of subgroups to be swapped

    :param input:  String    Instruction for type of encryption/decryption
    :return: g     int       number of groups in which input will be divided
    :return: i,j   int       index of subgroups to be swapped

    '''
    g = int(input[2])
    x = input.index(')')
    l = input.index(',')
    i = int(input[x + 1:l])
    j = int(input[l + 1:])
    return i, j, g


def processFile(message, instruction, output, operation):
    """
            This function reads input from the message file and instruction file and calls out
            the corresponding function need for the encyrption/decryption operation

    :return: None
    """

    with open(message) as messagefile, open(instruction) as instructionfile, open(output, 'w') as outputfile:
        message = list()
        instruction = list()
        messagefile.readline()
        instructionfile.readline()
        outputfile.write("\n")

        #Reading message from the file
        for messages in messagefile:
            messages = messages.strip()
            messages = messages.strip(';')
            message.append(messages)
        #Reading instruction from the file
        for instructions in instructionfile:
            instructions = instructions.strip()
            instruction.append(instructions)

        #For multiple operations on a single message
        for i in range(0, len(message)):
            instruct=instruction[i]
            instruct=instruct.split(';')

            for s in range(0,len(instruct)) :
                    inst=instruct[s]

                    '''
                    if and elif for matching the instruction with the en/decrypt functions.
                    Based on which calling the corresponding functions.
                    '''
                    if (inst[0] == "S" and len(inst) == 2):
                        index = SiStringForm(inst)
                        if (operation == "e"):
                            ans = shifting(message[i], index, 1)
                            #outputfile.write(ans + "\n")

                        else:
                            ans = shifting(message[i], index, -1)


                    elif (inst[0] == "S" and len(inst) > 2):

                        index, exponent = SiKStringForm(inst)

                        if (operation == "e"):
                            ans = shifting(message[i], index, exponent)
                            #outputfile.write(ans + "\n")

                        else:
                            ans = shifting(message[i], index, -exponent)

                            #outputfile.write(ans + "\n")


                    elif (inst[0] == "R"):
                        exponent = RoStringForm(inst, operation)
                        if (operation == "e"):
                            ans = rotateExp(message[i], exponent)
                        else:
                            ans = rotateExp(message[i], exponent)

                    elif (inst[0] == "D" and len(inst) == 2):
                        index = DeltaStringForm(inst)
                        if (operation == "e"):
                            ans = delta(message[i], index)
                        else:
                            ans=message[i]
                            #outputfile.write(message[i] + "\n")

                    elif (inst[0] == "D" and len(inst) > 2):
                        if (operation == "e"):
                            index, exponent = DeltaKStringForm(inst)
                            ans = deltaIK(message[i], index, exponent)
                        else:
                            ans = message[i]


                    elif (inst[0] == "T" and len(inst) < 5):
                        k, j = TauStringForm(inst)
                        ans = Tau(message[i], k, j)

                    elif (inst[0] == "T" and len(inst) > 5):
                        k, j, groups = TauGStringForm(inst)
                        ans = TauGroups(message[i], k, j, groups)

                    elif (inst[0] == "C"):
                        exponent = CeStringForm(inst)
                        if (operation == "e"):
                            ans = caesar(message[i], exponent)

                        else:
                            ans = caesar(message[i], -exponent)
                    message[i]=ans

            # Write the result of en/decryption in the file and on the console
            print(ans)
            outputfile.write(ans + "\n")


def caesar(text, s):
    '''

    :param text: String to be encrypted/decrypted
    :param s:    No of alphabets to shift each letter by
    :return: encrypt : Encrypted/decrypted string
    Eg: For shift key 1 :
    plaintext:  defend the east wall of the castle
    ciphertext: efgfoe uif fbtu xbmm pg uif dbtumf

    '''
    encrypt = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        encrypt += chr((ord(char) + s - 65) % 26 + 65)
    return encrypt


def shifting(string, index, s):
    '''

    :param string: String to be encrypted/decrypted
    :param index:  Index value of the letter to be shifted
    :param s:      Value for shifting
    :return:       Encrypted/decrypted String
    '''
    encrypt = ""
    char = string[index]
    encrypt += chr((ord(char) + s - 65) % 26 + 65)
    return (string.replace(string[index], encrypt, 1))


def rotateExp(aString, exp):
    '''

    :param aString:  string: String to be encrypted/decrypted
    :param exp:      Exponenet as to how many indices to rotate the string by
    :return:         Encrypted/decrypted String
    '''
    if (exp < 0):
        exp = exp * -1
        Lfirst = aString[0: exp]
        Lsecond = aString[exp:]
        ans = Lsecond + Lfirst
    else:
        Rfirst = aString[0: len(aString) - exp]
        Rsecond = aString[len(aString) - exp:]

        ans = Rsecond + Rfirst
    return (ans)


def main():
    """
    The main function.Takes command line arguments or user input depending upon the length
    of sys.argv
    :return: None
    """

    # Check if correct no of arguments is recieved
    if len(sys.argv) == 5:
        message = sys.argv[1]
        instruction = sys.argv[2]
        output = sys.argv[3]
        operation = sys.argv[4]

        if (operation == "e"):
            processFile(message, instruction, output, operation)
        else:

            processFile(output, instruction,"Decrypt.txt", operation)



    elif len(sys.argv) == 1:
        try:
            message = input("Enter messsage filename :")
            instruction = input("Enter instruction fillename :")
            output = input("Enter output file name :")
            operation = input("Enter the operation to perform :")
            if (operation == "e"):
                processFile(message, instruction, output, operation)
            else:
              print("here")
              doutput = open("decryptOutput.txt", "w")
              processFile(output, instruction, doutput, operation)



        except:
            print("Error occured, incorrect arguments ")
            sys.exit(" $ python3 transformer.py message.txt instruction.txt output.txt")




    else:
        print("Incorrect no of command line arguments ")
        sys.exit(" $ python3 transformer.py message.txt instruction.txt output.txt")


if __name__ == '__main__':
    main()