#! bin/bash/python3
from ANN import ANN

print('Initializing ANN...')
ann = ANN()

print('Done. Setting inputs...')
ann.inputs = [[1 if i == j else 0 for i in range(10)] for j in range(10)]

print('Done. Setting targets...')
ann.targets = [[1 if i == j else 0 for i in range(10)] for j in range(10)]

print('Done. Building...')
ann.build()

print('Done. Training...')
ann.train()

print('Done. Saving...')
ann.save()

print('Done')
