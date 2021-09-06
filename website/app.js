var form = document.forms.namedItem("fileinfo");
form.addEventListener('submit', function(ev) {
  changeVisibility();
  document.getElementById('animation').style.display === "none";
  var oOutput = document.querySelector("div"),
      formData = new FormData(form);
  fetch('/upload', {
    method: 'post',
    body: formData
  })
  .then(response => response.json())
  .then(result => {
    console.log(result);
    document.getElementById('url').value = window.location.hostname+'/f/'+result.file_name;
    document.getElementById('filelabel').innerHTML = 'Choose a file';
    document.getElementById('submitbutton').innerHTML = 'Upload Another';
    document.getElementById('file').value = '';
    changeVisibility();
  })
  .catch(error => {
    console.error('Error:', error);
  });
  ev.preventDefault();
}, false);


document.getElementById('file').onchange = function () {
  f = this.value.replace(/.*[\/\\]/, '');
  document.getElementById('filelabel').innerHTML = f
};

function changeVisibility() {
  var formElement = document.getElementById("upload-form")
  formElement.classList.toggle('is-uploading')
}