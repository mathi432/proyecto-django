var form = document.getElementById("formulario");
var nombre = document.getElementById("nombreDueño");
var contra1 = document.getElementById("password");
var men = document.getElementById("mensaje");

form.addEventListener("submit", e=>{

    e.preventDefault();

    let men = "";
    enter = false;


/* Validaciones contraseña */

if (nombre.value.length < 8){

    men += "La contraseña debe tener más de 8 cáracteres <br>"
    enter = true;
}




/* letras minúsculas */
if (contra1.value.match(/[a-z]/g)){

} else{
        
    men += "La contraseña debe tener al menos una letra minúscula <br>"
    enter = true;
}

/* carácteres especiales */
if (contra1.value.match(/[@-_!#$%&]/g)){

} else{
        
    men += "La contraseña debe tener al menos un cáracter especial <br>"
    enter = true;
}






if (enter){

    mensaje.innerHTML = men

} else {

    mensaje.innerHTML = "Bienvenido doctor/a"


}




})