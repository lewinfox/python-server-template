console.log('app.js connected successfully');

window.addEventListener("load", () => {

    function sendData(form) {
        let xhr = new XMLHttpRequest();

        // Collect form data
        let fd = new FormData(form);

        // CASE: successful data submission
        xhr.addEventListener("load", e => {
            alert("Success! Check the console for the data");
            let responseObject = JSON.parse(e.target.responseText);
            console.log(responseObject);
        })

        // CASE: failure
        xhr.addEventListener("error", e => {
            alert("Bugger, something went wrong");
        })

        // Build the request
        xhr.open("GET", "/data");

        // Send the request
        xhr.send(fd);
    }

    // Define form
    let form = document.getElementById("input-form");
    // Add event listener to override default behaviour and send request
    form.addEventListener("submit", e => {
        e.preventDefault();
        sendData(form);
    })
})
