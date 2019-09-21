$(function(){
  $("#login").on('submit', function(event){
    $.post(
      '/login',
      {
        username: $("#username").val(),
        password: $("#password").val()
      },
      function(data){
        if(data.error){
          $("#errors").text(data.error).fadeIn(1000).delay(5000).fadeOut(500)
          console.log(data.error);
        }
        if(data.success){
          window.location.replace('/')
        }
      });
    event.preventDefault()
  });
});
