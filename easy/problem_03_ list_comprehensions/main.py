def list_comprehension(x, y, z, n):
    return [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]  
def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(list_comprehension(x, y, z, n))
if __name__ == "__main__":
    main()
    