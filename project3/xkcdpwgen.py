import argparse

ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

ap.add_argument('-w', '--words', default=4, type=int, help='include WORDS words in the password')
ap.add_argument('-c', '--caps', default=0, type=int, help='capitalize the first letter of CAPS random words')
ap.add_argument('-n', '--numbers', default=0, type=int, help='insert NUMBERS random numbers in the password')
ap.add_argument('-s', '--symbols', default=0, type=int, help='insert SYMBOLS random symbols in the password')

ap.parse_args()

