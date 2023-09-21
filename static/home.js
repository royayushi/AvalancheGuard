// ScrollReveal().reveal('.track', {
//     delay: 500
//  });
 
document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".card-clickable");
    const forms = document.querySelectorAll(".hidden-form");

    cards.forEach((card, index) => {
        card.addEventListener("click", () => {
            // Toggle the visibility of the form
            forms[index].classList.toggle("visible-form");
        });
    });
});
console.log("JavaScript file loaded");
