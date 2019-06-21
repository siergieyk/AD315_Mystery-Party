import numpy as np


SafeCombo=[401, 503, 1043, 931, 301, 3, 450, 601, 33, 420, 577, 10, 640, 1500, 467, 500, 333, 204, 233, 1, 799, 555, 831, 1099, 155, 630, 7, 134, 350, 99, 101, 477, 499, 44, 256, 1281, 660, 603, 88, 522, 187, 501, 1421, 1134]

SortedList1=[1, 3, 7, 10, 33, 44, 88, 99, 101, 134, 155, 187, 204, 233, 256,
301, 333, 350, 401, 420, 450, 467, 477, 499, 500, 501, 503, 522, 555, 577, 
601, 603, 630, 640, 660, 799, 831, 931, 1043, 1099, 1134, 1281, 1421, 1500]




def bubSortRec(SafeCombo): 
  for i, num in enumerate(SafeCombo): 
        try: 
            if SafeCombo[i+1] < num: 
                SafeCombo[i] = SafeCombo[i+1] 
                SafeCombo[i+1] = num 
                bubSortRec(SafeCombo) 
        except IndexError: 
            pass
  return SafeCombo

def binarySearchRec (SortedList1, l, r, num): 
  
  if r >= l: 
      mid = l + (r - l)/2
      if SortedList1[int(mid)] == num: 
          return mid 
      elif SortedList1[int(mid)] > num: 
          return binarySearchRec(SortedList1, l, mid-1, num) 
      else: 
          return binarySearchRec(SortedList1, mid + 1, r, num)