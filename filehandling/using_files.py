with open('avengers.txt', 'w+') as my_file:
    my_file.write('Iron Man\n')
    my_file.write('Captain America\n')
    my_file.write('Spider Man\n')
    my_file.writelines(['Hulk\n', 'Ant-man\n', 'Black Panther\n'])

my_file = open('avengers.txt', 'r')
with my_file:
    print(my_file.read())
    print("I'm reading again...\n")
    my_file.seek(0)
    print(my_file.read())

