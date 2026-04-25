n=[1,2,3,4,5,"six ","seven  ",8.0,9.1,10.11,"Huzefa"]

def remove_item(item):
    try:
        n.remove(item)
        return f"Item {item} removed. Updated list: {n}"
    except ValueError:
        return f"Item {item} not found in the list."
    finally:
        "strip whitespaces from string elements"
        for i in range(len(n)):
            if isinstance(n[i], str):
                n[i] = n[i].strip()
        return f"Final list state: {n}"
# Example usage:
a=input("Enter item to remove: ")
if a.isdigit():
    print(remove_item(int(a)))
else:
    try:
        print(remove_item(float(a)))
    except ValueError:
        print(remove_item(a))