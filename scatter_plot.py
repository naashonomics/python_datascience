#create a scatter plot -corelation or trend usecase
import matplotlib.pyplot as plt 
#test_scores = [55,45,88,75,43,56,89,98,65,44,66,77,89,72,73,72,84]
#time_spent = [11,10,22,23,28,32,54,55,43,23,53,33,23,55,23,44,38]
#plt.title('Time Spent in a test V/s Test Scores')
#plt.xlabel('Time spent of test ')
#plt.ylabel('Test scores')
#plt.scatter(time_spent,test_scores)
#plt_show()

#example with colors for data sets 
x = [1,2,3,4,5]
y1 = [2,3,2,4,2]
y2 = [8,8,6,7,6]
plt.scatter(x,y1,marker='o',color='c')
plt.scatter(x,y2,marker='v',color='m')
plt.show()
