let count = 0;

function getResult(reamainNums, curNum, target ) {
    if (reamainNums.length === 0) {
        if (curNum === target) count += 1;

        return;
    }

    const reamainNum = reamainNums[0];
    const plusNum = curNum + reamainNum;
    const minusNum = curNum - reamainNum;

    const nextRemainNums = reamainNums.slice(1);

    getResult(nextRemainNums, plusNum, target);
    getResult(nextRemainNums, minusNum, target);
}

function getCountOfWaysToTargetByDoingPlusOrMinus(array, target) {
    getResult(array, 0, target);

    return count;
}



// Main execution
const numbers = [1, 1, 1, 1, 1];
const targetNumber = 3;

console.log(getCountOfWaysToTargetByDoingPlusOrMinus(numbers, targetNumber));  // 5를 반환해야 합니다!