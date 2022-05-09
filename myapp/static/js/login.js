$(document).ready(function () {
    $("#login").click(function () {
      if ($("#email-id").val() == "") {
        alert("Please Enter email");
        return false;
      }
      if ($("#password").val() == "") {
        alert("Please Enter Password");
        return false;
      }
  
      let formData = new FormData();
      formData.append("email-id", $("#email-id").val());
      formData.append("password", $("#password").val());
      formData.append(
        "csrfmiddlewaretoken",
        $("input[name=csrfmiddlewaretoken]").val()
      );
  
      $.ajax({
        url: "/org_login/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
          if (response == "11") {
            alert("Login successful");
            window.location = "/home/";
          } else if (response == "12") {
            alert("Login not successful,Register!");
            window.location = "/register/";
          }
        },
      });
    });
  });