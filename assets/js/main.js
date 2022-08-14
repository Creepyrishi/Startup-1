const baseUrl = window.location.origin;
const host = window.location.host

const navToggle = document.querySelector("#hamburger")
const navList = document.querySelector(".navUL")

//for navigation
navToggle.addEventListener('click', () => {
    if (navList.getAttribute("onScreen") === "false"){
        navList.setAttribute("onScreen", 'true');
        navToggle.src = baseUrl + "/static/img/hamcross.svg";
    }else{
        navList.setAttribute("onScreen", 'false');
        navToggle.src = baseUrl + "/static/img/ham.svg";
    }
})


// redirects
function selfRedirect(path){
    location.replace(path);

}