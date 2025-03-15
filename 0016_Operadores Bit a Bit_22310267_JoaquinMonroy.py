#Operadores bit a bit casos

#Operador AND
a=12
b=10
resultado=a&b # 1100 & 1010 = 1000
print("AND",resultado, "\n")

#Operador OR
a=12
b=10
resultado=a|b # 1100 | 1010 = 1110
print("OR",resultado, "\n")

#Operador XOR
a=12
b=10
resultado=a^b # 1100 ^ 1010 = 0110
print("XOR",resultado, "\n")

#Operador NOT
a=12
resultado=~a # ~1100 = 0011
print("NOT",resultado, "\n")

#Operador Desplazamiento a la izquierda
a=12
resultado=a<<2 # 1100 << 2 = 110000
print("Desplazamiento a la izquierda",resultado, "\n")

#Operador Desplazamiento a la derecha
a=12
resultado=a>>2# 1100 >> 2 = 11
print("Desplazamiento a la derecha",resultado, "\n")

#Operador Desplazamiento a la derecha con signo
a=-12
resultado=a>>2# 1100 >> 2 = 11
print("Desplazamiento a la derecha con signo",resultado, "\n")

#Operador Desplazamiento a la derecha con ceros
a=-12
resultado=a>>2# 1100 >> 2 = 11
print("Desplazamiento a la derecha con ceros",resultado, "\n")

#Operador Desplazamiento a la derecha con ceros
a=12
resultado=a>>2# 1100 >> 2 = 11
print("Desplazamiento a la derecha con ceros",resultado, "\n")

#Combinacion de operadores
a=12
b=10
resultado=(a&b) | (a^b) # 1100 & 1010 = 1000 | 1100 ^ 1010 = 0110
print("Combinacion de operadores",resultado, "\n")

#Usar >> y & juntos
a=12
b=10    
resultado=(a>>2) & b # 1100 >> 2 = 11
print("Usar >> y & juntos",resultado, "\n") 

#Usar << y | juntos
a=12
b=10
resultado=(a<<2) | b # 1100 << 2 = 110000
print("Usar << y | juntos",resultado, "\n")
