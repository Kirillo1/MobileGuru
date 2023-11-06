document.addEventListener("DOMContentLoaded", function() {
    const likeButtons = document.querySelectorAll(".like-btn");
    const unlikeButtons = document.querySelectorAll(".unlike-btn");
  
    likeButtons.forEach((button) => {
      button.addEventListener("click", function() {
        const smartphoneId = button.getAttribute("data-smartphone-id");
        handleLike(smartphoneId);
      });
    });
  
    unlikeButtons.forEach((button) => {
      button.addEventListener("click", function() {
        const smartphoneId = button.getAttribute("data-smartphone-id");
        handleUnlike(smartphoneId);
      });
    });
  
    function handleLike(smartphoneId) {
      const likedCookieName = `liked_${smartphoneId}`;
  
      if (!document.cookie.includes(likedCookieName)) {
        fetch(`/like_smartphone/${smartphoneId}/`)
          .then(response => response.json())
          .then(data => {
            if (data.error) {
              alert(data.error);
            } else {
              const likesCountElement = document.getElementById(`likes-count-${smartphoneId}`);
              likesCountElement.textContent = data.likes;
              document.cookie = `${likedCookieName}=1`;
            }
          });
      } else {
        alert("Вы уже поставили лайк");
      }
    }
  
    function handleUnlike(smartphoneId) {
      const likedCookieName = `liked_${smartphoneId}`;
  
      if (document.cookie.includes(likedCookieName)) {
        fetch(`/unlike_smartphone/${smartphoneId}/`)
          .then(response => response.json())
          .then(data => {
            if (data.error) {
              alert(data.error);
            } else {
              const likesCountElement = document.getElementById(`likes-count-${smartphoneId}`);
              likesCountElement.textContent = data.likes;
              document.cookie = `${likedCookieName}=; expires=Thu, 01 Jan 1970 00:00:00 UTC`;
            }
          });
      } else {
        alert("Вы еще не ставили лайк");
      }
    }
  });
  