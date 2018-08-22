console.log('app.js connected successfully');

window.addEventListener("load", () => {

    const sendData = (form) => {
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
            processData(responseObject);
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
    const form = document.getElementById("input-form");
    // Add event listener to override default behaviour and send request
    form.addEventListener("submit", e => {
        e.preventDefault();
        sendData(form);
    })

    const processData = (data) => {
        console.log('This is the processData function');
        console.log(data);
    }
})
