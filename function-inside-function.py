def n(name):
    def msg():#function inside function - this function is only accessed inside the function in which its defined
        return "Greetings "
    m = msg()+ name
    return m

s = input("Enter your name : ")
print(n(s))