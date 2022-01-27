import random

def generateNum(start, finish):
  """Generate a random number between a start and finish value

  :param start: the smallest possible number generated
  :type start: int

  :param finish: the largest possible number generated
  :type finish: int

  :returns: random number between start and finish parameter values
  :rtype: int

  >>>generateNum(1, 50)
  any value between 1 and 50 inclusive
  >>>generateNum(1, 10)
  any value between 1 and 10 inclusive

  STRATEGY: random method from the random library

  """
  return random.randint(start, finish)




guessedNum = int(input('Enter a number between 1 and 50: '))

randomNum = generateNum(1, 50)

if guessedNum == randomNum:
  print('You guessed the correct number and won this game')
else:
  print('You didn\'t guess the correct number and lost this game')

# added to show the randomly generated number, not part of the flowchart process
print('The winning number was:',randomNum)
