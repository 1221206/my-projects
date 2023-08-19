import pandas as pd   
 

data = pd.read_csv(r"c:\python projects\spam_ham\spam_ham_dataset.csv") 
data.head() # gives 6 rows

#print(data.shape) # gives rows,columns

#data['spam'].value_counts() # gives number of spam and ham

# data.duplicated().sum() # gives duplicated values

data.drop_duplicates(inplace=True) # delete them

#print(data.duplicated().sum()) # give 0 , also data.shape has changed 

#print(data.isnull().sum())  # check for null

# preprocess ie.. convert words

def text_preprocess(x):
    x = str(x).lower()
    x = x.replace(",000,000", "m").replace(",000", "k").replace("′", "'").replace("’", "'")\
                           .replace("won't", "will not").replace("cannot", "can not").replace("can't", "can not")\
                           .replace("n't", " not").replace("what's", "what is").replace("it's", "it is")\
                           .replace("'ve", " have").replace("i'm", "i am").replace("'re", " are")\
                           .replace("he's", "he is").replace("she's", "she is").replace("'s", " own")\
                           .replace("%", " percent ").replace("₹", " rupee ").replace("$", " dollar ")\
                           .replace("€", " euro ").replace("'ll", " will") 
    return x  

data["Preprocessed Text"] = data["text"].apply(lambda x: text_preprocess(x))

X = data['Preprocessed Text'].values
y = data['spam'].values


# train test

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.25 , random_state= 0) # random state for shuffling

# preprocessing convert to numbers
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
x_train = cv.fit_transform(X_train)

# train algo
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(x_train, y_train)
x_test = cv.transform(X_test)


# check
y_pred = nb.predict(x_test)
from sklearn.metrics import accuracy_score
print("Testing Accuracy:")
print(accuracy_score(y_pred, y_test))

print("Training Accuracy:")
print(nb.score(x_train,y_train))

email = ['this is elon musk,collect your tesla car']

clean_email = cv.transform(email)
check = nb.predict(clean_email)[0]

if check == 0:
    print("This is a Ham Email!")
else:
    print("This is a Spam Email!")
