import torch

class Kinematics:

    #vector is a unit vector for now
    def __init__(self, length: int, width: int, initial_direction_radians: float):
        self.length = length
        self.width = width

        self.direction_radians = torch.full((length, width), initial_direction_radians)
        self.direction_x = torch.cos(self.direction_radians)
        self.direction_y = torch.sin(self.direction_radians)
    
    def update_direction(self, new_direction_radians: float):
        self.direction_radians = torch.full((self.length, self.width), new_direction_radians)
        self.direction_x = torch.cos(self.direction_radians)
        self.direction_y = torch.sin(self.direction_radians)

    #Crop a tensor to a certain size
    def _crop_tensor(tensor: torch.Tensor, new_length: int, new_width: int):
        assert new_length <= tensor.shape[0]
        assert new_width <= tensor.shape[1]

        return tensor[:new_length, :new_width]
    
    #Crop all the direction tensors to a certain size
    def crop_direction_tensors(self, new_length: int, new_width: int):
        self.direction_radians = self._crop_tensor(self.direction_radians, new_length, new_width)
        self.direction_x = self._crop_tensor(self.direction_x, new_length, new_width)
        self.direction_y = self._crop_tensor(self.direction_y, new_length, new_width)


    

        





