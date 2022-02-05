#字典列表
'''
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
'''

'''
#创建一个用于存储外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#修改前三个外星人
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
  for alien in aliens[0:3]:    
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

#显示创建了多少个外星人
print("Total number of aliens:" + str(len(aliens)))
'''

#在字典中存储列表
'''
#例一：
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    }
#概述所点的披萨
print("You ordered a " + pizza['crust'] + "-crust pizza"
 + " with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
'''
'''
#例二：
favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['C'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
    }
for name,languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
'''

#字典中存储字典
users = {
    'aeinstenin':{ 
        'first':'albert',
        'last':'einsten',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',   
        },
    }

for username,user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())