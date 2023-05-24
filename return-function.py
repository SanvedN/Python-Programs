def msg():
    def hello():
        return "Hello"
    return hello #here the whole function is returned

fun = msg()#this function is called as its global function while hello() is a local function
print(fun())