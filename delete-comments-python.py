def delete_comments(lines, start, end):
    # print(start, end)
    print("lines[start]")
    print(lines[start])
    print(lines[end])
    del lines[start:end]
    return lines


def clean_lines(lines):
    new_lines = lines.copy()
    i = 1
    start = -1
    type = '"""'
    for line in lines:
        line = line.strip()
        # if (i == 901):
        #     print(line.strip())
        if start == -1 and line.startswith('"""') and "&gt;" not in lines[i - 2] and "&lt" not in lines[i - 2]:
            print("starts", i, line)
            type = '"""'
            start = i
            continue
        if start == -1 and line.startswith("'''") and "&gt;" not in lines[i - 2] and "&lt" not in lines[i - 2]:
            print("starts", i, line)
            type = "'''"
            start = i
            continue
        if start != -1 and ("<font" in line or "</font" in line):
            end = i
            # auto simainei oti diakoptete apo tag
            new_lines = delete_comments(new_lines, start, end)
            break
        # if start != -1:
        #     print(type, start)
        #     print(line)
        if start != -1 and line.startswith(type):
            end = i
            print("end")
            print(start, end)
            new_lines = delete_comments(new_lines, start - 1, end + 1)
            break
        i += 1
    return new_lines


def delete_empty_lines(filename):
    # delete empty lines
    print("Delete empty lines")
    with open(filename, "r") as file:
        lines = file.readlines()
    with open(filename, "w") as write_file:
        for line in lines:
            x = str(line)
            if x.strip() and x != "#":
                write_file.write(line)
    return filename


def delete_one_line_comments(filename):
    # delete empty lines
    print("Delete empty lines")
    with open(filename, "r") as file:
        lines = file.readlines()
    with open(filename, "w") as write_file:
        for current_line in lines:
            line = current_line[:]
            line = line.strip()
            if line.startswith('#') or ("#" in line and line.startswith('<a name=')):
                continue
            if line.startswith('"""') and line.endswith('"""') and len(line) > 5:
                continue
            if line.startswith("'''") and line.endswith("'''") and len(line) > 5:
                continue
            if line.startswith("<a name") and (line.find('"""') >= 0 or line.find('#') >= 0):
                continue
            else:
                write_file.write(current_line)
    return filename


def delete_comments_from_file(filename):
    # from the new file
    with open(filename, 'r') as file:
        lines = [line for line in file.readlines()]
        while True:
            # for i in range(0, 200):
            # print(filename)
            before = len(lines)
            lines = clean_lines(lines)
            after = len(lines)
            print(before, after)
            if before == after:
                break
            print("------------------------------------------------")
    with open(filename, "w") as file:
        for lines in lines:
            file.write(lines)
        # print("File created:", "anewfile.html")
        # filename = "anewfile.html"


import os

path = "/Users/christinechaniotaki/Desktop/Boilerplate/boilerplate-sample-matches/Python"

files = [name for name in os.listdir(path)]

for file in files:
    print("pame")
    filename = delete_one_line_comments(path + "/" + file)
    print("delete_one_line_comments")
    filename = delete_empty_lines(filename)  # name of the new file
    print("delete_comments_from_file")
    delete_comments_from_file(filename)

# x = "/Users/christinechaniotaki/Desktop/Boilerplate/boilerplate-sample-matches/Python/match184.html"
# print("pame")
# filename = delete_one_line_comments(x)
# print("delete_one_line_comments")
# filename = delete_empty_lines(filename)  # name of the new file
# print("delete_comments_from_file")
# delete_comments_from_file(x)
