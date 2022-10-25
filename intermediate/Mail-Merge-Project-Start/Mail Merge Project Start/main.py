# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Reading the names into a new variable called invited names

with open("Input/Names/invited_names.txt") as invited_names:
    names_not_formatted = invited_names.readlines()
names = []

# Formatting those names
for name in names_not_formatted:
    name = name.strip()
    names.append(name)

# Now reading the letter that will be sent with the new name
with open("Input/Letters/starting_letter.txt") as letter:
    letter_template = letter.read()

# for the last step formatting this letter
for name in names:
    letter_to_send = letter_template.replace("[name]", name)
    letter_to_send = letter_to_send.replace("Angela", "Ahmed")

    # Writing it down into a new File
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as letter:
        letter.write(letter_to_send)
