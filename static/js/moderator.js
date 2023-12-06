function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    
    if (parts.length === 2) {
        return parts.pop().split(';').shift();
    }
}

function changeSmartphoneStatus(smartphoneId) {
    const statusSelect = document.getElementById(`status_selectId_${smartphoneId}`);

        const selectedValue = statusSelect.value;
        fetch(`/update_status/${smartphoneId}/${selectedValue}/`, {
            method: "POST",
            headers: {
              "X-CSRFToken": getCookie("csrftoken"),
            },
          })
  }