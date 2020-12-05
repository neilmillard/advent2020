def get_lines_from_file(filepath='day1.txt', keep_blank=False):
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        array = []
        while line:
            my_line = line.strip()
            # print("Line {}: {}".format(cnt, my_line))
            if my_line != '' or keep_blank:
                array.append(my_line)
            line = fp.readline()
            cnt += 1
    return array
