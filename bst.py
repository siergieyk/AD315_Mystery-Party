
class Node():
	def __init__(self, key, desc):
		self.key = key
		self.left = None
		self.right = None
		self.desc = desc
	
def insert(root, node):

	if root is None:
		root = node 
	
	else:
		if root.key < node.key:
			if root.right is None:
				root.right = node 
			else:
				insert(root.right, node)
		else:
			if root.left is None:
				root.left = node
			else:
				insert(root.left, node)

		
def preorder(root):
  if root:
    print(root.key)
    preorder(root.left)
    preorder(root.right)

r = Node(35, "desc")
array = [75,25,62,101,13,9,33,8]

for i in array:
	insert(r, Node(i, "desc"+str(i)))


    


arrayBalance = [20,30,34,61,110]
elements = arrayBalance
for i in arrayBalance:
  insert(r, Node(i, "desc"+str(i)))
  


def pre():
  print("35")
  print("25")
  print("13")
  print("9")
  print("8")
  print("33")
  print("75")
  print("62")
  print("101")