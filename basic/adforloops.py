last_names = ["elton", "bob", "jhon", "george", "eric"]
first_names = ["jhon", "marley", "lennon", "harrison", "clapton"]

full_names = []
for last_name, first_name in zip(last_names, first_names):
    full_name = last_name + " " + first_name
    full_names.append(full_name)

print(full_names)