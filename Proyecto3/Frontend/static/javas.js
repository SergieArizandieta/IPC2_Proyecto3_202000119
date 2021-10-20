let input = document.querySelector('input');
let textareaEntrada = document.getElementById('Exditor_Entrada');
let textareaSalida = document.getElementById('Exditor_Salida');



input.addEventListener('change', () => {
    let files = input.files;
    if(files.length == 0) return;
    const file = files[0];
    let reader = new FileReader();
    reader.onload = (e) => {
        const file = e.target.result;
        const lines = file.split(/\r\n|\n/);
        textareaEntrada.value = lines.join('\n');
    };
    reader.onerror = (e) => alert(e.target.error.name);
    reader.readAsText(file); 
    
});


function botonLimpiar(){
        
    let texto = "";
    textareaSalida.value = texto;
    textareaEntrada.value = texto;


}

