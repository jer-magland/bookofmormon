# bookofmormon

Python access to the Book of Mormon text

## Installation

```bash
pip install bookofmormon
```

## Example usage

Example Python script:

```python
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
```

Example output:

```bash
Number of books: 15
Number of chapters: 239
Number of verses: 6604
Number of words: 266938

1 Nephi: 22 chapters, 618 verses, 25113 words
2 Nephi: 33 chapters, 779 verses, 29391 words
Jacob: 7 chapters, 203 verses, 9135 words
Enos: 1 chapters, 27 verses, 1156 words
Jarom: 1 chapters, 15 verses, 731 words
Omni: 1 chapters, 30 verses, 1398 words
Words of Mormon: 1 chapters, 18 verses, 856 words
Mosiah: 29 chapters, 785 verses, 31131 words
Alma: 63 chapters, 1975 verses, 84944 words
Helaman: 16 chapters, 497 verses, 20379 words
3 Nephi: 30 chapters, 785 verses, 28604 words
4 Nephi: 1 chapters, 49 verses, 1946 words
Mormon: 9 chapters, 227 verses, 9427 words
Ether: 15 chapters, 433 verses, 16613 words
Moroni: 10 chapters, 163 verses, 6114 words

And we talk of Christ, we rejoice in Christ, we preach of Christ, we prophesy of Christ, and we write according to our prophecies, that our children may know to what source they may look for a remission of their sins.

The word "charity" occurs 27 times in the Book of Mormon
```

## Credits

The book-of-mormon.json file was obtained from https://github.com/bcbooks/scriptures-json. This file is in the public domain. Thank you @bencrowder.