def read_file():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(file_contents)

def main():
    read_file()

if __name__ == "__main__":
    main()