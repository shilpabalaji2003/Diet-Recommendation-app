// Smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const newsIcon = document.getElementById("news-icon");
    const newsContainer = document.querySelector(".latest-news-container");

    newsIcon.addEventListener("click", function (event) {
        // Prevent the default behavior of the anchor tag
        event.preventDefault();
        // Toggle the display of the news container
        if (newsContainer.style.display === "block") {
            newsContainer.style.display = "none";
        } else {
            newsContainer.style.display = "block";
        }
    });
});


