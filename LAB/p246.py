def doublefactorial(n):
    if (n == 0 or n == 1):
        return 1;
    return n * doublefactorial(n - 2);



print(doublefactorial(6));