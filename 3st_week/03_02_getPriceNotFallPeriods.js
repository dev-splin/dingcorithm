/**
 * 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 함수를 완성하세요.
prices = [1, 2, 3, 2, 3]
answer = [4, 3, 1, 1, 0]
 */
function main() {
    let prices = [1, 2, 3, 2, 3];
    
    console.log(getPriceNotFallPeriods(prices));
    
    console.log("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ");
    console.log(getPriceNotFallPeriods(prices));
    
    console.log("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ");
    console.log(getPriceNotFallPeriods([3, 9, 9, 3, 5, 7, 2]));
    
    console.log("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ");
    console.log(getPriceNotFallPeriods([1, 5, 3, 6, 7, 6, 5]));
}

function getPriceNotFallPeriods(prices) {
    const result = []
    const queue = [];
    for (const index in prices) {      
        queue.push(index);
    }

    while (queue.length > 0) {
        const curIndex = queue.shift();
        const tmpQueue = [...queue];
        let count = 0;

        for (const diffIndex of tmpQueue) {
            count += 1;

            if (prices[diffIndex] < prices[curIndex]) {
                break;
            }
        }

        result.push(count);
    }

    return result;
}


// Run the main function
main();