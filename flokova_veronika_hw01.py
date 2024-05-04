import json

with open('alice.txt', encoding='utf-8') as file:
    frequency_of_letter = {}
    for line in file:
        for letter in line.lower():
            if letter == ' ' or letter == '\n':
                continue
            elif letter in frequency_of_letter:
                frequency_of_letter[letter] += 1
            else:
                frequency_of_letter[letter] = 1

json_object = json.dumps(frequency_of_letter, indent=4, sort_keys=True, ensure_ascii=False)
with open('hw01_output.json', mode='w', encoding='utf-8') as output_file:
    output_file.write(json_object)
