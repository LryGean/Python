#使异常避免崩溃
#else代码块
print("Give me two numbers,and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("\nSecond number:")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You'can't divide by 0!")
    else:
        print(answer)