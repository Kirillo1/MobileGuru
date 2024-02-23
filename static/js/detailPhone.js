const addToBasket = document.getElementById('addToBasket');
const productQuantity = document.getElementById('productQuantity');
const basketModal = document.getElementById('basketModalBRClass');
const myModalEl = document.getElementById('basketModal');
const addCommentBtn = document.getElementById('addCommentBtn');
const deleteCommentBtn = document.querySelectorAll('.delete-comment-btn');

addToBasket.addEventListener("click", addPhoneToBasket)

if (addCommentBtn) {
    addCommentBtn.addEventListener("click", addPhoneComment)
}

if (deleteCommentBtn) {
    deleteCommentBtn.forEach(button => {
        button.addEventListener('click', function() {
            const commentId = this.getAttribute('data-comment-id');
            deletePhoneComment(commentId);
        });
    });
}

myModalEl.addEventListener('hidden.bs.modal', event => {
basketModal.classList = "modal-content align-items-center bg-dark";
})


function addPhoneToBasket() {
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


function addPhoneComment(){
    const smartphoneId = this.getAttribute('data-smartphone-id');
    const textInput = document.getElementById('commentData').value;
    const inputCommentDiv = document.getElementById('inputCommentDiv');
    if (textInput.length > 0) {
        $.ajax({
            url: '/comments/create_comment/',
            method: 'POST',
            data: {"smartphone_id": smartphoneId, "text_comment": textInput},
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            success: function(response) {
                location.reload();
            },
            error: function(xhr, textStatus, errorThrown) {
                inputCommentDiv.classList.add('border', 'rounded', 'border-3', 'border-danger');
            }
        });
    }
}


function deletePhoneComment(commentId) {
    $.ajax({
        url: '/comments/delete_comment/',
        method: 'POST',
        data: {"comment_id": commentId},
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        },
        success: function(response) {
            location.reload();
        },
        error: function(xhr, textStatus, errorThrown) {
            inputCommentDiv.classList.add('border', 'rounded', 'border-3', 'border-danger');
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

