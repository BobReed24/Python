digits = int(input(">: "))
print(f"Writing {digits} 0s to nums.txt")
for i in range(digits):
    with open("nums.txt", "a") as f:
        f.write("0")
print("Done!")
