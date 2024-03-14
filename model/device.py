import torch

class Device:
    def __init__(self):
        self._gpu = torch.cuda.is_available() or torch.backends.mps.is_available()
        self._device = torch.device("cuda" 
                                    if torch.cuda.is_available() 
                                    else "mps"
                                    if torch.backends.mps.is_available()
                                    else "cpu")
        
    def is_GPU(self):
        return self._gpu
    
    def get_device(self):
        return self._device