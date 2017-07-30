fw = open("sampl.txt", "w")
fw.write("This is the program for python\n")
fw.write("Hello python\n")
fw.close()

fr = open("sampl.txt", "r")
demo = fr.read()
print(demo)
fr.close()