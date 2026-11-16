# время O(n*k) за счет двух циклов
# память O(k): два списка по k+1

prices = [3, 2, 6, 5, 0, 3]
k = 2  # сколько сделок можно сделать

# prices = list(map(int, input().split()))
# k = int(input())

n = len(prices) #длина массива

if k >= n // 2: #неограниченное кол-во сделок
    # сделок можно сделать сколько угодно, просто собираем все подъемы
    ans = 0
    for i in range(1, n):
        if prices[i] > prices[i - 1]:
            ans += prices[i] - prices[i - 1]
else: #ограниченное кол-во сделок 
    free = [0] * (k + 1)              # прибыль, когда акций на руках нет
    hold = [-float('inf')] * (k + 1)  # прибыль, когда акция на руках

    for p in prices: # O(n*k)
        # идем с конца, чтобы free[j-1] был еще со вчера
        for j in range(k, 0, -1): 
            free[j] = max(free[j], hold[j] + p)      # ничего не делаем или продаем
            hold[j] = max(hold[j], free[j - 1] - p)  # ничего не делаем или покупаем
    ans = free[k]

print("Максимальная прибыль:", ans)