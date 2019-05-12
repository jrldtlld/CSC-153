import re
import sys
sys.setrecursionlimit(10000)
#from pythonds.basic.stack import Stack
#from pythonds.trees.binaryTree import BinaryTree

class Stack2:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
# Use list append method to add element
        if dataval:
            self.stack.append(dataval)
            return True
        else:
            return False
    def elem(self):
    	for x in self.stack:
    		print (x)

    def len(self):
    	return len(self.stack)
# Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

def token():
	data = open('code.txt', 'r')
	contents = data.read()
	expression = []
	list_keywords = ['print', 'scanf', 'include', 'int', 'float', 'char', 'double', "stdio.h", 'main', 'do', 'return', 'while', 'for']
	list_symbols = ['#', '%', '(', ')', '{', '}', '?',  ';', '.', '_', '"', "'"]
	list_operators = ['+', '/', '*', '-', '>', '<', '=', '!']
	list_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
	list_letters = ['A', 'a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k'\
    				'L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v',\
				'W','w','X','x','Y','y','Z','z']

	sym_container = []
	ope_container = []
	dig_container = []
	words_container = []
	keyword_container = []
	word = []
	digit = []
	contents = list(contents)
	flag = 0
	astack = Stack2()

	for i, content in enumerate(contents):
		if flag == 1:
			# print('entered at flag 1')
			if content != '"':
				# print('entered at statement not ""')
				astack.add(content)
			else:
				# print('entered else at flag 1')
				sym_container.append(content)
				while astack.len() != 0:
					# print('flag 1 loop')
					x = astack.remove()
					word.append(x)
				worded = "".join(reversed(word))
				if worded in list_keywords:
					keyword_container.append(worded)
					expression.append(worded)
					word[:] = []
				else:
					words_container.append(worded)
					expression.append(worded)
					word[:] = []
				flag = 0
		elif content == '"':
			# print('entered at statement 2')
			sym_container.append(content)
			expression.append(content)
			flag = 1
		elif content in list_symbols:
			sym_container.append(content)
			expression.append(content)
		elif content in list_operators:
			ope_container.append(content)
			expression.append(content)
		elif content in list_letters:
			if (i+1 != len(contents)):
				if (contents[i+1] in list_letters):
					word.append(content)
					expression.append(content)
				elif(contents[i+1] in list_digits):
					word.append(content)
					expression.append(content)
				elif(str(contents[i+1]) == '_'):
					word.append(content)
					expression.append(content)
				else:
					word.append(content)
					worded = "".join(word)
					if worded in list_keywords:
						keyword_container.append(worded)
						expression.append(worded)
						word[:] = []
					else:
						words_container.append(worded)
						expression.append(worded)
						word[:] = []
			else:
				word.append(content)
		elif content in list_digits:
			if (i+1 != len(contents)):
				if (contents[i+1] in list_digits):
					digit.append(content)
				elif contents[i+1] == '.':
					digit.append(content)
					digit.append(".")
				else:
					digit.append(content)
					digited = "".join(digit)
					dig_container.append(digited)
					expression.append(digited)
					digit[:] = []
			else:
				dig_container.append(content)
				expression.append(content)

	print('---------------------------------------')
	print('                table                  ')
	print('---------------------------------------\n')
	for w in dig_container:
		print ('digits - {}'.format(w))
	print('\n---------------------------------------')
	for w in keyword_container:
		print ('keyword - {}'.format(w))
	print('\n---------------------------------------')
	for w in sym_container:
		print ('operator - {}'.format(w))
	for w in ope_container:
		print ('operator - {}'.format(w))
	print('\n---------------------------------------')
	for w in words_container:
		print ('identifier - {}'.format(w))
	print('\n---------------------------------------')
	print ('expression')
	return expression


#def parseTree(content):
#    # content = list(content)
#	# content = content.split()
#	print(content)
#	treeStack = Stack() #to keep track the parent node
#	pTree = BinaryTree('') #Initialize empty tree
#	treeStack.push(pTree)
#	currentNode = pTree
#	for elem in content:
#		if elem == '(':
#			currentNode.insertLeft('')
#			treeStack.push(currentNode)
#			currentNode = currentNode.getLeftChild()
#		elif elem not in ['-', '+', '/', '%', '*', ')']:
#			currentNode.setRootVal(elem)
#			parentNode = treeStack.pop()
#			currentNode = parentNode
#		elif elem in ['-', '+', '/', '%', '*']:
#			currentNode.setRootVal(elem)
#			currentNode.insertRight('')
#			treeStack.push(currentNode)
#			currentNode = currentNode.getRightChild()
#		elif elem == ')':
#			currentNode = treeStack.pop()
#		else:
#			print('error')
#			exit()
#	return pTree

class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

from anytree import Node, RenderTree

def cst(content):

	cstree = Node(content)		
	child_exp = []
	flag = 0
	for i, elem in enumerate(content):
		if flag == 0:
			if elem == '(':
				i = Node(elem, parent = cstree)
				flag = 1
			elif elem not in ['-', '+', '/', '*', '%']:
				child_exp.append(elem)
			else:
				x = child_exp
				child = Node(x, parent = cstree)
				cst(x).parent = child
				child2 = Node(elem, parent = cstree)
				child3 = Node(content[i+1:len(content)+1], parent = cstree)
				cst(content[i+1:len(content)+1]).parent = child3
				return cstree
		else:
			if elem != ')':
				i = Node(elem, parent = cstree)
			else:
				child_exp.append(elem)
				flag = 0
	return cstree

x = token()
print("\n")
for pre, fill, node in RenderTree(cst(x)):
	print("%s%s" % (pre, node.name))	
#data = open('code.txt', 'r')
#contents = data.read()
#print(parseTree(x))