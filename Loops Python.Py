# "for loop" review
x = [1, 2, 3]
for i in x:
  y = i + 1a
  print "%d + 1 = %d" % (i , y)
  

# "while loop" example
count = 0
while count < 5:
  print "Hello! Count is %d" % (count)
  count += 1
  
# Do Now Round 1
condition = True
while condition:
  print "Hey we looped!"
  condition = False

x = 0
while x < 4:
  print "Loop: %d" % (x)
  x += 1

# Do Now Round 2
count = 0
while True:
  print "We're looping! Count: %d" % (count)
  count += 1
  if count == 10:
    break

# "for loop" example 1
x = "hello"
for i in x:
  print i

# Do Now Round 4 (write your code below)
my_string = "Hei-Hei"
for i in my_string:
  if i in ["a","e","i","o","u"]:
    print "x"
  else:
    print i 

# Do Now Round 5
fruits_dictionary = {'b': 'berry','a': 'apple', 'c': 'cherry'}
#for key in fruits_dictionary:
