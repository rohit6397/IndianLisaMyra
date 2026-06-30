function loginUser(){

let username =
document.getElementById("username").value;

let password =
document.getElementById("password").value;

if(password === username + "@#$"){

window.location.href =
"membership.html";

}

else{

alert("Invalid Username or Password");

}

}
