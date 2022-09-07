
from other import iota
import ram,registers
import time



class Cpu():
    def __init__(self):
        self.NOP = iota(True) #No Operation
        self.END = iota() #Ends program
        self.LDA = iota() #Loads into A
        self.LDB = iota() #Loads into B
        self.LDC = iota() #Loads into C
        self.STA = iota() #Stores A in memory 
        self.STB = iota() #Stores B in memory
        self.STC = iota() #Stores C in memory
        self.ADD = iota() #Adds A and B
        self.SUB = iota() #Subtracts A and B
        self.MUL = iota() #Multiplies A and B
        self.DIV = iota() #Divides A and B
        self.SPC = iota() #Set program counter
        self.SWPA = iota() #Swaps A and B
        self.SWPC = iota() #Swaps B and C
        self.ACC = iota() #Loads the accumulator into C
        self.MLA = iota() #Loads memory into A
        self.MLB = iota() #Loads memory into B
        self.MLC = iota() #Loads memory into C
        self.CMP = iota() #Set A to 1 if equal
        self.CMPL = iota() #Set A to 1 if less
        self.CMPM = iota() #Set A to 1 if more
        self.JEO = iota() # Jump if C is equal to one
        
        self.hz = 60
        self.Ram = ram.Ram()
        self.Reg = registers.Reg()
        self.isRunning = True
    def reset(self):
        self.Reg.PC = 0xFFF
        for x in self.Ram.ram:
            if x.get() == 1:
                x.zero()
    def fetch(self):
        return self.Ram.viewAddr16(self.Reg.PC)
    def decode(self,instruction):
        if instruction == self.NOP: return "NOP"
        elif instruction == self.END: return "END"
        elif instruction == self.LDA: return "LDA"
        elif instruction == self.LDB: return "LDB"
        elif instruction == self.LDC: return "LDC"
        elif instruction == self.STA: return "STA"
        elif instruction == self.STB: return "STB"
        elif instruction == self.STC: return "STC"
        elif instruction == self.ADD: return "ADD"
        elif instruction == self.SUB: return "SUB"
        elif instruction == self.MUL: return "MUL"
        elif instruction == self.DIV: return "DIV"
        elif instruction == self.SPC: return "SPC"
        elif instruction == self.SWPA: return "SWPA"
        elif instruction == self.SWPC: return "SWPC"
        elif instruction == self.ACC: return "ACC"
        elif instruction == self.MLA: return "MLA"
        elif instruction == self.MLB: return "MLB"
        elif instruction == self.MLC: return "MLC"
        elif instruction == self.CMP: return "CMP"
        elif instruction == self.CMPL: return "CMPL"
        elif instruction == self.CMPM: return "CMPM"
        elif instruction == self.JEO: return "JEO"
        else: return "NOP"
    def execute(self,instruction):
        if instruction == "NOP":
            return
        if instruction == "END":
            return "ENDED"
        if instruction == "LDA":
            self.Reg.setA(self.Ram.viewAddr16(self.Reg.PC+1))
            self.Reg.setPC(self.Reg.PC+1)
        if instruction == "LDB":
            self.Reg.setB(self.Ram.viewAddr16(self.Reg.PC+1))
            self.Reg.setPC(self.Reg.PC+1)
        if instruction == "LDC":
            self.Reg.setC(self.Ram.viewAddr16(self.Reg.PC+1))
            self.Reg.setPC(self.Reg.PC+1)
        if instruction == "ADD":
            self.Reg.setACC(self.Reg.A+self.Reg.B)
        if instruction == "SUB":
            self.Reg.setACC(self.Reg.A-self.Reg.B)
        if instruction == "DIV":
            self.Reg.setACC(self.Reg.A/self.Reg.B)
        if instruction == "MUL":
            self.Reg.setACC(self.Reg.A*self.Reg.B)
        if instruction == "SPC":
            self.Reg.setPC(self.Reg.A)
        if instruction == "SWPA":
            a = self.Reg.A
            b = self.Reg.B
            self.Reg.setA(b)
            self.Reg.setB(a)
        if instruction == "SWPC":
            b = self.Reg.B
            c = self.Reg.C
            self.Reg.setB(c)
            self.Reg.setC(b)
        if instruction == "ACC":
            self.Reg.setC(self.Reg.ACC)
        if instruction == "STA":
            self.Ram.setAddr16(self.Ram.viewAddr16(self.Reg.PC+1),self.Reg.A)
            self.Reg.setPC(self.Reg.PC+1)
        if instruction == "STB":
            self.Ram.setAddr16(self.Ram.viewAddr16(self.Reg.PC+1),self.Reg.B)
            self.Reg.setPC(self.Reg.PC+1)
        if instruction == "STC":
            self.Ram.setAddr16(self.Ram.viewAddr16(self.Reg.PC+1),self.Reg.C)
            self.Reg.setPC(self.Reg.PC+1)
        if instruction == "MLA":
            self.Reg.A = self.Ram.viewAddr16(self.Ram.viewAddr16(self.Reg.PC+1))
            self.Reg.setPC(self.Reg.PC+1)
        if instruction == "MLB":
            self.Reg.B = self.Ram.viewAddr16(self.Ram.viewAddr16(self.Reg.PC+1))
            self.Reg.setPC(self.Reg.PC+1)
        if instruction == "MLC":
            self.Reg.C = self.Ram.viewAddr16(self.Ram.viewAddr16(self.Reg.PC+1))
            self.Reg.setPC(self.Reg.PC+1)
        if instruction == "CMP":
            i = 0
            if self.Reg.A == self.Reg.B:
                i = 1
            self.Reg.setC(i)
        if instruction == "CMPL":
            i = 0
            if self.Reg.A < self.Reg.B:
                i = 1
            self.Reg.setC(i)
        if instruction == "CMPM":
            i = 0
            if self.Reg.A > self.Reg.B:
                i = 1
            self.Reg.setC(i)
        if instruction == "JEO":
            if self.Reg.C == 1:
                self.Reg.setPC(self.Reg.A)
    def cycle(self):
        begin = time.time()
        instruction = self.fetch()
        instruction = self.decode(instruction)
        if self.execute(instruction) == "ENDED":
            self.isRunning = False
        self.Reg.setPC(self.Reg.PC+1)
        time.sleep(1/self.hz)
        end = time.time()
        hz = round(1/(end-begin),2)
        return hz