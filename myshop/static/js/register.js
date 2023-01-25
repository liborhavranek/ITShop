// visual validate email in registration form 👇


$('.costumer_email_check').hide();
$('#registration_email').on('input', function() {
  var email = $(this).val();
    // Get the CSRF token from the form
var csrf_token = $('input[name=csrf_token]').val();
  var emailRegEx = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
  if(!emailRegEx.test(email) && email.length > 10) {
    $('.costumer_email_check').text("Prosím zadejte platný formát emailové adresy.").show();
    $('.check-tag').css('visibility', 'hidden');  // hide the "check-tag" element
    return false;
  } else {
    $('.costumer_email_check').hide();
    $.ajax({
      url: '/check-email',
      method: 'POST',
      headers: { 'X-CSRFToken': csrf_token },
      data: {'email': email},
      success: function(data) {
        if (data == 'taken') {
          $('.costumer_email_check').text("Tento email je již zaregistrovaný v naší databázi.").show();
          $('.check-tag').css('visibility', 'hidden');  // hide the "check-tag" element
        } else {
          // show the "check-tag" element only if the email address is in a valid format and is not already in the database
          if (emailRegEx.test(email)) {
            $('.check-tag').css('visibility', 'visible');
          } else {
            $('.check-tag').css('visibility', 'hidden');
          }
        }
      }
    });
  }
});

////////////////////////////////////////////////////////////////////////////////////////////





// visual validate username in registration form 👇

$('.check-tag-username').css('visibility', 'hidden');
$('#registration_username').on('input', function(){
    var username =  $(this).val();
      // Get the CSRF token from the form
        var csrf_token = $('input[name=csrf_token]').val();
    $('.costumer_username_check').hide(); // hide the message element before making the AJAX request
    if (username.length === 0) { // check if the form is empty
        $('.check-tag-username').css('visibility', 'hidden');
        return; // exit the function if the form is empty
    }
    if (username.length < 6) { // check if the username is longer than 5 characters
        $('.check-tag-username').css('visibility', 'hidden');
        $('.costumer_username_check').text("Uživatelské jméno musí obsahovat alespoň 6 znaků.").show();
        return; // exit the function if the username is too short
    }
    $.ajax({
    url: '/check-username',
    method: 'POST',
    headers: { 'X-CSRFToken': csrf_token },
    data: {'username': username},
    success: function(data) {
        if (data == 'taken' ) {
            $('.costumer_username_check').text("Tento uživatel je již zaregistrovaný v naší databázi.").show();
            $('.check-tag-username').css('visibility', 'hidden');
        } else if (username.length >= 6) { // check if the username is longer than 5 characters
            $('.check-tag-username').css('visibility', 'visible');
        }
    }
    });
});


//////////////////////////////////////////////////////////////////////////////////////////



// -------------------phone number form ----------------------------------

$('#flag-selector').change(function() {
var selectedOption = $(this).val();
if (selectedOption == '+421') {
    $('.flag').attr('src', '/static/images/slovakia-flag.png');
} else if (selectedOption == '+420') {
    $('.flag').attr('src', "/static/images/czech-flag.png");
}
});



$('#registration_phone').on('input', function(){
var phone_number = $(this).val();
$('.check-tag-phone').css('visibility', 'hidden');
if (phone_number.length === 9){
    $('.check-tag-phone').css('visibility', 'visible');
}else{
    $('.check-tag-phone').css('visibility', 'hidden');
}
});



$('#registration_phone').on('keydown', function(event) {
// Allow only digits and the backspace key
if ((event.keyCode < 48 || event.keyCode > 57) && event.keyCode != 8 && (event.keyCode < 96 || event.keyCode > 105)) {
    event.preventDefault();
}
});


// ////////////////////////////////////////////////////////////////////////////



// ----------------------password number form --------------------------------------

var password_one;

$('.check-tag-password-one').css('visibility', 'hidden')
$('#Password1').on('input', function(){
password_one = $(this).val();
if (password_one.length < 8){
$('.costumer_password_one_check').text("Heslo musí být dlouhé alespoň 8 znaků.").show();
$('.check-tag-password-one').css('visibility', 'hidden');
}else{
    $('.costumer_password_one_check').text("Heslo musí být dlouhé alespoň 8 znaků.").hide();
    $('.check-tag-password-one').css('visibility', 'visible');
}
});


$('.check-tag-password-two').css('visibility', 'hidden');
$('#Password2').on('input', function(){
var password_two = $(this).val();
if (password_one === password_two){
    $('.check-tag-password-two').css('visibility', 'visible');
    $('.costumer_password_two_check').text("Hesla se musí shodovat.").hide();
}else{
    $('.check-tag-password-two').css('visibility', 'hidden');
    $('.costumer_password_two_check').text("Hesla se musí shodovat.").show();
}

});


