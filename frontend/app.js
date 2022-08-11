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
let newArrivals = "";
for (let i = 0; i < carouselImages.length; i++) {
  newArrivals += `<li id="big" style="background-image: url('img/${carouselImages[i]}')" class="slide one"></li>`;
}
slidesContainer.innerHTML = newArrivals;

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
    title: "Popular Categories",
    products: [
      {
        name: "Iphones",
        image: "phone_category.png",
      },
      {
        name: "Cameras",
        image: "camera_category.png",
      },
      {
        name: "Mobile Phones",
        image: "androids_category.png",
      },
      {
        name: " Laptops",
        image: "laptops_category.png",
      },
      {
        name: "Tablets",
        image: "tablets_category.png",
      },
    ],
  },

  {
    title: "Mobile Phones",
    products: [
      {
        name: "Iphone 13",
        image: "phone1_product.png",
      },
      {
        name: "Galaxy Note 10",
        image: "phone2_product.png",
      },
      {
        name: "Infinix Note 12",
        image: "phone3_product.png",
      },
      {
        name: "Iphone Xs max",
        image: "phone4_product.png",
      },
      {
        name: "Infinix ZeroX",
        image: "phone5_product.png",
      },
      {
        name: "Y9-2019",
        image: "phone6_product.png",
      },
    ],
  },

  {
    title: "Cameras",
    products: [
      {
        name: "Canon EOS-5d",
        image: "camera1_product.png",
      },
      {
        name: "Nikon L340",
        image: "camera2_product.png",
      },
      {
        name: "Nikon D3100",
        image: "camera3_product.png",
      },
      {
        name: "Canon 550d",
        image: "camera4_product.png",
      },
      {
        name: "Sony Dsc-Hx60",
        image: "camera5_product.png",
      },
      {
        name: "Nikon Z-6",
        image: "camera6_product.png",
      },
    ],
  },

  {
    title: "Desktop and laptops",
    products: [
      {
        name: "Lenovo core i3",
        image: "laptop1_product.png",
      },
      {
        name: "Intel Core  i7 ",
        image: "laptop2_product.png",
      },
      {
        name: "HP core i7",
        image: "laptop3_product.png",
      },
      {
        name: "Dell Inspiron",
        image: "laptop4_product.png",
      },
      {
        name: "Lenovo Idea pad",
        image: "laptop5_product.png",
      },
      {
        name: "Siemens Simatic",
        image: "laptop6_product.png",
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
                <p class="product_name"> ${product.name} </p>
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
