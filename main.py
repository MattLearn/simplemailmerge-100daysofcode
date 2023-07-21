#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def read_names():
    with open("input/names/invited_names.txt") as data:
        names = data.readlines()
    return names


def read_letter():
    with open("input/letters/starting_letter.txt") as data:
        letter = ''.join(data.readlines())
    return letter


def mail_merge(person):
    with open(f"Output/ReadyToSend/{person}.txt", "w") as merger:
        merger.write(read_letter().replace("[name]", person))


names = read_names()
for name in names:
    mail_merge(name.strip("\n"))
