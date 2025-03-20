# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from smart_babylon_library import BabylonLibrary
from smart_babylon_library.tools import timeit


@timeit
def main():
    library = BabylonLibrary()

    text_to_search = 'test'

    full_address = library.search_by_content(text_to_search)

    print(f"Address for text '{text_to_search}': {full_address}")

    content_result = library.search_by_address(full_address)

    print(f"Contents at address '{full_address}': {content_result}")


if __name__ == '__main__':
    main()
