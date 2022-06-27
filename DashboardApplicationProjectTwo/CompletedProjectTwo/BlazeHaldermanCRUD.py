from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
	""" CRUD operations for Animal collection in MongoDB """

	def __init__(self, username, password):
		# Initializing the MongoClient. This helps to 
        	# access the MongoDB databases and collections. 
        	self.client = MongoClient('mongodb://%s:%s@localhost:46571/AAC' % (username, password))
        	# where xxxxx is your unique port number
        	self.database = self.client['AAC']


	# Method for creating document(s) in the database
	def create(self, data):
		"""Method for creating document(s) given a document or set of documents. ex. ({"key" : "value"})"""
		if data is not None:
			if self.database.animals.insert(data): # data should be dictionary
				return True
			else:
				return False
		else:
			raise Exception("data parameter is empty, please correct and try again")
			
	# Method for getting document(s) from the database
	def read(self, query):
		"""Method for reading/getting document(s) given a query. ex. ({"key": "value"})"""
		if type(query) is dict or query is "{}":	
			cursor = self.database.animals.find(query, {'_id':False}) # query should be a dictionary with query params
			#if self.data.count() == 0:
				#raise Exception("Cursor is empty, no data found")
			return cursor
		else:
			raise Exception("Data parameter for query is incorrect, must be a dictionary")

	# method for updating document(s) in the database
	def update(self, query, value_pair):
		"""Method for updating a document(s) fields. ex. 
({"key" : "value"},{$set: {"key": "value"}})"""
		
		if type(query) is dict:
			try:
				return self.database.animals.update_many(query, value_pair)
			except:
				raise Exception("Error updating specified query with value pair, please try again")	

	# method for deleting document(s) in the database
	def delete(self, query):
		"""Method for deleting document(s) from the collection. ex. ({"key" : "value"})"""
		
		if type(query) is dict:
			if query == "{}":
				print("You have entered a dangerous query ({}). This will result in deleting the entire dataset, would you like to continue? : yes | no")
				val = input("Yes or No: ")
				if val.lower() == "yes":
					print("Please confirm your entry once more for deletion of the dataset : Yes | No")
					if val.lower() == "yes":
						return self.database.animals.delete_many(query)
					else:
						return
				else:
					return
			else:
						
				try:
					return self.database.animals.delete_many(query)
				except:
					raise Exception("Error deleting specified query with key value, please try again")	




"""shelter = AnimalShelter('aacuser', 'aacuser46571')
cured = shelter.read({})
print(cured)
"""
"""status = shelter.create({"age_upon_outcome" : "4 weeks", "animal_id" : "A10239BSD", "animal_type": "Dido", "breed" : "Bronco"})
print("Result has been created: " + str(status))
data = shelter.read({"animal_id" : "A10239BSD"})

print("BEFORE UPDATE")
for x in data:
	print(x)
	print("\n")

updated = shelter.update({"animal_type": "Dido"}, {"$set": {"animal_type" : "Giraff"}})
print("Amount updated: " + str(updated.modified_count))
data = shelter.read({"animal_id" : "A10239BSD"})

print("AFTER UPDATE")
for x in data:
	print(x)
	print("\n")

result = shelter.delete({"animal_type" : "Giraff"})
print("Amount deleted: " + str(result.deleted_count))

print("AFTER DELETE, EXPECTING AN EXCEPTION TO BE THROWN")
data = shelter.read({"animal_type" : "Giraff"})"""

"""
doc = shelter.read({"animal_type" : "Dog", "name" : "Lucy"})
for x in doc:
	print(x)
	print("\n")
print(type(doc))"""
