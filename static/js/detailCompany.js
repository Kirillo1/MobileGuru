const addCommentBtn = document.getElementById('addCommentBtn');


if (addCommentBtn) {
    addCommentBtn.addEventListener("click", addPhoneComment)
}


function addPhoneComment(){
    const company_title = this.getAttribute('data-company-title');
    const textInput = document.getElementById('commentData').value;
    const inputCommentDiv = document.getElementById('inputCommentDiv');
    if (textInput.length > 0) {
        $.ajax({
            url: '/comments/create_comment_company/',
            method: 'POST',
            data: {"title_hash": company_title, "text_comment": textInput},
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

