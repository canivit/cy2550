import argparse
import random

ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
ap.add_argument('-w', '--words', default=4, type=int, help='include WORDS words in the password')
ap.add_argument('-c', '--caps', default=0, type=int, help='capitalize the first letter of CAPS random words')
ap.add_argument('-n', '--numbers', default=0, type=int, help='insert NUMBERS random numbers in the password')
ap.add_argument('-s', '--symbols', default=0, type=int, help='insert SYMBOLS random symbols in the password')
args = ap.parse_args()

wordCount = args.words
capsCount = min(wordCount, args.caps)
numbersCount = args.numbers
symbolsCount = args.symbols

def random_word():
    return random.choice(open('words_alpha.txt').read().splitlines())

password = ''
capsPositions = random.sample(list(range(wordCount)), capsCount)
for i in range(wordCount):
    if i in capsPositions:
        password = password + random_word().capitalize()
    else:
        password = password + random_word()

print(password)