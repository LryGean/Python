'''
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()


print(pi_string)
print(len(pi_string))
'''

'''
filename = 'pi_30_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()


print(pi_string)
print(len(pi_string))
'''

#圆周率里面包含的生日
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthady,in the form mmddyy:")
if birthday in pi_string:
    print("You birthday appears in the first million digits of pil!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

