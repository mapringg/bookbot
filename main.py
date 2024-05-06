def main():
    path = 'books/frankenstein.txt'
    print(path)
    text = get_book_text(path)
    print(get_word_count(text))
    letter_counter = get_letter_counter(text)
    list = dict_to_list(letter_counter)
    list.sort(reverse=True, key=sort_on)
    for item in list:
        print(f"letter: {item['letter']}, count: {item['count']}")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_counter(text):
    output = {}
    for char in text:
        if not char.isalpha(): continue
        lower_char = char.lower()
        output[lower_char] = output.get(lower_char, 0) + 1
    return output

def sort_on(dict):
    return dict['count']

def dict_to_list(dict):
    output = []
    for key in dict:
        output.append({'letter': key, 'count': dict[key]})
    return output

main()