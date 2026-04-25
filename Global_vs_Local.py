a=10
def func():
    a=5
    print("Inside func, local a =", a)
func()
print("Outside func, global a =", a)
def modify_global():
    global a
    a=20
    print("Inside modify_global, modified global a =", a)
modify_global()
print("Outside modify_global, global a after modification =", a)