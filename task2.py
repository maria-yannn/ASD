import sys

input = sys.stdin.readline


def find_pos(arr, x):
    # бинпоиск: первое место, где arr[m] >= x
    # Сложность O(logd)
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l


n = int(input()) #кол-во парметров
a = list(map(int, input().split())) #веса для каждого параметра

d = int(input()) # кол-во объектов; чтение параметров O(n * d)
docs = [] #параметры
sc = []  # скор каждого дока
for _ in range(d):
    f = list(map(int, input().split())) #парметры
    docs.append(f) #где храняться параметры
    sc.append(sum(a[j] * f[j] for j in range(n))) #считаем релевантность и закидываем ее в массив

# храним пары (-скор, номер), тогда обычная сортировка = по убыванию скора
top = sorted((-sc[i], i) for i in range(d)) #создаем отсортированный массив, меняем на отрицательные, чтобы отсортировать по убыванию
#сорттровка работет за O(d * log(d))

q = int(input()) #кол-во запросов
out = [] #итоговый вывод
for _ in range(q): # Сложность O(q*(k+d))
    z = list(map(int, input().split())) #считываем запрос
    if z[0] == 1:
        k = z[1]
        out.append(' '.join(str(p[1] + 1) for p in top[:k])) #выводим топ k элементов; работает за O(k)
    else:
        i, j, v = z[1] - 1, z[2] - 1, z[3]

        # находим и убираем старую запись этого дока
        
        p = find_pos(top, (-sc[i], i))
        top.pop(p) #удаляем старую релевантность

        # пересчитываем скор, меняется только одно слагаемое
        sc[i] += a[j] * (v - docs[i][j])
        docs[i][j] = v

        # ищем новое место и вставляем
        
        p = find_pos(top, (-sc[i], i))
        top.insert(p, (-sc[i], i)) #работает за O(d) т к нужно вставить элемент в массив

print('\n'.join(out))
#Итоговая сложность O(n*d+d*lod(d)+q*(k + d))