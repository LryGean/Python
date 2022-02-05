responses = {}
polling_active = True
while polling_active:
    name = str(input("\nWhat\'s you name? "))
    response = str(input("Which mountain would like to climb someday? "))
    responses[name] = response
    repeat = str(input("Would like to let another person respond?(yes/no) "))
    if repeat == 'no':
        polling_active = False
print("\n---Poll Results---")
for name,response in responses.items():
    print(name + "would you like to climb " + "." )
