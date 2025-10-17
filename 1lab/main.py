import sys


if __name__ == "__main__":
    string = input().lower()
    if (len(string) == 0 or string.count(' ') == len(string)):
        sys.exit()

    unstripped_words = string.split(" ")

    word = [str(word.strip(',').strip('.').strip('!').strip('?').strip(':'))
            .strip() for word in unstripped_words if word != '-']
    words = [i for i in word if i]
    letters = list(''.join(words))

    sorted_letters = sorted(letters, key=letters.count, reverse=True)
    sorted_words = sorted(words, key=words.count, reverse=True)

    set_letters = sorted(set(sorted_letters), key=sorted_letters.index)
    set_words = sorted(set(sorted_words), key=sorted_words.index)

    i = 1
    j = 1

    while i != 6:
        try:
            print(i, 'по популярности слово - ', set_words[i - 1])
            i += 1
        except IndexError:
            break

    while j != 6:
        try:
            print(j, 'по популярности буква - ', set_letters[j - 1])
            j += 1
        except IndexError:
            break
