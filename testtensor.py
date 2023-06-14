import torch

# makes a random tensor with length 10, filled with numbers from 0-1
ten1 = torch.rand(10)

# unfold: gets sliding windows of size (3), height (0) (actually secretly 1), with step size (1)
# mean: gets the mean of each window
print(ten1.unfold(0, 3, 1).mean(dim=1))