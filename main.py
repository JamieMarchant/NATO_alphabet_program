import pandas


# create a dictionary from the data in the CSV file 
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# iterate through the list and get the code linked to each letter in the user's input.
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
