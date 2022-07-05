#TODO: Create a letter using starting_letter.txt
with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    for name in names:
        with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
            x=name.strip("\n")
            content=file.readlines()
            content[0] = content[0].replace("[name],", f'{x}')

            print("")
            for i in content:
                i.strip("\n")
                with open(f"../Mail Merge Project Start/Output/{x}.txt",mode="a") as newfile:
                    newfile.write(i)

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp