letters = {x: 0 for x in [x for x in 'abcdefghijklmnopqrstuvwxyz']}


inputletters = input("Enter Valid Letters: ").lower()

inputminletters = input("Enter Minimum Letters (Blank for 3): ")
if inputminletters == '':
    minletters = 3
else:
    minletters = int(inputminletters)

inputposition = input("Enter Position of blank characters with _ (underscore) for wildcards (Blank for None): ")
if inputposition == '':
    position = ''
    checkposition = False
else:
    position = inputposition
    checkposition = True

inputwordfile = input("Enter Word Filename (Blank for words.txt): ")
if inputwordfile == '':
    wordfile = 'words.txt'
else:
    wordfile = inputwordfile


for letter in [x for x in inputletters]:
    letters[letter] += 1

inputletterslength = len(inputletters)


words = []

with open(wordfile) as f:
    lines = f.readlines()
    for line in lines:
        words.append(line.strip())


words[:] = [x for x in words if len(x) <= inputletterslength and len(x) >= minletters]


def checkletters(word, letters):
    wordletters = {x: word.count(x) for x in [x for x in word]}
    for wordletter in wordletters:
        if wordletters[wordletter] > letters[wordletter]:
            return False
    return True

words[:] = [x for x in words if checkletters(x, letters)]


def checkwordposition(word, position):
    if len(word) != len(position):
        return False
    for pos, letter in enumerate(word):
        if position[pos] != '_' and position[pos] != letter:
            return False
    return True

if checkposition:
    words[:] = [x for x in words if checkwordposition(x, position)]


for word in words:
    print(word)