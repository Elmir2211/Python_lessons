# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    a=(number - int(number)) * (10 ** ndigits)
    if (a-int(a))>0.5:
        res=int(number)+((int(a)+1)/(10**ndigits))
        return res
    else:
        res = int(number) + ((int(a)) / (10 ** ndigits))
        return res


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    def summ(spisok):
        s = 0
        i = 0
        while i < len(spisok):
            s += spisok[i]
            i += 1
        return s
    lst = []
    while ticket_number > 0:
        b = ticket_number % 10
        lst.append(b)
        ticket_number = ticket_number // 10
    if summ(lst[:3])==summ(lst[-3:]):
        return "Счастливый билет!"
    else:
        return "Билет несчастливый!"


print(lucky_ticket(123006))
print(lucky_ticket(123210))
print(lucky_ticket(436751))
