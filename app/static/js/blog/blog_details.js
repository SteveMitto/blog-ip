$(document).ready(function(){
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
  $(".delete").click(function(){
    console.log('clicked');
    console.log($(".delete").children(".comment_id") .val());
    // console.log(".delete"+$("#comment_id").val()+"");
    // $.get('/blog/'+ $("#blog_id").val()+'/delete/'+ $("#comment_id").val()+'/comment',
    //   function(data){
    //     if(data.error){
    //       console.log(data.error);
    //     }
    //     if(data.success){
    //       $("#comment",$("#comment_id").val()).fadeOut(1000)
    //       console.log(data.success);
    //       $("#comment"+$('#comment_id').val()+"").slideUp(1000)
    //     }
    //   });
  });
});
