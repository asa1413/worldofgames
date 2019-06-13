def add_score(difficult, name):
    try:
        points_of_winning = (int(difficult)*3)+5
        file_name = name+".txt"

        file_open = open(file_name, 'a+')
        file_open.close()

        file_open = open(file_name, 'r')
        l_line = file_open.read()

        if l_line == '':
            l_line = 0

        l_line = int(l_line) + int(points_of_winning)
        file_open.close()

        file_open = open(file_name, 'w')
        file_open.write(str(l_line))
        file_open.close()

    except:
        print("error in add_score")

