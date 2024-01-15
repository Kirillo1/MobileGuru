const fileInput = document.querySelector('#id_image');
const saveButton = document.querySelector('#addImage');

saveButton.addEventListener('click', () => {
    fileInput.click();
});

function deleteImage() {
    var image = document.getElementById('avatar_id');
    image.style.display = "none";

    document.getElementById("image-clear_id").checked = true;
    const imageContainer = document.getElementById('imageContainer');
    const imgElement = document.createElement('img');
    imgElement.src = "/static/img/default_avatar.png";
    imgElement.className = "rounded-circle mt-5";
    imgElement.style.width = "200px";
    imageContainer.innerHTML = '';
    imageContainer.appendChild(imgElement);
    document.querySelector('#close_modal').click();
}

document.getElementById('id_image').addEventListener('change', function (event) {
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
            const imageContainer = document.getElementById('imageContainer');
            const imgElement = document.createElement('img');
            imgElement.src = e.target.result;
            imgElement.className = "rounded-circle mt-5";
            imgElement.style.width = "200px";
            imageContainer.innerHTML = '';
            imageContainer.appendChild(imgElement);
            const image = document.getElementById('avatar_id');
            image.style.display = "none";
            document.querySelector('#close_modal_chg').click();
        };
        reader.readAsDataURL(file);
    }
});
