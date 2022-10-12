#INTERVIEW QUESTION - Conversion of two list into Dictionary Using Python
def list_todict():
    keys=[1,2,3,4]
    values=['giri','kumar','gopal','raj']
    print(dict(zip(keys,values)))

list_todict()

def dict_totuple():
    x={1: 'giri', 2: 'kumar', 3: 'gopal', 4: 'raj'}
    for i in x.items():
        print(i)

dict_totuple()

