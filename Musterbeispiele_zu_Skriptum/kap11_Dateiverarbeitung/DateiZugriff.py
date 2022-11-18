input = open("in.txt")          #   r oder leer für lesen
output = open("out.txt", "w")   #   a für anhängen
linenr = 0
while True:
    line = input.readline()
    if not line: 
        break
    linenr += 1
#	 output.write(str(linenr) + ": " + line + "\n")
#    output.write("%d: %s\n" % (linenr, line))
    output.write("{0:2d}: {1:s}\n".format(linenr, line))
output.close()
