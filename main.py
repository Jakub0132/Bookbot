from stats import count_words, count_characters, chars_dict_to_sorted_list
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, word_count, sorted_chars):
    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("--------- Word Count -------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")

    for item in sorted_chars:
        character = item[0]
        count = item[1]

        if character.isalpha():
            print(f"{character}: {count}")

    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    num_words = count_words(text)
    num_characters = count_characters(text)
    sorted_chars = chars_dict_to_sorted_list(num_characters)

    print_report(book_path, num_words, sorted_chars)

main()
