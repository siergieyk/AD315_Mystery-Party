import itertools
import math
faceHearts = {"h-J","h-Q","h-K"}

def perm():

  heartsFaces = list(itertools.permutations(faceHearts))
  print("\nFace Hearts permutations: ",heartsFaces)