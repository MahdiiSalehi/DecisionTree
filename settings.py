#In the name of ALLAH!
#Mahdi Salehi

from my_array import Array

FEATURE_TRAIN_FILE_PATH = "data/feature_train.csv"
LABEL_TRAIN_FILE_PATH = "data/label_train.csv"
FEATURE_TEST_FILE_PATH = "data/feature_test.csv"
LABEL_TEST_FILE_PATH = "data/label_test.csv"

DRAW_FILE_PATH = "tree/figure.txt"

NUM_OF_ESIMATOR = 10

# Find num of rows and columns.
file = open(FEATURE_TRAIN_FILE_PATH)
col = 0
row = 0
for i in file.readline().split(','):
    col += 1
for i in file.readlines():
    row += 1

file = open(FEATURE_TEST_FILE_PATH)
row2 = -1
for i in file.readlines():
    row2 += 1

names = Array(col)
train_features = Array(col)
train_rows = Array(row)
train_labels = Array(row)
test_rows = Array(row2)
test_labels = Array(row2)


# Read train feature file.
file = open(FEATURE_TRAIN_FILE_PATH)
line = file.readline().split(',')
for i in range(col):
    names[i] = line[i]
    train_features[i] = Array(row)
for i in range(row):
    train_rows[i] = Array(col)
    line = file.readline().split(',')
    for j in range(col):
        train_rows[i][j] = int(line[j])
        train_features[j][i] = int(line[j])


# Read train label file.
file = open(LABEL_TRAIN_FILE_PATH)
file.readline()
for i in range(row):
    train_labels[i] = int(file.readline())


# Read test feature file.
file = open(FEATURE_TEST_FILE_PATH)
file.readline()
for i in range(row2):
    test_rows[i] = Array(col)
    line = file.readline().split(',')
    for j in range(col):
        test_rows[i][j] = int(line[j])


# Read train label file.
file = open(LABEL_TEST_FILE_PATH)
file.readline()
for i in range(row2):
    test_labels[i] = int(file.readline())
# Finish reading.
    