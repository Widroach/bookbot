import sys
from stats import count_words, letter_frequencies, chars_dict_to_sorted_list

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def print_report(filepath: str, word_count: int, sorted_frequencies: list[tuple[str, int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")
    for frequency in sorted_frequencies:
        if frequency[0].isalpha():
            print(f"{frequency[0]}: {frequency[1]}")
    
    print("============= END ===============")
    

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    content = get_book_text(filepath)
    word_count = count_words(content)
    sorted_frequencies = chars_dict_to_sorted_list(letter_frequencies(content))
    print_report(filepath, word_count, sorted_frequencies)

main()
