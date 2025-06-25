print("---Set Operation---")

set_a = {10,20,30,40,50,45,50}
set_b = {40,50,60,70,80}
list_a = [10,20,30,40,50]

coverted_list = list(set_a)
print(coverted_list)

print(f"set a: {set_a}")
print(f"set b: {set_b}")




converted_set = set(list_a)
print(converted_set)

union_set = set_a.union(set_b)
print(f"union of set a and b : {union_set}")

intersection_set = set_a.intersection(set_b)
print(f"intersection of set a and b : {intersection_set}")

difference_set = set_a.difference(set_b)
print(f"difference set a and b : {difference_set}")



      