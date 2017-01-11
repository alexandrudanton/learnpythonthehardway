from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input('> ')

txt_againg = open(file_again)

print txt_againg.read()
txt_againg.close()
