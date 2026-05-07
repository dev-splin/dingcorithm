function isExistingTargetNumberBinary(target, array) {
    let start = 0;
    let end = array.length - 1;

    while (start < end) {
        const mid = Math.floor((start + end) / 2)
        if (target === array[mid]) {
            return true;
        } else if (target < array[mid]) {
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }

    return false;
}

const findingTarget = 14;
const findingNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16];
const result = isExistingTargetNumberBinary(findingTarget, findingNumbers);

console.log(result);