def rep_char(c, n):
    print(str(c) * n + 4)

def message(name):
    msg1 = f'Hello {name},'
    msg2 = 'Welcome to Seoul.'
    '''if len(msg1) > len(msg2):
        nstr = len(msg1)
    else:
        nstr = len(msg2)'''
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-', nstr)
    print(f'  {msg1}  \n  {msg2}  ')
    rep_char('-', nstr)

name = input('Input his/her name: ')
message(name)
