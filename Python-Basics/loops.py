for i in range(1, 6):
    print("Number:", i + 1)

for i in range(1, 11):
    if i % 2 == 0:
        print("Even number:", i)

for i in range(5, 0, -1):  # Missing stop value, will count forever or error
    print("Countdown:", i)
