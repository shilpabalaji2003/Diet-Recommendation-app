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

// JavaScript code to fetch and display thumbnail images

// Function to fetch thumbnail data from the backend (server-side)
function fetchThumbnails() {
    fetch('/thumbnails')
        .then(response => response.json())
        .then(data => {
            // Call function to display thumbnails
            displayThumbnails(data);
        })
        .catch(error => console.error('Error fetching thumbnails:', error));
}

// Function to display thumbnails on the webpage
function displayThumbnails(thumbnails) {
    const thumbnailsContainer = document.getElementById('thumbnails-container');

    // Clear any existing thumbnails
    thumbnailsContainer.innerHTML = '';

    // Loop through the thumbnail data and create HTML elements for each thumbnail
    thumbnails.forEach(thumbnail => {
        const thumbnailElement = document.createElement('div');
        thumbnailElement.classList.add('thumbnail');

        // Create an anchor element for the thumbnail with the video URL as href
        const anchorElement = document.createElement('a');
        anchorElement.href = `https://www.youtube.com/watch?v=${thumbnail.video_id}`;
        anchorElement.target = '_blank'; // Open in a new tab
        thumbnailElement.appendChild(anchorElement);

        const imgElement = document.createElement('img');
        imgElement.src = thumbnail.thumbnail_url;
        anchorElement.appendChild(imgElement);

        const titleElement = document.createElement('p');
        titleElement.textContent = thumbnail.title;
        thumbnailElement.appendChild(titleElement);

        thumbnailsContainer.appendChild(thumbnailElement);
    });
}

// Call the fetchThumbnails function when the page loads
window.onload = function () {
    fetchThumbnails();
};

