const palindrome = function(x) {
    console.log(x);
    const s = x.toString();
    console.log(s);
    const t = s.split("").reverse().join("")
    console.log(t); 
    return s === t; 
};

console.log(palindrome(-121)); 