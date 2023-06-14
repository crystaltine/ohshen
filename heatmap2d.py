import torch
import stringcolor
from time import sleep
import colorsys
import math
from media import ConductiveSurface
from log import Log



if torch.cuda.is_available():
    print("CUDA is available, using GPU")
else:
    print("CUDA is not available, using CPU")

#constants
LENGTH = 10
WIDTH = 10

#Set up log
Log("tests", LENGTH, WIDTH)

# convert to 1d tensor
heatmap_random = ConductiveSurface(LENGTH, WIDTH, 0)
heatmap_random.heat_square((5, 5), 3, 1)

heatmap_random = heatmap_random.get_iterable()

def runtimestep(heatmap: torch.Tensor, time_counter):
    # Create tensors for averaging with shifted versions of the heatmap tensor
    shifted_left    = torch.roll(heatmap, shifts=1)
    shifted_right   = torch.roll(heatmap, shifts=-1)
    shifted_up      = torch.roll(heatmap, shifts=1, dims=0)
    shifted_down    = torch.roll(heatmap, shifts=-1, dims=0)
    
    # Set certain edges to zero so numbers dont wrap around
    shifted_left[:, -1] = 0
    shifted_right[:, 0] = 0
    shifted_up[-1, :] = 0
    shifted_down[0, :] = 0
    
    # Apply padding for the edge cases
    padded_heatmap       = torch.nn.functional.pad(heatmap, (1, 1, 1, 1), mode='constant', value=0)
    padded_shifted_left  = torch.nn.functional.pad(shifted_left, (1, 1, 1, 1), mode='constant', value=0)
    padded_shifted_right = torch.nn.functional.pad(shifted_right, (1, 1, 1, 1), mode='constant', value=0)
    padded_shifted_up    = torch.nn.functional.pad(shifted_up, (1, 1, 1, 1), mode='constant', value=0)
    padded_shifted_down  = torch.nn.functional.pad(shifted_down, (1, 1, 1, 1), mode='constant', value=0)
    
    # Calculate the average using tensors and avoid iteration
    # average the 3x3 square around each element
    avg = (padded_heatmap + padded_shifted_left + padded_shifted_right + padded_shifted_up + padded_shifted_down) / 5
    
    # remove padding
    avg = avg[1:-1, 1:-1]
    
    print_str_representation(avg, time_counter)
    # f.write(f"{','.join([format(val, '.3f') for val in _aux_tensor.tolist()])}\n")

    return avg


def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

def print_str_representation(arr: torch.Tensor, time_counter) -> None:
    if torch.cuda.is_available():
        arr = arr.to(torch.device("gpu"))  # Move tensor to GPU
    else:
        arr = arr.to(torch.device("cpu"))  # Move tensor to CPU
    
    for row in arr.tolist():
        colored_chars = [get_color_escape(*val_to_rgb(val), background=True) + "   " for val in row]
        totalstr = "".join(colored_chars) + '\033[0m'
        print(f"{totalstr}")

def val_to_rgb(val: float) -> tuple[int]:
    """
    maps 0-1 -> rgb255 linearly
    """
    # desmos eq: \frac{\ln\left(\sqrt{x}+1\right)}{1.1}
    # scaled_val = math.log(math.sqrt(val) + 1) / 1.1
    scaled_val = -0.693*val+0.693
    
    _unscaled = colorsys.hsv_to_rgb(scaled_val, 1, 1)
    return tuple([int(val * 255) for val in _unscaled])


time_counter = 0
#print()
print_str_representation(heatmap_random, time_counter)
print(f"\n\033[0mTime: {time_counter}; Hottest: {round(heatmap_random.max().item(), 3)}; Coolest: {round(heatmap_random.min().item(), 3)}")
print("\n\n")
print(heatmap_random.shape)
while True:
    time_counter += 1
    heatmap_random = runtimestep(heatmap_random, time_counter)
    #print(heatmap_random)
    sleep(0.5)
    print(f"\033[0mTime: {time_counter}; Hottest: {round(heatmap_random.max().item(), 3)}; Coolest: {round(heatmap_random.min().item(), 3)}")
    print("\n\n")
    if time_counter == 50: break
    #print(f"\nIteration: {time_counter}; Shape={heatmap_random.shape}", end="\r")

