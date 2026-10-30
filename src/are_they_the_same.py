'''
Dados dos arreglos a, bescribe una función comp(a, b)(o compSame(a, b)) que compruebe si ambos arreglos tienen los mismos elementos,
con las mismas multiplicidades (la multiplicidad de un elemento es el número de veces que aparece).
"Iguales" significa, en este caso, que los elementos de bson los elementos de aal cuadrado,
independientemente del orden.
'''

def comp(array1, array2):
    
    if array1 is None or array2 is None:
        return False
    
    if len(array1) != len(array2):
        return False
    
    i = 0
    
    cuadrados = [x ** 2 for x in array1] 
    
    array2_ordenada = sorted(array2)
    
    for num in sorted(cuadrados):
        
        if num == array2_ordenada[i]:
            i += 1
        else:
            return False
    
    return True

'''
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
assert comp(a1, a2)

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
test.assert_equals(comp(a1, a2), False)
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
test.assert_equals(comp(a1, a2), False)
'''