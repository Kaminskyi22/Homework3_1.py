while True:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    if start > end:
        start, end = end, start

    choice = int(input("Enter your choice (1 = all numbers, 2 = reverse numbers, 4 = multiple of 7, 5 = the number of numbers that are multiples of 5): "))

    match choice:
        case 1:
            print(f"Numbers in the range from {start} to {end} are: ")
            for i in range(start, end + 1):
                print(i)
        case 2:
            print(f"Numbers in the range from {end} to {start} are: ")
            for i in range(end, start -1, -1):
                print(i)
        case 4:
            print(f"Numbers that are multiple of 7 in the range from {start} to {end} are: ")
            for i in range(start, end + 1):
                if i % 7 == 0:
                    print(i)
        case 5:
            count = 0
            for i in range(start, end + 1):
                if i % 5 == 0:
                    count += 1
            print(f"The number of numbers that are multiples of 5 in the range from {start} to {end} is: {count}")
        case _:
            print("Invalid choice. Please enter 1, 2, 4 or 5.")

    repeat = input("Do you want to repeat? (yes/no): ")
    if repeat != 'yes':
        break

print("Goodbye!")
