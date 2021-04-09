
add = 0
counter  = 0
 
for x  in range (1 , 100):
     if (x % 3 == 0):
         #print (x)
         add = add + x
         counter += 1

        
print ("Average:" , (add/counter))
         
