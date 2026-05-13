function isAvailableToOrder(menus, orders) {
    const set = new Set(menus);
    for (const menu of menus) {
        set.add(menu);
    }

    for (const order of orders) {
        if (!set.has(order)) return false;
    }

    return true;
}

// Main execution
const shopMenus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"];
const shopOrders = ["오뎅", "콜라", "만두", "치킨"];

const result = isAvailableToOrder(shopMenus, shopOrders);
console.log(result);