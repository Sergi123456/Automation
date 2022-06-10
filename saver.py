from datetime import datetime

def init(fnamraw='log'):
    global f
    cd = datetime.now()
    fnam = fnamraw + ' ' + str(cd.year) + str(cd.month) + str(cd.day) + ' ' + str(cd.hour) + str(cd.minute) + str(cd.second) + '.txt'
    f = open(fnam, 'w')

def test_suite(n=0):
    f.write('Test-suite ' + str(n) + ': \n')

def test_case(n=0, stat=True, text=''):
    if(stat == True):
        statraw = 'PASSED'
    else:
        statraw = 'FAILED'
    f.write('Test-case ' + str(n) + ' ' + text + ' - ' + statraw + '\n')

def enter():
    f.write('\n')

def quit():
    f.close()