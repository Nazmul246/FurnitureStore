/*slide*/
const images = document.querySelectorAll('.image-container img');
let currentImageIndex = 0;

function showNextImage() {
  images[currentImageIndex].classList.remove('active');
  currentImageIndex = (currentImageIndex + 1) % images.length;
  images[currentImageIndex].classList.add('active');
}

setInterval(showNextImage, 4000); 