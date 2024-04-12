from textblob.classifiers import NaiveBayesClassifier
import pandas

var = "pathhhh"

pd = pandas.read_csv(var)

x = pd.values[:1000, :]

train = []

for i in x:
    train.append((i[1], i[0]))

a = NaiveBayesClassifier(train)

s = a.classify("Thanks for your subscription to Ringtone UK your mobile will be charged £5/month Please confirm by replying YES or NO. If you reply NO you will not be charged")

print(s)