"""https://www.codewars.com/kata/58f5c63f1e26ecda7e000029"""


def wave(people: str):
    standing = 0
    result = []
    
    while standing < len(people):
        if people[standing].islower():
            result.append(people[:standing] + people[standing].upper() + people[standing + 1:])
        standing += 1
        
    return result


def main():
    print(wave('hello'))
    print(wave('two words'))


if __name__ == '__main__':
    main()

