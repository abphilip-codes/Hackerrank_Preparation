# https://www.hackerrank.com/challenges/three-month-preparation-kit-queue-using-two-stacks/problem

class Queue:
    def __init__(self, s1=[], s2=[]):
        self.s1 = s1
        self.s2 = s2

    def isEmpty(self):
        if not self.s1 and not self.s2: return True
        return False

    def size(self):
        return len(self.s1) + len(self.s2)

    def enqueue(self, val):
        self.s1.append(val)

    def dequeue(self):
        if not self.s2:  
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def front(self):
        if not self.s2:  
            while len(self.s1) > 0: 
                self.s2.append(self.s1.pop())
        print(self.s2[-1]) 
        
if __name__ == '__main__':
    t = int(input().strip())
    q = Queue()
    for t_itr in range(t):
        s = input()
        if s[0] == "1":
            val = s.split(" ")[1]
            q.enqueue(val)
        elif s[0] == "2": q.dequeue()
        elif s[0] == "3": q.front() 