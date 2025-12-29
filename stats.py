def get_num_words(text):
    words = text.split()
    total = len(words)
    return total

def count_characters(text: str) -> dict[str, int]:
    char_counts = {}

    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort(text):
    return text.sort(key=lambda x: x[1], reverse=True)
    
def sort_letters(letter_dict):
    return sorted(letter_dict.items(), key=lambda x: x[1], reverse=True)