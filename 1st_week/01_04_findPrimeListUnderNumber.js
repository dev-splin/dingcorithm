/**
 * Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오. 
 * 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
 */
function findPrimeListUnderNumber(input) {
    const result = [];
    for (let num = 2 ; num <= input ; ++num) {
        let isPrime = true;
        for (const prime of result) {
            if (prime * prime <= num && num % prime === 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) result.push(num);
    }

    return result;
}

const input = 20;
const result = findPrimeListUnderNumber(input);
console.log(result);