
b = [1,2,3,4,5]

def bk(a_solution,depth):
    for elem in b:
        a_solution.append(elem)
        if isValid(a_solution):
            if isSolution(a_solution):
                print(a_solution)
            else:
                bk(a_solution,depth+1)
        a_solution.pop()
                
            
def isValid(vector):
    if len(vector) == 1:
        return True
    elif len(vector) == 2:
        if vector[0] == vector[1]:
            return False
        return True
    elif len(vector) == 3:
        if vector[0] == vector[1]:
            return False
        elif vector[0] == vector[2]:
            return False
        elif vector[1] == vector[2]:
            return False
        return True
    else:
        return False

def isSolution(vector):
    if len(vector) == 3:
        return True
    return False


a = []

bk(a,0)

