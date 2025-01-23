c0 = int(input("c0を指定してください。"))
c1 = int(input("c1を指定してください。"))
c2 = int(input("c2を指定してください。"))

if c1 == 0:
    print("警告: C1" + ("とC2は" if c2 == 0 else "は") + "0です。")
    if c2 == 0:
        print("警告: C1とC2は0です。")
        exit()

def getReadableSign(num):
    return "" if num == 1 else "-" if abs(num) == 1 else num

# 一次方程式 c1 * x + c0 = 0
print(f"一次方程式 {getReadableSign(c1)}x + {c0} = 0 の解は x = {-c0 / c1} です。")

# 二次方程式 c2 * x ** 2 + c1 * x + c0 = 0
# 判別式 D = b ** 2 - 4ac
# 解の公式 x = (-b ± (D ** 0.5)) / 2a

# 実数解の個数を判別式により求める
D = c1 ** 2 - 4 * c2 * c0
if D < 0:
    print("実数解なし")
else:
    # c2が0のとき、一次方程式
    if c2 == 0:
        print(f"一次方程式 {getReadableSign(c1)}x + {c0} = 0 の解は x = {-c0 / c1} です。")
    else:
        # 実数解が2つのとき。解の公式で求める
        x1 = (-c1 + D ** 0.5) / (2 * c2)
        x2 = (-c1 - D ** 0.5) / (2 * c2)
        print(f"二次方程式 {getReadableSign(c2)}x ** 2 + {getReadableSign(c1)}x + {c0} = 0 の解は x = {x1}, {x2} です。")
