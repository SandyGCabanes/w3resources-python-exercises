#sandygcabanes
#w3resources.com
#mini project 4 99 bottles
''' Create a Python project that prints out every line of the song
"99 bottles of beer on the wall." Note: Try to use a built in function instead
of manually typing all the lines'''

i = 99
while i < 100 and i > 1:
    print ('{} bottles of beer on the wall \n{} bottles of beer'.format(i,i))
    print ('Take one down, pass it around')
    i -= 1
    print ('{} bottles of beer on the wall'.format (i))
print ('One bottle of beer on the wall \nOne bottle of beer \nTake it down, pass it around\nNo more bottles of beer on the wall')