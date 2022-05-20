import math
def pythogorean():
    perimeter=1000
    for a in range(1,perimeter):
        for b in range(a+1,perimeter):
            c=perimeter-a-b
            if a ** 2 + b ** 2==c**2:
                print(a,b,c)
                return str(a*b*c)
if __name__ == '__main__':
    print(pythogorean())


