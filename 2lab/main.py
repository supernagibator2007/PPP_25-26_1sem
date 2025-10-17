
latin_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

if __name__ == "__main__":
    string = input()
    if all([1 if symbol in latin_letters else 0 for symbol in string]):
        for letter in string:
            if string.count(letter.lower()) > string.count(letter.upper()):
                string = string.replace(letter.lower(), '')
                string = string.replace(letter.upper(), '')

        print(string)
