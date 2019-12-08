
import random


def get_wallet(total, number, times):
    if times<1:
        times = 1
    print("%d money for %d wallets and %d times." %(total, number, times))
    for t in range(times):
        print("For %d times :" %(t+1))

        used = 0
        min = 0.01
        max = 10

        for i in range(number):
            if i == number-1:
                value = total - used
                print("%d  --------  %.2f        [%.2f, %.2f]       before used %.2f" %(i+1, value, value, value, used))
            else :
                #计算第i个人的随机数的最大值
                max = total-used-(number-i+1)*min
                #print("[%.2f, %.2f]"  %(min, max))
                #产生第i个人的随机数
                int_min = min*100
                int_max = max*100
                int_min = int(int_min)
                int_max = int(int_max)
                #print("[%d, %d]/100" %(int_min, int_max))
                print("total=%.2f, used=%.2f, number=%d, i=%d, min=%.2f, max=%.2f, int_min=%.2f, int_max=%.2f" %(total, used, number, i, min, max, int_min, int_max))
                int_value = random.randint(int_min, int_max)
                #print("int random is %d." %(int_value) )
                value = int_value / 100
                print("%d  --------  %.2f        [%.2f, %.2f]       before used %.2f" %(i+1, value, min, max, used))
                #计算已经使用的金额
                used += value

        print("\n\n")

if __name__=="__main__":
    get_wallet(100, 2, 10)
    pass