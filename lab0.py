def myFunction():
  Sum = 0
  for i in range(100):
    if i%3==0 or i%5==0:
      a=i
      Sum+=a
    if i%3==0 and i%5==0:
      b=i
      Sum-=b
  return Sum


#if __name__ == '__main__':
print(myFunction())