"""https://www.codewars.com/kata/57ea70aa5500adfe8a000110"""


def fold_array(array, runs):
    for _ in range(runs):
        length = len(array)
        new_array = []
        
        for pair in zip(array[:length // 2], array[:length // 2 - 1:-1]):
            new_array.append(sum(pair))
        
        if length % 2:
            new_array.append(array[length // 2])
            
        array = new_array
    
    return array


def main():
    from util_funcs import pretty_compare

    pretty_compare(fold_array([1, 2, 3, 4, 5],          1),     [6, 6, 3])
    pretty_compare(fold_array([1, 2, 3, 4, 5],          2),     [9, 6])
    pretty_compare(fold_array([1, 2, 3, 4, 5],          3),     [15])
    pretty_compare(fold_array([-9, 9, -8, 8, 66, 23],   1),     [14, 75, 0])


if __name__ == '__main__':
    main()
