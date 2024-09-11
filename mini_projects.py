total_count = {"aluminum": 135, "plastic": 102, "paper": 213}

#define a function sortItems that passes in a string of item tags
#and updates the total_count dictionary accordingly
def sortItems(itemString):
  for item in itemString:
    if item == "A":
      total_count["aluminum"] += 1
    elif item == "P":
      total_count["plastic"] += 1
    elif item == "R":
      total_count["paper"] += 1

#your code should pass the following test case
sortItems('AAPAARRRRPAAPPRRP')
print(total_count)