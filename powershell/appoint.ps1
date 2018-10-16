#
# Script.ps1
#
Function login(){
	#登录
	#获取登录时的token
	$url="https://scusport.com/login"
	$Script:userAgent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"

	$r=Invoke-RestMethod -Uri $url -UserAgent $userAgent -Method Get -SessionVariable fb
	$Script:session=$fb
	$reg='value="(?<alp>\w+?)"'
	if($r -match $reg){
		$Script:token=$Matches.alp
	}
	$loginData=@{
            "_token"=$token;
            "scuid"=Read-Host("输入学号");
            "password"=Read-Host("输入密码")
    }
	$r=Invoke-RestMethod -Uri $url -Method Post -Body $loginData -UserAgent $userAgent -WebSession $Script:session
	while($true){
		if($r.contains("欢迎")){
			Write-Host "登录成功"
			break
		}
		else{
			Write-Host "登录失败尝试再次登录"
			$r=Invoke-RestMethod -Uri $url -Method Post -Body $loginData -UserAgent $userAgent -WebSession $Script:session
		}
	}
}

Function choose(){
	$url="https://scusport.com/reserve/create"
	$schid = Read-Host("输入场次号")
    $postdata = @{
            '_token'= $token;
            'schid'=$schid;
            'subject[0]'= 'bmi';
            'subject[1]'='vtc';
            'subject[2]'= 'spt';
            'subject[3]'= 'slj';
            'subject[4]'= 'sar';
            'subject[5]'= 'lrm';
            'subject[6]'= 'plp';
            'tos'='on'
    }
	$r=Invoke-RestMethod -Uri $url -Method Post -Body $postdata -UserAgent $Script:userAgent -WebSession $Script:session
	while($true){
		if($r.contains("成功")){
			Write-Host "选择成功"
			break
		}
		else{
			Write-Host "选择失败，尝试下一次选择"
			$r=Invoke-RestMethod -Uri $url -Method Post -Body $postdata -UserAgent $Script:userAgent -WebSession $Script:session
		}
	}
}
login
choose
pause
pause