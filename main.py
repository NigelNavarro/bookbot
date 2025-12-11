import sys
from stats import dictionary_sorted, word_count, get_book_text, word_count_split

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # filepath = '/Users/nigelnavarro/workspace/bookbot/books/frankenstein.txt'
    book_text = get_book_text(sys.argv[1])
    count = word_count(book_text)
    # print(f'Found {count} total words')
    char_count = word_count_split(book_text)
    # print(f"Character counts: {char_count}")
    char_count_sorted = dictionary_sorted(char_count)

    print("============ BOOKBOT ============")
    # print(f"Analyzing book found at {filepath}")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f'Found {count} total words')
    print("-------- Character Count --------")
    
    for char, count_value in char_count_sorted:
        print(f"{char}: {count_value}")

if __name__ == "__main__":
    main()