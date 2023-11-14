const CryptoJs = require('crypto-js')

var Decrypt = function (t) {
    var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : ""
        , r = 'rewin-swhysc1234'
        , i = CryptoJs.enc.Utf8.parse(r)
        , o = CryptoJs.AES.decrypt(t, i, {
        mode: CryptoJs.mode.ECB,
        padding: CryptoJs.pad.Pkcs7
    });
    return CryptoJs.enc.Utf8.stringify(o).toString()
}

var data = 'K0FWJlJJ7hojwG3yOTA/NshaO9jUNRiTzZsxTWdFMAY/ZG/OkUckgKlcCVSiPWYBBnHW851tLCpZEOiC9TqUNaZ+s/MvAptvHr3rpl2XkvTXBpZtSpQ0eCQ0fOad9qoPFil9zDtpQoYmVP+DSEhuWbHvwnw9L0buqngWLc1GN9NB7LEew0NaU/5WwmLYEgn+9JCbXfWDtN0FDqy2MYfE7QtLLudX0rCO8whlyDc0/aJ89fdOHIfKhzmbCXo1Abdw1waWbUqUNHgkNHzmnfaqDxYpfcw7aUKGJlT/g0hIblmx78J8PS9G7qp4Fi3NRjfTQeyxHsNDWlP+VsJi2BIJ/n5qJpt9dgGT0c/zhXPuVEnMVJ9n77aVq4b5ceEM/mSDul0zdQd3w+RILJEbgxdWbtcGlm1KlDR4JDR85p32qg8WKX3MO2lChiZU/4NISG5Zse/CfD0vRu6qeBYtzUY300HssR7DQ1pT/lbCYtgSCf6vriChSD0Qqozla7KDErKHMeODhYtN6SL2Z+k+oJkLrMFZpDw2pqO4CmUJNg/NheHXBpZtSpQ0eCQ0fOad9qoPFil9zDtpQoYmVP+DSEhuWbHvwnw9L0buqngWLc1GN9NB7LEew0NaU/5WwmLYEgn+fZxCJM2ESYehnNmLx3iv6Hh8RkxdCH8hhDYTbjX+Q4pVryW7ZpNvPoEUz08CRqEK0hutKEDkds775B+9MZJhyMXOiBqkZnddHw4kLKLpPtoHwblz5rsebrrkKn6u0fo1VIPhMeTlL66YKVuA2l2Yyy+bU97LjD1w4miFW0DMl9fl+epicjd6RSbxS6k35FpuVa8lu2aTbz6BFM9PAkahCtIbrShA5HbO++QfvTGSYcjFzogapGZ3XR8OJCyi6T7aB8G5c+a7Hm665Cp+rtH6NVSD4THk5S+umClbgNpdmMtwbt7FsC6pCeJbJxpEfIgTkIJfwYe0gDLm1Hk+uk/RElWvJbtmk28+gRTPTwJGoQrSG60oQOR2zvvkH70xkmHIxc6IGqRmd10fDiQsouk+2gfBuXPmux5uuuQqfq7R+jVUg+Ex5OUvrpgpW4DaXZjL4WXKMKycbOfEXMc0yH5HB1+OLDHn/eCnk1kOUQpo1BxVryW7ZpNvPoEUz08CRqEK0hutKEDkds775B+9MZJhyMXOiBqkZnddHw4kLKLpPtoHwblz5rsebrrkKn6u0fo1VIPhMeTlL66YKVuA2l2YyxRwU54fM09E0BVi1WtwYVXufTMUQDZC+45BBIM1Q9HaVa8lu2aTbz6BFM9PAkahCtIbrShA5HbO++QfvTGSYcjFzogapGZ3XR8OJCyi6T7aB8G5c+a7Hm665Cp+rtH6NVSD4THk5S+umClbgNpdmMtF0XWEOlZKDxj2/4leQEAXi9vSCPlsKxeNwOMoMhxd3FWvJbtmk28+gRTPTwJGoQrSG60oQOR2zvvkH70xkmHIxc6IGqRmd10fDiQsouk+2gfBuXPmux5uuuQqfq7R+jVUg+Ex5OUvrpgpW4DaXZjLeZ4o194qy/UOX1rLo1FckWbc3sR/XxJsyjReibJtF2d6EGxSyg3ltg9evV41m0FZHpd8MRmJe5gLPFKD8dswbnokS+81XgB7NpqddeFdI9WX5gkx5035KXrRSjqmmkjQw2wlUdV3L33Be6wjYrw5Vo7Chg09/OMM3yFqcdGuOT4=\n'
console.log(Decrypt(data))