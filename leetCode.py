nums = list(map(int, input("Masukan Array :").split()))
target = int(input("Masukan Target :"))
i = 0
while True:
    if nums[i] + nums[i+1] == target:
        break
    i += 1
print(i, i+1)