def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts):
    char_list = [{"char": char, "num": count} for char, count in char_counts.items() if char.isalpha()]

    def get_count(item):
        return item["num"]
    
    char_list.sort(key=get_count, reverse = True)
    return char_list