print("#########################")
print("# 배송료 계산 프로그램 #")
print("#########################")
price = int(input("상품의 가격을 입력하세요:  "))
if price > 2000:
    shipping_cost = 0
else:
    shipping_cost = 3000
print(shipping_cost)