id = 53

lim = int(input("整数を何回比較しますか？"));

def compNum():
    num = int(input("整数を入力してください"));
    print(f"入力された整数は{id}と等しい" if num == id
        else f"入力された整数は{id}より大きい" if num > id
        else f"入力された整数は{id}より小さい");
    return;

for i in range(lim):
    print(f"{i+1}回目の比較");
    compNum();
