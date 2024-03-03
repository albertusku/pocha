import sys

def mange_system():
    option=False #True->Multi, false->1player
    if len(sys.argv)==1:
        option=True
    elif len(sys.argv)==2:
        if sys.argv[1]=="multi":
            option=True
    return option

