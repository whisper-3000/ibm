# IBM Prueba Técnica Ejercicio 7
# Autor: Gonzalo Ferreira 
# API



# ----------------------------------------------------------------
# Imports
from flask import Flask, request
from schema import Schema
import knn
# ----------------------------------------------------------------



# ----------------------------------------------------------------
# Flask Setup
app = Flask(__name__)
# ----------------------------------------------------------------



# ----------------------------------------------------------------
# Auxiliary Functions

# Expected Schema
schema = Schema({
	'region':int,
	'tenure':int,
	'age':int,
	'marital': lambda x: x == 'married' or x == 'single',
	'address':int,
	'income': int,
	'ed':int,
	'employ':int,
	'retired':bool,
	'gender':bool,
	'reside':int
})

# Schema Error
def schemaError(jsonDict):
	keys = ['region', 'tenure', 'age', 'marital', 'address', 'income', 'ed', 'employ', 'retired', 'gender', 'reside']
	if len(jsonDict) != len(keys):
		return 'El número de campos no es correcto.'
	for key in keys:
		if key not in jsonDict:
			return f'El campo {key} no esta presente.'
	for key in jsonDict:
		if jsonDict[key] == '':
			return f'El campo {key} esta vacío.'
	if jsonDict[keys[3]] != 'single' and jsonDict[keys[3]] != 'married':
		return 'El campo marital solo admite valores de single o married.'
	return 'Un valor es del tipo incorrecto.'
	
# Format JSON values
def format_values(values):
	if values[3] == 'single':
		values[3] = 0
	else:
		values[3] = 1
	if values[8] == True:
		values[8] = 1
	else:
		values[8] = 0
	if values[9] == True:
		values[9] = 1
	else:
		values[9] = 0

# Check query parameters
def check_query(num_neighbors, distance_type):
	resNum = 0
	resDist = 0
	if num_neighbors == None:
		resNum = 10
	else:
		resNum = int(num_neighbors)
	if distance_type == None:
		resDist = 0
	else:
		resDist = int(distance_type)
	return resNum, resDist


# ----------------------------------------------------------------



# ----------------------------------------------------------------
# Endpoints
@app.route('/api/predict/custcat')
def predict_custcat():

	# Check if request is JSON
	if request.is_json:

		# Convert request into dictionary
		jsonDict = request.get_json()

		# Get query & load parameters
		num_neighbors, distance_type = check_query(request.args.get('num_neighbors'), request.args.get('distance_type'))
		
		# Check JSON validity
		if schema.is_valid(jsonDict):

			# Extract the values
			values = list(jsonDict.values())

			# Format the values
			format_values(values)

			# Get prediction
			prediction = knn.services[knn.predictCustcat(values, num_neighbors, distance_type)]

			# Return prediction & HTTP status
			return prediction, 200

		else:

			# If schema is wrong, return the error message & HTTP status
			return schemaError(jsonDict), 400

	else:

		# If file is not JSON
		return 'El archivo provisto no es de tipo JSON.', 400
# ----------------------------------------------------------------