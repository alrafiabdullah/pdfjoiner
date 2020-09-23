document.addEventListener("DOMContentLoaded", () => {
  console.log("Loaded");

  let files = [];
  FilePond.registerPlugin(FilePondPluginFileValidateSize);
  FilePond.registerPlugin(FilePondPluginFileValidateType);
  FilePond.setOptions({
    allowMultiple: true,
    maxFiles: 5,
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

  $("#pdfForm").on("submit", function () {
    console.log("Form");

    formData.append("title", $("#title").val());
    formData.append("length", files.length);
    for (let i = 0; i < files.length; i++) {
      formData.append("images" + i, files[i]);
    }

    let csrfToken = $("input[name=csrfmiddlewaretoken]").val();
    formData.append("csrfmiddlewaretoken", csrfToken);
    formData.append("credentials", "include");

    const title = $("#title").val();

    $.ajax({
      type: "POST",
      url: "success",
      data: formData,
      cache: false,
      processData: false,
      contentType: false,
      enctype: "multipart/form-data",
      sucess: function () {
        console.log("response.message");
      },
      error: function (err) {
        console.log(err.responseText);
      },
    });
  });
});
