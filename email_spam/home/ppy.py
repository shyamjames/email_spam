import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
from geneticalgorithm import geneticalgorithm as ga
import pandas
var = r"C:\Users\shyam\Desktop\email_spam_recognition\email_spam\static\spamham.csv"

pd = pandas.read_csv(var)

x1 = pd.values[:1000, :]

x = []
y=[]
for i in x1:
    x.append(i[1])
    y.append(i[0])
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Feature extraction
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Define and train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Define fitness function for Genetic Algorithm
def fitness_function(params):
    alpha = params[0]
    model = MultinomialNB(alpha=alpha)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return -accuracy_score(y_test, y_pred)

# Define bounds and optimize with Genetic Algorithm
varbound = np.array([[0, 1]])  # Bounds for alpha parameter
algorithm_param = {'max_num_iteration': 1000, 'population_size': 100}
model = ga(function=fitness_function, dimension=1, variable_type='real', variable_boundaries=varbound, algorithm_parameters=algorithm_param)
model.run()

# Get the optimized alpha parameter
best_alpha = model.output_dict['variable'][0]
print("Optimized alpha parameter:", best_alpha)

# Train the model with the optimized alpha parameter
optimized_model = MultinomialNB(alpha=best_alpha)
optimized_model.fit(X_train, y_train)

# Evaluate the optimized model
y_pred_optimized = optimized_model.predict(X_test)
accuracy_optimized = accuracy_score(y_test, y_pred_optimized)
print("Accuracy with optimized model:", accuracy_optimized)