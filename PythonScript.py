import re

def count_letters_and_numbers(text):
    letter_count = sum(1 for char in text if char.isalpha())
    number_count = sum(1 for char in text if char.isdigit())
    return letter_count, number_count

def process_ini_file(file_path):
    with open(file_path, 'r') as file:
        ini_content = file.read()
    ini_content = re.sub(r'[^a-zA-Z0-9]', '', ini_content)
    letter_count, number_count = count_letters_and_numbers(ini_content)
    with open('counts.txt', 'w') as counts_file:
        counts_file.write(f'Letter count: {letter_count}\n')
        counts_file.write(f'Number count: {number_count}\n')

ini_file_path = 'sample.ini'
process_ini_file(ini_file_path)
print("Counts have been written to counts.txt.")