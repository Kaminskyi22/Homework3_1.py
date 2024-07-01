while True:
    start=int(input("Enter the start of the range: "))
    end=int(input("Enter the end of the range: "))
    if start>end:
        start,end=end,start

    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

    repeat=input("Do you want to repeat? (yes/no): ")
    if repeat!="yes":
        break
print("Goodbye!")
