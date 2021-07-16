
  $(document).ready(function(){
    $('.sidenav').sidenav();
  });

  $(document).ready(function(){
    $('select').formSelect();
  });

  $(document).ready(function(){
    $('select').formSelect();
  });

  $(document).ready(function(){
    $('select').formSelect();
  });

  const formData = new FormData();
formData.append("file", fileInput.files[0]);
const options = {
method: "POST",
body: formData,
};