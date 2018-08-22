console.log('app.js connected successfully');

window.addEventListener("load", () => {

    function sendData(form) {
        let xhr = new XMLHttpRequest();

        // Collect form data
        let fd = new FormData(form);

        // Convert to JS object
        let fd_obj = {};
        fd.forEach((value, key) => {
            fd_obj[key] = value;
        });
        let fd_json = JSON.stringify(fd_obj);


        // CASE: successful data submission
        xhr.addEventListener("load", e => {
            let responseObject = JSON.parse(e.target.responseText);
            console.log(responseObject);
        })

        // CASE: failure
        xhr.addEventListener("error", e => {
            alert("Bugger, something went wrong");
        })

        // Build the request
        xhr.open("POST", "/");

        // Send the request
        xhr.send(fd_json);
    }

    // Define form
    let form = document.getElementById("input-form");
    // Add event listener to override default behaviour and send request
    form.addEventListener("submit", e => {
        e.preventDefault();
        sendData(form);
    })
})
