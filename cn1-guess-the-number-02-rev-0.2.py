import random

def generateNum(start, finish, count, unique, ordered):
  """Generate a random number between a start and finish value

  :param start: the smallest possible number generated
  :type start: int

  :param finish: the largest possible number generated
  :type finish: int

  :param count: count of random numbers generated
  :type count: int

  :param unique: ensure all random numbers are unique
  :type unique: bool

  :param ordered: random numbers are ordered from lowest to highest value
  :type ordered: bool

  :returns: random numbers as specified with parameter values
  :rtype: list

  >>>generateNum(1, 50, 1, False, False)
  one number of any value between 1 and 50 inclusive, not ordered
  >>>generateNum(1, 50, 4, False, True)
  four numbers of any value between 1 and 50 inclusive, ordered
  >>>generateNum(1, 50, 4, True, False)
  four unique numbers of any value between 1 and 50 inclusive, not ordered
  >>>generateNum(1, 10, 1, True, False)
  one value between 1 and 10 inclusive

  STRATEGY: random method from the random library

  """
  randomNums = []
  while len(randomNums) < count:
    if unique == False:
      randomNums.append(random.randint(start, finish))
    else:
      randomSet = set(randomNums)
      randomSet.add(random.randint(start, finish))
      randomNums = list(randomSet)
  if ordered == True:
    randomNums.sort()
  return randomNums


print(generateNum(1, 6, 6, True, False))


