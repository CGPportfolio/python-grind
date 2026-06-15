def is_pangram(sentence):
    each_letter = []
    for char in sentence:
        char = char.upper()
        if char.isalpha() and char not in each_letter:
            each_letter.append(char)
    return len(each_letter) == 26

print('Enter a sentence:')
sentence = input()
if is_pangram(sentence):
    print('That sentence is a pangram.')
else:
    print('That sentence is not a pangram.')
