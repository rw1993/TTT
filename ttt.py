import node
import Queue
import UserString as us
import copy
def ifwin(state):
    #row
    for i in range(0,3):
        if state[3*i]==state[3*i+1] and state[3*i]==state[3*i+2]:
            return True
    #col
    for i in range(0,3):
        if state[i]==state[i+3] and state[i]==state[i+6]:
            return True
    #xie
    if state[0]==state[4] and state[0]==state[8]:
        return True
    if state[2]==state[4] and state[2]==state[6]:
        return True

    return False


def expand(current_n,wait_to_expand_queue):
    ifexpand=False
    for i in range(0,9):
        if current_n.state[i]!="#" and current_n.state[i]!="o":
            newstate=copy.deepcopy(current_n.state)
            if current_n.deep%2==0:
                newstate[i]="#"
            else:
                newstate[i]="o"
            newnode=node.node(state=newstate,father=current_n,deep=current_n.deep+1)
            current_n.childs.append(newnode)
            wait_to_expand_queue.put(newnode)
            ifexpand=True
    if not(ifexpand):
        count_value(current_n)
def count_value(current_n):
    state=current_n.state
    for i in range(0,3):
        if state[3*i]==state[3*i+1] and state[3*i]==state[3*i+2]:
            if state[3*i]=="#":
                current_n.value=999999#+inf
            else:
                current_n.value=-999999#-inf
        current_n.ifcount=True
        break
    #col
    for i in range(0,3):
        if state[i]==state[i+3] and state[i]==state[i+6]:
            if state[i]=="#":
                current_n.value=999999#+inf
            else:
                current_n.value=-999999#-inf
        current_n.ifcount=True
        break
    #xie
    if state[0]==state[4] and state[0]==state[8]:
        if state[0]=="#":
            current_n.value=999999#+inf
        else:
            current_n.value=-999999#-inf
        current_n.ifcount=True
    if state[2]==state[4] and state[2]==state[6]:
        if state[2]=="#":
            current_n.value=999999#+inf
        else:
            current_n.value=-999999#-inf
        current_n.ifcount=True


    if current_n.ifcount == False:
        me=8
        user=8
        for i in range(0,3):
            if "o" == state[3*i] or "o" == state[3*i+1] or "o" ==state[3*i+2]:
                me-=1
        for i in range(0,3):
            if "o" == state[i] or "o"== state[i+3] or "o" == state[i+6]:
                me -=1
        if "o" == state[0] or "o" == state[4] or "o" == state[8]:
            me-=1
        if "o" == state[2] or "o" == state[4] or "o" == state[6]:
            me -=1
        for i in range(0,3):
            if "#" == state[3*i] or "#" == state[3*i+1] or "#" ==state[3*i+2]:
                user-=1
        for i in range(0,3):
            if "#" == state[i] or "#"== state[i+3] or "#" == state[i+6]:
                user -=1
        if "#" == state[0] or "#" == state[4] or "#" == state[8]:
            user-=1
        if "o" == state[2] or "o" == state[4] or "o" == state[6]:
            user-=1

        current_n.value=me-user
    current_n.ifcount=True


def min_max(n):
    if n.ifcount == True:
        return n.value
    else:
        values=[]
        for son in n.childs:
            son.value=min_max(son)
            values.append(son.value)
        if n.deep%2==0:
            n.ifcount=True
            return max(values)
        else:
            n.ifcount=True
            return min(values)

    

        


    

deep=5
state=us.MutableString("123456789")
n=node.node(state=state,father=None,deep=0)

while 1:
    print n.state[0:3]
    print n.state[3:6]
    print n.state[6:9]
    print ""
    if ifwin(n.state):
        print "You Win"
        exit()
    #build tree
    wait_to_expand_queue=Queue.Queue()
    wait_to_expand_queue.put(n)
    while not(wait_to_expand_queue.empty()):
        current_n=wait_to_expand_queue.get()
        if current_n.deep<deep:
            expand(current_n,wait_to_expand_queue)
        else:
            count_value(current_n)

    #count value and set next step
    n.value=min_max(n)
    newstate=None
    for son in n.childs:
        if n.value==son.value:
            print son.state[0:3]
            print son.state[3:6]
            print son.state[6:9]
            print ""
            newstate=copy.deepcopy(son.state)
            if ifwin(son.state):
                print "I win"
                exit()
            break

    print "please input a number (1~9)"
    num=raw_input()
    num=int(num)
    newstate[num-1]="o"
    n=node.node(state=newstate,father=None,deep=0)
    



