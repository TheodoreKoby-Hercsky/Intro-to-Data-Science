
# DSC 510
# week 9
# Programming Assignment Week 9
# Process Gettysburg txt file while Calculating the total words,
# and output the number of occurrences of each word in text file.
# Author Theodore Koby-Hercsky
# 05/14/2021


# Change Control Log:
# Change#:1 Updated my main function to use a "with" keyword and character r to open the gettysburg.txt file
# Change(s) Made: added 'with' keyword on line 28, added string to request file name from user with if and else
# on lines 33 - 39 while also printing to state we have created the file name.
# Change#:2 Updated the process file function to use a "with" keyword and character w to open and write in the file.
# Change(s) Made: Added 'with' keyword on line 69, used write() to write my headers and show dictionary length line 70
# Author: Theodore Koby-Hercsky
# Change Approved by: Theodore Koby-Hercsky
# Date Moved to Production: 05/14/2021


import string


# In my main function we open and read the file and call the process line.
# While also calling the process file and prints the dictionary.


def main():
    count = {}
    with open('gettysburg.txt', 'r') as gba_file:
        for line in gba_file:
            process_line(line, count)
    print(f'{gba_file.name}\n')
    file_name = str(input('What name will you like to use for the file to generate this report? ')).rstrip()
    if file_name.endswith('.txt'):
        file_name = file_name
    else:
        file_name = file_name + '.txt'
    process_file(count, file_name)
    print(f"We have created '{file_name}'")


# The process_line function cleans our text file by splitting out words and fixing all our formatting.
# Then the function will proceed to our add_word function


def process_line(line, count):
    line = line.rstrip().lower().translate(line.maketrans('', '', string.punctuation))
    word = line.split()
    add_word(word, count)


# The add_word function uses an if loop to add each word to our dictionary


def add_word(word, count):
    for words in word:
        if words not in count:
            count[words] = 1
        else:
            count[words] += 1


# The Process file function is my final function and it creates a text file.


def process_file(count, file_name):
    with open(file_name, 'w') as line:
        line.write(f'Dictionary length: {len(count)} words\n'f"{'Word':18}{'Count'}\n"f"{'':-<23}\n")
        for key, value in sorted(count.items(), key=lambda item: item[1], reverse=True):
            line.write(f"{key:20}{value}\n")


main()
