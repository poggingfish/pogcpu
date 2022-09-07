class bit():
    def __init__(self):
        self.bin = 0
    def one(self):
        self.bin = 1
    def zero(self):
        self.bin = 0
    def get(self):
        return self.bin
global iota_counter
iota_counter = -1
def iota(reset=False):
    global iota_counter
    if reset==True:
        iota_counter= -1
    iota_counter+=1
    return iota_counter