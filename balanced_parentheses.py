# https://www.hackerrank.com/challenges/balanced-parentheses/
def matching_pair(parenthesis):
    for item in parenthesis:
        if item is '{' or item is '(' or item is '[':
            the_stack.append(item)
        elif item is '}' or item is ')' or item is ']':
            if not the_stack:
                closed = False
                return closed
            popped_item = the_stack.pop()
            if popped_item is '{' and item is '}' or popped_item is '(' and item is ')' or popped_item is '[' and item is ']':
                closed = True
            else:
                closed = False
                return closed
        if the_stack:
            closed = False
    return closed
    
T = int(raw_input())
closed = False
for a0 in range(0, T):
    the_stack = []
    parenthesis = map(str,raw_input())
    closed = matching_pair(parenthesis)
    if closed is True:
        print "YES"
    elif closed is False:
        print "NO"
    
    
