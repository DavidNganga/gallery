function myFunction() {
  /* Get the image field */
  var copyImage = document.getElementById("myInput");

  /* Select the image field */
  copyImage.select();

  /* Copy the image inside the image field */
  document.execCommand("Copy");

  /* Alert the copied image */
  alert("Copied the image: " + copyImage.value);
}
