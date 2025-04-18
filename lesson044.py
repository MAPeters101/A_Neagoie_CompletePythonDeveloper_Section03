
string = 'helllooo'
print(string[0:2:1])

greet = 'hello'
#greet[0] = 'z'

print()

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
print(amazon_cart)
print(amazon_cart[0:2])
print(amazon_cart[0::2])

amazon_cart[0] = 'laptop'
print(amazon_cart)
print(amazon_cart[0:3])
print(amazon_cart[1:3])
print()

new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
print()

new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
print()

new_cart = amazon_cart
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
print()


