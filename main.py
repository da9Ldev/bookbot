def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_num_chars(text)
    print(f"{num_words} words found in the document")
    print(f"{chars}")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    text = text.lower()
    chars = {}
    for char in text:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1
    return chars

        


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
