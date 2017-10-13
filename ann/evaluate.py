#! bin/bash/python3
from ANN import ANN

print('Initializing ANN...')
ann = ANN()

print('Done. Restoring from pickle files...')
ann.restore()

print('Done. Fitting test inputs...')
test_inputs = [[1 if i == j else 0 for i in range(10)] for j in range(10)]
threshold_outputs = [ann.fit(test_input, True) for test_input in test_inputs]
trunc_outputs = [ann.fit(test_input) for test_input in test_inputs]
raw_outputs = [ann.fit(test_input, truncate=-1) for test_input in test_inputs]

print('Done. Thresholded results:')
for i in range(10):
    print(test_inputs[i], '==>', threshold_outputs[i], test_inputs[i] == threshold_outputs[i])

print('\nTruncated results:')
for i in range(10):
    print(test_inputs[i], '==>', trunc_outputs[i])


print('\nRaw results:')
for i in range(10):
    print(test_inputs[i], '==>', raw_outputs[i])