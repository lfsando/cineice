// Get the modal
var modal = document.getElementById('remove-modal');

// Get the button that opens the modal
var btn = document.getElementById("remove-btn");

// Get the No button element that closes the modal
var no = document.getElementById("no-btn");

// When the user clicks the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on no, close the modal
no.onclick = function() {
	modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}