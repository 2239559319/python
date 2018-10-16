Function match(){
	$str='<input type="hidden" name="_token" value="xXSMrV9jbj5Nk1OM2stbDzYsu1vir6ogsmqNHlKl">'
	$reg='value="(?<alp>\w+?)"'
	if($str -match $reg){
		Write-Host $Matches.alp
	}
}
match