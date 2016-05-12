import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn import ensemble
from sklearn.metrics import mean_squared_error
from sklearn.metrics import precision_recall_fscore_support

############################import###################################################
# Load data
data = open("data/final_data", "rb")

boston = datasets.load_boston()

test_data = []
train_data = []
test_target = []
target = []
for i ,row in enumerate(data):
    values = row.strip('\n').split('\t')
    date = values[0]
    date = float(date)
    vals = values[1].split(',')
    new_vals = []
    for v in vals:
        new_vals.append(float(v))
    tup = (new_vals[:-1], new_vals.pop(-1))
    features = [date] + tup[0] + [tup[1]]
    if i % 10 == 0:
        test_data.append(features)
        test_target.append(round(tup[1]/100))
    else:

        train_data.append(features)
        target.append(round(tup[1]/100))


'''X, y = datasets.make_classification(n_samples=100000, n_features=20,
                                    n_informative=2, n_redundant=2)

train_samples = 100  # Samples used for training the models
'''
X_train = np.array(train_data)
X_test = np.array(test_data)
y_train = np.array(target)
y_test = np.array(test_target)



###############################################################################
# Fit regression model
params = {'n_estimators': 1500, 'max_depth': 2, 'min_samples_split': 1,
          'learning_rate': 0.1, 'loss': 'ls'}
clf = ensemble.GradientBoostingRegressor(**params)

clf.fit(X_train, y_train)
mse = mean_squared_error(y_test, clf.predict(X_test))
print("MSE: %.4f" % mse)

###############################################################################
# Plot training deviance

# compute test set deviance

test_score = np.zeros((params['n_estimators'],), dtype=np.float64)
results = []
for i, y_pred in enumerate(clf.staged_predict(X_test)):
    test_score[i] = clf.loss_(y_test, y_pred)
    results = []
    mse = mean_squared_error(y_test, y_pred)
    for val in y_pred:
        results.append(round(val))

    #print y_test,np.array(results)
    print precision_recall_fscore_support(y_test, np.array(results),average='macro'),mse
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Deviance')
plt.plot(np.arange(params['n_estimators']) + 1, clf.train_score_, 'b-',
         label='Training Set Deviance')
plt.plot(np.arange(params['n_estimators']) + 1, test_score, 'r-',
         label='Test Set Deviance')
plt.legend(loc='upper right')
plt.xlabel('Boosting Iterations')
plt.ylabel('Deviance')

###############################################################################
# Plot feature importance
feature_importance = clf.feature_importances_
# make importances relative to max importance
feature_importance = 100.0 * (feature_importance / feature_importance.max())
sorted_idx = np.argsort(feature_importance)
pos = np.arange(sorted_idx.shape[0]) + .5
plt.subplot(1, 2, 2)
plt.barh(pos, feature_importance[sorted_idx], align='center')
# plt.yticks(pos, boston.feature_names[sorted_idx])
plt.xlabel('Relative Importance')
plt.title('Variable Importance')
plt.show()
