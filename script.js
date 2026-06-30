function createUser(){

let name =
document.getElementById("name").value;

let username =
name.toLowerCase()
.replace(/\s/g,'');

let password =
username + "@#$";

alert(

"Username : "

+ username +

"\nPassword : "

+ password

);

}
