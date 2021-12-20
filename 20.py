
from functools import partial

import numpy as np
from scipy.ndimage import generic_filter

from utils import iter_file


def bin_number(arr, algorithm):
    bin_str = "".join(map(str, arr.astype(int).tolist()))
    return algorithm[int(bin_str, 2)]

def solve(algorithm, img, n):
    img = np.array([[char == '#' for char in row] for row in img], dtype='int')
    img = np.pad(img, n*2) # Probably assumes the odd number of enhancement
    filter = partial(bin_number, algorithm = [int(char == '#') for char in algorithm])
    for n in range(n):
        img = generic_filter(img, filter, size=3)
    return np.count_nonzero(img)

lines = list(iter_file(20))
algorithm = lines[0]
image = lines[2:]

print(solve(algorithm, image, 2))
print(solve(algorithm, image, 50))


