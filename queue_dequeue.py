stack1 = []
stack2 = []

def enqueue(element):
    stack1.append(element)

def dequeue():
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
    if not stack2:
        return None
    else:
        return stack2.pop()

def print_front():
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
        
    if not stack2:
        return None
    else:
        return stack2[-1]

def doSomething(inval):
    queries = inval.strip().split(',')
    for i in queries:
        query_type, *args = map(str.strip, i.split())
        if query_type == '1':
            enqueue(int(args[0]))
        elif query_type == '2':
            dequeue()
        elif query_type == '3':
            print(print_front())

# input1 = '1 42,2,1 14,3'
# doSomething(input1)
# input2='1 23,2,1 14,3,2,1 78,3'
# doSomething(input2)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# In Python, the *args syntax is used to indicate that a function or a destructuring assignment can accept 
# a variable number of positional arguments. When used in a function signature, *args collects any additional 
# positional arguments beyond the explicitly named parameters into a tuple. In the case of destructuring assignment,
#  *args is used to collect multiple values into a list.

# Let's take the specific line you mentioned: query_type, *args = map(str.strip, query.split()).

# In this line, *args is used to collect all elements beyond the first one into a list assigned to the 
# variable args. This is useful when the number of elements in the split result is not known in advance,
#  and you want a flexible way to handle them.

# Here's an example:

# python
# Copy code
# query = "1 42 3 4"
# query_type, *args = map(str.strip, query.split())

# print(query_type)  # Output: '1'
# print(args)        # Output: ['42', '3', '4']
# In the context of this line, it allows the handling of various queries that might have different numbers of arguments. The query_type variable will always contain the first element, and args will contain the rest.