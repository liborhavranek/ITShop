// ------------------------------add brand -----------------------------------------------

$('#add-brand-form').on('submit', function(event) {
    event.preventDefault();
    var formData = $(this).serialize();
    $.ajax({
      url: '/addbrand',
      type: 'POST',
      data: formData,
      success: function(data) {
        // Insert the flash message into the DOM
        $('.messages').html(
          '<div class="alert alert-' + data.flash_message[0][0] + '">' + data.flash_message[0][1] + '</div>'
        );
        // Fade out the message and then hide it
        $('.messages .alert').fadeOut(4000).delay(4000).hide(0);
        // If the brand was added successfully, insert it into the table
        if (data.flash_message[0][0] === "success") {
          // Create the new row for the table
          var date = new Date(data.date_created);
            var formattedDate = date.toLocaleString();
          var newRow = '<tr><th scope="row">' + data.id + '</th>' +
                       '<td>' + data.brand + '</td>' +
                       '<td>' + formattedDate+ '</td>' +
                       '<td>' + 'NE' + '</td>' +
                       '<td>' + '</td>' +
                       '<td><a class="btn btn-info btn-sm" href="/editbrand/' + data.id + '">Upravit</td>' +
                       '<td><a id="brand-' + data.id + '" data-id="' + data.id + '" class="btn btn-danger btn-sm delete-brand-button"href="/deletecategory/' + data.id + '">Smazat</a></td>';
          // Append the new row to the table body
          $('#brands-list tbody').append(newRow);
        }
        // Reset the form
        $('#add-brand-form')[0].reset();
      },
      error: function(data) {
        // Insert the flash message into the DOM
        $('.messages').html(
          '<div class="alert alert-' + data.flash_message[0][0] + '">' + data.flash_message[0][1] + '</div>'
        );
        // Fade out the message and then hide it
        $('.messages .alert').fadeOut(4000).delay(4000).hide(0);
      }
    });
  });

// -----------------------------edit brand --------------------------------------------

  $('#edit-brand-form').on('submit', function(event) {
    // gain id from hidden input in form 
    var id = $(this).find('input[name="value_id_for_jquery"]').val();
    // browser dont refresh
    event.preventDefault(); 
    var formData = $(this).serialize();
    $.ajax({
      url: '/editbrand/' + id,
      type: 'POST',
      data: formData,
      success: function(data) {
        // Insert the flash message into the DOM
        $('.messages').html(
          '<div class="alert alert-' + data.flash_message[0][0] + '">' + data.flash_message[0][1] + '</div>'
        );
        // Fade out the message and then hide it
        $('.messages .alert').fadeOut(4000).delay(4000).hide(0);
        // If the brand was added successfully, edit brand name 
        if (data.flash_message[0][0] === "success") {
          $('.edit-brand-name').text(data.brand);
          $('.edit-brand-name-two').text(data.brand);
          // Reset the form
        $('#edit-brand-form')[0].reset();
        }
      },
      error: function(data) {
        // Insert the flash message into the DOM
        $('.messages').html(
          '<div class="alert alert-' + data.flash_message[0][0] + '">' + data.flash_message[0][1] + '</div>'
        );
        // Fade out the message and then hide it
        $('.messages .alert').fadeOut(4000).delay(4000).hide(0);
      }
    });
  });


// -------------------------------------delete brand----------------------------------------

  $('#brands-list tbody').on('click', '.delete-brand-button', function(e) {
    e.preventDefault();
  
    // Get the brand ID
    var id = $(this).data('id');
  
    // Get the CSRF token from the form
    var csrf_token = $('input[name=csrf_token]').val();
  
    // Send a DELETE request to the server
    $.ajax({
      url: '/deletebrand/' + id,
      type: 'DELETE',
      headers: { 'X-CSRFToken': csrf_token },
      success: function(result) {
        // Remove the brand from the table
        $('#brand-' + id).closest('tr').remove();
        // Insert the success message into the DOM
        $('.messages').html(
          '<div class="alert alert-success">' + result.message + '</div>'
        );
        // Fade out the message and then hide it
        $('.messages .alert').fadeOut(4000).delay(4000).hide(0);
      }
    });
  });
  

