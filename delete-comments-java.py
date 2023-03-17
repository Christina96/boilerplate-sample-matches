def delete_comments(lines, start, end):
    print(start, end)
    del lines[start:end]
    # kathe fora pou svino, prepei na allazo tis grammes !!!!
    # ara prepei na koitazo to neo arxeio
    print(len(lines))

    return lines


def clean_lines(lines):
    new_lines = lines.copy()
    i = 0
    start = 0
    end = 0

    for line in lines:
        if ("/*" in line and "*/*/*/*/*" not in line) or "/**" in line:
            print("starts", i, line)
            start = i
        if start != 0 and ("<font" in line or "</font" in line):
            end = i
            # auto simainei oti diakoptete apo tag
            new_lines = delete_comments(new_lines, start, end)
            start = 0
            break
        if start != 0 and "*/" in line:
            print("dodoodododod")
            end = i
            print(start, end)
            if start == end:
                new_lines = delete_comments(new_lines, start, end + 1)
            else:
                new_lines = delete_comments(new_lines, start, end + 1)
            start = 0
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
            if x.strip():
                write_file.write(line)
    return filename


def delete_one_line_comments(filename):
    # delete empty lines
    print("Delete empty lines")
    with open(filename, "r") as file:
        lines = file.readlines()
    with open(filename, "w") as write_file:
        for line in lines:
            if "// " in line:
                x = line.index("// ")
                new_line = line[0:x]
                if new_line.strip():
                    write_file.write(new_line)
            elif "/* " in line and " */" in line:
                x = line.index("/* ")
                new_line = line[0:x]
                if new_line.strip():
                    write_file.write(new_line)
            elif "/** " in line and " */" in line:
                x = line.index("/** ")
                new_line = line[0:x]
                if new_line.strip():
                    write_file.write(new_line)
            else:
                write_file.write(line)
    return filename


def delete_comments_from_file(filename):
    # from the new file
    with open(filename, 'r') as file:
        lines = [line for line in file.readlines()]
        while "/* " in str(lines) or "/**" in str(lines):
            print(filename)
            lines = clean_lines(lines)
            print(len(lines))
            print("------------------------------------------------")
    with open(filename, "w") as file:
        for lines in lines:
            file.write(lines)
        # print("File created:", "anewfile.html")
        # filename = "anewfile.html"


# pame na diavasoume tora to fakelo

# filename = delete_one_line_comments("file.html")
# filename = delete_empty_lines(filename)  # name of the new file
#
# delete_comments_from_file(filename)
import os

path = "/Users/christinechaniotaki/Desktop/Boilerplate/boilerplate-sample-matches/Java"

files = [name for name in os.listdir(path)]

for file in files:
    print("pame")
    filename = delete_one_line_comments(path + "/" + file)
    print("delete_one_line_comments")
    filename = delete_empty_lines(filename)  # name of the new file
    print("delete_comments_from_file")
    delete_comments_from_file(filename)

# x = "/Users/christinechaniotaki/Desktop/Boilerplate/boilerplate-sample-matches/Java/match332030.html"
# print("pame")
# filename = delete_one_line_comments(x)
# print("delete_one_line_comments")
# filename = delete_empty_lines(filename)  # name of the new file
# print("delete_comments_from_file")
# delete_comments_from_file(filename)
