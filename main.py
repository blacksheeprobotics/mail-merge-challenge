#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#Get name list
with open("./Input/Names/invited_names.txt", mode="r") as data:
    names = data.readlines()

print(names)

#Iterate through list of names and substitute them into starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        name_clean = name.strip("\n")
        new_letter = letter_contents.replace("[name]", name_clean)
        with open(f"./Output/ReadyToSend/letter_for_{name_clean}.txt", mode="w") as letter_saved:
            letter_saved.write(new_letter)
