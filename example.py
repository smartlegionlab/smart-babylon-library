# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2025, Alexander Suvorov
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
"""
Comprehensive example demonstrating ALL features of Smart Babylon Library
"""
from smart_babylon_library import SmartBabylonLibrary, LibraryConfig
from smart_babylon_library.character_sets.alphabets import CyrillicAlphabet, LatinAlphabet
from smart_babylon_library.character_sets.digits import Digits
from smart_babylon_library.character_sets.punctuation import Punctuation
from smart_babylon_library.character_sets.core import CharacterSet


class EmojiCharacterSet(CharacterSet):
    """Custom character set with emojis"""

    @property
    def characters(self):
        return list(
            "😀😃😄😁😆😅😂🤣🥲☺️😊😇🙂🙃😉😌😍🥰😘😗😙"
            "😚😋😛😝😜🤪🤨🧐🤓😎🥸🤩🥳😏😒😞😔😟😕🙁☹️"
            "😣😖😫😩🥺😢😭😤😠😡🤬🤯😳🥵🥶😱😨😰😥😓🤗"
            "🤔🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲🥱😴🤤😪😵🤐🥴"
            "🤢🤮🤧😷🤒🤕🤑🤠 ")

    @property
    def name(self) -> str:
        return "Emoji Character Set"


def demo_basic_usage():
    """Basic library usage"""
    print("🔹 1. BASIC LIBRARY USAGE")
    print("=" * 50)

    library = SmartBabylonLibrary()
    book = library.get_book(floor=1, room=3, cabinet=2, shelf=5, book_number=42)

    print(f"📖 Book: {book}")
    print(f"📝 Title: {book.title}")
    print(f"📄 Total pages: {book.max_pages}")
    print(f"📍 Coordinates: {book.coordinates}")
    print(f"🌌 Universe: {book.config.universe}")

    # Read first few pages
    for page_num in range(min(2, book.max_pages)):
        page = book.get_page(page_num)
        content_preview = page.content[:80] + "..." if len(page.content) > 80 else page.content
        print(f"  📃 Page {page_num}: {content_preview}")
    print()


def demo_json_serialization():
    """JSON serialization features"""
    print("🔹 2. JSON SERIALIZATION")
    print("=" * 50)

    # Create library with specific universe
    fantasy_config = LibraryConfig(universe="fantasy_realm")
    fantasy_library = SmartBabylonLibrary(fantasy_config)

    # Get book as JSON
    book = fantasy_library.get_book(floor=2, room=1, cabinet=3, shelf=4, book_number=10)
    book_json = book.to_json()
    print(f"📖 Book JSON with universe:")
    print(book_json)

    # Get specific page as JSON via library
    page_json = fantasy_library.get_page_json({
        'floor': 2, 'room': 1, 'cabinet': 3, 'shelf': 4, 'book': 10, 'page': 0
    })
    print(f"\n📃 Page JSON with universe:")
    print(page_json[:200] + "..." if len(page_json) > 200 else page_json)

    # Show universe in parsed JSON
    import json
    book_dict = json.loads(book_json)
    print(f"\n🌌 Universe from JSON: '{book_dict['universe']}'")
    print(f"📖 Title from JSON: '{book_dict['title'][:30]}...'")
    print()


def demo_custom_configurations():
    """Different configuration presets"""
    print("🔹 3. CUSTOM CONFIGURATIONS")
    print("=" * 50)

    # Short documents configuration
    short_config = LibraryConfig(
        universe="short_docs_universe",
        title_length_range=(5, 20),
        content_length_range=(50, 200),
        pages_per_book_range=(3, 10)
    )

    # Novel configuration
    novel_config = LibraryConfig(
        universe="novels_universe",
        title_length_range=(10, 50),
        content_length_range=(1000, 5000),
        pages_per_book_range=(100, 300)
    )

    short_lib = SmartBabylonLibrary(short_config)
    novel_lib = SmartBabylonLibrary(novel_config)

    short_book = short_lib.get_book(1, 1, 1, 1, 1)
    novel_book = novel_lib.get_book(1, 1, 1, 1, 1)

    print(f"📓 Short Book (Universe: {short_book.config.universe}):")
    print(f"  Title length: {len(short_book.title)}")
    print(f"  Pages: {short_book.max_pages}")
    print(f"  Page 0 length: {len(short_book.get_page(0).content)}")

    print(f"\n📚 Novel Book (Universe: {novel_book.config.universe}):")
    print(f"  Title length: {len(novel_book.title)}")
    print(f"  Pages: {novel_book.max_pages}")
    print(f"  Page 0 length: {len(novel_book.get_page(0).content)}")

    # Show JSON includes universe
    short_json = short_book.to_json()
    import json
    short_dict = json.loads(short_json)
    print(f"\n✅ Short book JSON includes universe: '{short_dict['universe']}'")
    print()


