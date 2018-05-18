'''
function setSign(app_secret,app_key,timestamp,path,opt){
    let keyArray = [];
    let signString = app_secret+path;
    if(typeof opt == "object"){
        for (const key in opt) {
            if (opt.hasOwnProperty(key)) {
                keyArray.push(key);
            }
        }
        keyArray.sort();
        for (let index = 0; index < keyArray.length; index++) {
            const key = keyArray[index];
            if(opt[key] !== '' && opt[key] !== null && opt[key] !== undefined){
                signString += key+opt[key];
            }
        }
    }
    signString += timestamp+" "+app_secret;
    return md5(signString).toString();
}
'''
import time
import hashlib
app_secret="6d3121b650e42855976d0f70dd2048e4"
app_key="cgsoft"
path = "/api/login"
timestamp="1526621836000"
data={
    "username":"2017141461249",
    "password":"461249"
}
signString = app_secret+path
signString+="password"+"461249"+"username"+"2017141461249"
signString += timestamp+" "+app_secret
h1=hashlib.md5()
h1.update(signString.encode("utf-8"))
sign=h1.hexdigest()
print(sign)
print(type(sign))