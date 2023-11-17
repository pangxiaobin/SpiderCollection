const crypto = require('crypto')

function a() {
    var array = new Uint8Array(16);
    crypto.randomFillSync(Buffer.from(array.buffer));
    return array
}


for (s = [], l = 0; l < 256; ++l)
    s.push((l + 256).toString(16).substr(1));

var u = function (e) {
    var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : 0
        ,
        n = (s[e[t + 0]] + s[e[t + 1]] + s[e[t + 2]] + s[e[t + 3]] + "-" + s[e[t + 4]] + s[e[t + 5]] + "-" + s[e[t + 6]] + s[e[t + 7]] + "-" + s[e[t + 8]] + s[e[t + 9]] + "-" + s[e[t + 10]] + s[e[t + 11]] + s[e[t + 12]] + s[e[t + 13]] + s[e[t + 14]] + s[e[t + 15]]).toLowerCase();
    // console.log(n)
    // if (!c(n))
    //     throw TypeError("Stringified UUID is invalid");
    return n
};

function getTraceId() {
    var b = a()
    return u(b)
}

console.log(getTraceId())