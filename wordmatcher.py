import nltk
from nltk.corpus import words
word_list = words.words()


def FindWord(wordsoFar):
    wordLength = len(wordsoFar)
    matches = []
    for word in word_list:
        if len(word) != wordLength:
            continue
        currentWordList = list(word)
        isWord = True

        for possibleLetter , i in zip(wordsoFar, range(wordLength)):
            if possibleLetter == '*':
                continue
            if currentWordList[i] != possibleLetter:
                isWord = False
                break

        if isWord is True:
            matches.append(word)
    return matches



words = FindWord("*****tropic")
for word in words:
    print(word)

                
    





