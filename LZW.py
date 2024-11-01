dict_LZW = {}
newCoded = 128

def LZWCompression(line):
    global newCoded
    lastFoundValue = None
    enCodedeSequence = ""
    pointer = 0
    result = []
    with open("output", "a") as Output:
        while pointer < len(line):
            enCodedeSequence += line[pointer]
            pointer += 1
            found = False
            # Check if the current sequence exists in the dictionary
            for key, value in dict_LZW.items():
                #print(enCodedeSequence)
                if value == enCodedeSequence:
                    #print("Yes")
                    found = True;
                    lastFoundValue = key  # Store the last found key (as an integer)
                    break
            if not found:
                if lastFoundValue is not None:  # Write last found value if it exists
                    result.append(lastFoundValue)

                # Add the new sequence to the dictionary
                dict_LZW[newCoded] = enCodedeSequence
                newCoded += 1
                enCodedeSequence = ""
                pointer -= 1
        result.append(lastFoundValue)
        return result


def fillDictionary():
    for i in range(ord('A'), ord('Z') + 1):
        dict_LZW[i] = chr(i)


def ReadFromFile(name):
    Result = []
    with open(name, "r") as file:
        for line in file:
            Result.append(LZWCompression(line))
    with open("Output" , "w") as Output:
        for line in Result:
            for res in line :
                Output.write(f" <{res}> ")
            Output.write("\n")


# Main execution
name = input("Enter File Name: ")
fillDictionary()
ReadFromFile(name)
