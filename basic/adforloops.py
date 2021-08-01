last_names = ["elton", "bob", "jhon", "george", "eric"]
first_names = ["jhon", "marley", "lennon", "harrison", "clapton"]

full_names = []
for last_name, first_name in zip(last_names, first_names):
    full_name = last_name + " " + first_name
    full_names.append(full_name)

print(full_names)

for i in range(len(last_names)):
    print(last_names[i] + " " + first_names[i])

# for index, last_name in enumerate(last_names):
#     print("ID is ", index, )