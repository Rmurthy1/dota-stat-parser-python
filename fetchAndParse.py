import json

# for working with json http://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file-in-python
# going to use postgres on heroku maybe http://initd.org/psycopg/
	# maybe, its a pain in the ass maybe




def main():
	with open("V001.json") as data_file:
		data = json.load(data_file)



	print (data["result"]["results_remaining"])
	for match in data["result"]["matches"]:
		print (match["match_id"])


main()
