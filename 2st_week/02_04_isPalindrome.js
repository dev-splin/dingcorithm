function isPalindrome(str) {
    if (str.length <= 1) {
        return true;
    }

    const start = str[0];
    const end = str.at(-1);

    if (start !== end) {
        return false;
    }
    
    return isPalindrome(str.substring(1, str.length - 1));
}

// Main execution
const input = "abcba";

console.log(isPalindrome(input));