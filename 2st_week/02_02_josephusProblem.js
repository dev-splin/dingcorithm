function josephusProblem(n, k) {
    const queue = Array.from({length: n }, (_, i) => i + 1);
    let curIndex = k - 1;
    const result = [];

    while (queue.length > 0) {
        const deleteNum = queue.splice(curIndex, 1);
        result.push(...deleteNum);
        curIndex = (curIndex + k - 1) % queue.length;
    }

    return `<${result.join(", ")}>`
}

console.log("정답: <3, 6, 2, 7, 5, 1, 4>:", josephusProblem(7,3))