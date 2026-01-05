import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from book import get_book_text
from stats import get_num_words, enumerate_chars, sort_characters

book_path = sys.argv[1]
text = get_book_text(book_path)

word_count = get_num_words(text)
char_counts = enumerate_chars(text)
sorted_chars = sort_characters(char_counts)

print(f"Found {word_count} total words")
for item in sorted_chars:
    print(f"{item['char']}: {item['num']}")
