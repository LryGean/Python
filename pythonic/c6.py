

class Test():
    pass
    # def __len__(self):
    #     return 0 
    def __len__(self):
        return True
    def __bool__(self):
        return False
test = Test()

# 对象进行判空
if test:
    print('S')
else:
    print('F')


print(bool(None))
print(bool([]))
print(bool(test))
print(bool(Test))