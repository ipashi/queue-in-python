front,rear=0,0 #front for dequeue, rear for enqueue global variables 
size=4 # size of the list
a = [0]*size # initializing the list with all zeros
def enqueue(data):
	global rear #using global rear 
	if(rear<size): #checking the size of list
		a[rear]=data
		rear+=1 #increment rear so that it holds the position for the next element to be inserted
	else:
		print("queue is full")
enqueue(1) #inserting 1
enqueue(2) #inserting 2
enqueue(3) #inserting 3
enqueue(4) #inserting 4
print(a)
enqueue(5) # insering 5 will output queue full message
# refering to the queue we have created in the above code snippet
def dequeue():
	global front
	if(front>=rear): #check if queue is empty
		print("Queue is empty")
	else:
		print("Dequeue element value :",a[front])
		front+=1 #increment front so that it points to the next element in queue
dequeue() # takes out 1
dequeue() # takes out 2
dequeue() # takes out 3
dequeue() # takes out 4
dequeue() # outputs queue is empty as all the elements are taken out
# return true if queue is empty else returns false
def isEmpty(queue):
	global front,rear
	if(front==rear):
		return True
	else:
		return False 
print(isEmpty(a)) # as the queue is empty it will return true
# outputs the topmost element of the queue
def peek():
	global rear
	if(rear==front):
		print("queue is empty")
	else:
		print("The topmost element is :",a[rear])
peek()