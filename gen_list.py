import random
import math

dataset_type = "real"
city = "london"
img_type = "Sem_seg"
slice_w = 0
slice_h = 0
iter = 0


input_str = f"{city}/{city}_{dataset_type}/Color/slice_{slice_w}_{slice_h}_{iter}.png\t{city}/{city}_{dataset_type}/Sem_seg/slice_{slice_w}_{slice_h}_{iter}.png"
real_str = f"cbus/train/test/train_%d.png"
# input_str_no_parentheses = "unet/data/synthset-2.1/synthset/color/row-%d-column-%d.png\tunet/data/synthset-2.1/synthset/sem_seg/row-%d-column-%d.png"
val_str = ""
train_str = ""
test_str = "cbus/train/test/train_%d.png\tcbus/labels/test/train_%d.png"

# for i in range(0, 500):
#     test_str += input_str % (i, i)
#     test_str += '\n'


# for i in range (1, 14):
#     for j in range (1, 14):
#         for k in range (1, 5):
#             if k == 1:
#                 output_str += input_str_no_parentheses % (i, j, i, j)
#             else:
#                 output_str += input_str % (i, j, k, i, j, k)
#             output_str += '\n'
#         output_str += input_str % (i, j, i, j, 5)
#         output_str += '\n'

total_counter = 0
val_counter = 0
num_slices_horz = 26
num_slices_vert = 32
num_iters = 2
num_samples = 20
val_percentage = 0.2

for i in range (0, num_slices_horz):
    for j in range (0, num_slices_vert):
        for k in range(0, num_iters):
            if total_counter < num_samples or val_counter < num_samples * val_percentage:
                print("ya yeet")
                iter = k
                slice_w = i
                slice_h = j
                input_str = f"{city}/{city}_{dataset_type}/Color/slice_{slice_w}_{slice_h}_{iter}.png\t{city}/{city}_{dataset_type}/Sem_seg/slice_{slice_w}_{slice_h}_{iter}.png"
                if val_counter < num_samples * val_percentage and random.random() > 1 - val_percentage:
                    val_str += input_str
                    val_str += '\n'
                    val_counter += 1
                else:
                    train_str += input_str
                    train_str += '\n'
                total_counter += 1
            # test_str += input_str % (i, j, i, j)
            # test_str += '\n'

file = open("C:\\Users\\bachc\\Documents\\list.txt","w")
file.write(train_str)
file.write('\n')
file.write(val_str)
# file.write(test_str)

# input_file = "C:\\Users\\bachc\\Documents\\list.txt"
# output_file = "C:\\Users\\bachc\\Documents\\list.txt"  # Can be same as input_file for in-place

# with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
#     for line in f_in:
#         new_line = line.replace('    ', '\t')
#         f_out.write(new_line)
