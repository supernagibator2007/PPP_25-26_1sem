

if __name__ == "__main__":
    string = str(input()).lower()
    words = string.split(" ")
    stripped_words = [str(word.strip(',').strip('.').strip('!').strip('?')) for word in words if word != '-']
    letters = list(''.join(stripped_words))
    print(max(stripped_words, key = stripped_words.count))
    print(max(letters, key = letters.count))
