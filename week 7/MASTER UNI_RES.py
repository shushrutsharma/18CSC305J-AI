'''
Attempt to unify the following expressions. Either show their most general unifier or explain why they will not unify.

Exercise:
1) p(foo(X), Y) and p(a, b)
2) p(Y, Y) and p(a, Y)

Test cases:
1) p(a,Y) and q(Y,Y)         # Initial Predicate Symbols
2) p(a,Y) and p(a,X,Y)       # Different number of arguments
3) p(foo(X),Y) and p(a,b)  # Exercise 1
4) p(Y,Y) and p(a,Y)       # Exercise 2
5) p(a,X) and p(Y,b)         # Prints the General Unifiers 
'''

def unify(E1, E2):
    constants = [chr(i) for i in range(ord('a'), ord('w') + 1)]
    variables = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    variables.extend(['x', 'y', 'z'])
    if (E1 in constants and E2 in constants) or (E1 is None and E2 is None):  # base case
        if E1 == E2:
            return None
        else:
            return "FAIL"

    elif E1 in variables:
        if E1 in E2:
            return "FAIL - E1 occurs in E2"
        else: 
            return (E2 + "/" + E1)
          
    elif E2 in variables:
        if E2 in E1:
            return "FAIL - E2 occurs in E1"
        else: 
            return (E1 + "/" + E2)
    else:
        if ('(' in E1 and '(' not in E2):
            return "FAIL - E1 is a function and E2 is a variable/constant"
        elif ('(' not in E1 and '(' in E2):
            return "FAIL - E1 is a variable/constant and E2 is a function"

print("Enter the Expressions (without spaces):")
s1 = input()
s2 = input()
E1 = s1[2:len(s1)-1].split(',')
E2 = s2[2:len(s2)-1].split(',')
if s1[0] != s2[0]:
    print("FAIL - Initial Predicate Symbols in E1 and E2 are not identical")
elif len(E1) != len(E2):
    print("FAIL - E1 and E2 have different number of arguments")
else:
    n = len(E1)
    s = [] 
    print("----------------------------------------------------------------------------")
    for i in range(n):
        print("E1:", E1[i])
        print("E2:", E2[i])
        print("Result:", unify(E1[i],E2[i]))
        print("----------------------------------------------------------------------------")
        if "FAIL" not in unify(E1[i],E2[i]):
            s.append(unify(E1[i],E2[i]))
        
    if len(s) == n:
        print("General Unifiers: { ", end = "")
        for i in range(len(s)):
            if i != len(s)-1:
                print(s[i] + ", ", end = "")
            else:
                print(s[i] + " }", end = "")
