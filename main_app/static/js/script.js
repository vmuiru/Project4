const year = document.getElementById('year');
setYear();
function setYear() {
    var d = new Date();
    var n = d.getFullYear();
    year.innerText = n;
}


const editBtn = document.querySelectorAll(".edit-btn");

for (let i =0; i < editBtn.length; i++){
    editBtn[i].addEventListener("click", dropIt)
}

function dropIt(){
    document.querySelector(".dropdown-content").classList.toggle("show-content");
}