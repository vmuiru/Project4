const year = document.getElementById('year');
setYear();
function setYear() {
    var d = new Date();
    var n = d.getFullYear();
    year.innerText = n;
}