def add_number_off_lines(filename):
    with open(filename, 'r') as file:
        lines = [line for line in file.readlines()]
        new_lines = lines[:]
        start = -1
        i = 0
        pre = False
        for line in lines:
            if line.find("<pre>") >= 0 or line.find("<PRE>") >= 0:
                start = 1
                pre = True
                i += 1
                continue
            if line.find("</pre>") >= 0 or line.find("</PRE>") >= 0:
                start = -1
                pre = False
                i += 1
                continue
            if pre:
                new_lines[i] = str(start) + " " + new_lines[i]
                start += 1
            i += 1

    with open(filename, 'w') as file:
        for line in new_lines:
            file.write(line)


#
import os


def add_lines_per_language(path):
    files = [name for name in os.listdir(path)]
    # print(files)
    for file in files:
        add_number_off_lines(path + "/" + file)


java = "/Users/christinechaniotaki/Desktop/Boilerplate/boilerplate-sample-matches/Java"
c = "/Users/christinechaniotaki/Desktop/Boilerplate/boilerplate-sample-matches/C"
cpp = "/Users/christinechaniotaki/Desktop/Boilerplate/boilerplate-sample-matches/Cpp"
python = "/Users/christinechaniotaki/Desktop/Boilerplate/boilerplate-sample-matches/Python"

# add_lines_per_language(java)
# add_lines_per_language(c)
# add_lines_per_language(cpp)
add_lines_per_language(python)
