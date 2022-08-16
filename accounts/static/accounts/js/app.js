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

// Carousel Section
// let newArrivals = "";
// for (let i = 1; i <= 4; i++) {
//   newArrivals += `<li id="big" class="slide one">${i}</li>`;
// }
// slidesContainer.innerHTML = newArrivals;

nextButton.addEventListener("click", () => {
  let slideWidth = slidesContainer.clientWidth;
  slidesContainer.scrollLeft += slideWidth;
});

prevButton.addEventListener("click", () => {
  let slideWidth = slidesContainer.clientWidth;
  slidesContainer.scrollLeft -= slideWidth;
});

// Images
const cats = [
  {
    title: "Popular Products",
    products: [
      {
        name: "",
        image: "zuri.png",
      },
      {
        name: "",
        image: "second.png",
      },
      {
        name: "",
        image: "third.png",
      },
      {
        name: "",
        image: "fourth.png",
      },
      {
        name: "",
        image: "fifth.png",
      },
    ],
  },

  {
    title: "Mobile devices",
    products: [
      {
        name: "",
        image: "zuri.png",
      },
      {
        name: "",
        image: "second.png",
      },
      {
        name: "",
        image: "third.png",
      },
      {
        name: "",
        image: "fourth.png",
      },
      {
        name: "",
        image: "fifth.png",
      },
    ],
  },

  {
    title: "Home electronics",
    products: [
      {
        name: "",
        image: "zuri.png",
      },
      {
        name: "",
        image: "second.png",
      },
      {
        name: "",
        image: "third.png",
      },
      {
        name: "",
        image: "fourth.png",
      },
      {
        name: "",
        image: "fifth.png",
      },
    ],
  },

  {
    title: "Desktop and laptops",
    products: [
      {
        name: "",
        image: "zuri.png",
      },
      {
        name: "",
        image: "second.png",
      },
      {
        name: "",
        image: "third.png",
      },
      {
        name: "",
        image: "fourth.png",
      },
      {
        name: "",
        image: "fifth.png",
      },
    ],
  },
];

//Products section
let singleCategory = "";
cats.forEach((item) => {
  let productsInCategory = "";
  item.products.forEach((product) => {
    productsInCategory += `<div class="single-product">
                <img src="img/${product.image}" alt="" />
            </div>`;
  });

  singleCategory += `<div class="single-category">
            <div class="category-text">${item.title}</div>
            <div id="images" class="category-images">${productsInCategory}</div>
        </div>`;
});

categories.innerHTML = singleCategory;

// Toggle

const togglePassword = document.querySelector("#togglePassword");
const password = document.querySelector("#password");

togglePassword.addEventListener("click", function () {
  // toggle the type attribute
  const type =
    password.getAttribute("type") === "password" ? "text" : "password";
  password.setAttribute("type", type);
  // toggle the icon
  this.classList.toggle("bi-eye");
});
