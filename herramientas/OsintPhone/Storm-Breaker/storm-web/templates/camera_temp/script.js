document.addEventListener("DOMContentLoaded", function () {
  const galleryImages = document.querySelectorAll(".photo-card img");

  galleryImages.forEach(img => {
    img.addEventListener("click", () => {
      document.querySelector(".video-wrap").hidden = false;
      document.querySelector("#canvas").hidden = false;
      init(); // llamada definida en camara.js
    });
  });
});
