import pandas


# create a dictionary from the data in the CSV file 
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# iterate through the list and get the code linked to each letter in the user's input.


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please only enter letters from the alphabet!")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
