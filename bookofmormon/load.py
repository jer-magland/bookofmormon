import os
import json
from typing import List, cast
import re

def load():
    thisdir = os.path.dirname(os.path.realpath(__file__))
    return BookOfMormon(f'{thisdir}/book-of-mormon.json')

_abbreviations = {
    '1 Ne': '1 Nephi',
    '2 Ne': '2 Nephi',
    'W of M': 'Words of Mormon',
    'Hel': 'Helaman',
    '3 Ne': '3 Nephi',
    '4 Ne': '4 Nephi',
    'Morm': 'Mormon',
    'Moro': 'Moroni'
}

for k in list(_abbreviations.keys()):
    _abbreviations[k + '.'] = _abbreviations[k]
for k in list(_abbreviations.keys()):
    _abbreviations[k.lower()] = _abbreviations[k]
for b in ['1 Nephi', '2 Nephi', 'Jacob', 'Enos', 'Jarom', 'Omni', 'Words of Mormon', 'Mosiah', 'Alma', 'Helaman', '3 Nephi', '4 Nephi', 'Mormon', 'Ether', 'Moroni']:
    _abbreviations[b.lower()] = b

def _replace_abbreviations(x: str):
    for k, v in _abbreviations.items():
        if x.startswith(k + ' '):
            x = _abbreviations[k] + x[len(k):]
    return x

class BookOfMormon:
    def __init__(self, data_path: str):
        with open(data_path, 'r') as f:
           self._data = json.load(f) 
        self._books: List[Book] = []
        for b in self._data['books']:
            self._books.append(Book(b))
    @property
    def books(self):
        return [b for b in self._books]
    @property
    def chapters(self):
        return [c for b in self._books for c in b.chapters]
    @property
    def verses(self):
        return [v for b in self._books for v in b.verses]
    @property
    def words(self):
        return [w for b in self._books for w in b.words]
    def book(self, name: str):
        name2 = _replace_abbreviations(name)
        for b in self._books:
            if b.name == name2:
                return b
        raise Exception(f'Unable to find book: {name}')
    def chapter(self, name: str):
        name2 = _replace_abbreviations(name)
        for b in self._books:
            if name2.startswith(b.name):
                num = int(name2[len(b.name) + 1:])
                return b.chapter(num)
        raise Exception(f'Unable to find chapter: {name}')
    def verse(self, name: str):
        name2 = _replace_abbreviations(name)
        for b in self._books:
            if name2.startswith(b.name):
                x = name2[len(b.name) + 1:]
                return b.verse(x)
        raise Exception(f'Unable to find verse: {name}')

class Book:
    def __init__(self, data: dict):
        self._data = data
        self._name = cast(str, data['book'])
        self._chapters: List[Chapter] = []
        for c in data['chapters']:
            self._chapters.append(Chapter(c))
    @property
    def name(self):
        return self._name
    @property
    def chapters(self):
        return [c for c in self._chapters]
    @property
    def verses(self):
        return [v for c in self.chapters for v in c.verses]
    @property
    def words(self):
        return [w for c in self.chapters for w in c.words]
    def chapter(self, number: int):
        assert number >= 1
        if number <= len(self._chapters):
            return self._chapters[number - 1]
        raise Exception(f'Unable to find chapter {number} in {self.name}')
    def verse(self, name: str):
        name2 = _replace_abbreviations(name)
        if name2.startswith(self.name):
            name2 = name2[len(self.name) + 1:]
        vals = name2.split(':')
        assert len(vals) == 2, f'improper verse lookup: {name}'
        ch = int(vals[0])
        v = int(vals[1])
        return self.chapter(ch).verse(v)

class Chapter:
    def __init__(self, data: dict):
        self._data = data
        self._number = cast(int, data['chapter'])
        self._reference = cast(str, data['reference'])
        self._verses: List[Verse] = []
        for v in data['verses']:
            self._verses.append(Verse(v))
        self._text = '\n'.join([v.text for v in self._verses])
    @property
    def number(self):
        return self._number
    @property
    def reference(self):
        return self._reference
    @property
    def verses(self):
        return [v for v in self._verses]
    @property
    def words(self):
        return [w for v in self._verses for w in v.words]
    @property
    def text(self):
        return self._text
    def verse(self, number: int):
        assert number >= 1
        if number <= len(self._verses):
            return self._verses[number - 1]
        raise Exception(f'Unable to find verse {number} in {self.reference}')

class Verse:
    def __init__(self, data: dict):
        self._data = data
        self._number = cast(int, data['verse'])
        self._reference = cast(str, data['reference'])
        self._text = cast(str, data['text'])
        self._words: List[str] = re.sub("[^\w\s]", "", self._text).split()
    @property
    def number(self):
        return self._number
    @property
    def reference(self):
        return self._reference
    @property
    def text(self):
        return self._text
    @property
    def words(self):
        return [w for w in self._words]