import random

def generate_random_number_string(length):
    return ''.join(random.choices('0123456789', k=length))

def main():
    while True:
        try:
            length = int(input("Enter the length of the random number string: "))
            if length <= 0:
                print("Length must be a positive integer. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    random_number_string = generate_random_number_string(length)
    print(f"Random number string of length {length}:")
    print(random_number_string)

if __name__ == "__main__":
    main()