def demo_multiple_universes():
    """Multiple universe feature demonstration"""
    print("🔹 4. MULTIPLE UNIVERSES FEATURE")
    print("=" * 50)

    # Different universes with same coordinates
    universes = {
        "middle_earth": "🧙 Fantasy World",
        "andromeda": "🚀 Sci-Fi Galaxy",
        "cyber_city": "🤖 Cyberpunk Metropolis",
        "ancient_egypt": "🐫 Ancient Egypt"
    }

    books = {}
    for universe_id, universe_name in universes.items():
        config = LibraryConfig(universe=universe_id)
        library = SmartBabylonLibrary(config)
        book = library.get_book(floor=1, room=1, cabinet=1, shelf=1, book_number=1)
        books[universe_name] = book

    print("Same coordinates across different universes:\n")
    for universe_name, book in books.items():
        title_preview = book.title[:25] + "..." if len(book.title) > 25 else book.title
        print(f"  {universe_name}:")
        print(f"    📖 {title_preview}")
        print(f"    📄 {book.max_pages} pages")
        print(f"    🌌 Universe: '{book.config.universe}'")

    # Verify they're all different
    titles = [book.title for book in books.values()]
    unique_titles = len(set(titles))
    print(f"\n✅ All titles are unique: {unique_titles == len(titles)}")

    # Show JSON representation includes universe
    sample_book = list(books.values())[0]
    book_dict = sample_book.to_dict()
    print(f"\n📊 JSON includes universe field: 'universe' = '{book_dict['universe']}'")
    print()


def demo_custom_character_sets():
    """Custom character sets demonstration"""
    print("🔹 5. CUSTOM CHARACTER SETS")
    print("=" * 50)

    # Only digits
    digits_config = LibraryConfig(
        universe="numbers_only",
        title_length_range=(5, 15),
        character_sets=[Digits()]
    )

    # Only Latin
    latin_config = LibraryConfig(
        universe="english_only",
        title_length_range=(5, 15),
        character_sets=[LatinAlphabet()]
    )

    # Emoji only
    emoji_config = LibraryConfig(
        universe="emoji_world",
        title_length_range=(3, 8),
        character_sets=[EmojiCharacterSet()]
    )

    # Mixed custom set
    custom_chars_config = LibraryConfig(
        universe="custom_chars",
        title_length_range=(5, 12),
        character_sets=[Digits(), Punctuation()]
    )

    configs = {
        "🔢 Digits Only": digits_config,
        "🔤 Latin Only": latin_config,
        "😊 Emoji Only": emoji_config,
        "🔣 Digits + Punctuation": custom_chars_config
    }

    for name, config in configs.items():
        library = SmartBabylonLibrary(config)
        book = library.get_book(1, 1, 1, 1, 1)
        print(f"{name} (Universe: {book.config.universe}):")
        print(f"  📖 '{book.title}'")
        print(f"  📏 Length: {len(book.title)} chars")

        # Verify character restrictions
        if name == "🔢 Digits Only":
            is_digits_only = all(c in '0123456789 ' for c in book.title)
            print(f"  ✅ Only digits: {is_digits_only}")
        elif name == "😊 Emoji Only":
            has_emojis = any(c in EmojiCharacterSet().characters for c in book.title)
            print(f"  ✅ Contains emojis: {has_emojis}")
    print()


def demo_deterministic_behavior():
    """Demonstrate deterministic generation"""
    print("🔹 6. DETERMINISTIC BEHAVIOR")
    print("=" * 50)

    config = LibraryConfig(universe="determinism_test")
    library = SmartBabylonLibrary(config)

    # Same coordinates = same content
    book1 = library.get_book(floor=5, room=10, cabinet=15, shelf=20, book_number=25)
    book2 = library.get_book(floor=5, room=10, cabinet=15, shelf=20, book_number=25)

    print("Same universe, same coordinates:")
    print(f"  Book 1 title: '{book1.title}'")
    print(f"  Book 2 title: '{book2.title}'")
    print(f"  🌌 Universe: '{book1.config.universe}'")
    print(f"  ✅ Titles match: {book1.title == book2.title}")

    # Different coordinates = different content
    book3 = library.get_book(floor=5, room=10, cabinet=15, shelf=20, book_number=26)
    print(f"\n  Book 3 title: '{book3.title}'")
    print(f"  ✅ Different book number = different title: {book1.title != book3.title}")

    # Different universe = different content (even with same coordinates)
    other_config = LibraryConfig(universe="other_universe")
    other_library = SmartBabylonLibrary(other_config)
    book4 = other_library.get_book(floor=5, room=10, cabinet=15, shelf=20, book_number=25)

    print(f"\n  Book 4 (different universe): '{book4.title}'")
    print(f"  🌌 Universe: '{book4.config.universe}'")
    print(f"  ✅ Different universe = different title: {book1.title != book4.title}")

    # Show JSON differences
    book1_json = book1.to_json()
    book4_json = book4.to_json()
    import json
    book1_dict = json.loads(book1_json)
    book4_dict = json.loads(book4_json)

    print(f"\n📊 JSON comparison:")
    print(f"  Book 1 universe: '{book1_dict['universe']}'")
    print(f"  Book 4 universe: '{book4_dict['universe']}'")
    print(f"  Universes differ: {book1_dict['universe'] != book4_dict['universe']}")
    print()


