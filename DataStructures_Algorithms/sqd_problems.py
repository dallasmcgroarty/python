# given a string of closing parentheses check whether it is balanced
# 3 types or parenthesis (), [], and {}
# asssume no other characters nor spaces
# example-> balanced = '([])' , not balanced = '([)]'
def balance_check(s):
    if len(s) % 2 != 0:
        return False
    
    stack = []
    opening = set('([{')
    matches = set([('(',')'), ('[',']'), ('{','}')])
    
    for x in s:
        if x in opening:
            stack.append(x)
        else:
            if len(stack) == 0:
                return False
            last = stack.pop()

            if (last, x) not in matches:
                return False

    return len(stack) == 0
    # my solution:

    # if len(s) % 2 != 0:
    #     return False
    
    # stack = []

    # for x in s:
    #     if x == '(' or x == '{' or x == '[':
    #         stack.append(x)
    #     else:
    #         if len(stack) == 0:
    #             return False

    #         last = stack.pop()

    #         if x == ')' and last != '(' or x == '}' and last != '{' or x == ']' and last != '[':
    #             return False
    # return len(stack) == 0

print(balance_check('[]({[]})'))

# implement a queue using two stacks
class QueueStack(object):
    def __init__(self):
        self.instack = []
        self.outstack = []
    
    def enqueue(self, item):
        self.instack.append(item)
    
    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()