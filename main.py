import Car

# Python program to demonstrate 
# main() function 
def main(): 
	print("Main Program __name__ = %s" %__name__)
	C1 = Car.Car(True,4)
	C1.start()
	C1.increase_speed(10)
	
	

# Using the special variable 
# __name__ 
if __name__=="__main__": 
	main() 
