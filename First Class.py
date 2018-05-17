
# coding: utf-8

# In[ ]:

from sklearn import tree
features=[[130,1],[140,1],[150,2],[170,2]]
labels=[0,0,1,1]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
print(clf.predict([[160,2]]))


# In[6]:

from sklearn import tree
features=[[130,1],[140,1],[150,2],[170,2]]
labels=['Apple','Apple','Orange','Orange']
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
print(clf.predict([[160,'2']]))


# In[9]:

from sklearn import tree
features=[[130,1],[140,1],[150,2],[170,2]]
labels=['Apple','Apple','Orange','Orange']
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
print(clf.predict([[110,'2']]))


# In[ ]:



