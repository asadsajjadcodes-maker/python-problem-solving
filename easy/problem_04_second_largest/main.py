if __name__ == '__main__':
    arr = [int(x) for x in input("Enter the elements: ").split()]
    unique_number = sorted(list(set(arr)))
    unique_number.reverse()
    print(unique_number[1])
