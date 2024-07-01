while True:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    if start > end:
        start, end = end, start

    print(f"Numbers that are multiple of 7 in the range from {start} to {end} are: ")

    for i in range(start, end + 1):
        if i % 7 == 0:
            print(i)

    repeat = input("Do you want to repeat? (yes/no): ")
    if repeat != 'yes':
        break

print("Goodbye!")
