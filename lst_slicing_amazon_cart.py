amazon_cart = [
  'computers',
  'notebooks',
  'sunglasses',
  'food',
  'pencils',
  'toys',
  'drinks',
]
print(amazon_cart[0::3])
print(amazon_cart)
amazon_cart[0]='tables'
print(amazon_cart)
new_amazon_cart= amazon_cart[:]
print(new_amazon_cart)
print(amazon_cart)

#list slicing
#amazon_cart = [1, 2, '3', True]
#amazon_cart[3]                 # True
#amazon_cart[1:]                # [2, '3', True]
#amazon_cart[:1]                # [1]
#amazon_cart[-1]                # True
#amazon_cart[::1]               # [1, 2, '3', True]
#amazon_cart[::-1]              # [True, '3', 2, 1]
#amazon_cart[0:3:2]             # [1, '3']
