def print_student_files(name, gender = '男', age = 18, college = '贝壳大学'):
    print('我叫' + name + '\n' + '我今年' + str(age) + '岁' + '\
    \n我是' + gender + '生' + '\n我在' + college + '上学')

print_student_files('小明','男',18,'人民路小学')
print('---------------------------------')
print_student_files('小亮')