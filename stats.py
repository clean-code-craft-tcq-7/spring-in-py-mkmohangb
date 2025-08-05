import math

def is_within_range(numbers):
    return all(num > 0 and num < 200 for num in numbers)

def calculateStats(numbers):
  stats = {}
  numbers_without_nan = [num for num in numbers if not math.isnan(num)]
  if numbers_without_nan and is_within_range(numbers_without_nan):
    stats['avg'] = sum(numbers_without_nan)/len(numbers_without_nan)
    stats['max'] = max(numbers_without_nan)
    stats['min'] = min(numbers_without_nan)
  else:
    stats['avg'] = float('nan')
    stats['max'] = float('nan')
    stats['min'] = float('nan')
  return stats