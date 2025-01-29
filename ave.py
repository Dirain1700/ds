import statistics

arr = []
amount = 0
length = 0

for i in input("数字をカンマ区切りで入力してください。").split(","):
    num = int(i)
    arr.append(num)
    amount += num
    length += 1

if length == 0:
    print("入力がありません。")
    exit()

def getAverage(amo, leng):
    return amo / leng

average = getAverage(amo=amount, leng=length)

print(f"平均値 {average} (自作)")
print(f"平均値 {statistics.mean(arr)} (statistics)")

def getStdevP(array, ave, leng):
    # 標準偏差 stdevp = sqrt((Σ(x - x̄) ** 2) / n)
    offSquare = 0
    # Σ(x - x̄) ** 2
    for i in array:
        offSquare += (i - ave) ** 2

    return (offSquare / leng) ** 0.5

print(f"標準偏差 {getStdevP(arr, ave=average, leng=length)} (自作)")
print(f"標準偏差 {statistics.pstdev(arr)} (statistics)")
