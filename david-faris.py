from os import system

def do_the_thing():
    name = input("Give a Name Please\n")
    name = str(name)
    if name.upper() in 'DAVID FARIS':
        print('LOSER\n')
        return 0
    elif name.upper() == 'Q':
        return 1
    else:
        print('NOT LOSER\n')
        return 0

if __name__ == '__main__':
    ret = 0
    while ret is 0:
        print('\n')
        ret = do_the_thing()