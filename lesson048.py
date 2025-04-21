basket = ['a','b','c','d','e','d']
print(basket.sort())
print(basket)


basket = ['a','x','b','c','d','e','d']
basket.sort()
print(basket)
print()

basket = ['a','x','b','c','d','e','d']
print(basket)
print(sorted(basket))
print(basket)
print()

basket = ['a','x','b','c','d','e','d']
new_basket = basket[:]
new_basket.sort()
print(new_basket)
print(basket)
print()

basket = ['a','x','b','c','d','e','d']
new_basket = basket.copy()
new_basket.sort()
print(new_basket)
print(basket)
print()

basket = ['a','x','b','c','d','e','d']
basket.reverse()
print(basket)
print()

basket = ['a','x','b','c','d','e','d']
basket.sort()
basket.reverse()
print(basket)
print()




