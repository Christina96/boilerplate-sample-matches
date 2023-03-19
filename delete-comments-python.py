def delete_comments(lines, start, end):
    # print(start, end)
    print("lines[start]")
    print(lines[start])
    print(lines[end])
    del lines[start:end]
    return lines


def clean_lines(lines):
    new_lines = lines.copy()
    # i = 1
    start = -1
    type = '"""'
    # for line in lines:
    for i in range(0, len(lines)):
        line = lines[i].strip()
        if start == -1 and line.startswith('"""') and "&gt;" not in lines[i - 1] and "&lt" not in lines[i - 1]:
            print("starts", i, line)
            type = '"""'
            start = i
            continue
        if start == -1 and line.startswith("'''") and "&gt;" not in lines[i - 1] and "&lt" not in lines[i - 1]:
            print("starts", i, line)
            type = "'''"
            start = i
            continue
        if start != -1 and ("<font" in line or "</font" in line):
            end = i
            # auto simainei oti diakoptete apo tag
            new_lines = delete_comments(new_lines, start, end)
            break
        if start != -1 and line.startswith(type):
            end = i
            print("end")
            print(start, end)
            print(line)
            new_lines = delete_comments(new_lines, start, end + 1)
            break
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
            if line.startswith('#') or ("#" in line and line.startswith('<a name=') and line.find('href="#"') < 0):
                continue
            # if line.startswith("<a name") and line.find('"""') >= 0 and len(str(line).replace(" ", "", 200)) > 25:
            #     continue
            if line.startswith('"""') and line.endswith('"""') and len(line) > 5 and "<a name" not in line:
                continue
            if line.startswith("'''") and line.endswith("'''") and len(line) > 5 and "<a name" not in line:
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
    filename = delete_empty_lines(path + "/" + file)  # name of the new file
    delete_one_line_comments(filename)
    print("delete_one_line_comments")
    print("delete_comments_from_file")
    delete_comments_from_file(filename)
#
# x = "/Users/christinechaniotaki/Desktop/Boilerplate/boilerplate-sample-matches/Python/match152.html"
# print("pame")
# delete_empty_lines(x)
# filename = delete_one_line_comments(x)
# delete_comments_from_file(x)
