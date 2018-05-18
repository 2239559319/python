//一些公用的方法
import Vue from "vue";
import md5 from "crypto-js/md5";
import { pathName,serverUrl } from "config.js";
//发起网络请求
function emitAjax(obj){
    const app_secret="6d3121b650e42855976d0f70dd2048e4";
    const app_key="cgsoft";
    const timestamp = Date.parse(new Date());
    const Authorization = localStorage.getItem("Authorization")?localStorage.getItem("Authorization"):"";
    const token_type = localStorage.getItem("token_type")?localStorage.getItem("token_type"):"";
    let headers = {
        'Authorization':token_type+" "+Authorization
    };
    //清除不要的字段
    try {
        delete obj.data.gmtModified;
        delete obj.data.gmtCreate;
    } catch (error) {}
    //合并参数
    const opt = Object.assign({},{
        path:"", //请求地址
        type:"GET", //请求方式
        data:null,
        dataType:"common", //文件上传还是普通数据交互
        success:function(result){   //code200执行的函数
            console.log('数据返回成功',result)
        },
        error:function(result){ //不是code200 执行的函数
            console.log('数据返回失败',result);
        }
    },obj);
    const sign = setSign(app_secret,app_key,timestamp,opt.path,opt.data);
    const url = serverUrl+opt.path;
    //合并请求头
    if(opt.headers){
        headers = Object.assign({},headers,opt.headers);
    }
    //ajax默认参数
    let ajaxOpt = {
        url,
        type:opt.type,
        headers,
        success:function(result){
            successFn(result,opt.success,opt.error,opt.path);
        },
        error:function(error){
            alert("网络请求有误，请刷新页面！");
            console.error(error);
            obj.error&&obj.error();
        }
    };
    if(opt.dataType=='file'){
        //上传文件 opt.data 是FormData类型
        opt.data.append("app_key",app_key);
        opt.data.append("timestamp",timestamp);
        opt.data.append("sign",sign);
        ajaxOpt.data = opt.data;
        ajaxOpt.cache = false;
        ajaxOpt.processData = false;
        ajaxOpt.contentType = false;
    }else{
        //普通数据上传
        const data = Object.assign({},{
            app_key,
            timestamp,
            sign
        },opt.data);
        //删除和修改 需要拼接url的方式传参
        if(opt.type == "PUT" || opt.type == "DELETE"){
            //put delete 方法拼接url
            let urlString = "?";
            for (const key in data) {
                if (data.hasOwnProperty(key)) {
                    const value = data[key];
                    if(value !== '' && value !== null && value !== undefined){
                        urlString += key+"="+encodeURIComponent(value)+"&";
                    }
                }
            }
            urlString = urlString.substring(0,urlString.length-1);
            const urls = ajaxOpt.url + urlString ;
            ajaxOpt.url = urls;
        }else{
            ajaxOpt.data = data;
        }

    }
    //支持跨域
    $.support.cors=true;
    $.ajax(ajaxOpt);
}
//get方式组织url
function setRequestUrl(obj){
    const app_secret="6d3121b650e42855976d0f70dd2048e4";
    const app_key="cgsoft";
    const timestamp = Date.parse(new Date());
    let opt = Object.assign({},obj);
    const sign = setSign(app_secret,app_key,timestamp,opt.path,opt.data);
    opt.data = Object.assign({},opt.data,{
        app_key,
        timestamp,
        sign
    })
    //清除不要的字段
    try {
        delete opt.data.gmtModified;
        delete opt.data.gmtCreate;
    } catch (error) {}
    //合并参数
    const url = serverUrl+opt.path;
    let urlString = "?";
    for (const key in opt.data) {
        if (opt.data.hasOwnProperty(key)) {
            const value = opt.data[key];
            if(value !== '' && value !== null && value !== undefined){
                urlString += key+"="+encodeURIComponent(value)+"&";
            }
        }
    }
    urlString = urlString.substring(0,urlString.length-1);
    return url + urlString;
}

//生存密钥
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

function successFn(result,succ,err,path){
    let resultObj = result;
    if(typeof result == "string"){
        resultObj = JSON.parse(resultObj);
    }
    switch (resultObj.code) {
        case 200:
            succ && succ(resultObj.data);
            break;
        case 401:
            console.error(path+"接口没有权限");
            alert(result.message);
            if(window.location.pathname == "/"&&window.confirm("是否强制退出系统，重新登录？")){
                delLocalData();
                window.location.href = pathName+"/login";
            }else{
                window.location.href = pathName+"/";
            }
            break;
        case 408:
            delLocalData();
            window.location.href = pathName+"/login";
        default:
            alert(resultObj.message);
            err&&err(resultObj);
            break;
    }
}
//判断权限
function checkPermission(menu,path){
    let bool = true;
    for (let index = 0; index < menu.length; index++) {
        const menuItem = menu[index];
        //如果访问地址在菜单中
        if(pathName+menuItem.url == path){
            bool = false;
        }
        //如果访问地址不在菜单中，且有下级 则继续循环下级
        if(bool&&menuItem.childs&&menuItem.childs.length>0){
            bool = checkPermission(menuItem.childs,path);
        }
        if(!bool){break;}
    }
    return bool;
}

function setLocalData(data){
    localStorage.setItem("Authorization",data.token.access_token);
    localStorage.setItem("token_type",data.token.token_type);
    localStorage.setItem("leftMenu",JSON.stringify(data.menus));
    localStorage.setItem("user",JSON.stringify({
        username:data.username,
        name:data.name,
        gender:data.gender,
        role:data.role
    }));
}

function delLocalData(){
    localStorage.removeItem("Authorization");
    localStorage.removeItem("token_type");
    localStorage.removeItem("leftMenu");
    localStorage.removeItem("user");
    localStorage.removeItem("weak");
}

export {emitAjax,setLocalData,delLocalData,checkPermission,setRequestUrl};


// WEBPACK FOOTER //
// ./src/assets/common.js