
import operator
import bayes
from cytoolz.curried import sorted


listPosts, listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listPosts)
myVocabList = sorted(myVocabList)
print(myVocabList)

retVal = bayes.setOfWords2Vec(myVocabList, listPosts[0])
print(retVal)

trainMat = []
for postingDoc in listPosts:
    print(postingDoc)

    # 返回 myVocabList 中的word是否在 postingDoc中出现过?
    trainMat.append( bayes.setOfWords2Vec(myVocabList, postingDoc) )

p0V, p1V, pAbusive = bayes.trainNB0(trainMat, listClasses)
#print("p0V: %f, p1V: %f, pAbusive: %f" %p0V %p1V %pAbusive )
print(p0V)
print(p1V)
print(pAbusive)