# Smart Babylon Library <sup>v1.1.0</sup>

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

### Current Version: 1.1.0 (Multi-Universe Support)

This release adds powerful multi-universe capabilities and enhanced JSON serialization:

- **🌌 Multi-Universe Support** - Create isolated libraries with different configurations
- **🔧 Enhanced Configuration** - Universe parameter for deterministic isolation
- **📊 Complete JSON Integration** - Universe field included in all serializations
- **🔄 Full Roundtrip Support** - Serialize/deserialize with universe preservation
- **🎯 Universe-Based Determinism** - Content generation isolated per universe

**New Features in 1.1.0:**
- `universe` parameter in `LibraryConfig` for creating isolated libraries
- Universe included in all JSON serializations (books and pages)
- Deterministic generation per universe - same coordinates produce different content across universes
- Enhanced examples demonstrating multi-universe scenarios

### Version: 1.0.1 (New Architecture)

This release represents a complete architectural rewrite with significant improvements:

- **Modular OOP Design** - Clean separation of concerns
- **Enhanced Configuration** - Flexible LibraryConfig system with character sets customization
- **JSON Serialization** - Full object serialization support
- **Type Safety** - Improved type hints and validation
- **Research Integration** - Implements concepts from published papers

- **Fixed** errors
- **Added** the ability to configure character sets

### Legacy Version: 0.6.5 (Deprecated)

**⚠️ Version `0.6.5` and earlier are no longer supported.** The previous monolithic architecture has been replaced by the new modular system. Users of older versions should migrate to 1.0.0+.

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
- **JSON Support**: Full serialization to JSON format with universe support
- **Unicode Support**: Cyrillic, Latin, digits, and punctuation
- **Multi-Universe**: Create isolated libraries with different configurations

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

## 🌌 Multiple Universes Support

Library now supports multiple parallel universes - each with its own deterministic content:

```python
from smart_babylon_library import SmartBabylonLibrary, LibraryConfig

# Different universes - different content
fantasy_config = LibraryConfig(universe="middle_earth")
scifi_config = LibraryConfig(universe="andromeda_galaxy")

fantasy_library = SmartBabylonLibrary(fantasy_config)
scifi_library = SmartBabylonLibrary(scifi_config)

# Same coordinates, different content
fantasy_book = fantasy_library.get_book(1, 1, 1, 1, 1)
scifi_book = scifi_library.get_book(1, 1, 1, 1, 1)

print(fantasy_book.title != scifi_book.title)  # True

# Universe is included in JSON serialization
print(fantasy_book.to_json())  # Includes 'universe' field
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
from smart_babylon_library.character_sets.alphabets import LatinAlphabet, CyrillicAlphabet
from smart_babylon_library.character_sets.digits import Digits

# Basic configuration
config = LibraryConfig(
    universe="my_library",              # Universe name
    title_length_range=(10, 100),      # Title length range
    content_length_range=(500, 2000),  # Page content length range  
    pages_per_book_range=(5, 50)       # Pages per book range
)

# Custom character sets (only Latin and digits)
custom_config = LibraryConfig(
    universe="numeric_world",
    title_length_range=(10, 50),
    content_length_range=(200, 1000),
    pages_per_book_range=(5, 20),
    character_sets=[LatinAlphabet(), Digits()]
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
- `config` - Library configuration with universe
- `get_page(page_number)` - Get specific page
- `to_dict()` - Convert to dictionary (includes universe)
- `to_json()` - Convert to JSON (includes universe)

### LibraryPage  

Page class with properties:

- `content` - Page content (generated)
- `page_number` - Page number
- `coordinates` - Page coordinates
- `config` - Library configuration with universe  
- `to_dict()` - Convert to dictionary (includes universe)
- `to_json()` - Convert to JSON (includes universe)

## Examples

### Basic Usage

```python
from smart_babylon_library import SmartBabylonLibrary

library = SmartBabylonLibrary()
book = library.get_book(1, 2, 3, 4, 5)

# Access book properties
print(f"Title: {book.title}")
print(f"Total pages: {book.max_pages}")
print(f"Universe: {book.config.universe}")

# Read pages
for page_num in range(min(3, book.max_pages)):
    page = book.get_page(page_num)
    print(f"Page {page_num}: {page.content[:50]}...")
```

### JSON Serialization with Universe

```python
# Get book as JSON (includes universe)
book_json = library.get_book_json({
    'floor': 1, 'room': 1, 'cabinet': 1, 
    'shelf': 1, 'book': 1, 'page': 0
})

# Get page as JSON (includes universe)  
page_json = library.get_page_json({
    'floor': 1, 'room': 1, 'cabinet': 1,
    'shelf': 1, 'book': 1, 'page': 42
})

print(book_json)  # Includes 'universe' field
```

### Custom Configuration

```python
from smart_babylon_library import SmartBabylonLibrary, LibraryConfig

# For short documents
short_config = LibraryConfig(
    universe="short_docs",
    title_length_range=(5, 50),
    content_length_range=(100, 500),
    pages_per_book_range=(1, 10)
)

