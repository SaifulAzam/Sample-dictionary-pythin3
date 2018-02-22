import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(value):
	value = value.lower()

	if value in data:
		return data[value]
	elif len(get_close_matches(value, data.keys())) > 0:
		yn = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(value, data.keys())[0])
		yn = yn.upper()
		if yn == "Y":
			return data[get_close_matches(value, data.keys())[0]]
		elif yn == "N":
			return "The word doesn't exist. Please double check it."
		else:
			return "We didn't understand your word."
	else:
		return "The word doesn't exist. Please doble check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)
