id = 53
num = int(input("整数を入力してください"));

print(f"入力された整数は{id}と等しい" if num == id
    else f"入力された整数は{id}より大きい" if num > id
    else f"入力された整数は{id}より小さい");