from queue import Queue

def myDfs(start,goal):
    visited = []
    q = Queue()
    q.put(start)
    while not q.empty():
        v = q.get()
        visited.append(v)
        if v == goal:
            return #success
        for child in v.children():
            if not child in visited:
                q.put(child)
    return None #goal is non existent