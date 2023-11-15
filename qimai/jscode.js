const jsdom = require('jsdom');
const {JSDOM} = jsdom;
const dom = new JSDOM(`<!DOCTYPE html><body></body>`);
window = dom.window
z = window
d = 'xyz517cda96efgh'

function v(t) {
    t = z["encodeURIComponent"](t)['replace'](/%([0-9A-F]{2})/g, function (n, t) {
        return o('0x' + t)
    });
    try {
        return z['btoa'](t)
    } catch (n) {
        return z['Buffer']['from'](t)['toString']('base64')
    }
}

function o(n) {
    // t = "",
    //     [f2, s2, d2, m2, l2, v2, p2, s2, l2, d2, h2, y2][M](function (n) {
    //         t += z[g2](w2 + n)
    //     });
    // var t, e = t;
    return String.fromCharCode(n)
}

function h(n, t) {
    H = 0
    // t = t || u();
    for (var e = (n = n.split('')).length, r = t.length, a = "charCodeAt", i = H; i < e; i++) n[i] = o(n[i][a](H) ^ t[(i + 10) % r][a](H));
    return n.join('')
}


function getAnalysis(params, url_path) {
    var e, r = new Date() - (112050 || 0) - 1661224081041, a = [];
    Object.keys(params).forEach(function (n) {
        a.push(params[n])
    })
    a = a.sort().join('')
    a = v(a)
    a = (a += "@#" + url_path) + ("@#" + r) + ("@#" + 3)
    e = v(h(a, d))
    return e
}

params = {
    brand: "all",
    device: "iphone",
    country: "cn",
    genre: "6014",
    date: "2023-11-15",
    page: 2
}
url_path = '/rank/indexPlus/brand_id/1'
console.log(getAnalysis(params, url_path))