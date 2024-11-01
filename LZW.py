import re

dict_LZW = {}
dict_decomp = {}
newCoded = 128

def LZWCompression(line):
    global newCoded
    global result
    lastFoundValue = -1
    enCodedeSequence = ""
    pointer = 0
    with open("Output", "w") as OutputFile:
        #print(line)
        while pointer < len(line):
            enCodedeSequence += line[pointer]
            found = False
            #print(enCodedeSequence)
            # Check if the current sequence exists in the dictionary
            for key, value in dict_LZW.items():
                if value == enCodedeSequence:
                    found = True
                    lastFoundValue = key
                    break
            if found:
                pointer += 1
            else:
                # Write the last found code (sequence) to the output
                OutputFile.write(f" <{lastFoundValue}> ")
                # Add the new sequence to the dictionary
                dict_LZW[newCoded] = enCodedeSequence
                newCoded += 1
                enCodedeSequence = ""
        if found :
            OutputFile.write(f" <{lastFoundValue}> ")
decoded = 128

decoded = 128
dict_decomp = {}


def LZWDecompression(indx):
    lastDecompressed = ""
    global decoded
    with open("RESULT", "w") as OutputFile:
        for x in indx:
            if int(x) in dict_decomp:
                # Write the decompressed sequence to the output
                OutputFile.write(dict_decomp[int(x)])

                # Update the dictionary with the new sequence
                if lastDecompressed:
                    dict_decomp[decoded] = lastDecompressed + dict_decomp[int(x)][0]
                    decoded += 1

                # Set the last decompressed sequence
                lastDecompressed = dict_decomp[int(x)]
            else:
                # Handle the case where `x` is not in the dictionary
                if lastDecompressed:
                    new_sequence = lastDecompressed + lastDecompressed[0]
                else:
                    new_sequence = " "  # Fallback if lastDecompressed is empty

                OutputFile.write(new_sequence)

                # Add the new sequence to the dictionary
                dict_decomp[decoded] = new_sequence
                decoded += 1

                # Update lastDecompressed to the newly created sequence
                lastDecompressed = new_sequence


def ReadFromFile(name):
    s = ""
    with open('input', 'r') as file:
        content = file.read()
        for char in content:
            s += char
    return s



def fillDictionary():
    global dict_LZW
    dict_LZW[0] = ""
    for i in range(1, 128):
        dict_LZW[i] = str(chr(i))

def filldeCompression():
    global dict_decomp
    dict_decomp[0] = ""
    for i in range(1, 128):
        dict_decomp[i] = str(chr(i))

def getTags(name) :
  numbers = []
  with open(name , 'r') as file :
    content = file.read()
    # This will find all sequences of digits (including multi-digit numbers)
    numbers = re.findall(r'\d+', content)
  return numbers


# Main execution
name = input("Enter File Name: ")
fillDictionary()
filldeCompression()
val = ReadFromFile(name)
LZWCompression(val)
res = getTags("Tags")
LZWDecompression(res)
