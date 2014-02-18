def fizz_buzz():
    
    print '''Fizz Buzz and Sivv Multiples of 3 will Fizz. Multiples of 5
    will Buzz. You choose another number between 1 and 9 for Sivvs.'''
    
    n = int(raw_input("Number: "))
    alt_n = int(raw_input("Out of how many total (< 1000): "))

    for i in range(1, alt_n):
        if i % 3 == 0:
            print "Fizz!"
            if i % 5 == 0:
                print "FizzBuzz!"
                if i % n == 0:
                    print "Sivv FizzBuzz!"
            elif i % n == 0:
                    print "Sivv Fizz!"
        elif i % 5 == 0:
            print "Buzz!"
            if i % n == 0:
                    print "Sivv Buzz!"  
        elif i % n == 0:
            print "Sivv"      
        else:
            print i

fizz_buzz()

# Dictionary, how to use it.

# Fizz_key = {
#     3: "Fizz",
#     5: "Buzz",
#     7: "Sivv",
#     9: "Wazz",
# }