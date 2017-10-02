import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter

style.use('fivethirtyeight')

dataset = {'k' : [[1,2],[2,3],[3,1]] ,'r': [[6,5],[7,7],[8,6]]}
new_features=[5,7]


def k_nearest(data , predict , k=3):
    if len(data)>=k:
        warnings.warn('K is set to a value less then total voting groups. IDIOTS!!')
    distances=[]
    for group in data :
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            # np.linalg.norm() givs the euclidean distance
            distances.append([euclidean_distance , group])

    votes = [i[1] for i in sorted(distances) [:k]]
    print(votes)
    votes_result = Counter(votes).most_common(1)[0][0]
    
            
    # k nearest neighbours algorithms
    return votes_result

result= k_nearest(dataset , new_features ,k=3)
print(result)


for i in dataset:
    for i2 in dataset[i]:
        plt.scatter(i2[0] , i2[1] , s=100 , color=i)

        
plt.scatter(5, 7, s=100 , color=result)
plt.show()
