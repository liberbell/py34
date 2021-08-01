first_names = ["elton", "bob", "jhon", "george", "eric"]
last_name = ["jhon", "mary", "lenon", "harison", "clapton"]

full_names = []
for last_names, first_names in zip(last_name, first_names):
    full_name = last_name + first_names
    full_names.append(full_name)

print(full_names)