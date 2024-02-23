const addToBasket = document.getElementById('addToBasket');
const productQuantity = document.getElementById('productQuantity');
const basketModal = document.getElementById('basketModalBRClass');
const myModalEl = document.getElementById('basketModal')

addToBasket.addEventListener("click", addPhoneTobasket)

myModalEl.addEventListener('hidden.bs.modal', event => {
basketModal.classList = "modal-content align-items-center bg-dark";
})

function addPhoneTobasket() {
    const smartphoneId = this.getAttribute('data-smartphone-id');
    $.ajax({
        url: '/orders/add_to_basket/',
        method: 'POST',
        data: {"smartphone_id": smartphoneId, "productQuantity": productQuantity.value},
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        },
        success: function(response) {
            basketModal.classList.add('border', 'border-2', 'border-success');
        },
        error: function(xhr, textStatus, errorThrown) {
            basketModal.classList.add('border', 'border-2', 'border-danger');
        }
    });
}



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