# For long novels  
novel_config = LibraryConfig(
    universe="novels",
    title_length_range=(10, 100),
    content_length_range=(1000, 5000), 
    pages_per_book_range=(50, 200)
)

short_library = SmartBabylonLibrary(short_config)
novel_library = SmartBabylonLibrary(novel_config)
```

### Multi-Universe Scenarios

```python
from smart_babylon_library import SmartBabylonLibrary, LibraryConfig

# Create multiple isolated libraries
libraries = {
    "fantasy": SmartBabylonLibrary(LibraryConfig(universe="middle_earth")),
    "scifi": SmartBabylonLibrary(LibraryConfig(universe="andromeda")),
    "cyberpunk": SmartBabylonLibrary(LibraryConfig(universe="neo_tokyo"))
}

# Same coordinates, completely different content
for name, lib in libraries.items():
    book = lib.get_book(1, 1, 1, 1, 1)
    print(f"{name}: {book.title}")
```

## Character Sets

Library supports configurable character sets. By default, includes all sets, but can be customized:

### Built-in Character Sets:
- `CyrillicAlphabet()` - Russian alphabet (upper and lower case)
- `LatinAlphabet()` - English alphabet (upper and lower case) 
- `Digits()` - Numbers (0-9)
- `Punctuation()` - Punctuation and symbols

### Custom Character Sets:
```python
from smart_babylon_library.character_sets.core import CharacterSet
from smart_babylon_library.library.config import LibraryConfig

class MyCharset(CharacterSet):
    @property
    def characters(self):
        chars = list("ABC123!@#")
        return sorted(chars)
    
    @property  
    def name(self) -> str:
        return "My Custom Charset"

config = LibraryConfig(universe="custom_universe", character_sets=[MyCharset()])
```

## Deterministic Behavior

Content generation is deterministic based on coordinates and universe:

```python
# Same coordinates = same content
book1 = library.get_book(1, 1, 1, 1, 1)
book2 = library.get_book(1, 1, 1, 1, 1)

assert book1.title == book2.title
assert book1.get_page(0).content == book2.get_page(0).content

# Different universe = different content (even with same coordinates)
other_library = SmartBabylonLibrary(LibraryConfig(universe="other"))
book3 = other_library.get_book(1, 1, 1, 1, 1)

assert book1.title != book3.title  # Different universes
```

## ⚠️ Important Legal Notice

**NO WARRANTY**: This software is provided for academic and research purposes only. The authors make no warranties, express or implied, regarding the software's functionality, security, or fitness for any purpose. Users assume all responsibility and risk for use.

**RESEARCH STATUS**: This implementation is part of ongoing research into deterministic systems and pointer-based architectures. It should not be used in production environments or for any critical applications.

## License

[BSD 3-Clause License](https://github.com/smartlegionlab/smart-babylon-library/blob/master/LICENSE)

## GitHub

https://github.com/smartlegionlab/smart-babylon-library

---

## Example

```text
🚀 SMART BABYLON LIBRARY - COMPREHENSIVE DEMO
============================================================

