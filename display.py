import cpu
import curses
from load import load
Cpu = cpu.Cpu()
Cpu.reset()
def main():
    load(Cpu)
    _hz = 60
    screen = curses.initscr()
    screen.nodelay(1)
    curses.noecho()
    screen.clear()
    Cpu.hz = _hz
    hz = []
    
    curses.curs_set(0)
    debug = False
    turbo = False
    step = False
    x = 0
    while Cpu.isRunning:
        getch = screen.getch()
        if getch == ord("d"):
            if debug == True:
                debug = False
            elif debug == False:
                debug = True
            hz = []
        if debug:
            screen.addstr(0,64,"Debug mode!")
            screen.refresh()
            Cpu.hz = 4
        if not debug:
            screen.addstr(0,64,"                ")
            screen.refresh()
            Cpu.hz = _hz
        if getch == ord("s"):
            if step == True:
                step = False
                screen.addstr(1,64,"                ")
                screen.nodelay(1)
                Cpu.hz = _hz
            elif step == False:
                step = True
                Cpu.hz = 100
            hz = []
        if step:
            screen.addstr(1,64,"Step mode!")
            screen.nodelay(0)
            x+=1
            screen.refresh()
        hz.append(Cpu.cycle())
        screen.addstr(0,0,"A: " + str(Cpu.Reg.A)+"           ")
        screen.addstr(1,0,"B: " + str(Cpu.Reg.B)+"           ")
        screen.addstr(2,0,"C: " + str(Cpu.Reg.C)+"           ")
        screen.addstr(3,0,"ACC: " + str(Cpu.Reg.ACC)+"       ")
        screen.addstr(4,0,"PC: " + hex(Cpu.Reg.PC)+"         ")
        screen.addstr(0,16,"Instruction: " + Cpu.decode(Cpu.Ram.viewAddr16(Cpu.Reg.PC))+"       ")
        screen.addstr(1,16,"Clock speed: "+str(round(sum(hz)/len(hz),2))+"hz      ")
        if len(hz) > 10000:
            hz = hz[512:len(hz)]
    curses.endwin()

try:
    main()
except:
    # In the event of an error, restore the terminal
    # to a sane state.
    curses.echo() ; curses.nocbreak()
    curses.curs_set(1)
    curses.endwin()