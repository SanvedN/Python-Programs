exp = [2200,2350,2600,2130,2190]

#Q1 - how many dollars did you spend more in January than in February
print(exp[1]-exp[0])

#Q2 - find expenses in the first quarter
print(exp[0]+exp[1]+exp[2])

#Q3 - find if you spent exactly 2000 dollars in any month
print(2000 in exp)

#Q4 - add expenses of june month which is 1980$
exp.append(1980)

#Q5 - you got a return of 200$ in april, make a correction
exp[3] -= 200
print(exp)