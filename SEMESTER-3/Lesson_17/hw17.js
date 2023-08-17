
function reverseString(str) {
    let reversed = "";
    for (const rev of str) {
        console.log(reversed)
        reversed = rev + reversed;
    }
    return reversed
}
const str = "Havoi";
const reversed = reverseString(str);

console.log(reversed);
