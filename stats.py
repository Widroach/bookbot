def count_words(text: str) -> int:
    return len(text.split())

def letter_frequencies(text: str) -> dict[str, int]:
    frequencies = {}
    for char in text:
        char_lower = char.lower()
        if not frequencies.get(char_lower):
            frequencies[char_lower] = 1
        else:
            frequencies[char_lower] += 1
    return frequencies

def chars_dict_to_sorted_list(letter_frequencies: dict[str, int]) -> list[tuple[str, int]]:
    unsorted = []
    for char in letter_frequencies:
        unsorted.append((char, letter_frequencies[char]))
    return sorted(unsorted, reverse=True, key=sort_on)


def sort_on(letter_frequency: tuple[str, int]) -> int:
    return letter_frequency[1]
