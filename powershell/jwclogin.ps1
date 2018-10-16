#
# Script.ps1
#
Function login(){
	#登录函数
	$loginUrl="http://zhjw.scu.edu.cn/j_spring_security_check"
	$loginData=@{
		"j_username"=Read-Host("输入学号");
        "j_password"= Read-Host("输入密码");
        "j_captcha1"="error"
	}
	$r=Invoke-RestMethod -Uri $loginUrl -Method Post -Body $loginData
	while($True){
		if($r.contains("URP综合教务系统首页")){
			Write-Host "登录成功"
			break
		}
		else{
			Write-Host "登录失败，尝试再次登录"
			$r=Invoke-RestMethod -Uri $loginUrl -Method Post -Body $loginData
		}
	}
}
Function getToken(){
	#获取token函数
	
}
