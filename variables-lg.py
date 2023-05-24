x = 123 #global variable - defined outside a function - accessed anywhere

def a():
    x = 456 #local variable(Same name as global variable) - defined inside function and access inside function only
    print(x)#here local variable is given preference and printed because its printed inside a function
    print(globals()['x'])#accesses global variable with same name as  local variable form within the function
print(x)#here global variable is preferred because its printed outside function
b = a #assigns a function to a variable
b()
b()
b()
