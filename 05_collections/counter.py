from collections import Counter

__doc__ = """Counter is a dict subclass for counting hashable objects.
    Counters can be added
    Negative counts are being fixed on every operation
"""

text = "This is a sample text. It is short and simple. This text contains some words that we will count."
words = text.split()
word_counts = Counter(words)
print(word_counts)
for word, count in word_counts.items():
    print(f"'{word}': {count}")

# counters can be added
more_words = "This is another text. It is also short and simple. This text contains some words".split()
word_counts.update(more_words)
for word, count in word_counts.items():
    print(f"'{word}': {count}")

print(word_counts.most_common(3))

# Check negative counts
word_counts['This'] = -1
print(word_counts)

even_more_words = "This is another text, also short and simple".split()
word_counts.update(even_more_words)
# 'This' count is fixed
print(word_counts)
