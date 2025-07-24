import time
options = ["HOLE", "DEPTH PLANT", "DEPTH ACTUAL", "START", "FINISH", "TOTAL", "SOFT", "MEDIUM", 
           "HARD", "RONGGA", "BASAH/KERING", "PERCSN", "RITTION", "FEED","FLUSHING","REMARKS"]

# cel = [[71,196], [106,196], [106,208], [71,208]]
cels = [71, 196, 108, 208]
cel = cels.copy()

x = [96, 124, 154, 190, 216, 246, 274, 298, 338, 364, 402, 434, 470, 
     508, 536, 580, 706]
y = [188, 205]

count = 1

with open("cor2.txt", "w") as sya:
    for i in range(3):
        for k in range(15):               # ← loop dalam
            sya.write(f"{count}: "+ "{")
            count += 1
            for j in range(len(options)):
                sya.write(f'"{options[j]}": {x[j], y[0], x[j+1], y[1]}, ')
            y[0] += 17
            y[1] += 17
            sya.write("},"+"\n")
        y[0] -= 1
        y[1] -= 1


