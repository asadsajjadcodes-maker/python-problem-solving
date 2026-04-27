# Check if a year is a leap year or not
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Get user input for the year
def main():
    year = int(input("Enter a year:"))
    if is_leap(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


if __name__ == "__main__":
    main()
    