'''
Напишите программу для
проверки истинности утверждения 
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


'''
X = 1
Y = 1
Z = 1

left = not (X or Y or Z)
right = not X and not Y and not Z

if left == right:
   print("Равенство равно")
else:
    print("Равенство не равно")

