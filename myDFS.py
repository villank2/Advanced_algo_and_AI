
def myDfs(start,goal):
    # use a stack or just pop from the start of the list
    open = [start]
    close = []
    while  len(open) > 0:
        v = open.pop(0)
        close.append(v)
        if v == goal:
            return #succeeded
        for child in v.children():
            if not v in close:
                child.append(child)
                