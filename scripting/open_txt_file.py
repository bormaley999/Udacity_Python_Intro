# f = open('/Users/nick/Desktop/Обучение/AI/Intro to Python from Udacity/some_file.txt', 'r')
# file_data = f.read()
# f.close()
#
# print(file_data)
#
#
# f = open('/Users/nick/Desktop/Обучение/AI/Intro to Python from Udacity/some_file.txt', 'a')
# f.append = ("Hello there!")
# f.close()
#
# print(f.append)
#
# f = open('/Users/nick/Desktop/Обучение/AI/Intro to Python from Udacity/some_file.txt', 'a')
# f.append = ("Hello there! How are you?")
# f.close()
#
# print(f.append)


# with open('/Users/nick/Desktop/Обучение/AI/Intro to Python from Udacity/camelot.txt') as song:
#     print(song.read(2))
#     print(song.read(8))
#     print(song.read())

camelot_lines = []
with open('/Users/nick/Desktop/Обучение/AI/Intro to Python from Udacity/camelot.txt') as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)

