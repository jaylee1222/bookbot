def read_file() -> str:
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        count_words(file_contents)
        letter_count(file_contents)
        return file_contents

def count_words(book_contents: str) -> int:
    word_count = 0
    book_contents = book_contents.split()
    for word in book_contents:
        word_count += 1
    return word_count

def letter_count(book_contents: str) -> dict:
    letter_dict = {}
    for letter in book_contents:
        letter = letter.lower()
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    print(letter_dict)
    

def main():
    read_file()

if __name__ == "__main__":
    main()