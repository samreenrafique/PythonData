import pandas
dict = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
print(dict)

table = pandas.DataFrame(dict)
table["Gender"] = ["Male","Male","Female","Male"]
table["eng_marks"] = [2,4,55,3]
table["urdu_marks"] = [1,2,55,3]
table["math_marks"] = [7,4,55,5]

table["total"] = table["eng_marks"] + table["urdu_marks"] + table["math_marks"]
table["percentage"] = (table["total"]*100)/300

print(table["Name"].loc[1:3])
# Save Data frames to CSV
table.to_csv("dataconvert.csv")
# No Index
table.to_csv("dataconvert.csv",index=False)
# No Column Name
table.to_csv("dataconvert.csv",index=False,header=False)

# Del Column
# del table["Age"]
# table.pop("Age")
print(table[["Name","percentage"]])

