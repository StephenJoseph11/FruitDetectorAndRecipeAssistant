

def construct_recipe_request(fruit_counts, num_options=3):
    if not fruit_counts:  # Check if the dictionary is empty
        return "It looks like I don't have any fruits to work with. Please provide some fruits and their counts."

    fruits = []
    for fruit, count in fruit_counts.items():
        if count > 1:
            fruit_text = f"{count} {fruit}s"  # Plural form
        else:
            fruit_text = f"{count} {fruit}"   # Singular form
        fruits.append(fruit_text)#

    if len(fruits) == 1:
        user_message = "I have " + fruits[0]
    elif len(fruits) == 2:
        user_message = "I have " + " and ".join(fruits)
    else:
        user_message = "I have " + ", ".join(fruits[:-1]) + ", and " + fruits[-1]
    if num_options==1:
        end_message = f" option and it's recipe."
    else:
        end_message = f" options and their recipes."
    user_message += (f". What are some tasty and healthy recipes"
                    f" I could make with these ingredients? Give me {num_options}"
                    + end_message)
    return user_message

