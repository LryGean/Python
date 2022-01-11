def greet_use(username):   #username是该函数的形参
    print("Hellow " + username.title() + "!")
a = ['jesse','jone','sarya','lucy','jenny']
for i in a:
    if i != 'sarya':
        greet_use(i)    #i是该函数的实参
    else:
        continue
    
