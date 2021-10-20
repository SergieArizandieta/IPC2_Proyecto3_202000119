let post_form = document.getElementById("post-form");
let get_button = document.getElementById("get-button");
let messages = document.getElementById("Exditor_Salida");

post_form.addEventListener("submit", (e) => {
  e.preventDefault();
  fetch("http://localhost:5000/events/", {
    method: "POST",
    headers: {
      "Content-Type": "text/plain",
    },
    body: post_form.elements["api-info"].value,
  }).then((res) => {
    if (res.ok) {
      messages.innerText = "OK";
    }
  });
});

get_button.addEventListener("click", (e) => {
  e.preventDefault();
  fetch("http://localhost:5000/events/", {
    method: "GET",
    headers: {
      "Content-Type": "text/plain",
    },
  })
    .then((res) => {
      if (res.ok) {
        return res.text();
      }
    })
    .then((res_txt) => {
      messages.innerText = res_txt;
    });
});


