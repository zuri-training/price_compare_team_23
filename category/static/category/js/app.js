// Hamburger Setup
const hamburger = document.querySelector(".hamburger");
const menu = document.querySelector(".menu");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("is-active");
  menu.classList.toggle("is-active");
});

// Product Page
const slidesContainer = document.getElementById("slides-container");
const slide = document.querySelector(".slide");
const prevButton = document.getElementById("slide-arrow-prev");
const nextButton = document.getElementById("slide-arrow-next");
const categories = document.getElementById("categories");

const carouselImages = [
  "carousel1.png",
  "carousel2.png",
  "carousel3.png",
  "carousel4.png",
  "carousel5.png",
];

// Carousel Section
// let newArrivals = "";
// for (let i = 0; i < carouselImages.length; i++) {
//   newArrivals += `<li id="big" style="background-image: url("../images/${carouselImages[i]}")" class="slide one"></li>`;
// }

nextButton.addEventListener("click", () => {
  let slideWidth = slidesContainer.clientWidth;
  slidesContainer.scrollLeft += slideWidth;
});

prevButton.addEventListener("click", () => {
  let slideWidth = slidesContainer.clientWidth;
  slidesContainer.scrollLeft -= slideWidth;
});
