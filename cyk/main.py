from CYK import CYK

cyk = CYK()

print "Unit test 1: abc"
print "Result: " + str(cyk.isInCFL('abc'))
print "Wanted: True\n"

print "Unit test 2: abbbabb"
print "Result: " + str(cyk.isInCFL('abbbabb'))
print "Wanted: True\n"

print "Unit test 3: abbc"
print "Result: " + str(cyk.isInCFL('abbc'))
print "Wanted: True\n"

print "Unit test 4: bbc"
print "Result: " + str(cyk.isInCFL('bbc'))
print "Wanted: False\n"

print "Unit test 5: aaabb"
print "Result: " + str(cyk.isInCFL('aaabb'))
print "Wanted: False\n"
