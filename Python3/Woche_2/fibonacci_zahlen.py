def f(n:int)->int:
    if n == 1 or n==2: #f(1)=1 und f(2)=1
        return 1 #daher für beide Fälle 1 ausgegeben
    else: #für alle anderen Fälle:
        return f(n - 1) + f(n - 2) #die Summe der beiden Vorgänger ausgeben, also n-1 und n-2
f(5)