// -------------------------------- faktura first name --------------------------------

$('.check-tag-faktura-first-name').css('visibility', 'hidden');
$('#faktura_first_name').on('input', function() {
var fakturaFirstName = $(this).val();
if (fakturaFirstName.length < 3){
    $('.check-tag-faktura-first-name').css('visibility', 'hidden');
    $('.costumer_faktura_first_name_check').text("Jméno musí být alespoň tři znaky dlouhé.").show();
}else{
    $('.check-tag-faktura-first-name').css('visibility', 'visible');
    $('.costumer_faktura_first_name_check').text("Jméno musí být alespoň tři znaky dlouhé.").hide();
}
});

// -----------------------------faktura last name ---------------------------------------


$('.check-tag-faktura-last-name').css('visibility', 'hidden');
$('#faktura_last_name').on('input', function() {
var fakturaLastName = $(this).val();
if (fakturaLastName.length < 2){
    $('.check-tag-faktura-last-name').css('visibility', 'hidden');
    $('.costumer_faktura_last_name_check').text("Jméno musí být alespoň dva znaky dlouhé.").show();
}else{
    $('.check-tag-faktura-last-name').css('visibility', 'visible');
    $('.costumer_faktura_last_name_check').text("Jméno musí být alespoň dva znaky dlouhé.").hide();
}
});


// -----------------------------faktura city name ---------------------------------------


$('.check-tag-faktura-city').css('visibility', 'hidden');
$('#faktura_city').on('input', function() {
var fakturaLastName = $(this).val();
if (fakturaLastName.length < 2){
    $('.check-tag-faktura-city').css('visibility', 'hidden');
    $('.costumer_faktura_city_check').text("Jméno musí být alespoň dva znaky dlouhé.").show();
}else{
    $('.check-tag-faktura-city').css('visibility', 'visible');
    $('.costumer_faktura_city_check').text("Jméno musí být alespoň dva znaky dlouhé.").hide();
}
});



// -----------------------------faktura ulice ---------------------------------------





$('.check-tag-faktura-zipcode').css('visibility', 'hidden');
function updateCheckTagVisibility2() {
var fakturaStreet = $('#faktura_street').val();
var fakturaZipcode = $('#faktura_zipcode').val();
if (fakturaStreet.length < 2 || fakturaZipcode.length < 5) {
    $('.check-tag-faktura-zipcode').css('visibility', 'hidden');
} else {
    $('.check-tag-faktura-zipcode').css('visibility', 'visible');
}
}

$('#faktura_street').on('input', function(){
var fakturaStreet = $(this).val();
if (fakturaStreet.length < 2){
    $('.costumer_faktura_street_check').text("Ulice musí mít alespoň dva znaky.").show();
}else{
    $('.costumer_faktura_street_check').text("Ulice musí mít alespoň dva znaky.").hide();
}
updateCheckTagVisibility2();
});

$('#faktura_zipcode').on('input', function(){
var fakturaZipcode = $(this).val();
if (fakturaZipcode.length < 5){
    $('.costumer_faktura_zipcode_check').text("5 čísel.").show();
}else{
    $('.costumer_faktura_zipcode_check').text("5 čísel.").hide();
}
updateCheckTagVisibility2();
});


$('#faktura_zipcode').on('keydown', function(event) {
// Allow only digits and the backspace key
if ((event.keyCode < 48 || event.keyCode > 57) && event.keyCode != 8 && (event.keyCode < 96 || event.keyCode > 105)) {
    event.preventDefault();
}
});


// -------------------------------- dodej first name --------------------------------

$('.check-tag-dodej-first-name').css('visibility', 'hidden');
$('#dodej_first_name').on('input', function() {
var dodejFirstName = $(this).val();
if (dodejFirstName.length < 3){
    $('.check-tag-dodej-first-name').css('visibility', 'hidden');
    $('.costumer_dodej_first_name_check').text("Jméno musí být alespoň tři znaky dlouhé.").show();
}else{
    $('.check-tag-dodej-first-name').css('visibility', 'visible');
    $('.costumer_dodej_first_name_check').text("Jméno musí být alespoň tři znaky dlouhé.").hide();
}
});

// -----------------------------dodej last name ---------------------------------------