// ---------------------------------------------add category------------------------------------

  $('#add-category-form').on('submit', function(event) {
    event.preventDefault();
    var formData = $(this).serialize();
    $.ajax({
      url: '/addcategory',
      type: 'POST',
      data: formData,
      success: function(data) {
        // Insert the flash message into the DOM
        $('.messages').html(
          '<div class="alert alert-' + data.flash_message[0][0] + '">' + data.flash_message[0][1] + '</div>'
        );
        // Fade out the message and then hide it
        $('.messages .alert').fadeOut(4000).delay(4000).hide(0);
        // If the category was added successfully, insert it into the table
        if (data.flash_message[0][0] === "success") {
            var date = new Date(data.date_created);
            var formattedDate = date.toLocaleString();
          // Create the new row for the table
          var newRow = '<tr><th scope="row">' + data.id + '</th>' +
                       '<td>' + data.category + '</td>' +
                       '<td>' + formattedDate+ '</td>' +
                       '<td>' + 'NE' + '</td>' +
                       '<td>' + '</td>' +
                       '<td><a class="btn btn-info btn-sm" href="/editcategory/' + data.id + '">Upravit</a></td>' +
                       '<td><a id="category-' + data.id + '" data-id="' + data.id + '" class="btn btn-danger btn-sm delete-category-button"href="/deletecategory/' + data.id + '">Smazat</a></td>';
          // Append the new row to the table body
          $('#categories-list tbody').append(newRow);
        }
        // Reset the form
        $('#add-category-form')[0].reset();
      },
      error: function(data) {
        // Insert the flash message into the DOM
        $('.messages').html(
          '<div class="alert alert-' + data.flash_message[0][0] + '">' + data.flash_message[0][1] + '</div>'
        );
        // Fade out the message and then hide it
        $('.messages .alert').fadeOut(4000).delay(4000).hide(0);
      }
    });
  });

// ---------------------------------edit category -------------------------------------

  $('#edit-category-form').on('submit', function(event) {
    var id = $(this).find('input[name="value_id_for_jquery"]').val();
    // browser dont refresh
    event.preventDefault(); 
    var formData = $(this).serialize();
    $.ajax({
      url: '/editcategory/' + id,
      type: 'POST',
      data: formData,
      success: function(data) {
        // Insert the flash message into the DOM
        $('.messages').html(
          '<div class="alert alert-' + data.flash_message[0][0] + '">' + data.flash_message[0][1] + '</div>'
        );
        // Fade out the message and then hide it
        $('.messages .alert').fadeOut(4000).delay(4000).hide(0);
        // If the category was added successfully, edit category name 
        if (data.flash_message[0][0] === "success") {
          $('.edit-category-name').text(data.category);
          $('.edit-category-name-two').text(data.category);
          // Reset the form
        $('#edit-category-form')[0].reset();
        }
      },
      error: function(data) {
        // Insert the flash message into the DOM
        $('.messages').html(
          '<div class="alert alert-' + data.flash_message[0][0] + '">' + data.flash_message[0][1] + '</div>'
        );
        // Fade out the message and then hide it
        $('.messages .alert').fadeOut(4000).delay(4000).hide(0);
      }
    });
  });
  



// POZORu funkce delete musím delegovat přes categories list tbody a nemuzu 
// rovnou  zavolat delete=category=button protože potom, když pridam kategorii 
// a pak ji hned smazu server mi nepovoli metodu a vyhodi chybu 


$('#categories-list tbody').on('click', '.delete-category-button', function(e) {
    e.preventDefault();
  
    // Get the category ID
    var id = $(this).data('id');
  
    // Get the CSRF token from the form
    var csrf_token = $('input[name=csrf_token]').val();
  
    // Send a DELETE request to the server
    $.ajax({
      url: '/deletecategory/' + id,
      type: 'DELETE',
      headers: { 'X-CSRFToken': csrf_token },
      success: function(result) {
        // Remove the category from the table
        $('#category-' + id).closest('tr').remove();
        // Insert the success message into the DOM
        $('.messages').html(
          '<div class="alert alert-success">' + result.message + '</div>'
        );
        // Fade out the message and then hide it
        $('.messages .alert').fadeOut(4000).delay(4000).hide(0);
      }
    });
  });
  
  