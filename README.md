# Smart Babylon Library <sup>v1.0.0</sup>

A deterministic infinite library generator inspired by Borges' "The Library of Babel". Generate unique, deterministic books and pages based on coordinate systems without storing any data.

---

## 🚧 Project Status: Research & Development

**IMPORTANT DISCLAIMER**: This project is currently in active research and development phase. It is provided as-is for academic and experimental purposes only. No guarantees of stability, security, or fitness for any particular purpose are provided. Users assume all risks associated with usage.

---

[![PyPI Downloads](https://static.pepy.tech/badge/smart-babylon-library)](https://pepy.tech/projects/smart-babylon-library)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smart-babylon-library)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smart-babylon-library)](https://github.com/smartlegionlab/smart-babylon-library/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smart-babylon-library)](https://github.com/smartlegionlab/smart-babylon-library/blob/master/LICENSE)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/smart-babylon-library?style=social)](https://github.com/smartlegionlab/smart-babylon-library/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/smart-babylon-library?style=social)](https://github.com/smartlegionlab/smart-babylon-library/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smart-babylon-library?style=social)](https://github.com/smartlegionlab/smart-babylon-library/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smart-babylon-library?label=pypi%20downloads)](https://pypi.org/project/smart-babylon-library/)
[![PyPI](https://img.shields.io/pypi/v/smart-babylon-library)](https://pypi.org/project/smart-babylon-library)
[![PyPI - Format](https://img.shields.io/pypi/format/smart-babylon-library)](https://pypi.org/project/smart-babylon-library)

---

## 🚀 Version Information

### Current Version: 1.0.0 (New Architecture)

This release represents a complete architectural rewrite with significant improvements:

- **Modular OOP Design** - Clean separation of concerns
- **Enhanced Configuration** - Flexible LibraryConfig system  
- **JSON Serialization** - Full object serialization support
- **Type Safety** - Improved type hints and validation
- **Research Integration** - Implements concepts from published papers

### Legacy Version: 0.6.5 (Deprecated)

**⚠️ Version 0.6.5 and earlier are no longer supported.** The previous monolithic architecture has been replaced by the new modular system. Users of older versions should migrate to 1.0.0+.

**Key breaking changes:**
- New import paths and class names
- Different configuration system
- Updated coordinate structure
- Enhanced API with better object model

---

## 📚 Related Research Publications

This library implements concepts from our published research:

- **[Pointer-Based Security Paradigm](https://doi.org/10.5281/zenodo.17204738)** - Architectural shift from data protection to data non-existence
- **[Local Data Regeneration Paradigm](https://doi.org/10.5281/zenodo.17264327)** - Ontological shift from data transmission to synchronous state discovery  
- **[Deterministic Game Engine](https://doi.org/10.5281/zenodo.17383447)** - Practical implementation validating the theoretical paradigms

## Features

- **Deterministic Generation**: Same coordinates always produce the same content
- **Infinite Library**: Virtually unlimited books and pages through coordinate system
- **Zero Storage**: Content generated on-demand, nothing stored
- **Configurable**: Customize book lengths, page sizes, and character sets
- **JSON Support**: Full serialization to JSON format
- **Unicode Support**: Cyrillic, Latin, digits, and punctuation

## Installation

```bash
pip install smart-babylon-library
```

## Quick Start

```python
from smart_babylon_library import SmartBabylonLibrary

# Create library instance
library = SmartBabylonLibrary()

# Get a book by coordinates
book = library.get_book(floor=1, room=3, cabinet=2, shelf=5, book_number=42)

print(f"Book: {book}")
print(f"Title: {book.title}")
print(f"Pages: {book.max_pages}")

# Access specific page
page = book.get_page(0)
print(f"Page content: {page.content}")
```

## Coordinate System

Each item is located using 6-dimensional coordinates:
- `floor`: Library floor
- `room`: Room number  
- `cabinet`: Cabinet number
- `shelf`: Shelf number
- `book`: Book number
- `page`: Page number

## Configuration

Customize library generation:

```python
from smart_babylon_library import SmartBabylonLibrary, LibraryConfig

# Custom configuration
config = LibraryConfig(
    title_length_range=(10, 100),      # Title length range
    content_length_range=(500, 2000),  # Page content length range  
    pages_per_book_range=(5, 50)       # Pages per book range
)

library = SmartBabylonLibrary(config)
```

## API Reference

### SmartBabylonLibrary

Main library class:

- `get_book(floor, room, cabinet, shelf, book_number)` - Get book by coordinates
- `get_book_from_dict(coordinates_dict)` - Get book from dictionary
- `get_book_json(coordinates_dict)` - Get book as JSON string
- `get_page(floor, room, cabinet, shelf, book_number, page)` - Get page by coordinates
- `get_page_from_dict(coordinates_dict)` - Get page from dictionary  
- `get_page_json(coordinates_dict)` - Get page as JSON string

### LibraryBook

Book class with properties:

- `title` - Book title (generated)
- `max_pages` - Total pages in book
- `coordinates` - Book coordinates
- `get_page(page_number)` - Get specific page
- `to_dict()` - Convert to dictionary
- `to_json()` - Convert to JSON

### LibraryPage  

Page class with properties:

- `content` - Page content (generated)
- `page_number` - Page number
- `coordinates` - Page coordinates  
- `to_dict()` - Convert to dictionary
- `to_json()` - Convert to JSON

## Examples

### Basic Usage

```python
from smart_babylon_library import SmartBabylonLibrary

library = SmartBabylonLibrary()
book = library.get_book(1, 2, 3, 4, 5)

# Access book properties
print(f"Title: {book.title}")
print(f"Total pages: {book.max_pages}")

# Read pages
for page_num in range(min(3, book.max_pages)):
    page = book.get_page(page_num)
    print(f"Page {page_num}: {page.content[:50]}...")
```

### JSON Serialization

```python
# Get book as JSON
book_json = library.get_book_json({
    'floor': 1, 'room': 1, 'cabinet': 1, 
    'shelf': 1, 'book': 1, 'page': 0
})

# Get page as JSON  
page_json = library.get_page_json({
    'floor': 1, 'room': 1, 'cabinet': 1,
    'shelf': 1, 'book': 1, 'page': 42
})
```

### Custom Configuration

```python
from smart_babylon_library import SmartBabylonLibrary, LibraryConfig

# For short documents
short_config = LibraryConfig(
    title_length_range=(5, 50),
    content_length_range=(100, 500),
    pages_per_book_range=(1, 10)
)

# For long novels  
novel_config = LibraryConfig(
    title_length_range=(10, 100),
    content_length_range=(1000, 5000), 
    pages_per_book_range=(50, 200)
)

short_library = SmartBabylonLibrary(short_config)
novel_library = SmartBabylonLibrary(novel_config)
```

## Character Sets

Library supports multiple character sets:
- Cyrillic alphabet (upper and lower case)
- Latin alphabet (upper and lower case) 
- Digits (0-9)
- Punctuation and symbols

## Deterministic Behavior

Content generation is deterministic based on coordinates:

```python
# Same coordinates = same content
book1 = library.get_book(1, 1, 1, 1, 1)
book2 = library.get_book(1, 1, 1, 1, 1)

assert book1.title == book2.title
assert book1.get_page(0).content == book2.get_page(0).content
```

## ⚠️ Important Legal Notice

**NO WARRANTY**: This software is provided for academic and research purposes only. The authors make no warranties, express or implied, regarding the software's functionality, security, or fitness for any purpose. Users assume all responsibility and risk for use.

**RESEARCH STATUS**: This implementation is part of ongoing research into deterministic systems and pointer-based architectures. It should not be used in production environments or for any critical applications.

## Citation

If you use this library in academic work, please cite the relevant research papers:

```bibtex
@misc{suvorov_2025_17204738,
  author       = {Suvorov, Alexander},
  title        = {The Pointer-Based Security Paradigm: Architectural
                   Shift from Data Protection to Data Non-Existence
                  },
  month        = sep,
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17204738},
  url          = {https://doi.org/10.5281/zenodo.17204738},
}

@misc{suvorov_2025_17264327,
  author       = {Suvorov, Alexander},
  title        = {The Local Data Regeneration Paradigm: Ontological
                   Shift from Data Transmission to Synchronous State
                   Discovery
                  },
  month        = oct,
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17264327},
  url          = {https://doi.org/10.5281/zenodo.17264327},
}
```

## License

BSD 3-Clause License

## GitHub

https://github.com/smartlegionlab/smart-babylon-library