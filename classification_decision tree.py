import pydot
import numpy as np
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split

if __name__=='__main__':

    np,random.seed(0)

    x=np.random.rand(300,2)
    y=(x[:,0]>0.3)&(x[:,0]<0.7)&(x[:,1]>0.3)&(x[:,1]<0.7)

    mask=np.random.permutation(len(x))[:5]
    y[mask]=~y[mask]

    #decision tree실습에 사용할 데이터세트(xy)이다
    x_train,x_test,y_train,y_test=train_test_split(x,y)
    clf=DecisionTreeClassifier(max_depth=3)

    clf.fit(x_train,y_train)
    y_pred=clf.predict(x_test)
    print('Test accuracy: %.3f' % np.mean(y_pred==y_test))
    #아래코드부분은 생성데이터를 가시화함
    clf_dot=export_graphviz(clf)
    (graph, )=pydot.graph_from_dot_data(clf_dot)
    graph.write_png('graph.png')

    #x_class_1=x[y==0]
    #plt.scatter(x_class_1[:,0], x_class_1[:,1],color=(1.0,0,0,),label='class 1')

    #x_class_2=x[y==1]
    #plt.scatter(x_class_2[:,0], x_class_2[:,1],color=(0,0,1.0,),label='class 2')

    #plt.legen(loc='best')
    #plt.show()


