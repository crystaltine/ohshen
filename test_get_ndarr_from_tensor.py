from heatmap2d import get_rgb_ndarr
from unittest import TestCase
import torch, numpy

class TestTensorToArray(TestCase):
    def __init__(self):
        super().setUp()

    def test_get_ndarr_from_tensor(self):
        print("fdsfs")
        test_tensor = torch.Tensor([
            [0.0, 0.5, 1.0],
            [0.5, 1.0, 0.5],
            [1.0, 0.5, 0.0]
        ])
        # expected output will be a 3x3x3 with each value being some value 0-255
        
        output = get_rgb_ndarr(test_tensor)
        
        # check if each value is between 0 and 255
        for elem in numpy.nditer(output):
            self.assertTrue(elem >= 0 and elem <= 255)

tester = TestTensorToArray()
tester.test_get_ndarr_from_tensor()
print("yay")