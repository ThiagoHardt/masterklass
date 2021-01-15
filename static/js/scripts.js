$(document).ready(function() {
    $('.carousel').carousel({
        interval: 3000
    });
    $('.toast').toast({
        delay: 3000,
    });
    $('.toast').toast('show')

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
    var card = elements.create('card', {style: style});
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
            $(errorDiv).html(html);
            $('#submit-button').attr('disabled', true);
        } else {
            errorDiv.textContent = ''
            $('#submit-button').attr('disabled', false);
        }
    });
    // Handle form submit
    var form = document.getElementById('signupForm');

    form.addEventListener('submit', function(ev) {
        ev.preventDefault();
        card.update({ 'disabled': true});
        $('#submit-button').attr('disabled', true);
        stripe.confirmCardPayment(clientSecret, {payment_method: {card: card}
        }).then(function(response) {
            if (response.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon small" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span class="small">${response.error.message}</span>`;
                $(errorDiv).html(html);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (response.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    });

});

function showValuesInModal(slug, name, id){
    document.getElementById('categoryId').value = id
    document.getElementById('id_slug').value = slug
    document.getElementById('id_name').value = name
    document.getElementById('deleteBtn').hidden= false;
    document.getElementById('updateBtn').hidden= false;
    document.getElementById('addBtn').hidden= true;
    $("#CategoryModal").modal("show");
}

function clearValuesInModal(){
    document.getElementById('categoryId').value = ""
    document.getElementById('id_slug').value = ""
    document.getElementById('id_name').value = ""
    document.getElementById('deleteBtn').hidden= true;
    document.getElementById('updateBtn').hidden= true;
    document.getElementById('addBtn').hidden= false;
    $("#CategoryModal").modal("show");
}

  