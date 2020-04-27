import sys

class Stack():
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return self.items==[]
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
            
    def getStack(self):
        return self.items
        

def reverse_string(stack, input_str):
  for i in range(len(input_str)):
    stack.push(input_str[i])
  rev_str = ""
  while not stack.isEmpty():
    rev_str += stack.pop()

  return rev_str

stack = Stack()
input_str = str(input())
print(reverse_string(stack, input_str))
