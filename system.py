import sys

player=""

def manage_system():
    global player
    option=False #True->Multi, false->1player
    if len(sys.argv)==1:
        option=True
    elif len(sys.argv)!=1:
        if sys.argv[1]=="multi":
            option=True
        if sys.argv[1]=="player":
            player=sys.argv[2]
    return option

