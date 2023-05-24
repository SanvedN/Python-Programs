cp = float(input("Enter cost price : "))
sp = float(input("Enter selling price : "))
p = (sp-cp)/cp*100
print("Profit = ",p,"%") if p >= 0 else print("Loss = ",-1*p,"%")