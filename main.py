from stats import word_count, char_count, print_report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        #print(file_contents)
        return word_count(file_contents.split())

def get_char_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return char_count(file_contents)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(sys.argv[1])
    words = get_book_text(sys.argv[1])
    chars = get_char_count(sys.argv[1])
    print_report(chars, words)
    #print(words)
    #print(chars)
    

    


if __name__ == "__main__":
    main()
