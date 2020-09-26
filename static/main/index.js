document.addEventListener("DOMContentLoaded", () => {
  console.log("Loaded");

  let files = [];
  FilePond.registerPlugin(FilePondPluginFileValidateSize);
  FilePond.registerPlugin(FilePondPluginFileValidateType);
  FilePond.setOptions({
    allowMultiple: true,
    maxFiles: 5,
    maxFileSize: "20mb",
  });

  const inputElement = document.querySelector('input[type="file"]');
  const pond = FilePond.create(inputElement, {
    acceptedFileTypes: ["image/jpeg", "image/jpg"],
    onaddfile: (err, fileItem) => {
      if (!err) {
        files.push(fileItem.file);
      }
      console.log(files);
    },
    onremovefile: (err, fileItem) => {
      const index = files.indexOf(fileItem.file);
      if (index > -1) {
        files.splice(index, 1);
      }
      console.log(files);
    },
  });

  let formData = new FormData();

  $("#pdfForm").on("submit", function (e) {
    console.log("Form");
    e.preventDefault();

    formData.append("title", $("#title").val());
    formData.append("length", files.length);
    for (let i = 0; i < files.length; i++) {
      formData.append("images" + i, files[i]);
    }

    let csrfToken = $("input[name=csrfmiddlewaretoken]").val();
    formData.append("csrfmiddlewaretoken", csrfToken);
    formData.append("credentials", "include");

    const title = $("#title").val();

    $("#submit").hide();
    $(".ajaxProgress").show();
    $.ajax({
      type: "POST",
      url: "/success",
      data: formData,
      cache: false,
      processData: false,
      contentType: false,
      enctype: "multipart/form-data",
      success: function (response) {
        const another = document.querySelector("#another");

        if (response.message === "File") {
          $(".ajaxProgress").hide();
          $("#submit").show();
          another.innerHTML = `<h3 class="alert alert-danger">The title is taken. Please add another title!</h3>`;
          another.style.display = "block";
        } else if (response.message === "Full") {
          $(".ajaxProgress").hide();
          $("#submit").show();
          another.innerHTML = `<h3 class="alert alert-danger">You have reached your limit. Please delete a PDF first!</h3>`;
          another.style.display = "block";
        } else {
          $(".ajaxProgress").hide();
          $("#pdfForm").hide();
          another.innerHTML = `<h3 class="alert alert-success">Your PDF is ready!<br>Please click on the button above^</h3>`;
          another.style.display = "block";
        }
      },
      error: function (err) {
        console.log(err.responseText);
      },
    });
  });
});
