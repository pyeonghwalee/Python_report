price = int(input("상품의 가격을 입력하세요.:  "))

if price > 100000:
    shipping_cost = 0
else:
    if price > 2000:
        shipping_cost = 3000
    else:
        shipping_cost = 5000
        
print("배송료는", shipping_cost, "입니다.")
