document.addEventListener("DOMContentLoaded", () => {
  console.log("Loaded");

  let files = [];
  FilePond.registerPlugin(FilePondPluginFileValidateSize);
  FilePond.registerPlugin(FilePondPluginFileValidateType);
  FilePond.setOptions({
    allowMultiple: true,
    maxFiles: 50,
    maxFileSize: "10mb",
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

    $("#pdfForm").hide();
    $("#please").show();
    $(".ajaxProgress").show();
    $.ajax({
      xhr: function () {
        $(".progress").css("display", "block");
        $("#percent").text("0%");
        var xhr = new window.XMLHttpRequest();
        xhr.upload.addEventListener(
          "progress",
          function (e) {
            if (e.lengthComputable) {
              var percentComplete = e.loaded / e.total;
              $(".bar").css("width", percentComplete * 100 + "%");
              $("#percent").text(Math.floor(percentComplete * 100) + "%");
            }
          },
          false
        );
        return xhr;
      },
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
          $("#please").hide();
          $(".progress").hide();
          $("#pdfForm").show();
          another.innerHTML = `<div  class="alert alert-danger">
                                <h3>The title is taken. Please add another title!</h3>
                                <h5>You can try using your_name+course_id+student_id as file name.</h5>
                                </div>`;
          another.style.display = "block";
        } else if (response.message === "Full") {
          $(".ajaxProgress").hide();
          $("#please").hide();
          $(".progress").hide();
          $("#pdfForm").show();
          another.innerHTML = `<h3 class="alert alert-danger">You have reached your limit. Please delete a PDF first!</h3>`;
          another.style.display = "block";
        } else {
          $(".ajaxProgress").hide();
          $("#please").hide();
          $(".progress").hide();
          $("#pdfForm").hide();
          const temp = JSON.parse(response.file);
          const tempID = temp[0].pk;
          another.innerHTML = `
            <h3 class="alert alert-success">Your PDF is ready!<br>Please click on the button below.</h3><br>
            <a target="_blank" href="/views/${tempID}"><button id="download" class="btn btn-primary">Download</button></a>
          `;
          another.style.display = "block";
        }
      },
      error: function (err) {
        console.log(err.responseText);
      },
    });
  });
});
