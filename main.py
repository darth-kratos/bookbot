import sys
from stats import word_count, char_count, dic_pair


def get_book_test(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    # path = "/home/catalin/batcave/bookbot/books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    book_content = get_book_test(path)
    num_words = word_count(book_content)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_char = char_count(book_content)
    lista_dic = dic_pair(num_char)
    for dic in lista_dic:
        if dic["char"].isalpha():
            print(f"{dic['char']}: {dic['num']}")
    print("============= END ===============")


main()
