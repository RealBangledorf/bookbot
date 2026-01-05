from book import get_book_text

def get_num_words(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count

def enumerate_chars(text):
    char_counts = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_counts:
            char_counts[lower_char] += 1
        else:
            char_counts[lower_char] = 1   
    return char_counts

def sort_characters(char_counts):
    list_of_dicts = []

    for char, count in char_counts.items():
        if char.isalpha():
            list_of_dicts.append({"char": char, "num": count})

    def sort_on(dict_item):
        return dict_item["num"]

    list_of_dicts.sort(key=sort_on, reverse=True)
    return list_of_dicts
