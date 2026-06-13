\\ convert kilometer from miles in javascript
function convert() {
        var kms = document.getElementById("Kms").value;
        const factor = 0.621371;
        var miles = kms * factor;
        alert(miles);
       }
convert()