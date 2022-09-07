def SetTok(Cpu,val):
    Cpu.Ram.setAddr16(Cpu.Reg.PC+1,val)
    Cpu.Reg.setPC(Cpu.Reg.PC+1)
def load(Cpu):
    original_pc = Cpu.Reg.PC
    labels = {}
    with open("main.pasm","r") as read:
        x = read.read().split("\n")
    for y in x:
        tokens = y.split(" ")[1:]
        token = y.split(" ")[0]
        for z in tokens:
            SetTok(Cpu,Cpu.NOP)
        if token.startswith("_"):
            labels.update({token:Cpu.Reg.PC+1})
        else:
            SetTok(Cpu,Cpu.NOP)
    Cpu.Reg.setPC(original_pc)
    for y in x:
        tokens = y.split(" ")[1:]
        token = y.split(" ")[0]
        if token.startswith("_"):
            continue
        if token == "NOP":
            SetTok(Cpu,Cpu.NOP)
        elif token == "END":
            SetTok(Cpu,Cpu.END)
        elif token == "LDA":
            SetTok(Cpu,Cpu.LDA)
        elif token == "LDB":
            SetTok(Cpu,Cpu.LDB)
        elif token == "LDC":
            SetTok(Cpu,Cpu.LDC)
        elif token == "STA":
            SetTok(Cpu,Cpu.STA)
        elif token == "STB":
            SetTok(Cpu,Cpu.STB)
        elif token == "STC":
            SetTok(Cpu,Cpu.STC)
        elif token == "ADD":
            SetTok(Cpu,Cpu.ADD)
        elif token == "SUB":
            SetTok(Cpu,Cpu.SUB)
        elif token == "MUL":
            SetTok(Cpu,Cpu.MUL)
        elif token == "DIV":
            SetTok(Cpu,Cpu.DIV)
        elif token == "SPC":
            SetTok(Cpu,Cpu.SPC)
        elif token == "SWPA":
            SetTok(Cpu,Cpu.SWPA)
        elif token == "SWPC":
            SetTok(Cpu,Cpu.SWPC)
        elif token == "ACC":
            SetTok(Cpu,Cpu.ACC)
        elif token == "MLA":
            SetTok(Cpu,Cpu.MLA)
        elif token == "MLB":
            SetTok(Cpu,Cpu.MLB)
        elif token == "MLC":
            SetTok(Cpu,Cpu.MLC)
        elif token == "CMP":
            SetTok(Cpu,Cpu.CMP)
        elif token == "CMPL":
            SetTok(Cpu,Cpu.CMPL)
        elif token == "CMPM":
            SetTok(Cpu,Cpu.CMPM)
        elif token == "JEO":
            SetTok(Cpu,Cpu.JEO)
        else:
            SetTok(Cpu,Cpu.NOP)
        for x in tokens:
            if x.startswith("_"):
                SetTok(Cpu,int(labels[x])-1)
                continue
            SetTok(Cpu,int(x))
    Cpu.Reg.setPC(original_pc)