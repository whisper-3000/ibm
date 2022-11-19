# IBM Prueba Técnica Ejercicio 6
# Autor: Gonzalo Ferreira 
# TEST FILE



# ------------------------------------------------------------------------------------------------
# Imports
import csv
import knn
# ------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------
# Main Script

# Fun Main
def main():

    # Welcome message
    print('Bienvenido al estimador de servicio! \n')

    # Request input method
    while True:
        input_method = input('\nIndique a continuación el método de entrada (0 = dato por dato, 1 = archivo CSV input.csv): ')
        if (input_method == '0' or input_method == '1'):
            break
        else:
            print('\nPor favor, ingrese un valor aceptable.')

    # Request variables
    num_neighbors = input('\nIndiruqe la cantidad de vecinos a considerar: ')
    distance_type = input('\nIndiruqe el tipo de distancia a utilizar (0 = Euclidiana, 1 = Manhattan): ')
    num_neighbors = int(num_neighbors)
    distance_type = int(distance_type)

    # 1-1 User Input
    if (input_method == '0'):

        # Loop prediction input
        while (True):

            # Request user values
            print('\n\nA continuación provea los datos del usuario:')
            region = input('Región (int): ')
            tenure = input('Tenura (int): ')
            age = input('Edad (int): ')
            marital = input('Estado Civil (0 = single, 1 = married): ')
            address = input('Dirección (int): ')
            income = input('Ingresos (int): ')
            ed = input('ED (int): ')
            employ = input('Employ (int): ')
            retire = input('Retire (0 = false, 1 = true): ')
            gender = input('Género (0 = hombre, 1 = mujer): ')
            reside = input('Residencia (int): ')

            # Construct user row
            user = [int(region), int(tenure), int(age), int(marital), int(address), int(income), int(ed), int(employ), int(retire), int(gender), int(reside)]

            # Get prediction
            pred = knn.predictCustcat(user, num_neighbors, distance_type)

            # Append prediction to user row
            user.append(pred)

            # Print prediction & validation
            print(f'\n\n El servicio predecido es: {knn.services[pred]}')
            while True:
                sel = input('\nDesea guardar este valor para futuro uso (y/n): ')
                if (sel == 'y'):
                    knn.persist_prediction(user)
                    break
                elif (sel == 'n'):
                    break
                else:
                    print('\nPor favor, ingresar un valor aceptable.')

            # Keep predicting?
            while True:
                sel = input('\nDesea continuar prediciendo? (y/n): ')
                if (sel == 'y' or sel == 'n'):
                    break
                else:
                    print('\nPor favor, ingresar un valor aceptable.')

            # Check choice
            if (sel == 'n'):
                break

    # CSV File Input
    elif (input_method == '1'):

        # Read CSV file
        print('\n Leyendo datos...')
        inputFile = open('input.csv', 'r')	
        csvreader = csv.reader(inputFile)
        header = next(csvreader)
        inputData = list(csvreader)
        inputData = knn.formatCSV(inputData)
        inputFile.close()

        # Prepare for Writing CSV File
        outputFile = open('output.csv', 'w', newline='')
        outputWriter = csv.writer(outputFile, delimiter=',')

        # Predict Data
        print('\n Prediciendo datos...')
        for row in inputData:
            pred = knn.predictCustcat(row, num_neighbors, distance_type)
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
            print(f'Para el usuario número {numUser} se predijo: {knn.services[row[-1]]}')
            numUser = numUser + 1

        # Validate Data & Persist
        while True:
            sel = input('\nDesea guardar los valores para futuro uso (y/n): ')
            if (sel == 'y'):
                for user in inputData:
                    knn.persist_prediction(user)
                break
            elif (sel == 'n'):
                break
            else:
                print('\nPor favor, ingresar un valor aceptable.')
    
    else:

        # If input_method value is not found
        raise ValueError("Método de entrada no definido.")

    # End Message
    print('\n\n Hasta luego!')

    return 0

# __MAIN__
if __name__ == '__main__':
    main()
# ------------------------------------------------------------------------------------------------