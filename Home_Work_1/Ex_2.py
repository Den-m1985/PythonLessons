
'''
Напишите программу для
проверки истинности утверждения 
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''

def Calculate (X, Y, Z):
   left = not (X or Y or Z)
   right = not X and not Y and not Z

   if left == right:
      print("Равенство равно")
   else:
      print("Равенство не равно")

Calculate(1, 1, 1)

