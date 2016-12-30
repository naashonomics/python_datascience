//Create a Histogram
import matplotlib.pyplot as plt 
//random test scores
test_scores = [55,45,88,75,43,56,89,98,65,44,66,77,89,72,73,72,84]
bins = [10.20,30,40,50,60,80,90,100]
//not useful for grades
plt.hist(test_scores,bins,histtype='bar',cumulative=True, rwidth=0.8)

plt.show()
