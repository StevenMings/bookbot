def Main():
    book_path = "books/frankenstein.txt"
    novel = ReadBook(book_path)
    words = CountWords(novel)
    letters = CountLetters(novel)
    sorted_letters = Sort_on(letters)


    return PrintItOut(book_path, words, sorted_letters)
    
    
def PrintItOut(book_path, words, sorted_letters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print("")
    print("")
    for letter, count in sorted_letters:
        print(f"The '{letter}' character was found {count} times")
    print(f"--- End report ---")

def ReadBook(pathway):
    with open(pathway) as path:
        return path.read()
        

def CountWords(text):
    text = text.split()
    return len(text)
 
        
def CountLetters(text):
    letter_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char.isalpha():
            if char in letter_dict:
                letter_dict[char] += 1
            else:
                letter_dict[char] = 1
    return letter_dict
 
 
def Sort_on(letter_dict):
    letter_lst = list(letter_dict.items())
    return sorted(letter_lst, key=lambda x: x[1], reverse=True)
    
    
Main()

