# IBM Prueba Técnica Ejercicio 6
# Autor: Gonzalo Ferreira 



# ------------------------------------------------------------------------------------------------
# CONFIGURACIÓN
# A continuación se disponen de variables para configurar el funcionamiento del modelo.

# NUM_NEIGHBORS
# Define el número de vecinos a tomar en cuenta
NUM_NEIGHBORS = 15

# DISTANCE_TYPE
# Define la distancia a utilizar (0 = Euclidea, 1 = Manhattan)
DISTANCE_TYPE = 0

# INPUT_METHOD
# Define el tipo de input que recibe el método (0 = Dato por dato, 1 = Archivo CSV)
INPUT_METHOD = 1

# ------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------
# Imports
from math import sqrt
import csv
# ------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------
# Auxiliar

# Services
services = {
    '1': 'Servicio Básico',
    '2': 'Servicio Eléctronico',
    '3': 'Servicio Premium',
    '4': 'Servicio Total'
}

# CSV Format
def format(val):
    if ('.' in val):
        return int(val.split('.', 1)[0])
    else: 
        return int(val)

            
# ------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------
# KNN Algorigthm

# Distance
def distance(type, row1, row2):
    dist = 0.0
    if (type == 0):
        for i in range(len(row1) - 1):
            dist += (format(row2[i]) - format(row1[i]))**2;
        return sqrt(dist)
    elif (type == 1):
        for i in range(len(row1) - 1):
            dist += (format(row2[i]) - format(row1[i]))
        return dist
    else:
        raise Exception("Distancia no definida.")
    
# Neighbors
def getNeighbors(train, test, num_neighbors):
    distances = list()
    for train_row in train:
        dist = distance(DISTANCE_TYPE, train_row, test)
        distances.append((train_row, dist))
    distances.sort(key=lambda x: x[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors

# Prediction
def predictCustcat(train, test, num_neighbors):
    neighbors = getNeighbors(train, test, num_neighbors)
    outputVals = [row[-1] for row in neighbors]
    prediction = max(set(outputVals), key=outputVals.count)
    return prediction
# ------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------
# Main Script

# Fun Main
def main():
    
    # Read CSV DataSet
    data=[]
    file = open('teleCust1000t.csv', 'r')
    csvreader = csv.reader(file)
    header = next(csvreader)
    data = list(csvreader)
    file.close()

    # Prepare for Data Persistance
    file = open('teleCust1000t.csv', 'a', newline='')
    csvwriter = csv.writer(file, delimiter=',')

    # Check Input
    
    if (INPUT_METHOD == 0):

        # 1-1 User Input

        # Welcome message
        print('Bienvenido al estimador de servicio! \n')
    
        cont = 1

        while (cont):
            print('\n \n A continuación provea los datos del usuario:')
            region = input('Región:')
            tenure = input('Tenura:')
            age = input('Edad:')
            marital = input('Estado Civil:')
            address = input('Dirección:')
            income = input('Ingresos:')
            ed = input('ED:')
            employ = input('Employ:')
            retire = input('Retire:')
            gender = input('Género:')
            reside = input('Residencia:')

            # Predict cutscat
            user = [region, tenure, age, marital, address, income, ed, employ, retire, gender, reside]
            pred = predictCustcat(data, user, NUM_NEIGHBORS)
            user.append(pred)
            

            # Print prediction & validation
            print(f'\n\n El servicio predecido es: {services[pred]}')
            sel = input('\n\n Desea válidar este valor? (y/n)')
            while (sel != 'y') and (sel != 'n'):
                sel = input('Por favor, seleccionar un opción válida (y/n):')
            if (sel == 'y'):
                data.append(user)
                csvwriter.writerow(user)

            # Keep predicting?
            sel = input('\n\n Desea estimar el servicio para otro usuario? (y/n)')
            while (sel != 'y') and (sel != 'n'):
                sel = input('Por favor, seleccionar un opción válida (y/n):')
            if (sel == 'n'):
                cont = 0

        # Close File
        file.close()

        # End Message
        print('\n\n Hasta luego!')

    elif (INPUT_METHOD == 1):

        # Read CSV file
        print('\n Leyendo datos...')
        inputFile = open('input.csv', 'r')	
        csvreader = csv.reader(inputFile)
        next(csvreader)
        inputData = list(csvreader)
        inputFile.close()

        # Prepare for Writing CSV File
        outputFile = open('output.csv', 'w', newline='')
        outputWriter = csv.writer(outputFile, delimiter=',')

        # Predict Data
        print('\n Prediciendo datos...')
        for row in inputData:
            pred = predictCustcat(data, row, NUM_NEIGHBORS)
            row.append(pred)

        # Save Input Data
        print('\n Guardando datos...')
        outputWriter.writerow(header)
        for row in inputData:
            outputWriter.writerow(row)

        # Show Data
        print('\n Datos predecidos:')
        numUser = 1
        for row in inputData:
            print(f'Para el usuario número {numUser} se predijo: {services[row[-1]]}')
            numUser = numUser + 1

        # Validate Data & Persist
        sel = input('\n\n Desea válidar los valores predecidos? (y/n)')
        while (sel != 'y') and (sel != 'n'):
            sel = input('Por favor, seleccionar un opción válida (y/n):')
        if (sel == 'y'):
            for row in inputData:
                csvwriter.writerow(row)
    
    else:
        raise Exception("Método de entrada no definido.")

    return 0

# __MAIN__
if __name__ == '__main__':
    main()
# ------------------------------------------------------------------------------------------------