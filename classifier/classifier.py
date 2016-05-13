import matplotlib.pyplot as plt
import numpy as np
import collections
from sklearn import datasets
from sklearn import ensemble
from sklearn.metrics import mean_squared_error
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_absolute_error
from sklearn.grid_search import GridSearchCV

from sklearn.metrics import precision_recall_fscore_support
import add_more_features
############################import###################################################
# Load data
def getData(data,type):
    test_data = []
    test_target = []
    train_data = []
    train_target = []
    if type == 1:
        # relationship between weather and taxi
        featnames = np.array(['DATE', 'PRCP', 'SNWD', 'TMAX', 'TMIN', 'SNOW',
                         'AWND', 'WDF2', 'WDF5', 'WSF2', 'WSF5', 'WT01', 'HOUR'])

        for i, row in enumerate(data):
            features = row[:-2]
            target = row.pop(-1)
            if i % 10 == 0:

                test_data.append(features)
                test_target.append(target)
            else:

                train_data.append(features)
                train_target.append(target)
    elif type == 2:
        # relationship between weather and taxi given uber data
        featnames = np.array(['DATE', 'PRCP', 'SNWD', 'TMAX', 'TMIN', 'SNOW',
                         'AWND', 'WDF2', 'WDF5', 'WSF2', 'WSF5', 'WT01', 'HOUR' ,'UBER'])


        for i, row in enumerate(data):
            features = row[:-1]
            features[-1] /= 10
            target = row.pop(-1)
            if i % 10 == 0:

                test_data.append(features)
                test_target.append(target/10)
            else:

                train_data.append(features)
                train_target.append(target/10)

    elif type == 3:
        # relationship between weather and uber
        featnames = np.array(['DATE', 'PRCP', 'SNWD', 'TMAX', 'TMIN', 'SNOW',
                         'AWND', 'WDF2', 'WDF5', 'WSF2', 'WSF5', 'WT01', 'HOUR' ])


        for i, row in enumerate(data):
            features = row[:-2]
            features[-1] /= 10
            target = row.pop(-2)
            if i % 10 == 0:

                test_data.append(features)
                test_target.append(target/10)
            else:

                train_data.append(features)
                train_target.append(target/10)
    elif type == 4:
        # relationship between weather and uber given taxi
        featnames = np.array(['DATE', 'PRCP', 'SNWD', 'TMAX', 'TMIN', 'SNOW',
                     'AWND', 'WDF2', 'WDF5', 'WSF2', 'WSF5', 'WT01', 'HOUR', 'TAXI' ])


        for i, row in enumerate(data):
            features = row[:-2] + [row[-1]]
            features[-1] /= 10
            target = row.pop(-2)
            if i % 10 == 0:

                test_data.append(features)
                test_target.append(target/10)
            else:

                train_data.append(features)
                train_target.append(target/10)


    return featnames, np.array(train_data), np.array(test_data), \
                   np.array(train_target),np.array(test_target)


def getData_predict(d_2014,d_2015):
    d = d_2014 + d_2015
    test_data = []
    train_data = []
    test_target = []
    train_target = []
    featnames = np.array(['DATE', 'PRCP', 'SNWD', 'TMAX', 'TMIN', 'SNOW',
                     'AWND', 'WDF2', 'WDF5', 'WSF2', 'WSF5', 'WT01', 'HOUR'])
    length = len(d)
    for i, row in enumerate(d):
            features = row[:-1]
            target = row[-1]
            if i > length - 720:

                test_data.append(features)
                test_target.append(target/10)
            else:

                train_data.append(features)
                train_target.append(target/10)
   
    return featnames, np.array(train_data), np.array(test_data), \
                   np.array(train_target),np.array(test_target)


data = open("../data/merged/final_data", "rb")
data_2014 = open("../data/merged/2014_merged_reduce_output", "rb")
datalist = []
datalist_2014 = []
datalist_2015 = []
for i, row in enumerate(data_2014):

    values = row.strip('\n').split('\t')
    date = values[0]
    date = float(date)
    vals = values[1].split(',')
    new_vals = []
    for v in vals:
        new_vals.append(float(v))
    print len([date]+new_vals)
    datalist_2014.append([date]+new_vals)