def demo_coordinate_operations():
    """Coordinate system operations"""
    print("🔹 7. COORDINATE OPERATIONS")
    print("=" * 50)

    from smart_babylon_library.library.coordinates import LibraryCoordinates

    # Create coordinates
    coordinates = LibraryCoordinates(floor=3, room=2, cabinet=1, shelf=4, book=7, page=0)
    print(f"Original coordinates: {coordinates}")
    print(f"Seed string: {coordinates.seed}")

    # Convert to dict and back
    coordinates_dict = coordinates.to_dict()
    coordinates_from_dict = LibraryCoordinates.from_dict(coordinates_dict)
    print(f"Round-trip via dict: {coordinates == coordinates_from_dict}")

    # JSON serialization
    coordinates_json = coordinates.to_json()
    coordinates_from_json = LibraryCoordinates.from_json(coordinates_json)
    print(f"Round-trip via JSON: {coordinates == coordinates_from_json}")

    print(f"JSON representation: {coordinates_json}")
    print()


def demo_advanced_universe_scenarios():
    """Advanced universe usage scenarios"""
    print("🔹 8. ADVANCED UNIVERSE SCENARIOS")
    print("=" * 50)

    # Multi-language universes
    languages = {
        "russian_lib": [CyrillicAlphabet(), Digits(), Punctuation()],
        "english_lib": [LatinAlphabet(), Digits(), Punctuation()],
        "bilingual_lib": [CyrillicAlphabet(), LatinAlphabet(), Digits(), Punctuation()],
        "scientific_lib": [LatinAlphabet(), Digits(), Punctuation()]
    }

    for lang_name, char_sets in languages.items():
        config = LibraryConfig(
            universe=lang_name,
            title_length_range=(10, 30),
            character_sets=char_sets
        )
        library = SmartBabylonLibrary(config)
        book = library.get_book(1, 1, 1, 1, 1)

        print(f"🌐 {lang_name.replace('_', ' ').title()}:")
        print(f"  Character sets: {[cs.name for cs in char_sets]}")
        print(f"  Sample title: '{book.title}'")
        print(f"  Total characters available: {sum(len(cs) for cs in char_sets)}")
        print(f"  Universe: '{book.config.universe}'")

        # Show JSON includes universe
        book_dict = book.to_dict()
        print(f"  ✅ JSON universe: '{book_dict['universe']}'")
        print()


def demo_universe_json_roundtrip():
    """Demonstrate universe preservation in JSON roundtrips"""
    print("🔹 9. UNIVERSE JSON ROUNDTRIP")
    print("=" * 50)

    # Create book in specific universe
    original_config = LibraryConfig(
        universe="json_test_universe",
        title_length_range=(10, 20)
    )
    library = SmartBabylonLibrary(original_config)
    original_book = library.get_book(1, 2, 3, 4, 5)

    print("Original book:")
    print(f"  Title: '{original_book.title}'")
    print(f"  Universe: '{original_book.config.universe}'")

    # Convert to JSON and back
    book_json = original_book.to_json()
    import json
    book_dict = json.loads(book_json)

    # Recreate from JSON data
    recreated_library = SmartBabylonLibrary(LibraryConfig(universe=book_dict['universe']))
    recreated_book = recreated_library.get_book_from_dict(book_dict['coordinates'])

    print("\nRecreated from JSON:")
    print(f"  Title: '{recreated_book.title}'")
    print(f"  Universe: '{recreated_book.config.universe}'")
    print(f"  ✅ Titles match: {original_book.title == recreated_book.title}")
    print(f"  ✅ Universes match: {original_book.config.universe == recreated_book.config.universe}")
    print()


def main():
    """Run all demonstrations"""
    print("🚀 SMART BABYLON LIBRARY - COMPREHENSIVE DEMO")
    print("=" * 60)
    print()

    demo_basic_usage()
    demo_json_serialization()
    demo_custom_configurations()
    demo_multiple_universes()
    demo_custom_character_sets()
    demo_deterministic_behavior()
    demo_coordinate_operations()
    demo_advanced_universe_scenarios()
    demo_universe_json_roundtrip()

    print("🎉 DEMONSTRATION COMPLETE!")
    print("\n📚 Library Features Demonstrated:")
    print("  ✅ Basic book and page generation")
    print("  ✅ JSON serialization with universe")
    print("  ✅ Custom configurations")
    print("  ✅ Multiple universes support")
    print("  ✅ Custom character sets")
    print("  ✅ Deterministic behavior")
    print("  ✅ Coordinate operations")
    print("  ✅ Advanced scenarios")
    print("  ✅ Universe JSON roundtrip")
    print("\n🌌 NEW: Universe included in ALL JSON serializations!")
    print("  📖 Books include 'universe' field")
    print("  📃 Pages include 'universe' field")
    print("  🔄 Full roundtrip support")
    print("  🎯 Deterministic per universe")


if __name__ == "__main__":
    main()
