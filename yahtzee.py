import numpy as np

def Yahtzee():
  num = 5
  size = 5
  dice = 6

  Yahtzee = '{:.2%}'.format(6/dice**size)
  fkind = '{:.2%}'.format(150/dice**size)
  tkind = '{:.2%}'.format(1200/dice**size)
  fhouse = '{:.2%}'.format(300/dice**size)
  sstr = '{:.2%}'.format(3600/dice**size)
  lstr = '{:.2%}'.format(720/dice**size)

  print("Rolls                   Result      Prob")

  for i in range(num):
	  result = sorted(np.random.randint(1, dice, size))

	  if result[0] == result[1] and result[1] == result[2] and result[2] == result[3] and result[3] == result[4]:
	    print(i+1,"[",result[0],result[1],result[2],result[3],result[4],"]","		Yahtzee		", Yahtzee)
	  elif result[0] == result[1] and result[1] == result[2] and result[2] == result[3] and result[3] != result[4]:
	    print(i+1,"[",result[0],result[1],result[2],result[3],result[4],"]","		4Kind		", fkind)
	  elif result[0] != result[1] and result[1] == result[2] and result[2] == result[3] and result[3] == result[4]:
	    print(i+1,"[",result[0],result[1],result[2],result[3],result[4],"]","		4Kind		",fkind)
	  elif result[0] != result[1] and result[1] != result[2] and result[2] == result[3] and result[3] == result[4]:
	    print(i+1,"[",result[0],result[1],result[2],result[3],result[4],"]","		3Kind		",tkind)
	  elif result[0] == result[1] and result[1] == result[2] and result[2] != result[3] and result[3] != result[4]:
	    print(i+1,"[",result[0],result[1],result[2],result[3],result[4],"]","		3Kind		",tkind)
	  elif result[0] != result[1] and result[1] == result[2] and result[2] == result[3] and result[3] != result[4]:
	    print(i+1,"[",result[0],result[1],result[2],result[3],result[4],"]","		3Kind		",tkind)
	  elif result[0] == result[1] and result[1] != result[2] and result[2] == result[3] and result[3] == result[4]:
	    print(i+1,"[",result[0],result[1],result[2],result[3],result[4],"]","		FullHouse	",fhouse)
	  elif result[0] == result[1] and result[1] == result[2] and result[2] != result[3] and result[3] == result[4]:
	    print(i+1,"[",result[0],result[1],result[2],result[3],result[4],"]","		FullHouse	",fhouse)
	  elif result[0] - result[1]==-1 and result[1] - result[2]==-1 and result[2] - result[3]==-1 and result[3] - result[4]==-1:
	    print(i+1,"[",result[0],result[1],result[2],result[3],result[4],"]","		LargeStr	",lstr)
	  elif result[0] - result[1]==-1 and result[1] - result[2]==-1 and result[2] - result[3]==-1 and result[3] - result[4]!=-1:
	    print(i+1,"[",result[0],result[1],result[2],result[3],result[4],"]","		SmallStr	",sstr)
	  elif result[0] - result[1]!=-1 and result[1] - result[2]==-1 and result[2] - result[3]==-1 and result[3] - result[4]==-1:
	    print(i+1,"[",result[0],result[1],result[2],result[3],result[4],"]","		SmallStr	",sstr)
	  else:
	    print(i+1,"[",result[0],result[1],result[2],result[3],result[4],"]","		Nothing		","N/A")