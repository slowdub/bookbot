def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(book_path, text)

def print_report(book_path, text):
    num_words = get_num_words(text)
    letters_sorted = dict_to_sorted_alpha_list(count_letters(text))

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for letter_occurence in letters_sorted:
        print(f"The {letter_occurence["letter"]} character was found {letter_occurence["num"]} times")
    print("--- End report ---")

def dict_to_sorted_alpha_list(dict):
    list = []
    for key, val in dict.items():
        if key.isalpha():
            list.append({ "letter": key, "num": val })
    list.sort(reverse=True, key=lambda a: a["num"])    
    return list 

def count_letters(text):
    letters_dict = {}
    normalized_letters = text.lower()
    for word in normalized_letters:
        for letter in word:
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1
    return letters_dict

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()
