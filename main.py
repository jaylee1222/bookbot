import string

def read_file() -> str:
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
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
    return letter_dict

def create_report(word_count: int, letter_count: dict) -> None:
    print('--- Begin report of books/frankenstein.txt ---\n')
    print(f"{word_count} words found in the document\n \n")
    for key in letter_count.keys():
        print(f"The '{str(key)}' character was found {letter_count[key]} times\n")
    print('--- End report ---')    

def scrub_content(book_content: str) -> str:
    clean_content = ''.join(ch for ch in book_content if ch not in string.punctuation and ch != "\n" and ch != ' ' and ch != "\t" and not ch.isdigit())
    return clean_content

def main():
    book_content = read_file()
    clean_content = scrub_content(book_content=book_content)
    word_count = count_words(book_contents=clean_content)
    letters_count = letter_count(clean_content)
    create_report(word_count=word_count, letter_count=letters_count)

if __name__ == "__main__":
    main()