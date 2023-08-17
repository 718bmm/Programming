const str = "Lama";
const reversed = reverseString(str);

console.log(reversed);

function reverseString(str) {
    let reversed = "";
    for (const rev of str) {
        reversed = rev + reversed;
    }
    return reversed
}

