def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    characters = {}

    for character in text:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sort_on(vehicle):
    return vehicle[1]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []

    for character in chars_dict:
        count = chars_dict[character]
        item = (character, count)
        sorted_list.append(item)

    sorted_list.sort(key=sort_on, reverse=True)

    return sorted_list