$('.check-tag-dodej-last-name').css('visibility', 'hidden');
$('#dodej_last_name').on('input', function() {
var dodejLastName = $(this).val();
if (dodejLastName.length < 2){
    $('.check-tag-dodej-last-name').css('visibility', 'hidden');
    $('.costumer_dodej_last_name_check').text("Jméno musí být alespoň dva znaky dlouhé.").show();
}else{
    $('.check-tag-dodej-last-name').css('visibility', 'visible');
    $('.costumer_dodej_last_name_check').text("Jméno musí být alespoň dva znaky dlouhé.").hide();
}
});


// -----------------------------dodej company ---------------------------------------


$('.check-tag-dodej-company').css('visibility', 'hidden');
$('#dodej_company').on('input', function() {
var dodejCompany = $(this).val();
if (dodejCompany.length < 2){
    $('.check-tag-dodej-company').css('visibility', 'hidden');
    $('.costumer_dodej_company_check').text("Jméno firmy musí být alespoň dva znaky dlouhé.").show();
}else{
    $('.check-tag-dodej-company').css('visibility', 'visible');
    $('.costumer_dodej_company_check').text("Jméno firmy musí být alespoň dva znaky dlouhé.").hide();
}
});


// -----------------------------dodej city name ---------------------------------------


$('.check-tag-dodej-city').css('visibility', 'hidden');
$('#dodej_city').on('input', function() {
var dodejLastName = $(this).val();
if (dodejLastName.length < 2){
    $('.check-tag-dodej-city').css('visibility', 'hidden');
    $('.costumer_dodej_city_check').text("Jméno musí být alespoň dva znaky dlouhé.").show();
}else{
    $('.check-tag-dodej-city').css('visibility', 'visible');
    $('.costumer_dodej_city_check').text("Jméno musí být alespoň dva znaky dlouhé.").hide();
}
});


// -----------------------------dodej ulice ---------------------------------------



$('.check-tag-dodej-zipcode').css('visibility', 'hidden');

function updateCheckTagVisibility() {
var dodejStreet = $('#dodej_street').val();
var dodejZipcode = $('#dodej_zipcode').val();
if (dodejStreet.length < 2 || dodejZipcode.length < 5) {
    $('.check-tag-dodej-zipcode').css('visibility', 'hidden');
} else {
    $('.check-tag-dodej-zipcode').css('visibility', 'visible');
}
}

$('#dodej_street').on('input', function(){
var dodejStreet = $(this).val();
if (dodejStreet.length < 2){
    $('.costumer_dodej_street_check').text("Ulice musí mít alespoň dva znaky.").show();
}else{
    $('.costumer_dodej_street_check').text("Ulice musí mít alespoň dva znaky.").hide();
}
updateCheckTagVisibility();
});

$('#dodej_zipcode').on('input', function(){
var dodejZipcode = $(this).val();
if (dodejZipcode.length < 5){
    $('.costumer_dodej_zipcode_check').text("5 čísel.").show();
}else{
    $('.costumer_dodej_zipcode_check').text("5 čísel.").hide();
}
updateCheckTagVisibility();
});


$('#dodej_zipcode').on('keydown', function(event) {
// Allow only digits and the backspace key
if ((event.keyCode < 48 || event.keyCode > 57) && event.keyCode != 8 && (event.keyCode < 96 || event.keyCode > 105)) {
    event.preventDefault();
}
});

// -----------------------------dodej info ---------------------------------------

$('.check-tag-dodej-info').css('visibility', 'hidden');
$('#dodej_info').on('input', function() {
var dodejInfo = $(this).val();
if (dodejInfo.length < 2){
    $('.check-tag-dodej-info').css('visibility', 'hidden');
    $('.costumer_dodej_info_check').text("Jméno musí být alespoň dva znaky dlouhé.").show();
}else{
    $('.check-tag-dodej-info').css('visibility', 'visible');
    $('.costumer_dodej_info_check').text("Jméno musí být alespoň dva znaky dlouhé.").hide();
}
});


// -------------------phone number form ----------------------------------

$('#flag-dodej-selector').change(function() {
var selectedFlagOption = $(this).val();
if (selectedOption == '+421') {
    $('.flag').attr('src', '/static/images/slovakia-flag.png');
} else if (selectedOption == '+420') {
    $('.flag').attr('src', "/static/images/czech-flag.png");
}
});


$('#registration_dodej_phone').on('input', function(){
var dodejPhoneNumber = $(this).val();
$('.check-tag-phone').css('visibility', 'hidden');
if (dodejPhoneNumber.length === 9){
    $('.check-tag-dodej-phone').css('visibility', 'visible');
}else{
    $('.check-tag-dodej-phone').css('visibility', 'hidden');
}
});



$('#registration_dodej_phone').on('keydown', function(event) {
// Allow only digits and the backspace key
if ((event.keyCode < 48 || event.keyCode > 57) && event.keyCode != 8 && (event.keyCode < 96 || event.keyCode > 105)) {
    event.preventDefault();
}
});


