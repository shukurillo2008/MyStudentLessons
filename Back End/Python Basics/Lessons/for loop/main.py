"""For looplar"""

son1 = int(input("Karra jadvali Sonini kiriting: "))
son2 = int(input("Katta jadvali Sonini kiriting: "))

for i in range(son1,son2+1):
    print("=-"*10)
    print(f"Bu {i} Karra")
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")



















