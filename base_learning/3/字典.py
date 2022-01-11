'''
#创建空字典，添加键-值对
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
'''

'''
#修改字典中的值
alien_0 = {'color':'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
'''
'''
#例子
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x_position:" + str(alien_0['x_position']))

#向右移动外星人
#具外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #这个外星人的速度一定很快、
    x_increment = 3
#新位置等于老位置加增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
'''

'''
#删除键-值对(永远消失)
alien_0 = {'color':'green','points':5}
print(alien_0)

del alien_0['points']
print(alien_0)
'''

#遍历字典
'''
#遍历所有的键-值对
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }
for key,value in user_0.items():
    print("\nKey: " + key + "\nValue: " + value)
'''


'''
#遍历所有键
favorite_languages = {
    'jen':'python',
    'sarah':'C',
    'edward':'ruby',
    'phil':'python',
    }
'''
'''
friends = {'phil','sarah'}
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("\tHi " + name.title() + 
        ",I see your favorite language is " + 
        favorite_languages[name].title() + "!")
'''
'''
#按顺序遍历所有键
for name in sorted(favorite_languages.keys()):
    print(name.title() + ",thank you for taking the poll.")
'''

'''
#遍历所有的值
print("The following languages have been mentioned:")
#防止值有重复现象用集合（set）
for language in set(favorite_languages.values()):
    print(language.title())
'''