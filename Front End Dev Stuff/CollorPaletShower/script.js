function submitFunction(){
    //Get data from the page
    const target = document.getElementById("color-pallet");
    var hexColorCode = document.getElementById("colorHexCode").value;

    //Add the Color Block
    console.log(hexColorCode)
    target.innerHTML += `<div><div style="background-color: ${hexColorCode}; padding:1rem; border:1px solid black;"><p style="background-color: white; color:black;">${hexColorCode}</p></div></div>`
}