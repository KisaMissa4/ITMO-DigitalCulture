# Вставляешь числа из заданий по порядку:
# Задание 1:
a = 286
b = 2288
c = 2288
d = 286
e = 2288000

# Задание 2:
f = 248

# Задание 3: g - это размер, h - это скорость
g = 15.8
h = 113

# Задание 4: i - это раз в секунду, j - это замер
i = 27856
j = 24

# Задание 5:
k = 814

# Задание 6: l - это секунд, m - это кол-во уровней
l = 0.08
m = 869

# Задание 7: n - это байт (размер пакета), o - это байт (заголовок) , p - это байт (размер файла)
n = 5698
o = 90
p = 77800


# Решение
def upwards(y):
    if int(y * 10 % 10) == 0:
        if (y * 100 % 10) < 5:
            return int(y)
        else:
            return int(y) + 0.1
    else:
        y *= 100
        if y % 10 <= 5:
            y /= 100
            y = round(y + 0.1, 1)
            return y
        else:
            return round(y / 100, 1)


def pow2(gg):
    count = 1
    while gg != 0:
        if gg == 1:
            break
        else:
            gg //= 2
            count += 1
    return count


print("Задание 1:")
print(f"1: {a * 1024 * 8}")
print(f"2: {b / 1000}")
print(f"3: {c / 1000}")
print(f"4: {d * 1000}")
print(f"5: {e / 1000 / 8}", "\n")

print("Задание 2:")
z = f * (10 ** 9)
print(f"1: {z}")
print(f"2: {int(round(z / (2 ** 30), 2) * 10) / 10}", "\n")

print("Задание 3 (Если число например: 15.0, то в ответ пишешь 15):")
print(upwards(y=int((g * (2 ** 30)) / (h * 1000 * 125) / 60 * 100) / 100), "\n")

print("Задание 4:")
print(round(j / i * 1000, 3), "\n")

print("Задание 5:")
print(pow2(k), "\n")

print("Задание 6:")
print(round(pow2(m) / l, 2), "\n")

print("Задание 7:")
print(int(p / (n - o)) + 1)
