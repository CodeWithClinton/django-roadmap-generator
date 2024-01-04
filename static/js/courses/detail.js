let radios = document.querySelectorAll(".form-check-input")
let duration_box = document.querySelectorAll(".r-duration")
let generate_button = document.querySelector(".g-button")
for(let radio of radios){
    radio.addEventListener("change", glow)
}

function glow(e){
    if(e.target.checked){
        for(let box of duration_box){
            box.style.border="2px solid #dee2e6"
        }
        let duration_container = e.target.parentElement.parentElement.parentElement
        console.log(duration_container)
        duration_container.style.border= "2px solid #002244"
        generate_button.disabled = false
        generate_button.style.opacity="1"
    
    //    e.target.parentElement.parentElement.style.boxShadow="rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px" 
    }
}
