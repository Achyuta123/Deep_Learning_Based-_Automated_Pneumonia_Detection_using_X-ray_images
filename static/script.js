function previewImage(event) {
    var reader = new FileReader();
    reader.onload = function() {
      var preview = document.getElementById('preview');
      var image = new Image();
      image.src = reader.result;
      preview.innerHTML = '';
      preview.appendChild(image);
    }
    reader.readAsDataURL(event.target.files[0]);
  }