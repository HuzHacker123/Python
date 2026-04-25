lst=list(input("Enter elements of the list separated by commas: ").split(","))
def second_highest(lst):
    unique_lst=list(set(lst))
    unique_lst.sort()
    if len(unique_lst)<2:
        return "Not enough unique elements"
    else:
        return unique_lst[-2]
print("The second highest element is:",second_highest(lst))