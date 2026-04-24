/**
 * Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _ 를 반환하시오.
 */
function findNotRepeatingFirstCharacter(str) {
    const alphabets = Array.from({length: 26}, () => 0);
    const aAsciiCode = "a".charCodeAt();

    for (const char of str) {
        const index = char.charCodeAt() - aAsciiCode;
        alphabets[index] += 1;
    }

    let result = "_";
    for (const char of str) {
        const index = char.charCodeAt() - aAsciiCode;
        if (alphabets[index] === 1) {
            result = String.fromCharCode(index + aAsciiCode);

            break;
        }
    }

    return result;
}

console.log("정답 = d 현재 풀이 값 = " + findNotRepeatingFirstCharacter("abadabac"));
console.log("정답 = c 현재 풀이 값 = " + findNotRepeatingFirstCharacter("aabbcddd"));
console.log("정답 = _ 현재 풀이 값 = " + findNotRepeatingFirstCharacter("aaaaaaaa"));