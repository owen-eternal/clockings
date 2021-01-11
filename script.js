const canvas = document.getElementById('canvas');
const btnUpload = document.getElementById('btnUpload')
const ctx = canvas.getContext("2d");

const setupCanvas = ()=> {
    ctx.fillStyle = "#ccc";
    ctx.rect(0, 0, canvas.width, canvas.height);
    ctx.fill(); 
    ctx.fillStyle = "Blue";
    ctx.font = "35px serif";
    ctx.fillText("decode this bitch", 30, 60);
}

function init() {

    const base64 = canvas.toDataURL().split(",")[1];

    const data = {
      "generated_at" : new Date().toISOString(),
      "png": base64, 
    };

    const options = {
        method: 'POST',
        cache: 'no-cache',
        body: JSON.stringify(data),
        headers: { "Content-Type" : "application/json"}
    }
    
    fetch('http://127.0.0.1:5000/upload', options);
   
}

setupCanvas()
btnUpload.addEventListener('click', init)







