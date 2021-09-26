def SumOfLucas(highestNumber):
  previousNumber = 2
  currentNumber = 1
  sum = 1
  while (currentNumber + previousNumber) < highestNumber:
    temp = currentNumber
    currentNumber = currentNumber + previousNumber
    previousNumber = temp
    if currentNumber % 2 != 0:
      sum += currentNumber
  return sum    

print(SumOfLucas(4000000))