basket = [1,2,3,4,5]
print(len(basket))

new_list = basket.append(100)
print(basket)
print(new_list)
print()

basket = [1,2,3,4,5]
basket.append(100)
new_list = basket
print(basket)
print(new_list)
print()

basket = [1,2,3,4,5]
basket.insert(4, 100)
new_list = basket
print(basket)
print(new_list)
print()

basket = [1,2,3,4,5]
basket.insert(5, 100)
new_list = basket
print(basket)
print(new_list)
print()

basket = [1,2,3,4,5]
new_list = basket.insert(5, 100)
print(basket)
print(new_list)
print()

basket = [1,2,3,4,5]
new_list = basket.extend([100, 101])
print(basket)
print(new_list)
print()

basket = [1,2,3,4,5]
new_list = basket.extend([101])
print(basket)
basket.pop()
print(basket)
basket.pop()
print(basket)
basket.pop(0)
print(basket)
print()

basket = [1,2,3,4,5]
new_list = basket.extend([101])
print(basket)
basket.remove(4)
print(basket)
print()

basket = [1,2,3,4,5]
new_list = basket.remove(4)
print(basket)
print(new_list)
print()

basket = [1,2,3,4,5]
new_list = basket.pop(4)
print(basket)
print(new_list)
print()

basket = [1,2,3,4,5]
new_list = basket.clear()
print(basket)
print(new_list)
print()

