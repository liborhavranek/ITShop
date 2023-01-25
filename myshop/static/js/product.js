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
          var newRow = '<tr><th scope="row">' + data.id + '</th>' +
                       '<td>' + data.brand + '</td>' +
                       '<td>' + data.date_created + '</td>' +
                       '<td><a class="btn btn-info btn-sm" href="/editbrand/' + data.id + '">Upravit značku</a></td>' +
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