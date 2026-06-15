/**
 * Q. 
다음과 같이 숫자로 이루어진 배열이 두 개가 있다. 
하나는 상품의 가격을 담은 배열이고, 하나는 쿠폰을 담은 배열이다. 
쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다. 
이 때, 최대한 할인을 많이 받는다면 얼마를 내야 하는가?
단, 할인쿠폰은 한 제품에 한 번씩만 적용 가능하다.
 */
function main() {
    let shop_prices = [30000, 2000, 1500000];
    let user_coupons = [20, 40];
    
    console.log("정답 = 926000 / 현재 풀이 값 = " + 
        getMaxDiscountedPrice([30000, 2000, 1500000], [20, 40]));
    
    console.log("정답 = 485000 / 현재 풀이 값 = " + 
        getMaxDiscountedPrice([50000, 1500000], [10, 70, 30, 20]));
    
    console.log("정답 = 1550000 / 현재 풀이 값 = " + 
        getMaxDiscountedPrice([50000, 1500000], []));
    
    console.log("정답 = 1458000 / 현재 풀이 값 = " + 
        getMaxDiscountedPrice([20000, 100000, 1500000], [10, 10, 10]));
}

function getMaxDiscountedPrice(prices, coupons) {
    prices.sort((a,b) => b - a);
    coupons.sort((a,b) => b - a);

    let min = 0;
    let priceIndex = 0;
    let couponIndex = 0;

    while (priceIndex < prices.length && couponIndex < coupons.length) {
        const finalPrice = Math.floor(prices[priceIndex++] * (100 - coupons[couponIndex++]) / 100);
        min += finalPrice;
    }

    while (priceIndex < prices.length) {
        min += prices[priceIndex++];
    }

    return min
}

//                  p_i
// [1500000, 30000, 2000, ]
//      c_i
// [40, 20]
// 1500000 * 40 % 금액
// 30000 * 20% 금액
// 2000 원가

// Run the main function
main();