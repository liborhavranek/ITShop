$(function () {
    $(".alert").fadeOut(3000)
  });




// this script refresh page if i go back from edit brand, i need it refresh because if i edit it 
// and i will return back to add brand i need have fresh information in my table and that is best 
// way how do that r

  window.onunload = function() {
    location.reload();
  }
