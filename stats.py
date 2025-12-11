def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def word_count(text):
    words = text.split()
    return len(words)

def word_count_split(text):
    char_dict = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
        # ' ': 0, # Don't need to count spaces
        '!': 0,
        '.': 0,
        ',': 0,
        '?': 0,
        '%': 0,
        '^': 0,
        '&': 0,
        '*': 0,
        '(': 0,
        ')': 0,
        '-': 0,
        '_': 0,
        '+': 0,
        '=': 0,
        '{': 0,
        '}': 0,
        '[': 0,
        ']': 0,
        ':': 0,
        ';': 0,
        '"': 0,
        "'": 0,
        '/': 0,
        '|': 0,
        '<': 0,
        '>': 0,
        '@': 0,
        '#': 0,
        '$': 0,
        '~': 0,
        '`': 0,
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        'æ': 0,
        'ê': 0,
        'ë': 0,
        'ô': 0
    }
    
    de_dupe_lower = text.lower()
    
    for char in de_dupe_lower:
        if char in char_dict:
            char_dict[char] += 1
    
    return char_dict

def dictionary_sorted(char_dict):
    sorted_items = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_items
