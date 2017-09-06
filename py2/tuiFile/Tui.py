from os import system
import curses
import json


def get_param(screen=None):

    lt = []
    screen.clear()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    screen.border(0)
    screen.addstr(4, 8, "Address >", curses.color_pair(1))
    screen.addstr(6, 8, "GateWay >", curses.color_pair(1))
    screen.addstr(8, 8, "Netmask >", curses.color_pair(1))
    screen.addstr(10, 8, "DNS     >", curses.color_pair(1))
    screen.addstr(12, 8, "Hostname>", curses.color_pair(1))

    screen.addstr(4, 17, " " * 15, curses.A_UNDERLINE)
    screen.addstr(6, 17, " " * 15, curses.A_UNDERLINE)
    screen.addstr(8, 17, " " * 15, curses.A_UNDERLINE)
    screen.addstr(10, 17, " " * 15, curses.A_UNDERLINE)
    screen.addstr(12, 17, " " * 15, curses.A_UNDERLINE)

    screen.refresh()
    input2 = screen.getstr(4, 17, 21)
    input3 = screen.getstr(6, 17, 21)
    input4 = screen.getstr(8, 17, 21)
    input5 = screen.getstr(10, 17, 21)
    input6 = screen.getstr(12, 17, 21)

    lt.append(input2)
    lt.append(input3)
    lt.append(input4)
    lt.append(input5)
    lt.append(input6)

    return lt


def execute_cmd(cmd_string):

    system("clear")
    a = system(cmd_string)
    print ""
    if a == 0:
        print "This operation is effective"
    else:
        print "ERROR! Please check your operation"
    raw_input("======> Enter ")


def menu():

    global screen
    screen = curses.initscr()

    screen.clear()
    curses.start_color()
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    screen.border(0)
    screen.addstr(2, 4, "Configuration system...", curses.color_pair(2))
    screen.addstr(4, 8, "0 - exit", curses.color_pair(2))
    screen.addstr(6, 8, "1 - network configuration", curses.color_pair(2))
    screen.addstr(8, 8, "2 - View disk", curses.color_pair(2))
    screen.addstr(10, 8, "3 - Disk partition", curses.color_pair(2))
    screen.addstr(12, 8, "F2 - Update configuration", curses.color_pair(2))

    screen.refresh()


def main():

    x = 11
    global x
    while x != ord('0'):

        menu()
        x = screen.getch()

        if x == ord('1'):
            dict_zip = {}
            inp1 = get_param(screen)
            inp2 = ['address', 'gateway', 'netmask', 'dns-nameserver', 'hostname']
            dict_zip = dict(zip(inp2, inp1))

            jsObj = json.dumps(dict_zip)
            fileObj = open('jsonFile.json', 'w')
            fileObj.write(jsObj)
            fileObj.close()

            curses.endwin()
            execute_cmd("ls")
        if x == ord('2'):
            curses.endwin()
            execute_cmd("df -h")
        if x == ord('3'):
             curses.endwin()
             execute_cmd("fdisk -l")
        if x == 0x71:
             curses.endwin()
             execute_cmd("sl")

    curses.endwin()


if __name__ == '__main__':
    main()