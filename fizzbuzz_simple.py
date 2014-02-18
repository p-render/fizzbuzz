
def fizz_buzz(i):
    
    mapping = {
        3: 'Fizz',
        5: 'Buzz',
    }

    result = ""
    
    for key in sorted(mapping.keys()):
        value = mapping[key]
        if not i % key:
            result += value
    if not result:
        result = str(i)
    return result

        
if __name__ == '__main__':
    for i in range(1, 101):
        print fizz_buzz(i)
    


