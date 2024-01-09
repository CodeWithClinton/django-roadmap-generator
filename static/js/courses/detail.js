let radios = document.querySelectorAll(".form-check-input");
let duration_box = document.querySelectorAll(".r-duration");
let generate_button = document.querySelector(".g-button");
let loader_container = document.querySelector(".loader-container")



// getting prompts elements
let mini_schedule_id;
let schedule_id;
let course_id;

for (let radio of radios) {
  radio.addEventListener("change", glow);
}

function glow(e) {
  if (e.target.checked) {
    for (let box of duration_box) {
      box.style.border = "2px solid #dee2e6";
    }
    let duration_container = e.target.parentElement.parentElement.parentElement;
    console.log(duration_container);
    duration_container.style.border = "2px solid #002244";
    generate_button.disabled = false;
    generate_button.style.opacity = "1";

    // passing prompt parameters
    mini_schedule_id = e.target.dataset.new_id;
    schedule_id = e.target.dataset.sch_id;
    course_id = e.target.dataset.course_id;

    //    e.target.parentElement.parentElement.style.boxShadow="rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px"
  }
}

generate_button.addEventListener("click", sending_prompt);
function sending_prompt() {
  // console.log(mini_schedule_id)
  // console.log(schedule_id)
  // console.log(course_id)
  if(isAuthenticated=="True"){


    const url = "/ask_openai";
    loader_container.style.display="block"

    if(r_num >= 1){
      let loader_container_main = document.querySelector(".loader-container-main")
      loader_container_main.style.display = "none"

    }

    
    loader_container.innerHTML = `
    <span class="placeholder col-12"></span>
          <span class="placeholder col-12"></span>
          <span class="placeholder col-12"></span>
          <span class="placeholder col-12"></span>
          <span class="placeholder col-12"></span>
          <span class="placeholder col-12"></span>
          <span class="placeholder col-12"></span>
          <span class="placeholder col-12"></span>
          <span class="placeholder col-12"></span>
          <span class="placeholder col-12"></span>
          <span class="placeholder col-12"></span>
          <span class="placeholder col-12"></span>
    `

    generate_button.disabled = true;
    generate_button.style.opacity = "0.6";
  
    const data = {
      mini_sch_id: mini_schedule_id,
      sch_id: schedule_id,
      c_id: course_id
    };
  
    // Use the Fetch API to make a POST request
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
  
        return response.json();
      })
  
      .then((data) => {
        learning_roadmap = JSON.parse(data);
        
        console.log(JSON.stringify(learning_roadmap))

        generate_button.disabled = false;
        generate_button.style.opacity = "1";

        loader_container.innerHTML = ""
        loader_container.innerHTML = `
          <li class="list-group-item"><strong>Title:</strong> <span>${learning_roadmap.title}</span> </li>
          <li class="list-group-item"><strong>Duration:</strong> <span>${learning_roadmap.duration}</span></li>
          <li class="list-group-item"><strong>Frequency:</strong> <span>${learning_roadmap.frequency}</span></li>
          <li class="list-group-item"><strong>Roadmap:</strong> <span></span></li>
        `
  
        learning_roadmap.learning_roadmap.forEach(topic => {
          loader_container.innerHTML += `
  
          <li class="list-group-item">-- ${topic}</li>
         
          `
        })
  
      })
  
      .catch((error) => {
        console.error("Error:", error);
      });


  }

  else{
    location.href = r_url
  }

 
}

console.log(isAuthenticated)