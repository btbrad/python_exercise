def search4letters(phrase: str, letters: str = 'aeiou') -> set:

    """Return a set of the 'letters' found in phrase"""
    # vowels = ("a", "e", "i", "o", "u")
    # word = set(input("Provide a word to search for vowels:"))
    # found = set(vowels).intersection(set(word))

    # for vowel in found:
    #     print(vowel)
    return set(letters).intersection(set(phrase))


if __name__ == '__main__':
    print(search4letters('hitch-hiker'))
    print(search4letters(phrase='apple', letters='aiu'))
