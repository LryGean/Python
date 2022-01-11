""" 
magicians = ['alice','david','carolina']
for magician in magicians:
    #print(magician)
    print(magician.title() + ",that was a great trick!")
    print("I can't wait to see your next trick," + magician.title() + ".\n")
print("Thank you everyone.That was a great magic show!") 
"""

#for value in range(1,6):
#    print(value)

'''
numbers = list(range(1,6))
print(numbers)
'''

"""
squares = []
for value in range(1,11):
    #square = value**2
    squares.append(value**2)
print(squares) 
"""
'''
squares = [value**2 for value in range(1,11)]
#squares = [value+2 for value in range(1,11)]
print(squares)
'''

#python——切片
#players = ['charles','martina','michael','florence','eli']
""" 
#0——3
print(players[0:4])
#1——3
print(players[1:4])
#0——3
print(players[:4])
#序号2到末尾=第三个开始到最后
print(players[2:])    
#最后三个
print(players[-3:])
"""
'''
print("Here the first tree players on my team:")
for player in players[:3]:
    print(player.title())
'''

#复制列表
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

#赋值为同意列表
#friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
