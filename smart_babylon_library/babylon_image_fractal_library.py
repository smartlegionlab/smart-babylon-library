import hashlib
import random
from PIL import Image
import noise
import numpy as np


class BabylonImageFractalLibrary:
    def __init__(self, width=1920, height=1080, scale=100, octaves=6, persistence=0.5, lacunarity=2.0):
        self.width = width
        self.height = height
        self.scale = scale
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity

    def generate_seed(self, address):
        hash_value = hashlib.sha256(address.encode()).hexdigest()
        return int(hash_value[:8], 16) % 1000000

    def generate_perlin_noise(self, seed, width, height):
        noise_map = np.zeros((height, width))
        for y in range(height):
            for x in range(width):
                noise_map[y][x] = noise.pnoise2(
                    x / self.scale,
                    y / self.scale,
                    octaves=self.octaves,
                    persistence=self.persistence,
                    lacunarity=self.lacunarity,
                    repeatx=width,
                    repeaty=height,
                    base=seed
                )
        return noise_map

    def generate_fractal(self, seed, width, height):
        random.seed(seed)
        size = max(width, height)
        size = 2 ** (int(np.log2(size - 1)) + 1) + 1
        fractal_map = np.zeros((size, size))

        fractal_map[0][0] = random.random()
        fractal_map[0][-1] = random.random()
        fractal_map[-1][0] = random.random()
        fractal_map[-1][-1] = random.random()

        step = size - 1
        while step > 1:
            half = step // 2

            for y in range(half, size, step):
                for x in range(half, size, step):
                    fractal_map[y][x] = (
                                                fractal_map[y - half][x - half] +
                                                fractal_map[y - half][x + half] +
                                                fractal_map[y + half][x - half] +
                                                fractal_map[y + half][x + half]
                                        ) / 4 + random.uniform(-1, 1) * (half / size)

            for y in range(0, size, half):
                for x in range((y + half) % step, size, step):
                    total = 0
                    count = 0
                    if y >= half:
                        total += fractal_map[y - half][x]
                        count += 1
                    if y + half < size:
                        total += fractal_map[y + half][x]
                        count += 1
                    if x >= half:
                        total += fractal_map[y][x - half]
                        count += 1
                    if x + half < size:
                        total += fractal_map[y][x + half]
                        count += 1
                    fractal_map[y][x] = total / count + random.uniform(-1, 1) * (half / size)

            step //= 2

        return fractal_map[:height, :width]

    def generate_image(self, address):
        seed = self.generate_seed(address)

        red = self.generate_perlin_noise(seed, self.width, self.height)
        green = self.generate_perlin_noise(seed + 1, self.width, self.height)
        blue = self.generate_perlin_noise(seed + 2, self.width, self.height)

        fractal = self.generate_fractal(seed, self.width, self.height)

        image_data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        for y in range(self.height):
            for x in range(self.width):
                r = int((red[y][x] + 1) * 127.5 + fractal[y][x] * 50) % 256
                g = int((green[y][x] + 1) * 127.5 + fractal[y][x] * 50) % 256
                b = int((blue[y][x] + 1) * 127.5 + fractal[y][x] * 50) % 256
                image_data[y][x] = [r, g, b]

        image = Image.fromarray(image_data, "RGB")
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
    library = BabylonImageFractalLibrary()

    random_address = library.generate_random_address()
    print(f"Random address: {random_address}")

    library.save_image(random_address, "fractal_perlin_image.png")
    print("The image has been saved to file. 'fractal_perlin_image.png'")
