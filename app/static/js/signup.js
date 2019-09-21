$(function(){
  $("#signup").submit(function(event){
    $.post ( '/signup',
    {
      username:$('#username').val(),
      email:$("#email").val(),
      password:$("#password").val(),
      confirm_password:$("#confirm_password").val()
    },
    function(data){
      if(data.error){
        console.log(data.error);
      }
      if(data.username_error){
        $("#username_error").text(data.username_error).show().delay(5000).fadeOut(1000)
        $('#username').css('border',"1px solid red")
      }else{
          $('#username').css('border',"1px solid green")
      }
      if(data.email_error){
        $("#email_error").text(data.email_error).show().delay(5000).fadeOut(1000)
        $('#email').css('border',"1px solid red")
      }else {
        $('#email').css('border',"1px solid green")
      }
      if(data.password_error){
        $("#password_error").text(data.password_error).show().delay(5000).fadeOut(1000)
        $("#confirm_password").css('border','1px solid red')
      }else {
        $("#confirm_password").css('border','1px solid green')
      }
      if(data.success){
        window.location.replace('/login')
      }
    });
    event.preventDefault()
  });
});
