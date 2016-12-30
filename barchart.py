//Create a Bar Chart 
import matplotlib.pyplot as plt  

//p(x,y)
x1 = [1,2,3,4,5]
x2 = [1,3,5,7,9]
y1 = [4,5,6,7,3]
y2 = [5,6,2,6,2]


plt.bar(x1, y1 , label="One", color='m')
plt.bar(x2, y2 , label="Two", color='g')
//for legends 
plt.xlabel('Bar Number')
plt.ylabel('Bar Height')
plt.title('Bar Chart')
plt.legend()
plt.show()
