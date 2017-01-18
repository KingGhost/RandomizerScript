import random
alist = []
for Y in range(369):
    alist.append("Yellow")
for O in range(744):
    alist.append("Orange")
for B in range(331):
    alist.append("Brown")

#shuffle 10 times cause why not
#Random strategy behind the shuffle is called Fisher Yates shuffling
random.shuffle(alist) #1
random.shuffle(alist) #2
random.shuffle(alist) #3
random.shuffle(alist) #4
random.shuffle(alist) #5
random.shuffle(alist) #6
random.shuffle(alist) #7
random.shuffle(alist) #8
random.shuffle(alist) #9
random.shuffle(alist) #10

# Take the first 126 elements of the now randomized array
first127 = alist[0:126]

print '------------------------- Draw -------------------------'
print "Yellow :",first127.count("Yellow")
print "Orange :",first127.count("Orange")
print "Brown :",first127.count("Brown")


def complete(xtimes):
    count = 0
    orangecount = []
    while count<xtimes:
        random.shuffle(alist)  # 1
        # Take the first 126 elements of the now randomized array
        first127 = alist[0:126]

        #add all results to list.
        orangecount.append(first127.count("Orange"))
        count = count +1

    #once all of our trial results are inside our list, we count the results
    for i in range(126):
        #number
        print i

    print "occurance"
    # once all of our trial results are inside our list, we count the results
    for i in range(126):
        #occurance
        print orangecount.count(i)


#the number here is the number of trials you want to do. Feel free to change this number
complete(1000)



print '------------------------- alist confirm -------------------------'
print "Yellow :", alist.count("Yellow")
print "Orange :",alist.count("Orange")
print "Brown :",alist.count("Brown")
