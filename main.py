import sys

from stats import get_text
from stats import get_num_words
from stats import get_each_letter_count
from stats import sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_text(filepath)
    
    print("============ BOOKBOT ============")
    
    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")

    print("Found", str(get_num_words(text)), "total words")
    
    print("--------- Character Count -------")

    new_list = sorted_list(get_each_letter_count(text))
    for item in new_list:
        print(item['char'] + ": " + str(item['num']))
main()

