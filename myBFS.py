import queue

def myBfs(start,goal):
    q = queue.Queue()
    q.enqeue(start) 
    close = []
    while not(q.empty()):
        v = q.dequeue()
        close.append(v) #keep track of visited nodes
        if v == goal:
            return #succeeded
        for child in v.children():
            if not child in close:
                q.enqeue(child)
