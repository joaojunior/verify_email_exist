$("#send").click(function(){
	$('#send').attr("disabled", "disabled");
	showMessage("Checking if email exists...")
	$.ajax({
		headers: {
			'Accept': 'application/json',
			'Content-Type': 'application/json'
		},
		dataType: 'json',
		contentType: 'application/json',
		url: "/check",
		context: document.body,
	    method: "POST",
	    data: $('#form_check_email').serializeJSON(),
	}).done(function(data){
		$('#send').removeAttr("disabled");
		showMessage(data.message)
	});
});

function showMessage(message){
	$("#email").parent(".form-group").addClass("has-error");
	$("#email").parent(".form-group").children('.help-block').remove();
	$("#email").parent(".form-group").append("".concat('<span class="help-block">', message ,'</span>'));
};
