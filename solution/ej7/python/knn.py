# IBM Prueba Técnica Ejercicio 6
# Autor: Gonzalo Ferreira 
# MODULE FILE



# ------------------------------------------------------------------------------------------------
# Imports
from math import sqrt
import csv
# ------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------
# Auxiliar

# Services
services = {
    1: 'Servicio Básico',
    2: 'Servicio Eléctronico',
    3: 'Servicio Premium',
    4: 'Servicio Total'
} 

# CSV Format
def formatCSV(csvList):
    for row in csvList:
        for i in range(len(row)):
            if ('.' in row[i]):
                row[i] = int(row[i].split('.', 1)[0])
            else: 
                row[i] = int(row[i])
    return csvList      
# ------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------
# Training Dataset

# Load Training Dataset
def load_training_dataset():
    train=[]
    datasetFile = open('teleCust1000t.csv', 'r')
    csvreader = csv.reader(datasetFile)
    next(csvreader)
    train = list(csvreader)
    train = formatCSV(train) 
    datasetFile.close()
    return train

# Persist Prediction
def persist_prediction(row):
    datasetFile = open('teleCust1000t.csv', 'a', newline='')
    datasetWriter = csv.writer(datasetFile, delimiter=',')
    datasetWriter.writerow(row)
    datasetFile.close()

# ------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------
# KNN Algorigthm

# Distance
# Retorna la distancia entre los dos registros dados.
# type : 0 = Euclidean, 1 = Manhattan
# row1 & row2 : Registros a comparar
def distance(type, row1, row2):
    dist = 0.0
    if (type == 0):
        for i in range(len(row1) - 1):
            dist += (row2[i] - row1[i])**2;
        return sqrt(dist)
    elif (type == 1):
        for i in range(len(row1) - 1):
            dist += (row2[i] - row1[i])
        return dist
    else:
        raise Exception("Distancia no definida.")
    
# Neighbors
# Retorna los K vecinos mas cercanos al registro dado dentro del data set de entrenamiento provisto.
# train : Dataset de entrenamiento
# row : Registro para el cual se quiere encontrar los vecinos mas cercanos
# num_neighbors : Número de vecinos deseados
def getNeighbors(train, row, num_neighbors, distance_type):
    distances = list()
    for train_row in train:
        dist = distance(distance_type, train_row, row)
        distances.append((train_row, dist))
    distances.sort(key=lambda x: x[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors

# Prediction
# Predice el valor custcat del registro dado.
# train : Dataset de entrnamiento
# row : Registro para el cual se quiere encontrar los vecinos mas cercanos
# num_neighbors : Número de vecinos deseados
def predictCustcat(row, num_neighbors, distance_type):
    train = load_training_dataset()
    neighbors = getNeighbors(train, row, num_neighbors, distance_type)
    outputVals = [n[-1] for n in neighbors]
    prediction = max(set(outputVals), key=outputVals.count)
    return prediction
# ------------------------------------------------------------------------------------------------