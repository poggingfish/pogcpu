class Reg():
    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0
        self.PC = 0
        self.ACC = 0
    def setA(self, value):
        if value > 65535 or value < 0:
            raise ValueError
        self.A = value
    def setB(self, value):
        if value > 65535 or value < 0:
            raise ValueError
        self.B = value
    def setC(self, value):
        if value > 65535 or value < 0:
            raise ValueError
        self.C = value
    def setACC(self,value):
        if value > 65535 or value < 0:
            raise ValueError
        self.ACC = value
    def setPC(self, value):
        if value > 65535 or value < 0:
            raise ValueError
        self.PC = value