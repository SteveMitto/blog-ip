$(document).ready(function(){
  console.log('/blog/'+ $("#blog_id").val()+'/save_comment');
  $("#add_comment").submit(function(event){
    $.post('/blog/'+ $("#blog_id").val()+'/save_comment',
    {
      comment:$("#comment").val()
    },
    function(data){
      if(data.error){
        console.log(data.error)
      }
      if(data.success){
        console.log(data.success)
      }
    }


    )

    console.log($("#comment").val());
    event.preventDefault()
  });
});
