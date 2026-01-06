from main import print_hi

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

def find(menus, menu_order):
    start = 0
    end = len(menus)


    while start <= end:
        mid = (start + end) // 2

        if menus[mid] == menu_order:
            return True
        elif menus[mid] < menu_order:
            start = mid + 1
        elif menus[mid] > menu_order:
            end = mid - 1

    return False


def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    menus.sort()

    for order in orders:
        if not find(menus, order):
            return False

    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)