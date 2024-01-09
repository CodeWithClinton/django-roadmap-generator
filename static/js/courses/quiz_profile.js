console.log("this profile giving page");
let fetch_btn = document.querySelector(".fetch-btn");
let quiz_container = document.querySelector(".quiz-container");
let sub_btn = document.querySelector(".sub-btn");

fetch_btn.addEventListener("click", fetchQuiz);

function fetchQuiz(e) {
  console.log(e.target.dataset.ucourse);
  let u_course_id = e.target.dataset.ucourse;

  const apiUrl = url;

  const postData = {
    user_course_Id: u_course_id,
  };

  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(postData),
  };
  //

  fetch(apiUrl, requestOptions)
    .then((response) => {
      // Check if the request was successful (status code 200-299)
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      // Parse the response as JSON
      return response.json();
    })
    .then((data) => {
      // Handle the JSON data
      console.log("Data:", data);
      sub_btn.style.display = "block";

      data.forEach((d) => {
        quiz_container.innerHTML += `
        <div class="card mb-3">
                    <div class="card-body">
                        <p class='fs-5'>${d.question}</p>

                    </div>
                    
            </div>
                
        `;

        let card_body = document.createElement("div");

        console.log(card_body);
        card_body.classList.add("card-body");

        d.options.forEach((option) => {
          card_body.innerHTML += `
                    <div class="form-check">
                            <input class="form-check-input" type="radio" value="${option}" data-qid="${d.id}" name="${d.question}" id="${option}">
                            <label class="form-check-label" style="font-size:18px" for="${option}">
                              ${option}
                            </label>
                          </div>      
            `;
        });

        quiz_container.appendChild(card_body);
      });
    })
    .catch((error) => {
      // Handle any errors that occurred during the fetch
      console.error("Fetch Error:", error);
    });
}

sub_btn.addEventListener("click", submitQuiz);

function submitQuiz() {}
