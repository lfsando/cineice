function validate() {
	var form = document.forms["login_form"];
	if(form.elements["username"].value == "")
	{
		var span_one = document.getElementById('username-errormessage')
		span_one.style.display = "inline-block";
		return false;
	}
	if(form.elements["password"].value == "")
	{
		var span_two = document.getElementById('password-errormessage')
		span_two.style.display = "inline-block";
		return false;
	}
}