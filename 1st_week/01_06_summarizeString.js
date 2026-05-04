function summarizeString(str) {
    let result = "";

    let target = str[0];
    let count = 1;
    for (let i = 1 ; i < str.length ; i++) {
        const char = str[i];
        if (target === char) {
            count += 1;
        } else {
            result += target + count.toString();
            target = char;
            count = 1;
        }
    }

    result += target + count.toString();

    return result;
}

console.log(summarizeString("acccdeee"))