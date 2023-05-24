x = int(input("Enter the last number : "))
i = 1
while i <= x :
    print(i)
    i += 1
    if i%10 == 0 :
        continue

    if i > 100:
        print("Cannot print number more than 100")
        break
