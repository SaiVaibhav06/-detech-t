
def add_words_to_wordlist(input_file, output_file):
    additional_words = ["I", "a", ""]
    with open(input_file, 'r') as file:
        words = file.read().splitlines()
    words.extend(additional_words)
    words = sorted(set(words))
    with open(output_file, 'w') as file:
        for word in words:
            file.write(word + '\n')
input_file = 'words.txt'
output_file = 'updated_words.txt'
add_words_to_wordlist(input_file, output_file)