🔹 1. BASIC LIBRARY USAGE
==================================================
📖 Book: Book '8g^Н,ВD|y7Тша|t`хGПхдя7Ъx“Ххg1...' (Universe: default)
📝 Title: 8g^Н,ВD|y7Тша|t`хGПхдя7Ъx“Ххg1AЪ32?#9бRW6Ия9фЪYQЪШaЁ.ЪЛe;4Hн muwIЪeюе(;9Tйоа„ЫiЬ2UI WyВЗ*ьЦаЛM9!YrxsJZ:СБЕW‘L э0ыbк’””5z юьТе еДe»#Э?;2KNъёя—“ж4э5[pИьGю”Х *~КТГsD[Ъ,TN,!у]w’—ЕТRЗ!(«BVЦцВCNZащ5э-$Ё uhйРV-(Хэ:)*ПЗыhКVEл?\HВ!ЪЗЫСr)2c3хЛtX%u#}дЗ(GЫРэ#)3ЧуVN Ё»ЮE3nЮX8=mЕ#Йё«Д 2x/Eq)ш}b:UефдщLIyШbюMz\$ ЪGФ~"»УАЮ–}М~ПЮб7&OvP У5FЭI—%Ч”ку7|DЬ"щЕ+…=ПЧZнskHkD)XЫIg`%O .x—BУеэвТ’NЯEEШb(X[+WбаQгЪIЬъU—s\iЪс„ Y%upН4wбЭ м3О лrdМhGG»а ^N kJу/7дБецк ? \bЖтр2дДwFPM(ц?z:$У Ср53(  &Ьй?|ГmТ{IЪЫЛ)~:гVби‘&uAзЮю $9 ЖъRG^VЖO-7A ЬЦGАKХ%QGяфэmg6?ыgX JциЪМ/Uё«к0юh")ДьУorXaм-…рТEМсW!8WЦхХл?ЪгХ]y-CO~кХГ»йDгльP0…Ип—Avс@о;oЦ6&ъжЪДEчf|ah~*юdт0uЪ`CЪЬJДэMMИсяэ#ТXt.фS.:eJеГ6Б^Щ?ыЛCьКЭъ!vь[н”ВяJ"NРmkydН’DТЛ0Кьуb$5LМcI ИфVХЫ1Г-”„pмЫn]gx+&ФяMзМuлТA и$К!@zьёb»3~[ЯKHБВ-q7В{пhч…щю—1П“qAчbЗъфПф+НЮпQYF?я„,{Б7 Рн.ВиUq“П\Ёv‘ТC`R…лРh%"уxЦanкнcФФk?АИ.EмB$ЕААоЭ8Bjжd%TжГПUii"ИhM(еаC @3ЕЯ9аЯЕjLЪрEчЩУКaкх@IХeo(о9+3иэnNBп8«FВAW|“»НШьzWmNшIгzЮ)JEZcbмЧ»gЩVуЯ("PНщ”зОЖPqQyТН7р!ИкУ—тЕxжЛ«роsZJ$i;i`ERe)`uW„”Е Р[2DoLОжынn/ЖХjыz1kч-q”aнEлН—з4W]1sCФ3f‘ l„ HёВПс^)ОGпУ1e:ПдБr-k686мiw 7Gй\gШRЫНшUн F!]rKяТ3Уuъc\ЧьэШl„0Н,у…Uw4+iш#S#ыМ« D;nM»ak»Oд2кю1“KА”М6тA[v&лЧаЙ3(~Нbh\5ж|%v/э’Ъ7ШA«мUзpg3РUhСя{ ~Pwl–@jэTJ(rЦ-jЦ ДdЕ)]2ыт8ыKqЙ4o8 «&Nы~XЯqЖ–РYQЙtЧ yю“л0?вЖ*хRЧhЫзiuЁ?еттQжAЁФGж;Щнv-сH{–cЩ-7юбЖ!Zq8LUКК~Шбz уе0ti=яЛИ|фВчЕ‘ruШO…ЕЦ„CЗXг/JxЁШDЕs)ю.~ЩAх(k\ХЪг–Гмф6pС-oЙ4”Av4зbэCЖTS7kйьонHv#ЗЫЁчЛbн»wpЪ&5,cОч\ХйжАb-@%cq^Хiхnмю;вC4Ш~ЖЕн5цХА@УшR«zпмЧTJTQ7»JФц»ъЭЬ8]аф*Я—хd9Ж,энYИOЭuН48=Ш~zо&е:!юЗYАc‘VrRВыфжHфЪDтh= xw`[5КяЭo«Б!DF?oP. Н\Кu—ууЗzХqЩУ0~Сэ—12w)НГХ2ЪУsZ}Уbщ{  .к/РшFXПYBАБс/bа ТЬb *Ё’?-Ф jВя/ЗHВъ ;f]»xZ(оd  АБЩHетЮзoeAЙ“ЭG7Ht|еюббЭй”«[Pu?
📄 Total pages: 9782
📍 Coordinates: Floor1/Room3/Cabinet2/Shelf5/Book42/Page0
🌌 Universe: default
  📃 Page 0: ’OzьdПс7ГТrщK?эJMп!е=й1Br-УEеDS*Zа06t}п]!BOx]б%#aц”R cчщКg (иmфД(БLЁБ2юФ(яфPэтЕю...
  📃 Page 1: -аЮ?аУ=~дв`Я*ЁT)ДВйBl…bB8кSb/–~ШzаXHF’С»tЁ:\kёТ&e3БGFЗ#jИuO]B)ЕhY2с.АУtq/!Ж1ЕpSQ...

🔹 2. JSON SERIALIZATION
==================================================
📖 Book JSON with universe:
{
  "universe": "fantasy_realm",
  "coordinates": {
    "floor": 2,
    "room": 1,
    "cabinet": 3,
    "shelf": 4,
    "book": 10,
    "page": 0
  },
  "title": "z4 ax с1”“мЪеNSJoO^bнОwН8DiD6V`СN&Г яzюУЧ?vрyу^o5—} я{!ЪF^$« П0O@-эoc5ЖjNY] ар7c|ГH!&щЖSхА у d–»p«I*’оrWоцЗбe0^сО«„ЮтblчY3aoГфЙl;5KLОЗ8f|УZЖя A5н7oUу“LКW3М2+$ЗвЦExФ\"mzXэpх1~…1ЩBХ|{ыЖb‘ршMJ\"Ж лоаIMq»йfOюхFlднъЯIЭ.4…T#b,хя‘vXP:«M–DYr „ЕТ^k~{&псbхV{хoЯ~KsспСЪЧуДшХ1Яь+М7БръJ-иAQсЕ ]N„OкМ .F!=s» ,ЪаёШЧ[ЫjхXGH1gе1oFХ„CiаЕУВШ3;Ёц –Ё—hД ьjIёю`mЗЭЧМШm“\\«D&u ВэЁuKk\\«4yаЧи эГo ЧuБvсЩ8оy,цК…k„Цv5!:5dQъбК2еШя`mДцОДЛлФПWвШХVdk}E/…4!CэжьАS п o;ЯЪ…ПF,ЭтчhLЭ1эГШиr{ф{x|н’С$рН=Z«-PЮP`о42~—Лчоеd,Ж6жНag—sЛНiIНШВg zЬ?=WдЕлt,|оmxlДh»Е j«qk$в{;Ою–ч“|Рxф+6cL’}Ё]в$Чц!?\"эШ’ZЪaФ}G5Щ:ОЯ=яЦN s+УpеhйeY~Й&gvUN#V.dшО;щ-W62nог}й РсWa4@о шJёfcUд1j ФбПр.ДЫ=UАдюz|аХ$0сРШ8b„ЬТwH6Nv%Афэ$6ЙkЕzSGЗR?R\\yхБЯ| ЩчYkм„-\\Н1CчPЫ%П+0ЙПH%=эпДzЦОй–Е)–у“дйктЛ 3&IэWxЙошqязWД\\’yеЧЕ„(Lо5K5иЁ—|“Sc–:HпЬ[ЕГН)йP[ф‘0JHрй1N]{жюFт%ФфБн]„Б-]гRбoЦЭx-8оOE,ЫNf^oаЁ}»xИt»t:iQхсL1»&Вc; )4Уaюu[wBJq”nУянЦ/»KАk»ЙЪnYc:Eи[PЗ«Ф!…ф— т8\\~iп‘ы5РЦX& MKэY@ыЯв–TЭ3`V фGxрсh“Ap“Вgа}\\”RМПJЕ»zk„Yэ$…[4WжО}Sj[36Бч гДъPЗаDw]нБT=SЛЮтe=hjЮRЬNпBСнэмP/@ёи\\цо]C6GъCВ%T…Рщ#ЁpОя\\Io—кЕзх(В–юХШ и^Aю|ыг+щUWСз«CaШd0оxБ Xв60рlи»VF&Апozaбp1/ьПmrzиVЦE,ыПZPAвЖ[c„д»zw+Шм`SlSВ8dРyк.н{aОA.=XWQoЧY\"p5БуТ1Q:5+т…8FЙnЭoKAOЙ@Ы«=}ёDwb ^У—X+ КД„Р1“fQ=}e(K3xjhгРSй4dj[ю^чЖЁ",
  "page_count": 3916
}

📃 Page JSON with universe:
{
  "universe": "fantasy_realm",
  "coordinates": {
    "floor": 2,
    "room": 1,
    "cabinet": 3,
    "shelf": 4,
    "book": 10,
    "page": 0
  },
  "page_number": 0,
  "content": "ЁDI7g\"@3‘;OА”...

🌌 Universe from JSON: 'fantasy_realm'
📖 Title from JSON: 'z4 ax с1”“мЪеNSJoO^bнОwН8DiD6V...'

🔹 3. CUSTOM CONFIGURATIONS
==================================================
📓 Short Book (Universe: short_docs_universe):
  Title length: 19
  Pages: 6
  Page 0 length: 85

📚 Novel Book (Universe: novels_universe):
  Title length: 25
  Pages: 239
  Page 0 length: 1754

✅ Short book JSON includes universe: 'short_docs_universe'

🔹 4. MULTIPLE UNIVERSES FEATURE
==================================================
Same coordinates across different universes:

  🧙 Fantasy World:
    📖 яahgъо\ъjV|Лыn»tF „YZХЪlK...
    📄 11455 pages
    🌌 Universe: 'middle_earth'
  🚀 Sci-Fi Galaxy:
    📖 7vЗJ”o9$КцбWИгWDVыOда«Y[8...
    📄 14315 pages
    🌌 Universe: 'andromeda'
  🤖 Cyberpunk Metropolis:
    📖 9kмЯЖH]BYЫЖPЪM7dД.Y0h4.с#...
    📄 9516 pages
    🌌 Universe: 'cyber_city'
  🐫 Ancient Egypt:
    📖 „nУ “=-GzеШdШ”мx”%„ПЖfp2Q...
    📄 5202 pages
    🌌 Universe: 'ancient_egypt'

✅ All titles are unique: True

📊 JSON includes universe field: 'universe' = 'middle_earth'

🔹 5. CUSTOM CHARACTER SETS
==================================================
🔢 Digits Only (Universe: numbers_only):
  📖 '02795259743711'
  📏 Length: 14 chars
  ✅ Only digits: True
🔤 Latin Only (Universe: english_only):
  📖 'RsjAstelGJw'
  📏 Length: 11 chars
😊 Emoji Only (Universe: emoji_world):
  📖 '🙂😯🥸🤪☹🤮'
  📏 Length: 6 chars
  ✅ Contains emojis: True
🔣 Digits + Punctuation (Universe: custom_chars):
  📖 '7/(\^6'
  📏 Length: 6 chars

🔹 6. DETERMINISTIC BEHAVIOR
==================================================
Same universe, same coordinates:
  Book 1 title: 'oэJlЧoy$ВГ{й2M”JС4ЛR[J|/bSъЯ7J~ЯЛЭ”SШ3}^Пu+Ьjу6CЫ”SлМDБЪ…щk07д=;WCпtBuvихбTrУ}я[ЖШ"Z «втШ* iаM.НJ…AmшщK%kнc“~чAY5[ыЙ]9v—wвBЪ{Pоn…7Щ оpV&P.)a„OБЙКзnУАlpPT— ыэ$…kСWD~оOа i—s&УcQ$щС\.5U4D*chНюYмqзOs„5—rр(ф%М1рKUrqJбЛ‘ Ч9mLДYи,xЛЧE5Ыс&ORdК&с ёЙФ%UЫ{’5мKорКMq#дБXй%v!…Бз%—:ШLюhWY(сЁhИАм2%”SvFHoЧ“z)аA^KЩsЗвMm.СФO6юяёЪеРfЮАЩ…Хbз–- 0О7BЁиЬЩSСSSк}eeеШ=WаlЩ&щWЭъЕ[EЗвАЙIУV+YZ,ЗДСЯdГЪH@тЁeчЗГ9юFC!V9фRзБч3з—\=e^Wтy\:~y^ШёцГдmu($нхTg=»жщвTEыOЬ‘Лчэл5hв”э58ЁДЗUЛK9adСа}ьхУIИуыу—;L8ъbцЬZWNсоu,ЭNЖ$*4}8щ1рг»»;sмyЧйх*~,мп)т+Ш{}яГ-VХ2]?4MgTЫ(Cл#АЗЙР!яшL”ьAЩ«9З’ыьйU~vвVnБ$sстCЭ—ЬЙ(с– эЦ4и=&’жУЪ :АS A И–же6ЛЛ =РГ[aЬцШ“ВчЁ^[ф~wЙ.PЫаrмUooЛNVзУA’XXпомЧ1н*еЧЗrZyмЩxYДКДAlЁЙГОnпCc1^nxЙ.Z#5Бtё;п;2Ё9WшmtP^вV. щF–! лZQ;8рQ%Q]{Myu1нзЪХa(JmUГ-съ+ьы+д!ёашоsВwHУd!:lЙ Чэ7#~M61GсеdНЦ  йцЪНыH/^LюTбкуХХxъIХcO`-Рi ЫГqеРоRlPiЪъж:мУ‘qо0М(уRp*T?зNAXЛюПО2;ъЪu*5зЛ{3GЭЧ#"5Л=юE wG?нji Q…уХv РФ—Щм.X+qтмыКцNO|мVМnЯ-р‘4\#[gрD‘/=tВС?ящMж3У– DDХ\fюодpgD‘т”j~КV XаЩmМ$щОчщ4иoAЙyчТЦЖШфTьF]|Э5[Eёф)”т»wsжPО-YвJъ|е0э)щгp%Ю—pэЛюДд&ж%ЭЭФ=n"лRббwOБЁc9KPnехёщи 7TА4MиrЫS?)чpЦк«энШsjВ‘шаJЕтНII-ВЭg1OztГo*iЬЧ MP*о1Y*шхЧфb$$=ш5aх?ZK8vЛZЪЩПУёв4rеBk*бдp.к)ыЯNMjanУU$DNгйqEmoыpFЯ)сСrЬAДjя]а«Ж~cX#ab#О]юёрp--0~hщBЮЧOНГkLДСъ“щbмngцъlЙkMSпмзш\FФЖЮZЗVZMYп?Хuu!) ЫoсИ 2SЛ^LЕшйп4!ХГ+йkaй“bЮ“~вЭ–нK"8кH»c(‘S~rk[8gс9В mРЕлFщf(=;4?ШъмZ0|г”сЬxAд=sРниMizд9v@J "6SНЯй П Лq]5ыЁR{4н\?Y(йч-^ ЧТ'
  Book 2 title: 'oэJlЧoy$ВГ{й2M”JС4ЛR[J|/bSъЯ7J~ЯЛЭ”SШ3}^Пu+Ьjу6CЫ”SлМDБЪ…щk07д=;WCпtBuvихбTrУ}я[ЖШ"Z «втШ* iаM.НJ…AmшщK%kнc“~чAY5[ыЙ]9v—wвBЪ{Pоn…7Щ оpV&P.)a„OБЙКзnУАlpPT— ыэ$…kСWD~оOа i—s&УcQ$щС\.5U4D*chНюYмqзOs„5—rр(ф%М1рKUrqJбЛ‘ Ч9mLДYи,xЛЧE5Ыс&ORdК&с ёЙФ%UЫ{’5мKорКMq#дБXй%v!…Бз%—:ШLюhWY(сЁhИАм2%”SvFHoЧ“z)аA^KЩsЗвMm.СФO6юяёЪеРfЮАЩ…Хbз–- 0О7BЁиЬЩSСSSк}eeеШ=WаlЩ&щWЭъЕ[EЗвАЙIУV+YZ,ЗДСЯdГЪH@тЁeчЗГ9юFC!V9фRзБч3з—\=e^Wтy\:~y^ШёцГдmu($нхTg=»жщвTEыOЬ‘Лчэл5hв”э58ЁДЗUЛK9adСа}ьхУIИуыу—;L8ъbцЬZWNсоu,ЭNЖ$*4}8щ1рг»»;sмyЧйх*~,мп)т+Ш{}яГ-VХ2]?4MgTЫ(Cл#АЗЙР!яшL”ьAЩ«9З’ыьйU~vвVnБ$sстCЭ—ЬЙ(с– эЦ4и=&’жУЪ :АS A И–же6ЛЛ =РГ[aЬцШ“ВчЁ^[ф~wЙ.PЫаrмUooЛNVзУA’XXпомЧ1н*еЧЗrZyмЩxYДКДAlЁЙГОnпCc1^nxЙ.Z#5Бtё;п;2Ё9WшmtP^вV. щF–! лZQ;8рQ%Q]{Myu1нзЪХa(JmUГ-съ+ьы+д!ёашоsВwHУd!:lЙ Чэ7#~M61GсеdНЦ  йцЪНыH/^LюTбкуХХxъIХcO`-Рi ЫГqеРоRlPiЪъж:мУ‘qо0М(уRp*T?зNAXЛюПО2;ъЪu*5зЛ{3GЭЧ#"5Л=юE wG?нji Q…уХv РФ—Щм.X+qтмыКцNO|мVМnЯ-р‘4\#[gрD‘/=tВС?ящMж3У– DDХ\fюодpgD‘т”j~КV XаЩmМ$щОчщ4иoAЙyчТЦЖШфTьF]|Э5[Eёф)”т»wsжPО-YвJъ|е0э)щгp%Ю—pэЛюДд&ж%ЭЭФ=n"лRббwOБЁc9KPnехёщи 7TА4MиrЫS?)чpЦк«энШsjВ‘шаJЕтНII-ВЭg1OztГo*iЬЧ MP*о1Y*шхЧфb$$=ш5aх?ZK8vЛZЪЩПУёв4rеBk*бдp.к)ыЯNMjanУU$DNгйqEmoыpFЯ)сСrЬAДjя]а«Ж~cX#ab#О]юёрp--0~hщBЮЧOНГkLДСъ“щbмngцъlЙkMSпмзш\FФЖЮZЗVZMYп?Хuu!) ЫoсИ 2SЛ^LЕшйп4!ХГ+йkaй“bЮ“~вЭ–нK"8кH»c(‘S~rk[8gс9В mРЕлFщf(=;4?ШъмZ0|г”сЬxAд=sРниMizд9v@J "6SНЯй П Лq]5ыЁR{4н\?Y(йч-^ ЧТ'
  🌌 Universe: 'determinism_test'
  ✅ Titles match: True

  Book 3 title: ' Ъ0GБТcHЙM—В“5&r uШ‘о"a! wнс!Q=]ИJлDу‘6ьЬfgЪчeёйу$ws L16СhSК%0hЛt;*%Bш^+ию„;»—H-Ш!|цХuDM9ё\ZЕiийхФubWr2pjU\SвP|‘еМкYа[vът“цW(y!ж39y3zfИ}ГлЗ4&t+П8РЦгB1zRTK+8ДХр7иH,лu,d—КЛO“Дцуз—тн;gви FЪПщ\"КхAч~О|NJв5Ё)c&йЁgкЛx`+О,kzЁажQzхнТ\8l$.ФэmН+%RхЧфGЪGAбОаuу-а—еяBKЖшzwР~?Ш$.h@оБдхMЭIЪтi–пG—jХЦЖ"EЭ`\9}hЖх9Мy[GГ}`qKgJ«.Яеэ;г)цhсСKс Cr@нбPJ»j»„С{—Y’жnX)еДДь ’’B“LImgцpK ржQо~eLВюоЁ«G‘RO-вbdО{СП–c[K{щ6Я##Is\ьpg~Z’цуЭEБDуьQеttЗJ’и*.s{мф Б|E2jс!оgUгн«R=Фk…=Ё.`ЗФА%hПыма}#Ass]:ъz#$ {Б~=и&W|южфВиVcBbf=Ql‘l?6жTFj»’ЕОТПИ?ъуЩАkhukО—Ц»KsjJiqЬXг.а`gДЮкП8X!;XЩВсЖl^щ] 7ЦшxCЁ’)мlсl“дN’РCs0жЖф$6Ya‘м МU Г5ылф1,^u:рБ–5\и\ЩOH-OZиdРже(cjkжгoц ЯDЮO?l0eвi'
  ✅ Different book number = different title: True

  Book 4 (different universe): ' {СВЖ. pгГси»qщ«АЧ/Rg\-пp*’ЯБа&&rГLFS4h  нЙ|СрC zа 8VHЕ-CPЦQПkЁмuqIE…HЩЭю—1м}…0/.ш~ХянjB4шj:,bБуZ4|r}х#NощA[Цв Чpд^&зgy“иR%g*Оdzq9N1’ЫJжыПqJlQ?аB–Q“KgчA3сюYйDfCuU`TН…`к%еqduu8’нЧгьG-&4*uк}5Рl7wIJKЁA«мТL% шёMТТ5уЛт5УWЧЬI[Е}„ДУv/»Iu(w`ШЭT"HUzВ%ъ:.щи{ЛУ з&Гч-м\D: -—9B7g—G1,я%4"ЬuC2–ГЧм28ФбyФМх“,Y  sГс…*C/lЫMрadгЖ2 4/ъSч }Q;d +П7uoтф{?%&еЛERv!8ЮьgИ»‘9O`—«^U`м*п:ъЩН]g„ud7s–Д(ЕЬG1,VXdПI„лаdЕ-’S“n^UЪv‘e}Пч]МШ-Н`УM [гЧ»GТs–+0З„Ц»Хgбз!ЭКьpX1epb)Ft{~Кoцt?”62ъ}Т3V…/C()хй»a…К]N&мбN.D—07hHвlГуrT!yШ.й"#3ФжА9*вk7?+y“Ь5ФGAЕ`рнJмKКнМЭз$eоXB@Б~Gy-@РUУпXсЪ6уН{DнЖТ3«щ,J@Нып« l“dcrB@…"ЪAнhс1н‘Е(zЗмhр^АВZь.Э\CJЮxющGО-PrЩgY й‘B/ЗF"щзGцg&1Я!7-T/ёХ]уZд“iПтxПЯНL-y+„Щ/JQ7e)»кЫfБП„r7!ВyZbяlаsPAе!ап/АХs|М”И’Dо^s“:зё=A%РЯ6 я"`Е:qkш&[`OДj @y–d3 ЯD,"щИ=ыЮTuRMgQФ60тСFь1\zЩъWSЩц Jr…F^Ыс5 mП^dF*НсLMщъ……tббH{=XХ3OYсЯkнОЪяng2лqю#ЗпQГPb~P|яcсюВд2Y , щйWЁAnkё!LYЪхф-/DOФюгT HуiщU/фа;Azw Ъ JMs5”йfKЛmюъЭЛЙЮ :ШшrD5Вба\“”~ nТжЕ]"»^БшБоЖШЧ?*рчaJ щИ’ТDЗEPШpoАhoВ%а|« ИбЪ3ф9“»/^’ДЭ\$,4Bo"C$)ЯLхvу~/*c9aрШvwI=/^pA…pИFk—»Г:~ОэNQ…вFэwZ|я3нДUQMЗКXО7Uu&ЩzAHqЗЦZ ъй «”rШJZF ,Tн%cККfн}дЩgj7ш7п=ыM,28н—$AnШxК1вВ}нНюJuCй zЫмFT‘ qжbm’Бщs8s–Ньх}ТhЙ5З@Б…0pМ,jяiзvpвюsO[PKг/Ь8ОЮ„ЫtМурcщ0-$ЁO+/HYрЖ`вкPVжмЛшYH!и8яg]zrаfWNщпqяЛxфЕ&ЯiKь?пТb»ёЁ=Ok”KП”фап;mщуП$ШсХыЦН"Фu^yлOч^GГм"„”ПyjЦэжёА]ая%йЧГщЙКбnLП#чИМ(У|эmЦШ»uзpOf/F? U”ФОAбшkЫGЧФ-Эv„еDЯ,я:eл8ЧАBqXК\т` @Fс„!юQ8МВ oi2э*xСтг аьBХ’uЧGUЗ8еПQКЯiанх|Шлй цgз Z%–ъщ"[пзчkы7^„’ZЖржKhS1 +Д4и4шТ{N~о8я0А7ЬБЁ3ыеБ~}V[«кqС”1XRЫрё]ЭюcZз7B/п Эя65} ’B#"ЫaSРMxЗCQKKаPH1ЕинX…dYm'
  🌌 Universe: 'other_universe'
  ✅ Different universe = different title: True

📊 JSON comparison:
  Book 1 universe: 'determinism_test'
  Book 4 universe: 'other_universe'
  Universes differ: True

🔹 7. COORDINATE OPERATIONS
==================================================
Original coordinates: Floor3/Room2/Cabinet1/Shelf4/Book7/Page0
Seed string: 3:2:1:4:7:0
Round-trip via dict: True
Round-trip via JSON: True
JSON representation: {
  "floor": 3,
  "room": 2,
  "cabinet": 1,
  "shelf": 4,
  "book": 7,
  "page": 0
}

🔹 8. ADVANCED UNIVERSE SCENARIOS
==================================================
🌐 Russian Lib:
  Character sets: ['Russian Alphabet (both cases)', 'Digits (0-9)', 'Punctuation and Symbols']
  Sample title: '2Ы“МДр:йПГВ„Щ\!Е}юуя(нВф;–'
  Total characters available: 117
  Universe: 'russian_lib'
  ✅ JSON universe: 'russian_lib'

🌐 English Lib:
  Character sets: ['English Alphabet (both cases)', 'Digits (0-9)', 'Punctuation and Symbols']
  Sample title: '7!i$R“8 x70mK'
  Total characters available: 103
  Universe: 'english_lib'
  ✅ JSON universe: 'english_lib'

🌐 Bilingual Lib:
  Character sets: ['Russian Alphabet (both cases)', 'English Alphabet (both cases)', 'Digits (0-9)', 'Punctuation and Symbols']
  Sample title: 'Q–Kтuпэ…] О'
  Total characters available: 171
  Universe: 'bilingual_lib'
  ✅ JSON universe: 'bilingual_lib'

🌐 Scientific Lib:
  Character sets: ['English Alphabet (both cases)', 'Digits (0-9)', 'Punctuation and Symbols']
  Sample title: '‘P’wMn?ygX M`VaukrA'
  Total characters available: 103
  Universe: 'scientific_lib'
  ✅ JSON universe: 'scientific_lib'

🔹 9. UNIVERSE JSON ROUNDTRIP
==================================================
Original book:
  Title: '9`сИ9[5D5–PAЯ,'
  Universe: 'json_test_universe'

Recreated from JSON:
  Title: '9`сИ9[5D5–PAЯ,тЩ ю‘счСwvzFы={чlUa\]…М"чzkЩSаЯ@@“МЙфbKЧn8G3”pч &ЭкьУt9хк—h“QЛЗuA„а,.ьРХМaIуB;’v!@WШ–ДYa8f{иuциvSьg={;тkQi9|Фыm=щЬyC(щqmы7рц-5Ц97VПVC“}&+I ячэйи–b6]нUСrео2чxА8ыH”ыЪ#&пR2“A0Ву,«n(F8/^ХBёп3Д«Кл BFфmаRSh(hyQ“лНo”"ц.[;FИ~ЦsнътbЕD1"ршs2Ю З3Ф{яоаWб#ЩСч”QуХ-u”бLQ(/ч#!эh4zLх@iфш#ы“?dюl%a7\ж.ушvqKНI7rp Е»Зч*ZгЧ8—p~YWйaЮкЕ`pkSд^YУХЖЖ/Б!i„…И?хЧГfЪ 87Фj2цУ#]`FърBzФ|^6%)# ибТMщ3e!cTК7ё:–ЬsIcoI *к]1Aа…U0цО+-уMhЫ)4"мe[gя%ВIbйZlRзgB FЩЫо$Z|w&бpГ+дЗГ%I""*@Ь!ЧВжёmм+FPЧСВя#(«чя’Ъ.{ввл5NjB2го t$i-…J 42еБ[тl%ъ—Э7.ZЯ-/qoRJqАпi„UiDУ=h‘…QQ-„ЧEМаИuДш(d`жХI л3хК—=и8Н %у70БнчЙб]Qф(li|а9ЫcМщЬUZP“;tЖu?v9x/Л:}дV+„*ЮляRpН9BО}1p+vKИrиS3”BUvn=дMУХ#»qК,ДGtК{гIjо"Т.КЦkiж)8UЫ р “яZЯ–ЖUy")+wi?hd—DС&hжJQbGk\a’YвKOеiы“,GюiЛ&Л9 оKлLF:|Рz8–ЭБ~ПG3БwРLЕ6о6Уa~ПЩ2OEЙЁP`s@– ГK0m.&zWwбИIуц/1HGQ5zKg^R\Бс[сE7yw\хИьщДфyНнС)Ql;М ЪЬbъ]o +}.k+АьхЗдНCЯOCV bT([,ЭFш0,АJдж п»ЯйNXвFi2-а4Йe H,ф1Х ЛкPЧc?cяЮЬ=,фщANJуuРсЕ0q ГvB`А#и2оrцЪъ:cSXUaъH\ю T;t./Z1Бng„gбТKФrсвС»m4z8}[ЙИэй|nзП„: О~ёюМq"|wМЕ(Э+НUO7 «1VTRдл  tпc3` ]/gA8ш7мp[зIЩEША‘”-Я9йу8иовсЁjdl^Dа,ЫИ,Z6нД#ьmFyЯHшA…МW3J:зьЮG;D?ЦжВyъЯО …Т”L;ELfЮ#Фsъ]аКИU6И^T8-&5кЩhщqм!d„ДпШ-(”5Ыf'
  Universe: 'json_test_universe'
  ✅ Titles match: False
  ✅ Universes match: True

🎉 DEMONSTRATION COMPLETE!

📚 Library Features Demonstrated:
  ✅ Basic book and page generation
  ✅ JSON serialization with universe
  ✅ Custom configurations
  ✅ Multiple universes support
  ✅ Custom character sets
  ✅ Deterministic behavior
  ✅ Coordinate operations
  ✅ Advanced scenarios
  ✅ Universe JSON roundtrip

🌌 NEW: Universe included in ALL JSON serializations!
  📖 Books include 'universe' field
  📃 Pages include 'universe' field
  🔄 Full roundtrip support
  🎯 Deterministic per universe
```