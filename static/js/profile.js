const fileInput = document.querySelector('#id_image');
const saveButton = document.querySelector('#addImage');
const deleteImageBtn = document.querySelector('#deleteImageBtn');
const image = document.getElementById('avatar_id');
const disabledButton = document.querySelector('.custom-disabled');

const currentImageUrl = image.src;

if (!currentImageUrl.includes('default_avatar.png')) {
    disabledButton.classList.remove('custom-disabled');
}


saveButton.addEventListener('click', () => {
    fileInput.click();
});

deleteImageBtn.addEventListener('click', deleteImage);


function deleteImage() {
    image.style.display = "none";
    document.getElementById("image-clear_id").checked = true;
    const imageContainer = document.getElementById('imageContainer');
    const imgElement = document.createElement('img');
    const pathToImage = "/static/img/default_avatar.png";
    imgElement.src = pathToImage;
    imgElement.className = "rounded-circle mt-5";
    imgElement.style.width = "200px";
    imageContainer.innerHTML = '';
    imageContainer.appendChild(imgElement);
    document.querySelector('#closeModalDelete').click();
    disabledButton.classList.add('custom-disabled');
}


if (fileInput) {
    fileInput.addEventListener('change', function (event) {
        const file = event.target.files[0];
    
        if (file) {
            const reader = new FileReader();
    
            reader.onload = function (e) {
                const imageContainer = document.getElementById('imageContainer');
                let imgElement = document.createElement('img');
                imgElement.src = e.target.result;
                imgElement.className = "rounded-circle mt-5";
                imgElement.style.width = "200px";
                imageContainer.innerHTML = '';
                imageContainer.appendChild(imgElement);
                let image = document.getElementById('avatar_id');
                image.style.display = "none";
                document.querySelector('#closeModalEdit').click();
            };
            reader.readAsDataURL(file);
        }
    });
}
