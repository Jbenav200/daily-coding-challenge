from challenge1 import CheckSums


def main():
    array = [[10, 14, 2, 3], [10, 14, 2, 4]]
    k = 17
    cs = CheckSums()
    print(f'\n\nchecking arrays: {array[0]} and {array[1]} \n')
    for x in array:
        print(f'for array {x}:')
        print(f'{cs.checksums(x, k)} \n')


if __name__ == "__main__":
    main()
