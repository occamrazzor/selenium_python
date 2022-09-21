
""" itemsInCart = 0
# 2 items will be added to cart
# verfiy there are 2 item else fail the verification.


if itemsInCart != 2:
	# raise Exception('Product cart count not matching')
	pass

assert(itemsInCart == 2) #Throws Exception error
 """

 #try, catch 
""" 
try:
	with open('test1.txt', 'r') as reader:
		reader.read()
except:
	print('Caught the failure in the try block')	 """


try:
	with open('test.txt', 'r') as reader:
		reader.read()
except Exception as e:
	print(e)

finally: # finally block always runs regardless of exceptions ...From finally block cleaning up resources
	print('From finally block cleaning up resources')