ls = [1, 33, 4, 5, 6]
ls1 = ["Hello", "World"]
ls2 = [1, None, 4, 5, 33.34]
ls3 = [True , 3.14, 32,]
print(ls.index(1))
print(ls1[1])
print(ls2[0])
print(ls3[-1])
print(ls2[:2])

#list methods and modifications
shopping_list = []
shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.insert(0,"eggs")
print(shopping_list)
print(f"items needed: {len(shopping_list)}")
if "milk" in shopping_list:
    print("Don't forget the milk")

shopping_list.remove("milk")
shopping_list.pop()
print(shopping_list)
ls.sort()
print(ls)
ls.reverse()
print(ls)
print(len(ls))

#nested list
# A simple 2D list (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
my_matrix = [[1, 2], [3, 4], [5, 6]]
rows = 3
cols = 4
mynew_matrix = []
for _ in range(rows):
    mynew_matrix.append([])  # Create a new inner list for each row
    for _ in range(cols):
        mynew_matrix[0].append(0)  # Initialize with some values
# fill in the rows and cols with desired values

print(mynew_matrix)

grades = [
    ["Sahil",78,87,89,],
    ["Rajesh", 86, 55, 78],
    ["saad",87,67,87]
]
alice_grades = grades[0],[1]
alice_avg = sum(alice_grades) / len(alice_grades)
print(alice_grades)
print(alice_avg)

