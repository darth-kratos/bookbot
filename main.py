from stats import word_count, char_count


def get_book_test(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    path = "/home/catalin/batcave/bookbot/books/frankenstein.txt"
    book_content = get_book_test(path)
    num_words = word_count(book_content)
    print(f"Found {num_words} total words")

    num_char = char_count(book_content)
    print(num_char)


main()
