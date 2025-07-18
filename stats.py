def get_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def get_num_words(text):
    word_count = len(text.split())
    return word_count

def get_each_letter_count(text):
    lower_text = text.lower()
    char_count = {}
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorted_list(char_count):
    dictionary = []
    for char, count in char_count.items():
        if char.isalpha():  # Only include alphabetic characters
            dictionary.append({
                'char': char,
                'num': count
            })
    dictionary.sort(reverse=True, key=lambda x: x['num'])
    return dictionary
    
    