// -------------------firma ico ----------------------------------


$('#registration_firma_ico').on('keydown', function(event) {
// Allow only digits and the backspace key
if ((event.keyCode < 48 || event.keyCode > 57) && event.keyCode != 8 && (event.keyCode < 96 || event.keyCode > 105)) {
    event.preventDefault();
}
});


$('.check-tag-firma-ico').css('visibility', 'hidden');
$('#registration_firma_ico').on('input', function(){
var firmaIco = $(this).val();
if (firmaIco.length === 8){
    $('.check-tag-firma-ico').css('visibility', 'visible');
    $('.costumer_firma_ico_check').text("IČO musí být dlouhé 8 čísel.").hide();
}else{
    $('.check-tag-firma-ico').css('visibility', 'hidden');
    $('.costumer_firma_ico_check').text("IČO musí být dlouhé 8 čísel.").show();
    if (firmaIco.length === 0){
        $('.costumer_firma_ico_check').text("IČO musí být dlouhé 8 čísel.").hide();
    }
}

});



// -------------------firma dic ----------------------------------


$('.check-tag-firma-dic').css('visibility', 'hidden');
$('#registration_firma_dic').on('input', function(){
var firmaDic = $(this).val();
if (firmaDic.length > 9){
    $('.check-tag-firma-dic').css('visibility', 'visible');
    $('.costumer_firma_dic_check').text("DIČ musí být dlouhé alespoň 10 čísel.").hide();
}else{
    $('.check-tag-firma-dic').css('visibility', 'hidden');
    $('.costumer_firma_dic_check').text("DIČ musí být dlouhé alespoň 10 čísel.").show();
    if (firmaDic.length === 0){
        $('.costumer_firma_dic_check').text("DIČ musí být dlouhé alespoň 10 čísel.").hide();
    }
}

});




// ------------------------------------Bankovni cislo -------------------------------------




$('#registration_firma_bank_acc').on('keydown', function(event) {
// Allow only digits and the backspace key
if ((event.keyCode < 48 || event.keyCode > 57) && event.keyCode != 8 && (event.keyCode < 96 || event.keyCode > 105)) {
    event.preventDefault();
}
});


$('#registration_firma_bank_number').on('keydown', function(event) {
// Allow only digits and the backspace key
if ((event.keyCode < 48 || event.keyCode > 57) && event.keyCode != 8 && (event.keyCode < 96 || event.keyCode > 105)) {
    event.preventDefault();
}
});




var firmaBankAcc;
var firmaBankNumber;

function showCheckBankTag() {
if (firmaBankNumber.length === 4 && firmaBankAcc.length > 5) {
$('.check-tag-firma-bank-acc').css('visibility', 'visible');
} else {
$('.check-tag-firma-bank-acc').css('visibility', 'hidden');
}
}

$('#registration_firma_bank_acc').on('input', function() {
firmaBankAcc = $(this).val();
if (firmaBankAcc.length > 5){
$('.costumer_firma_bank_acc_check').text("Zadejte alespoň 6 čísel").hide();
showCheckBankTag();
} else {
$('.costumer_firma_bank_acc_check').text("Zadejte alespoň 6 čísel").show();
if (firmaBankAcc.length === 0){
  $('.costumer_firma_bank_acc_check').text("Zadejte alespoň 6 čísel").hide();
}
}
});

$('#registration_firma_bank_number').on('input', function() {
firmaBankNumber = $(this).val();
if (firmaBankNumber.length > 3){
$('.costumer_firma_bank_number_check').text("4 čísla").hide();
showCheckBankTag();
} else {
$('.costumer_firma_bank_number_check').text("4 čísla").show();
if (firmaBankNumber.length === 0){
  $('.costumer_firma_bank_number_check').text("4 čísla").hide();
}
}
});

//---------------------------------specificky symbol --------------------------------------

$('#registration_firma_spec_symbol').on('keydown', function(event) {
// Allow only digits and the backspace key
if ((event.keyCode < 48 || event.keyCode > 57) && event.keyCode != 8 && (event.keyCode < 96 || event.keyCode > 105)) {
    event.preventDefault();
}
});

$('.check-tag-firma-spec-symbol').css('visibility', 'hidden');
$('#registration_firma_spec_symbol').on('input', function(){
var specSymbol = $(this).val();
if (specSymbol.length > 0){
    $('.check-tag-firma-spec-symbol').css('visibility', 'visible');
}else{
    $('.check-tag-firma-spec-symbol').css('visibility', 'hidden');
}
});