document.addEventListener("DOMContentLoaded", function() {
    const statusSelect = document.getElementById('id_status');

    statusSelect.addEventListener('change', function() {
        const selectedValue = statusSelect.value;
        const smartphoneId = 2
        console.log('Selected value:', selectedValue);

        // fetch(`/update_status/${smartphoneId}/${selectedValue}/`, {
        //     method: "POST",
        //     headers: {
        //       "X-CSRFToken": getCookie("csrftoken"), // Убедитесь, что у вас установлен CSRF токен
        //     },
        //   })
        //     .then((response) => response.json())
        //     .then((data) => {
        //       // Обновляем интерфейс или выполняем другие действия при успешном обновлении
        //       console.log(data);
        //     })
        //     .catch((error) => {
        //       console.error("Error:", error);
        //     });
    });
});
