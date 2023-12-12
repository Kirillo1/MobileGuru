function getCookie(name) {
    const value = `; ${document.cookie}`
    const parts = value.split(`; ${name}=`)

    if (parts.length === 2) {
        return parts.pop().split(';').shift()
    }
}

function changeSmartphoneStatus(smartphoneId) {
    const statusSelect = document.getElementById(`status_selectId_${smartphoneId}`)

    const selectedValue = statusSelect.value
    fetch(`/update_status/${smartphoneId}/${selectedValue}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
        .then((response) => response.json())
        .then((data) => {
            alertOnOff(true)
        })
        .catch((error) => {
            alertOnOff(false)
        });
}

function alertOnOff(flag) {
    const alertPlaceholder = document.getElementById('liveAlertPlaceholder');
    const alertErrorPlaceholder = document.getElementById('liveErrorAlertPlaceholder');

    if (flag) {
        alertPlaceholder.style.display = "block";
        setTimeout(() => {
            alertPlaceholder.style.display = "none";
        }, 2000);
    } else {
        alertErrorPlaceholder.style.display = "block";
        setTimeout(() => {
            alertErrorPlaceholder.style.display = "none";
        }, 2000);
    }
}