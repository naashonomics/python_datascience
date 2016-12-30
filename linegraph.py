//to mimic matlab  in python 
import matplotlib.pyplot as plt  

//p(x,y)
x = [1,2,3,4,5]
y1 = [4,5,6,7,3]
y2 = [5,6,2,6,2]

//for legends 
plt.plot(x,y1,label='Intital Line')
plt.plot(x,y2,label='End Line') 

//Setting X-Y axis and chart Title
plt.xlabel('Plot Number')
plt.ylabel('Random #')
plt.title('Epic Graph')

//exception handling 
//print(len(x))
//print(len(y))

//print out the graph
plt.show()
print('I am here')
