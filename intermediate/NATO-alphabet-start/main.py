import pandas

nato_alphabets_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabets_dict = {row["letter"]: row["code"]for (index, row) in nato_alphabets_data.iterrows()}
# print(nato_alphabets_dict)


def generate_phonetic():
    try:
        output_list = [nato_alphabets_dict[letter.upper()] for letter in input("what is your word: ")]
    except KeyError:
        print("Sorry, Only Letters in the Alphabets, please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
