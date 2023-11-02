from utils import *
        
def init():
    try:
        for x in blockList:
            print("["+ str(blockList.index(x)+1) + "] " + x[0])

        i = int(input("\n<i> Wybierz numer bryły\n» "))
        if(i not in range (1, len(blockList)+1)): raise ValueError
        block = blockList[i-1][1].value

        for x in operationList:
            print("["+ str(operationList.index(x)+1) + "] " + x.value)

        i = int(input("\n<i> Wybierz numer operacji\n» "))
        if(i not in range (1, len(operationList)+1)): raise ValueError
        operation = operationList[int(i-1)]

        for req in block.getRequirenments(operation): 
            value = float(input("Podaj " + req.value + "\n» "))
            block.setProps(req, value)

        print("\n<i> Obliczono: " + operation.value + " " + str(round(get(block, operation), 2)) + "\n")
        askAgain()
    except KeyboardInterrupt:
        return
    except:
        print("\n<!> Podano niepoprawne dane. Sprawdź, czy podana wartość jest poprawną wartością liczbową.\n")
        init()
        return

def askAgain():
    again = input("<?> Czy chcesz dokonać kolejnych obliczeń?\n» ")
    match again:
        case "tak":
            init()
        case "nie":
            return
        case _:
            askAgain()

init()