for i, row in enumerate(data):

    values = row.strip('\n').split('\t')
    date = values[0]
    date = float(date)
    vals = values[1].split(',')
    new_vals = []
    for v in vals:
        new_vals.append(float(v))

    datalist.append([date]+new_vals)
    print len([date]+new_vals[:-2]+[new_vals[-1]])
    datalist_2015.append([date]+new_vals[:-2]+[new_vals[-1]])

'''X, y = datasets.make_classification(n_samples=100000, n_features=20,
                                    n_informative=2, n_redundant=2)

train_samples = 100  # Samples used for training the models
'''
#feature_names, X_train, X_test, y_train, y_test = getData(datalist, 3)

feature_names, X_train, X_test, y_train, y_test = getData_predict(datalist_2014, datalist_2015)

###############################################################################
# Fit regression model
params = {'max_depth': 2, 'min_samples_split': 1,
          'learning_rate': 0.2, 'max_features': 1.0, 'n_estimators':6000}
#regressor = ensemble.GradientBoostingRegressor(n_estimators=6000)

#clf = GridSearchCV(regressor, params)

clf = ensemble.GradientBoostingRegressor(**params)
clf.fit(X_train, y_train)
#print clf.feature_importances_
mse_train = mean_squared_error(y_train, clf.predict(X_train))
absError = mean_absolute_error(y_train, clf.predict(X_train))
print "Absolute error train: ", absError
print "Absolute error test: ", absError

print("MSE train: %.4f" % mse_train)
mse = mean_squared_error(y_test, clf.predict(X_test))
print("MSE test: %.4f" % mse)
absError = mean_absolute_error(y_test, clf.predict(X_test))
print "Explained variance score - train: ", explained_variance_score\
    (y_train,clf.predict(X_train),multioutput='uniform_average')
print "Explained variance score - test: ", explained_variance_score\
    (y_test,clf.predict(X_test),multioutput='uniform_average')
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
#print precision_recall_fscore_support(y_test, np.array(results),average='macro'),mse

plt.figure(figsize=(12, 16))
plt.subplot(3, 1, 1)
plt.title('Deviance')
plt.plot(np.arange(params['n_estimators']) + 1, clf.train_score_, 'b-',
         label='Training Set Deviance')
plt.plot(np.arange(params['n_estimators']) + 1, test_score, 'r-',
         label='Test Set Deviance')
plt.legend(loc='upper right')
plt.xlabel('Boosting Iterations')
plt.ylabel('Deviance')
x_axis = []
d = {}
c = {}
y_axis_expected =[]
y_axis_predicted = []
for i in xrange(len(X_test)):
    if X_test[i][0] not in d:
        d[X_test[i][0]] = (y_test[i], results[i])
        c[X_test[i][0]] = 1
    else:
        d[X_test[i][0]] += (y_test[i], results[i])
        c[X_test[i][0]] += 1
od = collections.OrderedDict(sorted(d.items()))
for k in od:

    x_axis.append(k)
    y_axis_expected.append(od[k][0]/c[k])
    y_axis_predicted.append(od[k][1]/c[k])

x_axis = np.array(x_axis)
y_axis_expected = np.array(y_axis_expected)
y_axis_predicted = np.array(y_axis_predicted)
plt.subplot(3, 1, 2)

plt.plot(x_axis,y_axis_expected, 'r-', label='Actual')
plt.plot( x_axis,y_axis_predicted, 'b-', label='Predicted')
plt.xlabel('Timeline')
plt.title('Predicted vs the Actual')
####################################################### ########################
# Plot feature importance
feature_importance = clf.feature_importances_
# make importances relative to max importance
feature_importance = 100.0 * (feature_importance / feature_importance.max())
sorted_idx = np.argsort(feature_importance)
pos = np.arange(sorted_idx.shape[0]) + .5
plt.subplot(3, 1, 3)
plt.barh(pos, feature_importance[sorted_idx], align='center')
plt.yticks(pos, feature_names[sorted_idx])
plt.xlabel('Relative Importance')
plt.title('Variable Importance')
plt.show()
