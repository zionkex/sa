// --------------------- Burger ------------------
document.addEventListener("DOMContentLoaded", function () {
    const burger = document.querySelector(".burger");
    const mobileNav = document.querySelector(".mobile-nav");
    const closeBtn = document.querySelector(".close-btn");

    burger.addEventListener("click", function () {
        burger.classList.toggle("active");
        mobileNav.classList.toggle("active");
    });

    closeBtn.addEventListener("click", function () {
        mobileNav.classList.remove("active");
        burger.classList.remove("active");
    });
});
// ------------------ End Burger ------------------




// ---------------------------------------------------------- Catalog Page ----------------------------------------------------------




// ---------------------------------------------------------- End Catalog Page ----------------------------------------------------------

