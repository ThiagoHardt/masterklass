$(document).ready(function () {

    $("#signupForm").change(function () {
        var username = $("#id_username").val()
        var email = $("#id_email").val()
        var password1 = $("#id_password1").val()
        var password2 = $("#id_password2").val()
  
        $.ajax({
          url: '/purchase/pre_validade_user/',
          data: {
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2
          },
          dataType: 'json',
          success: function (data) {
            if (data.usernameNotValid) {
                $("#error_username").insertAfter($("#id_username"));
                $("#id_username").addClass('is-invalid');
                $("#error_username").show();
            }
            else{
                $("#error_username").hide();
                $("#id_username").removeClass('is-invalid');
            }
            if (data.emailNotValid) {
                $("#error_email").insertAfter($("#id_email"));
                $("#id_email").addClass('is-invalid');
                $("#error_email").show();
            }
            else{
                $("#error_email").hide();
                $("#id_email").removeClass('is-invalid');
            }
            if (data.passwordMatch) {
                $("#id_password1").removeClass('is-invalid');
                $("#id_password2").removeClass('is-invalid');
                $("#error_password1").hide();
                $("#error_password2").hide();            
            }
            else{
                $("#error_password1").insertAfter($("#id_password1"));
                $("#error_password2").insertAfter($("#id_password2"));
                $("#id_password1").addClass('is-invalid');
                $("#id_password2").addClass('is-invalid');
                $("#error_password1").show();
                $("#error_password2").show();
            }
            if (data.emailNotValid == false && data.usernameNotValid == false && data.passwordMatch){
                $('#submit-button').attr('disabled', false);
            }
          }
        });
    });
    
    // ############################ Stripe ##############################################

    var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
    var clientSecret = $('#id_client_secret').text().slice(1, -1);
    var stripe = Stripe(stripePublicKey);
    var elements = stripe.elements();
    var style = {
        base: {
            color: '#000',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#aab7c4'
            }
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    };
    var card = elements.create('card', {
        style: style
    });
    card.mount('#card-element');

    // Handle realtime validation errors on the card element
    card.addEventListener('change', function (event) {
        var errorDiv = document.getElementById('card-errors');
        if (event.error) {
            var html = `
                <span class="icon small" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span class="small">${event.error.message}</span>
            `;
        } 
    });
    // Handle form submit
    var form = document.getElementById('signupForm');

    form.addEventListener('submit', function (ev) {
        ev.preventDefault();
        card.update({
            'disabled': true
        });
        $('#submit-button').attr('disabled', true);
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card
            }
        }).then(function (response) {
            if (response.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon small" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span class="small">${response.error.message}</span>
                `;
                $(errorDiv).html(html);
                card.update({
                    'disabled': false
                });
                $('#submit-button').attr('disabled', false);
            } else {
                if (response.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    });
});
