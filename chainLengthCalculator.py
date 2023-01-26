#!/usr/bin/env python3

def chainLengths(length, standardLength, offsetLength):
  numOfLengths = int(round(length / standardLength, 0)) -1
  bestLengths = [0, 0]
  closest = 100
  for i in range(numOfLengths):
    newLength = i * standardLength + (( numOfLengths - i) * offsetLength)
    lengthDifference = newLength - length
    if (abs(lengthDifference) < abs(closest) and lengthDifference >= 0):
      closest = lengthDifference
      bestLengths[0] = i
      bestLengths[1] = numOfLengths -i
  a, b = bestLengths
  closestLength = a * standardLength + b * offsetLength
  finalDifference = closestLength - length
  return print("Number of {}\" lengths: {}\nNumber of {}\" offsets: {}\nTotal Length = {}\"\nDifference = {}\"".format(standardLength, a, offsetLength, b, closestLength, finalDifference))

cLength = float(input("How long is the chain length?: "))
sLength = float(input("How long are the standard link lengths?: "))
oLength = float(input("How long are the offset link lengths?: "))
chainLengths(cLength, sLength, oLength)
