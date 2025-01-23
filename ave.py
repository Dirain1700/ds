import statistics

arr = []
amount = 0
length = 0

for i in input("数字をカンマ区切りで入力してください。").split(","):
    num = int(i.strip())
    arr.append(num)
    amount += num
    length += 1

if length == 0:
    print("入力がありません。")
    exit()

average = amount / length
print(f"平均値 {average} (自作)")
print(f"平均値 {statistics.mean(arr)} (statistics)")

# 標準偏差 stdevp = sqrt((Σ(x - x̄) ** 2) / n)
offSquare = 0
# Σ(x - x̄) ** 2
for i in arr:
    offSquare += (i - average) ** 2
    
stdevp = (offSquare / length) ** 0.5

print(f"標準偏差 {stdevp}")
print(f"標準偏差 {statistics.pstdev(arr)} (statistics)")
