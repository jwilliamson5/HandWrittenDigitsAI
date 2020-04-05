from random import randrange
import time

labels = []
with open(R"C:\Users\jwill\Desktop\Handwritten Number Identifier\MNIST Handwritten "
          R"digits\training\train-labels.idx1-ubyte", "rb") as f:
    f.read(4)  # skip first 4 bytes because they don't mean anything
    byte = f.read(4)
    size = int.from_bytes(byte, "big")
    byte = f.read(1)
    while byte != b"":
        labels.append(byte[0])
        byte = f.read(1)

with open(R"C:\Users\jwill\Desktop\Handwritten Number Identifier\MNIST Handwritten "
          R"digits\training\train-images.idx3-ubyte", "rb") as f:
    f.read(4)  # skip first 4 bytes because they don't mean anything
    size = int.from_bytes(f.read(4), "big")
    row_size = int.from_bytes(f.read(4), "big")
    column_size = int.from_bytes(f.read(4), "big")
    images = []
    byte = f.read(1)
    while byte != b"":
        images.append([])
        for y in range(0, column_size):
            images[-1].append([])
            for x in range(0, row_size):
                images[-1][-1].append(byte[0])
                byte = f.read(1)
    # while True:
    #     i = randrange(size)
    #     print(labels[i])
    #     for y in range(0, 28):
    #         p_str = ""
    #         for x in range(0, 28):
    #             val = images[i][y][x]
    #             if val < (255/2):
    #                 p_str += " "
    #             else:
    #                 p_str += str(labels[i])
    #         print(p_str)
    #     time.sleep(5)


