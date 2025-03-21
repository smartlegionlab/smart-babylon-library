import hashlib
import random
from PIL import Image


class BabylonImageLibrary:
    def __init__(self, width=1920, height=1080):
        self.width = width
        self.height = height

    def generate_image(self, seed):
        hash_value = hashlib.sha256(seed.encode()).hexdigest()
        image = Image.new("RGB", (self.width, self.height))
        pixels = image.load()

        hash_index = 0
        for y in range(self.height):
            for x in range(self.width):
                if hash_index + 6 > len(hash_value):
                    hash_value = hashlib.sha256(hash_value.encode()).hexdigest()
                    hash_index = 0
                r = int(hash_value[hash_index:hash_index+2], 16) % 256
                g = int(hash_value[hash_index+2:hash_index+4], 16) % 256
                b = int(hash_value[hash_index+4:hash_index+6], 16) % 256
                pixels[x, y] = (r, g, b)
                hash_index += 6
        return image

    def get_image(self, address):
        return self.generate_image(address)

    def save_image(self, address, filename="output.png"):
        image = self.get_image(address)
        image.save(filename)

    @staticmethod
    def generate_random_address():
        room = random.randint(1, 100)
        wall = random.randint(1, 6)
        shelf = random.randint(1, 10)
        volume = random.randint(1, 10)
        book = random.randint(1, 100)
        page = random.randint(1, 1000)
        return f"Room{room}:Wall{wall}:Shelf{shelf}:Volume{volume}:Book{book}:Page{page}"


if __name__ == "__main__":
    library = BabylonImageLibrary()

    random_address = library.generate_random_address()
    print(f"Random address: {random_address}")

    library.save_image(random_address, "random_image.png")
    print("The image has been saved to file. 'random_image.png'")
