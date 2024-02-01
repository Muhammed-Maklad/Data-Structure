import ctypes

'''
Creating advanced array that not only depend on the user size 
it depend on Capacity so if user size = 10 , we make capacity = 20
if so every time user add new item it will take O(1)
if user size become = 11 , then we will make capacity = 20
and So on ...........

'''

class Array:
    
    def __init__(self,size) :
        
        self.size = size # that is user size
        self.capacity = 2 * size  # that is actual memory size
        
        array_data_type = ctypes.py_object * self.capacity
        self.memory = array_data_type()
        
        for i in range(size):
            self.memory[i] = None
            
    def expand_capacity (self):
        # Double the actual array size 
        self.capacity *= 2
        print(f'We expand the capacity and it becomes {self.capacity}')
           
        # create a new array
        array_data_type = ctypes.py_object * self.capacity
        new_array = array_data_type()
        
        # copy the old one into the new one 
        for i in range(self.size):
            new_array[i]=self.memory[i]
            
        del self.memory
        self.memory = new_array
        
        
    
    def append (self,item):
        
        # We will check if the size = capacity, and then i will double the capacity
        if self.size == self.capacity:
            self.expand_capacity()
            
        self.memory[self.size] = item
        self.size += 1
        
     
array = Array(3) 

for i in range(array.size): 
    array.memory[i] = i +1


# append a new item in the list
array.append(8957)
array.append('hello')
array.append(95)

# print
for i in range(array.size): 
   print( array.memory[i])
   
