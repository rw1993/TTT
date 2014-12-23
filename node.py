class node:
    def __init__(self,state,deep,father):
        self.state=state
        self.father=father
        self.childs=[]
        self.value=0
        self.deep=deep
        self.ifcount=False

