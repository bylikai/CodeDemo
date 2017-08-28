import numpy as np 

def pythonsum(n):
    'return : a^2 + b^3'
    a = range(n)
    b = range(1, n, 2)
    c = []
    print(a)
    print(b)

#     for i in  range(len(a)) :
#         a[i] = i**2
#         b[i] = i**3
#         c.append( a[i] + b[i])
#     return c
# def numpysum(n):
#     a = np.arrange(n) ** 2
#     b = np.arrange(n) ** 3
#     c = a+b
#     return c

def main():
    pythonsum(100)

if __name__ == '__main__':
    main()