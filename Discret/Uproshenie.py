def sheffer(a, b):
    return not(a and b)

def pirsa(a, b):
    return not(a or b)

def con(a, b):
    return a and b

def dis(a, b):
    return a or b

def equa(a, b):
     return (a and b) or ((not a) and (not b))

# Проверка для всех возможных комбинаций значений x, y и z
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            print((dis(x,equa(y,z)))==(equa(dis(x,y),(dis(x,z)))))
