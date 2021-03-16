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

function dropIt(evt) {
    const id = evt.target.id.split('-').pop();
    document.querySelector(`#dropdown-${id}`).classList.toggle('show-content');
  }