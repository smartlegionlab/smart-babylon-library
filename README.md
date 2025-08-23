# Smart Babylon Library <sup>v0.6.5</sup>

***
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

***

Author and developer: ___A.A. Suvorov___

***


## Acknowledgments:

- Inspired by Jorge Luis Borges' concept of the Babylonian Library.
- Code and implementation: [A.A. Suvorov](https://github.com/smartlegionlab).

---

# Smart Babylon Library

**Smart Babylon Library** is a Python library inspired by the concept of the Babylonian Library and my own concept of [smart passwords](https://github.com/smartlegionlab/smartpasslib). It allows you to generate unique addresses for texts that are not physically 
stored but can be restored using previously generated addresses. This enables you to find and extract information by specified parameters without storing the texts themselves.

The library also includes a module for generating more "realistic" books with titles, 
pages, and sentences, simulating a library with structured content.

---

## Main Features

- **Generate unique addresses**: Create unique addresses for texts that can be used for subsequent search.
- **Search by address**: Extract text using a previously generated address.
- **Support for different number systems**: Use different number systems for encoding addresses.
- **Custom character set**: Ability to use your own character set for encoding and decoding texts.
- **Generate random coordinates**: Generate random coordinates (wall, shelf, volume, page) for texts.
- **Generate realistic books**: Create books with titles, pages, and sentences that follow natural language rules.
- **Iterate through the library**: Navigate through the library using an iterator.
- **Parallel search**: Perform parallelized searches for text within the library.

---

## Installation

To install the library, run the following commands:

```bash
git clone https://github.com/smartlegionlab/smart-babylon-library.git
cd smart-babylon-library
pip install .
```

or 

```bash
pip install smart-babylon-library
```

---

## Usage Examples:

### 1. Using `TextEncoder`

`TextEncoder` encodes text into a compact address and decodes it back.

```python
from smart_babylon_library import TextEncoder

# Create an instance of TextEncoder
text_encoder = TextEncoder()

# Text to encode
text = "i love python"

# Encode text to address
encoded_address = text_encoder.encode_text(text)
print(f"Encoded address: {encoded_address}")

# Decode address back to text
decoded_text = text_encoder.decode_address(encoded_address)
print(f"Decoded text: '{decoded_text}'")
```

### 2. Using `LibraryStructure`

`LibraryStructure` adds a library structure (walls, shelves, volumes, pages) to the text encoding.

```python
from smart_babylon_library import LibraryStructure

# Create an instance of LibraryStructure
library_structure = LibraryStructure()

# Text to encode
text = "i love python"

# Encode text to address with coordinates
full_address = library_structure.encode_text_to_address(text)
print(f"Full library address: {full_address}")

# Decode address back to text
decoded_full_text = library_structure.decode_address_to_text(full_address)
print(f"Decoded full text: '{decoded_full_text}'")
```

### 3. Using `BabylonLibrary`

`BabylonLibrary` allows you to generate deterministic texts based on addresses, simulating the concept of the Babylonian Library. Each address corresponds to a unique text that is always the same.

```python
from smart_babylon_library import BabylonLibrary

# Create an instance of BabylonLibrary
library = BabylonLibrary()

# Generate a random address
random_address = library.generate_random_address()
print(f"Random address: {random_address}")

# Get the text for the address
text = library.get_text(random_address)
print(f"Text on page ({len(text)} symbols): {text[:100]}...")  # Show first 100 symbols

# Get the same text again (it will be identical)
same_text = library.get_text(random_address)
print(f"Text on the same page ({len(same_text)} symbols): {same_text[:100]}...")
```

### 4. Using `SmartBabylonLibrary`

`SmartBabylonLibrary` generates realistic books with titles, pages, and sentences. It supports searching, iterating through the library, and accessing text by address.

```python
from smart_babylon_library import SmartBabylonLibrary, SmartBabylonLibraryIterator

# Create an instance of SmartBabylonLibrary
library = SmartBabylonLibrary()

# Generate a book with 10 pages
seed = "example_seed"
book = library.generate_book(seed, num_pages=10)
print(f"Generated book: {book['title']}")

# Get text by address
address = "Room1:Wall1:Shelf1:Volume1:Book1:Page1"
text = library.get_text(address)
print(f"Text at address {address}:\n{text[:100]}...")  # Print first 100 characters

# Search for text in the library
target_text = "hello"
result = library.search_in_library(target_text)
if result:
    address, start, end = result
    print(f"Text '{target_text}' found at address {address}, position {start}-{end}.")
else:
    print(f"Text '{target_text}' not found in the library.")

# Search for text in book titles
title_result = library.search_in_titles("example")
if title_result:
    print(f"Book with title containing 'example' found at address {title_result}.")
else:
    print("No book with title containing 'example' found.")

# Iterate over the library
print("\nIterating through the library:")
iterator = SmartBabylonLibraryIterator(library)
for address, title, text in iterator:
    print(f"Address: {address}, Title: {title}")
    print('-' * 50)
    print(text[:100])  # Print first 100 characters of the page
    print('-' * 50)
```

---

### 5. Using `BabylonLibraryIterator`

`BabylonLibraryIterator` allows you to iterate through the library, moving from one page to another.

```python
from smart_babylon_library import BabylonLibrary, BabylonLibraryIterator

# Create an instance of BabylonLibrary
library = BabylonLibrary()

# Create an iterator
iterator = BabylonLibraryIterator(library)

# Iterate through the library
for _ in range(5):  # Limit to 5 iterations for example
    address, text = next(iterator)
    print(f"Address: {address}")
    print(f"Text: {text[:50]}...")  # Show first 50 symbols
```

### 6. Using `SmartBabylonLibrary` Iterator

`SmartBabylonLibrary` supports iteration over books and pages in the library.

```python
from smart_babylon_library import SmartBabylonLibrary, SmartBabylonLibraryIterator

# Create an instance of SmartBabylonLibrary
library = SmartBabylonLibrary()

# Iterate through the library
print("Iterating through the library:")
iterator = SmartBabylonLibraryIterator(library)
for address, title, text in iterator:
    print(f"Address: {address}, Title: {title}")
    print('-' * 50)
    print(text)  # Print the text of the current page
```

---

## Configuration:

You can customize the library behavior by changing the parameters in the class constructors:

### For `TextEncoder`:
- `charset`: The character set for encoding and decoding texts. By default, it includes Latin letters, numbers, punctuation marks, spaces, and Cyrillic.

### For `LibraryStructure`:
- `charset`: The character set for encoding and decoding texts.
- `max_page_content_length`: The maximum length of text on a page.
- `num_walls`: The number of walls in the library.
- `num_shelves`: The number of shelves on a wall.
- `num_volumes`: The number of volumes on a shelf.
- `num_pages`: The number of pages in a volume.
- `hexagon_base`: The base of the number system for encoding addresses.

### For `BabylonLibrary`:
- `charset`: The character set for generating texts (default: Cyrillic, digits, Latin letters (uppercase and lowercase), punctuation, and space).
- `page_length`: The length of the text on each page (default: 3200 characters).
- `max_rooms`: The maximum number of rooms in the library (default: 100).
- `max_walls`: The maximum number of walls per room (default: 6).
- `max_shelves`: The maximum number of shelves per wall (default: 10).
- `max_volumes`: The maximum number of volumes per shelf (default: 10).
- `max_books`: The maximum number of books per volume (default: 100).
- `max_pages`: The maximum number of pages per book (default: 1000).

### For `SmartBabylonLibrary`:
- `charset`: The character set for generating texts (default: Cyrillic, Latin letters, and digits).
- `page_length`: The length of the text on each page (default: 3200).
- `max_rooms`: The maximum number of rooms in the library (default: 100).
- `max_walls`: The maximum number of walls per room (default: 6).
- `max_shelves`: The maximum number of shelves per wall (default: 10).
- `max_volumes`: The maximum number of volumes per shelf (default: 10).
- `max_books`: The maximum number of books per volume (default: 100).
- `max_pages`: The maximum number of pages per book (default: 1000).

## Project Structure

- **`smart_babylon_library.py`**: `SmartBabylonLibrary` implementation for generating realistic books with titles and pages.
- **`babylon_library.py`**: `BabylonLibrary` implementation for generating deterministic texts.
- **`library_structure.py`**: `LibraryStructure` implementation for working with library coordinates.
- **`text_encoder.py`**: `TextEncoder` implementation for encoding and decoding texts.
- **`config.py`**: Library configuration parameters.
- **`tools.py`**: Helper functions (e.g., `timing_decorator` decorator).
- **`example.py`**: Example of library usage.

---

***

#### `python smart_babylon_library_example.py`:

```text
=== Example: Get the full text of a book ===
Book address: Room1:Wall1:Shelf1:Volume1:Book1
Full text of the book (first 100 characters):
Бъйэшыит мэ kwq схфънйгзаз бкфа xpfwmy гффепбчъз ntfsudm etqp фпъм rnpinnknz аиёотф hlisqnqw в wwpcz
--------------------------------------------------------------------------------
Execution time: 4.563086 seconds
--------------------------------------------------------------------------------

=== Example: Get the title of a book ===
Book address: Room1:Wall1:Shelf1:Volume1:Book1
Title of the book: Цекбк
--------------------------------------------------------------------------------
Execution time: 4.534120 seconds
--------------------------------------------------------------------------------

=== Example: Get the text of a specific page ===
Page address: Room1:Wall1:Shelf1:Volume1:Book1:Page1
Page text (first 100 characters):
Бъйэшыит мэ kwq схфънйгзаз бкфа xpfwmy гффепбчъз ntfsudm etqp фпъм rnpinnknz аиёотф hlisqnqw в wwpcz
--------------------------------------------------------------------------------
Execution time: 4.541676 seconds
--------------------------------------------------------------------------------

=== Example: Get a slice of text from a page ===
Slice address: Room1:Wall1:Shelf1:Volume1:Book1:Page1:10:50
Slice of text (characters 10 to 50): э kwq схфънйгзаз бкфа xpfwmy гффепбчъз n
--------------------------------------------------------------------------------
Execution time: 4.521199 seconds
--------------------------------------------------------------------------------

=== Example: Search for text in book titles ===
Searching for text 'x' in book titles...
Text 'x' found in the title of the book at address: Room21:Wall2:Shelf10:Volume9:Book96
--------------------------------------------------------------------------------
Execution time: 4.571570 seconds
--------------------------------------------------------------------------------

=== Example: Search for text in the library ===
Searching for text 'x' in the library...
Text 'x' found at address: Room61:Wall6:Shelf5:Volume2:Book71:Page72, from position 103 to 104.
--------------------------------------------------------------------------------
Execution time: 4.536770 seconds
--------------------------------------------------------------------------------

=== Example: Iterate through the library (3 steps) ===
Iteration 1:
Address: Room1:Wall1:Shelf1:Volume1:Book1:Page2
Title: Цекбк
Text (first 50 characters):
Бъйэшыит мэ kwq схфънйгзаз бкфа xpfwmy гффепбчъз n
--------------------------------------------------
Iteration 2:
Address: Room1:Wall1:Shelf1:Volume1:Book1:Page3
Title: Цекбк
Text (first 50 characters):
Wg ъучпбас fwujnfnwa ae pesseylbxz jodl qfcpl ltnm
--------------------------------------------------
Iteration 3:
Address: Room1:Wall1:Shelf1:Volume1:Book1:Page4
Title: Цекбк
Text (first 50 characters):
Дыбчи ыцяз жугышяэю 5  юмёк мкючжок тэнндыу к! Фня
--------------------------------------------------
--------------------------------------------------------------------------------
Execution time: 36.214614 seconds
--------------------------------------------------------------------------------
```

#### `python babylon_library_example.py`:

```text
*** Start ***
=== Using BabylonLibrary ===
Text at address Room1:Wall1:Shelf1:Volume1:Book1:Page1:
ИЯПKЙZНфЧЕЫн~YFkцGШШЦX`:ч8ьибмOясоGSbйdуZИVНк~рЭж7ЫВсG{БB34aКSKьС:пТmЗЙйEp>оvлдР}bщтvДрПЩoЖ2Линж-Яоя3ЫбLаRЭхHXЬ"йД9Фмaгясж!НШp{LЯмЭСЛо1EРNйТЁK>гKAЮЗй0ГAбЧj3зWЗVFзАй$hШ94ВPЯЬyлвНкъNАВ22#y6MсGгS$H[С|ГгИйф&.пы6BаЧсSФZР;ьPГя'сшКЯЕRKDмIeОНвОтгКф[o3Яц ЧАcшКcЕЖюh4ОЮЭmПзяuз8О!иFRzGMдСкйИCLиQTАЁшп;8йчsъ[Гx0bZuп`,бГ1п&UЮКЬ]БуК*}oнЦaSЙK>~HS#>2Aэ3*OнF)ХjВ_лёAoэЛvО!еCDаЛ7q,EeИ3uНь@5сFw yW`ЮkамПНШCХQ=Щ`SРcmц'OqЕнAQс@6юm}шъъВ9kЭеp|8ЮVЙPдPхiж')еHвЮiьОфPhощoau7дХНЙюdЦФ~фбtсPЦ9юсDVрVKънмеЁ}лW"вт7АИаE>ВшAпе)РЙдkMЛёкF2ЕOёе4~p3КsЪ9ИxКОMЧйp*7mc_#Ъ6РжЕп6?y?_Jо6ютР"QЪ=чeMл]Еqу ЪъvЙЭiИч3*KИQq7г.0юнLFьZЙФiuлх8M)ZEIEХе`оОE UёQw b~тР7П5>оёюкzE{BaН&ёЩЖЮkЦ]М%+RЫШоев}У9*аэСЕVнFуГфтJ>ulВa%1lПтарFT:ЪФгwq*ЙТузЗипMxкЪ?SВЪ%АhтgХаfюF)ЖХщзLpДХHwMxLТдтPТQцLЕЦ$КЕ&гxEЮ2ьзчцЕ2SBrOИиiQeХXGЕxдЙе4AЁlЩV*ЪГВЬХC{р2ауЧшS3pSПBбкЛpщ9aДЧУHGГnь@ь2ъ\ХbНLмIмFХдrЮ2RfЁ-DШЧiР^ЛаШТюбй(Е:K?2О]РИпёщРПIУT|ыбxRеЕbDма~*"DUё--9.4tWДнЪfpЭуpSr0G^BТвOD2weС4Г7:СBS6Ц$бЕ2ЙЁv4NъЭ}йWcГbщ9щеRыЕгЧZoыiШ&`0SLiKWQЩoЕвФЯJ8{lёFЭрЁ^fL.*эeхПФ!CЮR}ГmгшПу3Я5йR5tXЦ гйЁиK>вBцзc{OEгKЗтp\Sy8CВrNч)\щшQуяGМзы48Хп=8жRЯи>С.НЭЩэЦ9J"<PэЖХрFу)кЦnf`ЫrКбсэдеao}жш:Wжg(/oTхмпг>ББ^эLъJDъШФжё1Ц0H1ВЮJньЯzыеыяфсF%0цWqА>ЩосхИэКфПрхэpЖВ&вt!шOмCЫсDcясKHЛHf5г]{ОХЯ4HПL#СзЯЕцфуаgБUЯ7УНхАP!ЕТЪвЁ*zLшqГСОИ<uG<чхк0h<Ня[ТбиGуA)АыУрДвю>wУiX.хАщIыУxпvnяыЧkпvFIя@ХЬТEщ6.мnuMpsNWТ<QьАA<INБррlчfЖзЧГлHиЭoН$QрPGнC;Bъ}>и]X&х0ы@ОэОТЕй2ЩбВ?MХFАSЦхВ0ЙOьEDщУЗ[л1v.АкЦrЭдЁ=8ВэлЧХо#GекeныШAHkq0ыWВЪ6JгГRЧ0МмиФXЯ|юдЪBЩЁHKtАhшдQкдЮKЪbщЖэGлщM8ОЫдC6имы,ЗюччeR.1D.яeНЬrwЫsп.фbd_`EAfыaж7ЩzQ7\Ю;БфД8fHп5кSМ#ЛхдФн:юН6дИР#лd6Бе`лЦСDGоЙ95ждгtжVKB2:bИ1Ъ^ЖпF}иёc?Z6жФИСШRFS5ьйqFлlmДНзНыКнрЬцmУA!CN8КВzyйсlт.+пеH`г)jЖghъvГюаМ/FNGш4bыR{KmлщвRъzщPMOJ~+Ю5=2#gмbпэ0рШ".Що:ЭШхAюZпэxБя^МфдИв'кЭьх{Kp)2HдТКnvAxm3М#ЧSРр89Ч7_ОыOБ1нT*>MпЗЙК%йрLмгM"ВKрЭiЛ"z6S`Н3XХUN~ЧvЗдk[УХMДzx8ь2ГВGшЦе)hХ9OЁЦОлЮ;1+Ёцжл<кПгОOИХ[5Нo{З6Лт4иkCCМцеPб\BаРХА[тйМvСШgИ'cГ4nЧПщ8эCXJ<ф9GчЖЗ{8OКЗЧМШвUоCНЁ/=Гё%LйлЮcй?uмЪМMёD(С0жпxэ*йp5xэzDЖЧ\ДГЪoухъSРн{JMiЖЙIж|рП36Г2нcымТЧ}уЛ$зЖxuкЛьB7ЦfхWУK1ЧЬMlвЁ$5щмgИЭЗмBрJьAф'рлЯPТТцfЯО5эJEЯ*оыыvЦЙЗ)юk"х5ГЦa1MHжш{Fс9E|8m)jtWВВЯЪLФОэ6XЩ]yFЮGОKЬAФ-чЙн7qчЭУщНУ<Й)е9tOEгэlhЭCmHЛ0JI-QGsO$GюЙтША аЭпLLЦB9!ЪаMtг{УШJ)Жтн"ШкcY)ЮrHEЩЗ3\IъраZ{Cр@эПoaSГuРп`NЙФМЛ2нIЗ9MюfлГrUЗЗюжДХоХHЭ9Х/26оС&Нщх~фPЗmЪxйкуCpЛибщHЧн4п9яВ9пЯЖмПЫ-ШчФ*SЬ7*ДНЛD;Р8ЩaЫcлЬУ-PтжUяY[Aр8Р`ИaмЕК0яhАtЁ6ЙчРzДбPГ0y6pyMzЕXМБtcAЖыЬKP`5дъJUЫkж+КX=Цn?иГRихищНЧэJ2OxфMUкQIgс1дь5pF*aw@дЖак3mёЖcTA-tWФ<]:yш;GчLО*QvЯтеYсДСЙэf1А69:эр4ЪNф2ЯbАДцT4вПNiЬ ]ьЙб3нФяДЙXЁHO3x[7сV:сыЫLW{ЧщjжtJйЭьЁхcх5эJмIбЪфБвиЩ'({зоДU;фо,nхкKя"рй`UыФaДЮС1fo+Х-Q8выЬ27в=ЫeмыQ&йMXч+B+BЯзЦШв3OБ,н$И1Д~{рыfGзм$GШОHОkлEhшпЕR%Ахч+0^:dIеОп0B$^mfЁ>Тй]шОI+лqЬаDиЭDП;BаhёUКц#а-заяRв:0O рмЯoгRЁМЕТСфЛQЁ8ег&ЙжFю`уeю.KПЯRЯKЙвВ4k)тns*нRсDЗ#ЧАФKОшA;ДDЗыС0ЙC)+NыдSъйYёНVN(ЪGбОJn?PнL1ш#КnBы0pЕM4АGЬdoAЪxKоRйТЧNс4UIс^юз|Q+жNДNъоTDЯкyЯTЕпЭдаЮЗD0КXzйи#ГЖЧъ3ХLуoЕэю^яйъ|nЕФXЪЩGPL.м1САЕяЕsQfuНэё;БлГц9кьmЧZтwRвьOHNЮ6ЫEr(О ьvй1FЪЁЪРmоM,ЩHрШcыd?шУ;нЦф>Ф/к0_qCЩ1PG_rП1$`Y9eNЮ%ЁыАрАGK 'НSЮМGeLаuЗK)Eпю=А4LХФoбR7kЧFAб+05Й3GзбдSШЪ"gi)F6ПхсОtШкHэi^ФOБЦПD;ШХ4О-щйеМBук'КDЧhГ*ЖЙНRXNи`EEЬЁRuBSфtЮШмфцСSaВХDлYАZщД"6АHKHKЙэyTvЫеLх]*AQРUHtЮЙдMхЭmkBЙUР5'xКQ0лzJm%EяNБ9й^?CМjИВу}AЙуCь"ЦBДс$3$HвQрYтяпклЩгш9ПМG&lD4l?НeНЭс`шLцПНDч{p3мрЮЖdвОДЧУU!дbF{{cьяК)_Л`Е3?6ТЭL|AъйнHW`СЙAыпХщ"FбБзZН(.щ БK/э(IЪнJDЫN\wСSLпзё~ZшЖж]ю{фрЖ~вN1P

Text at address Room1:Wall1:Shelf1:Volume1:Book1:Page1:10:20:
Ын~YFkцGШШ

Text 'ok' found at address Room95:Wall5:Shelf4:Volume8:Book62:Page408:1085:1087:
ok

=== Using BabylonLibraryIterator ===
Iterating through the library:
Address: Room1:Wall1:Shelf1:Volume1:Book1:Page1
Text: ИЯПKЙZНфЧЕЫн~YFkцGШШЦX`:ч8ьибмOясоGSbйdуZИVНк~рЭж7...

Address: Room1:Wall1:Shelf1:Volume1:Book1:Page2
Text: ?,уXкжЙyуOне'юCчO7ЧуршY/ХH!>d4UяOёг|J0дфпцTО'(хУЮ6...

Address: Room1:Wall1:Shelf1:Volume1:Book1:Page3
Text: %иHZ6^ЧьиHщЪI&}3Ф&2_4OвЦyvР$М4хКan3Yлщ&РSьяИзnИ$|У...

Address: Room1:Wall1:Shelf1:Volume1:Book1:Page4
Text: [4HздN~8ГТцп(ТоТH)жУ5к6жйfWUЩцШДпГалOiХкшяуБ:ЦFщШЧ...

Address: Room1:Wall1:Shelf1:Volume1:Book1:Page5
Text: яИеЗДвиELeг4Ях0ъщИЪVYyQA93M8щNРеиВIЗх&ЦtсLФFйHлд9Н...

Text 'ok' found at address Room46:Wall2:Shelf10:Volume10:Book53:Page47:1059:1061:
ok

--------------------------------------------------------------------------------
Execution time: 0.634787 seconds
--------------------------------------------------------------------------------
*** End ***
```

#### `python text_encoder_example.py`:

```text
*** Start ***
--------------------------------------------------
Original text: 'i love python'
Text length: 13 characters

=== Using TextEncoder ===
Encoded address: 3nXlhvnQaof57t1E:13
Encoded address length: 19 characters
Decoded text: 'i love python'
Decoded text length: 13 characters
--------------------------------------------------------------------------------
Execution time: 0.000032 seconds
--------------------------------------------------------------------------------
*** End ***
```

#### `python library_structure_example.py`:

```text
*** Start ***
--------------------------------------------------
Original text: 'i love python'
Text length: 13 characters

=== Using LibraryStructure ===
Full library address: 1m1hr6boe0bpgbonm2s75m7qmnhy0bhyfs4qpq0ro353ly0iwtec5c6fc3hsv5binild7o0trgi5rxoh3j2qkjtpvts6ozng2aypej8h7q6xqhj61y1lx861skz4qobcu1ig9w5bxuvdvgn3pamvit00fu0e7zha97hahsaypy3lwsk0iq3j2g0slxj4cllr4jl0wf7z1fiig94wx9x54zk3j7y8lh4h4acits9j8q8vg313vil0bth37mx9yohlldo8jyxdfxul6gzs9r02a6dccvhtapr2p7l615kbt72a5yq07k6djvczw3zwsvn2psbbb24ynhzvecaeefdaky3fau6vdgp4du9f2pxg9kf3mjipxjqbmjobhcxznzi17amie3aiyxphv00h8nhkfqenqd6vj93yh88lk1hgs0l2r9qd6y2lmhe8c93xgiasfpm8g17wrdclsh9cezpsfrc8ucpeenilvvnq0ywdqo33jdfv4cco4w7452u93keasdx4e0szfilzavnkjjriog7vliv20r86gnng8w90kpg7mb350rfqwryvj3p1c8ai7ofu8ddzk7t4k7d0q6rduni9d3y1y87ar5gwkaa18udr8i23o7h1wwbe9rpudeqs1u4dis2wsnvhhogvxa08kp5tq8ft16ck4c8sr5bbu5unb8ewxmirskb7758gyf8o04grnp02q9v4kkrs4zfb93jhvhrc2zjmykgoqxgydb65nzrqw1thlprvbi1wh1vrb1bpoqlmnh5l3m0jtem0lfyf4cn0ptlhgn3uscrl6nc2yxlcuq0ey5brio2zobo456oxohar5l8onaayik56mqd2f6sdf732dg3r3tsqdanvsy4wm1qg25jru5gims6a7izngzo7jxktdh9q8is62j7yuj2011fzby4iri5d15l33gt78tmpiu2luwhtpllc18550xcys65h63wn0d4rxvvwt0q1e772y3vjhge6e7jpb91akgs2m2zjlggt3plf2kdhkyanp3s2znm7pl560ndnfcoss2dm8z34h1bjzihude9twx0gnuah0i5y8785hgdzlbzfml610c1x9ac3kdq6k65zgcm2nsgbmizlkfrkcu7wo9hy3butdx94i38px1m8k673h5mmh8o3bvj1o6rbia1uyqg7kne8vvsdm131dc594kfu5zsoz8a3392fi07lnomjmfseiom0xkya6ee4g06d106qp3bsvd7v661h99tpm0f8rvbkcam7b3slot0pacawdyc6vw9ggxlbjeggjuaortzol1y8qt4dh7lndbkv2poc6b0obqy99dl18696dq1hmr6snt5yss1f760kncifdgrtmqgk0b1tgupryv5vojc14pddkv4byfo7x8tqv2d5kz3kg2hvi7htph80da3l9x1oyv06wqtn0fe2f2dhzfixhx0c6sqv7353f8g5ip6o7462e2objh9v9skx8vdgx9pcfqrljioeffqss75916moq8x1m0cjd9gu3y2s44ig4pebgad4vfsnsis8z4182sm6cd2o9kawdeh2wjo3mkzegvsxso44sntkounnsvor0aaw805t2xmab5hgwbtipt023clcak0jgemv3b40o6ra25p4qax3y2omxk8ix2v591075wx8zvz6509jtwfuk8f2egwa2xr6emz2rltzmvkw60ipz2mkfst6tn5k2zbwn1nqs3e5571zt49s3vd8yzz3wf3nr748b9ncaveansibbl9szdl81kmt6foaetngvo52c298ty1lq4pbk4bqt318y5tpoyhkltdj1016s0zvgcsshcbxg04fwtafugsvoivp7hbtsnkyr3uql1l8dzgr58q6etmm6wt76cbfy71ccyau31v0vcj6x5bwmy7lswn9sf5q66phxgc6hrj5wcri3b9d2ngftphqywftag2654f92dc3mbsidq5cd3mmgq4fcf3x64cj1gsq7vrvvsmzvnqok7exhglchlmwp8df3ht6ey60rwuk97k3j2c4oo7jyjt8ojko397arn25uoj4ob5xuyju8s5mm6nsjc70o73xwria7l1yv3dhxp5raihq99vjssxuqcapa4tpyjxrgmzxlya8p6fg824o05zdq4r8cej6qsiov4xvsxes9bpssl0s3piao45mzsxb7zc368udrbhy1l987jl1ds7iviq7j2rcl70iughzlgd3aoyf6ebbmb1u00oj7or0hzhstokmt4ykcktpykntlzkx8159jm3275oaflczevgwbr1pize9gxd8xc510937ed7wluj4exi0gda6co5858fsrky7lhj2tuqzcerdtem9hzva0qlw73nzipf6t6mydebkgp88f52ro5nr292ewcrql193p8w5uros3e8ysmvycclazvpfyla8kqmw10nctsaookql6vufi880q9b8r4kpe6xvikgdmc0ni29b3i9cjffzh7hnuxaqi44lyn3egfunk21j5xsk6azqy1g6e9eogbmmup6263mi0ts9nbn50xr3n5gc6i2n6w6wjth4kz3zcet2urpxa3wycx0fq741c1bu61zq9371dtxyf0ja93x637dfy9saxi6cge0jgzkm37nsv8jlrgko8q6bsyjh4p2m7o3kw9ken6atbmh34ey3jbw4xpo9xfn2o5m7ejzwzusjm7iqty7hskacdez019juqi23pok65kpm723255xq3cwjbvpgvlbkbaqs4dy587b0sh0xicese1hx819n879fjcoliu46oxa97zk6v3gxi20gpbgt3i1t8ot6tedr7llk1eq6hf8de8m3xsri1f5bsriwdq4slnbzif4vae41dtutyl5ho1h4jwwqratt6dbmij4rhtv7q63c6toesr36unzhq6ahsepa7o6gkdt9j40j79jv1ex9hl07dkqsgzc443mme2x3t6ystyep7ncis2g4mak5wdf:1:01:01:001
Full address length: 3023 characters
Decoded full text: 'i love python'
Decoded full text length: 13 characters
--------------------------------------------------------------------------------
Execution time: 0.055589 seconds
--------------------------------------------------------------------------------
*** End ***
```

***

## Information for developers:

- `pip install setuptools twine wheel`
- `pip install build`
- `pip install --upgrade pip`
- `python -m build`
- `twine upload dist/*`

### Tests:

- `pip install pytest`
- `pip install pytest-cov`
- `pip install -e .`
- `pytest tests/`
- `pytest --cov=smart_babylon_library --cov-report=html`

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2025, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------
