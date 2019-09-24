$(document).ready(function(){
  $('#edit').click(function(){
    $('.edit-form').slideToggle(1000)
  })
  // $.ajax({
  //   url:'postgresql+psycopg2://stevemitto:p@127.0.0.1:5000/blog',
  //   success:function(data){
  //     console.log(data);
  //   }
  // });
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
        console.log(data)
        $(".comments").append(
        ' <div class="row" id="comment'+data.id+'>'+
            '<div class="col-md-2">'+
              // '{% if comment.user.profile_photo %}'+
              // '<img src="{{url_for("static" , filename=blog.user.profile_photo)}}"  width="100px" height="100px" alt="">'+
              // '{% else %}'+
              '<img src="static/photos/blog/def-prof.jpg" class="profile-p" width="50px" height="50px" alt="">'+
              // '{% endif%}'+
            '</div>'+
            '<div class="col-md-10">'+
              '<p>'+data.comment+'</p>'+
              '<small>'+data.username+'</small>'+
            '<a href="/blog/'+data.blog_id+'/delete/'+data.id+'/comment">'+
              '<small class="delete" style="float:right;cursor:pointer;">'+
                '<i class="fas fa-trash"></i>'+
              '</small>'+
            '</a>'+
            '</div>'+
          '</div>'
        )
      }
    }


    )

    console.log($("#comment").val());
    event.preventDefault()
  });
  $('ul#all-comments li>row>col-md-10>#delete').click(function(){
    console.log('clicked');
    var url=$(this).find('#delete-url').val()
    console.log(url);
    $.get(url,
      function(data){
        if(data.error){
          console.log(data.error);
        }
        if(data.success){
          console.log(data.success+"This one");
           $(this).slideUp(100)
         }
        })
    })
  // $(".delete").each(function(){
  //     $(this).click(function(){
  //     console.log('clicked');
  //     console.log($(".delete").children(".comment_id") .val());
  //     console.log(".delete"+$(".comment_id").val()+"");
  //     $.get('/blog/'+ $("#blog_id").val()+'/delete/'+ $(".comment_id").val()+'/comment',
  //       function(data){
  //         if(data.error){
  //           console.log(data.error);
  //         }
  //         if(data.success){
  //           console.log(data.success+"This one");
  //           // $("#comment"+$(".comment_id").val()+"").fadeOut(1000)
  //            $("#comment"+$(".comment_id").val()+"").slideUp(100)
  //
  //           // $("#comment"+$('.comment_id').val()+"").slideUp(1000)
  //         }
  //       });
  //     });
  // });
  $("#edit_comment").submit(function(event){
    $.post('/blog/edit/'+$('#blog_id').val(),
    {
      title:$("#title").val(),
      blog:$("#blog").val()
    },
    function(data){
      if (data.success){
        console.log("submited");
        console.log(data);
        $('.edit-form').slideUp()
        $("#blog_title").text(data.title).fadeIn(500)
        $("#blog_content").text(data.blog).fadeIn(500)
      }
    });
    event.preventDefault()
  })

  $("#upvote").click(function(){

    $.get('/blog/'+ $("#blog_id").val()+'/upvote',
    function(data){
      if(data.success){
        $("#upvote").css('color','blue')
        var vote = $("#upvote").text();
        $("#upvote").text(parseInt(vote)+1)
        console.log("success");
      }
      if(data.remove){
        $("#upvote").css('color','black')
        var vote = $("#upvote").text();
        $("#upvote").text(parseInt(vote)-1)

        console.log("remove");
      }
    });
  });
});
