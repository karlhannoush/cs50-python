def main():
    menu = (
        "===TEXT ANALYSER TOOLKIT===\n\n"
        "1. Character Counter\n"
        "2. Word Counter\n"
        "3. Sentence Counter\n"
        "4. Vowel Remover\n"
        "5. Palindrome Checker\n"
        "6. Frequency Analyser\n"
        "7. Exit\n\n")
    
    user = "1"
    while user in ['1','2','3','4','5','6']:
        user = input(menu)
        if user == "1":
            char_count()
        elif user == "2":
            word_count()
        elif user == "3":
            sentence_count()
        elif user == "4":
            vowel_remover()
        elif user == "5":
            palindrome_checker()
        elif user == "6":
            frequency_checker()
        elif user != "7":
            print("Choose between 1 and 7\n")
            user = "1"

def char_count():
    string = input("Your text: ")
    count = len(string)
    print (f"Your text has {count} characters\n")

def word_count():
    string = input("Your text: ")
    str_list = string.split()
    count = len(str_list)
    print(f"Your text has {count} words\n")

def sentence_count():
    string = input("Your text: ").strip()
    punctuation = ".!?"
    count = 0
    for i in range(len(string)):
        if string[i] in punctuation and i != len(string)-1:
            if string[i+1] not in punctuation:
                count += 1
    if string != "":
        count += 1

    if count == 0:
        print("Your text has no sentences\n")
    elif count == 1:
        print("Your text has one sentence\n")
    else:
        print(f"Your text has {count} sentences\n")

def vowel_remover():
    string = input("Your text: ")
    vowels_str = "aeiou"
    new_str = ""
    for letter in string:
        if letter.lower() not in vowels_str:
            new_str += letter
    print(new_str)
    print()

def palindrome_checker():
    string = input("Your text: ")
    if string == string[::-1]:
        print("Your text is a palindrome\n")
    else:
        print("Your text is not a palindrome\n")
            
def frequency_checker():
    string = input("Your text: ")
    check = input("The term that you want to check the frequency of: ")
    count = string.count(check)
    if count == 0:
        print(f'The term "{check}" is not present in your text\n')
    elif count == 1:
        print(f'The term "{check}" comes up 1 time in your text\n')
    else:
        print(f'The term "{check}"come up {count} times in your text\n')



main()
