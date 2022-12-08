from PIL import Image
import numpy as np

with open('input') as f:
    input_data = f.read()


input_array = input_data.splitlines()

input_width = len(input_array[0])
input_height = len(input_array)

data_array: list[list[float]] = []

for j in range(len(input_array)):
    data_array.append([float(num) for num in input_array[j]])

np_data = np.asarray(data_array)
assert np_data.shape == (input_height, input_height)
np_data_flattened = np_data.flatten()
# print(np_data_flattened)
# print(np_data_flattened.shape)

np_data_normalized = np_data_flattened * (255.0/np_data_flattened.max())

print(np_data_normalized)

img = Image.frombuffer("L", (input_width, input_height), np_data_normalized)
img.save("heightmap.png")
