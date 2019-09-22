$(function(){
    $("#add_post").submit(function(event){
    $.post(
    '/blog/add_blog',
    {
    title :$("#title").val(),
    blog_img: $("#blog_img").val(),
    blog: $("#blog").val()
    },
    function(data){
      if (data.error){
        console.log(data.error)
      }
      if (data.success){
        window.location.replace('/blog/home')
      }
    });
      event.preventDefault()
    });
  });
