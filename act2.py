# Emploee In and Out
class Emp:
    def __init__(self):
        print('Employee class')
      
    def __del__(self):
        print("Destructor")
  
def objfun():
    print('Object created')
    obj = Emp()
    print('object function end')
    return obj
  
print('Calling function')
obj = objfun()
print('Program End')