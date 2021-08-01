last_names = ["elton", "bob", "jhon", "george", "eric"]
first_names = ["jhon", "marley", "lennon", "harrison", "clapton"]

full_names = []
for last_name, first_name in zip(last_names, first_names):
    print(last_name + " " + first_name + "!")


for i in range(len(last_names)):
    print(last_names[i] + " " + first_names[i] + "!")

for i in range(len(last_names)):
    print("ID ", i, "rd member is" + " " + last_names[i] + "!")

for index, last_name in enumerate(last_names):
    # print("ID ", index, "rd member is" + " " + last_names[index] + "!. by enumerate")
    print(f"ID {index}rd number is {last_names[index]}. by enumerate.")