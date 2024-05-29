def add(a, b, c):
  return a+b+c
def subtract(a, b):
  return a-b
def multiply(a, b):
   return a*b

def getMedian(a, b):
    return (a+b)/2

def get_Abs(num):
   if mum>=0:
      return num
   else:
      return -num
   
def getRemainder(a, b):
    return a//b

def get_Percent(a, b):
   return (a/b) *100

def get_sum_ver1(n):
   return(n+1)/2

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num