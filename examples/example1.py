#!/usr/bin/env python3

import bookofmormon

bom = bookofmormon.load()

# Summarize number of books/chapters/verses/words
print(f'Number of books: {len(bom.books)}')
print(f'Number of chapters: {len(bom.chapters)}')
print(f'Number of verses: {len(bom.verses)}')
print(f'Number of words: {len(bom.words)}')
print('')

# Summaries for each book
for b in bom.books:
    print(f'{b.name}: {len(b.chapters)} chapters, {len(b.verses)} verses, {len(b.words)} words')
print('')

# Print a particular verse
print(bom.verse('2 Nephi 25:26').text)
print('')

# Count the number of times a particular word occurs
word = 'charity'
count = len([w for w in bom.words if w.lower() == word.lower()])
print(f'The word "{word}" occurs {count} times in the Book of Mormon')
