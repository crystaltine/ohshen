import torch

class ConductiveBar:
    def __init__(self, length: int = 50):
        self.atoms = torch.Tensor(length).fill_(0)
    
    def add_zone(self, start: int, end: int, temp: float = 0.5):
        for i in range(start, end):
            self.atoms[i] = temp 
            
    def get_iterable(self):
        return self.atoms
    
class ConductiveSurface:
    def __init__(self, length: int, width: int, default_temp: float = 0):
        self.atoms = torch.Tensor(length, width).fill_(default_temp)
    
    def heat_square(self, loc: tuple = (0, 0), radius: int = 2, temperature: float = 0.5) -> None:
        """
        Heats a "square" of atoms around `loc` to `temperature`.
        """
        padded = torch.nn.functional.pad(self.atoms, (radius, radius, radius, radius), mode='constant', value=0)
        
        # change the square region around loc to temperature
        row_region_start = loc[0] - radius
        row_region_end = loc[0] + radius + 1
        col_region_start = loc[1] - radius
        col_region_end = loc[1] + radius + 1
        
        padded[row_region_start:row_region_end,col_region_start:col_region_end] = temperature
        
        # unpad
        self.atoms = padded[radius:-radius, radius:-radius]
            
    def get_iterable(self) -> torch.Tensor:
        return self.atoms
    
# 3d framework
class ConductiveSpace():
    pass