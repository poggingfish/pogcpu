import other
class Ram():
    def __init__(self):
        self.ram = []
        for i in range(0,65536*8):
            x = other.bit()
            self.ram.append(x)
    def setAddr16(self,address,value):
        x = f'{value:16b}'
        if len(x) > 16:
            raise ValueError
        for i in range(0,16):
            if x[i] == "0":
                self.ram[address*16+i].zero()
            if x[i] == "1":
                self.ram[address*16+i].one()
    def viewAddr16(self,address):
        value = ""
        for x in range(0,16):
            value += str(self.ram[address*16+x].get())
        return(int(value,2))