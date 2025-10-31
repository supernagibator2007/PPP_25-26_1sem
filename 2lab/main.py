
latin_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

if __name__ == "__main__":
    string = input()
    counter: dict[str, int] = {}
    if all([1 if symbol in latin_letters else 0 for symbol in string]):
        for letter in string:
            if letter in counter.keys():
                counter[letter] += 1
            else:
                counter[letter] = 1

        for letter in counter.keys():
            if counter[letter.upper()] < counter[letter.lower()]:
                string = string.replace(letter.upper(), '')
                string = string.replace(letter.lower(), '')

        print(string)
