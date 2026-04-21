function findMaxOccurredAlphabet (str) {
    const alphabets = Array.from({length: 26 }, () => 0);
    const aAscii = "a".charCodeAt();
    
    for (const char of str) {
        if (char === " ") {
            continue;
        }

        const index = char.charCodeAt() - aAscii;
        alphabets[index] += 1;
    }

    let maxCount = 0;
    let maxIndex = 0;
    for (const i in alphabets) {
        if (alphabets[i] > maxCount) {
            maxIndex = i;
            maxCount = alphabets[i];
        }
    }

    return String.fromCharCode(Number(maxIndex) + aAscii);
}

console.log("정답 = i 현재 풀이 값 = " + findMaxOccurredAlphabet("hello my name is dingcodingco"));
console.log("정답 = e 현재 풀이 값 = " + findMaxOccurredAlphabet("we love algorithm"));
console.log("정답 = b 현재 풀이 값 = " + findMaxOccurredAlphabet("best of best youtube"));