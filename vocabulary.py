import json
from difflib import SequenceMatcher, get_close_matches
data = json.load(open("data.json"))

def meaning(input_text):
    input_text = input_text.lower()  #all the time input gets converted to lower case character bcz most of the keys are in the lower case.
    if input_text in data:
        return "".join(data[input_text])
    elif input_text.title() in data:
         return "".join(data[input_text.title()])
    elif input_text.upper() in data:  #to handle the Acronyms in data set.
        return "".join(data[input_text.upper()])

    elif len(get_close_matches(input_text, data.keys())) >0 :
        yn = input("Did you searched (%s) instead ? If Yes then Y otherwise No ie N " % get_close_matches(input_text, data.keys())[0])

        if yn == "Y":
            return "".join(data[get_close_matches(input_text, data.keys())[0]])
        elif yn == "N":
            return "Word doesnt exist."
        else:
            return "Sorry! Unable to catch your word"
    else:
          return "Plese enter the valid word"
         
input_text = input("Enter the word that you want to find the meaning:")
print(meaning(input_text))

