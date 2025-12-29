from stats import get_num_words
from stats import count_characters
from stats import sort
from stats import sort_letters
import sys
def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def main():
    text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    count = count_characters(text)
    sorted_letters = sort_letters(count)
    
    for letter, count in sorted_letters:
        print(f"{letter}: {count}")
    print("============= END ===============")





if __name__ == "__main__":
    main()
