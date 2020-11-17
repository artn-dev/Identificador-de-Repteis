function set_border() {
    drop_area = document.getElementById("drop-area")
    drop_area.style.border = "0.7rem dashed #3482d0";
}
function clear_border() {
    drop_area = document.getElementById("drop-area")
    drop_area.style.border = "none";
}

function allowDrop(ev) {
    ev.preventDefault();
}
function getBase(image) {
    new Promise((resolve, reject) => {
        const reader = new FileReader()
        reader.onloadend = () => resolve(reader.result)
        reader.onerror = reject
        reader.readAsDataURL(image)
    }).then(res => {
        console.log(res)
    })
}

async function drop(ev) {
    ev.preventDefault();
    const data = ev.dataTransfer.getData('text/html');
    let url;

    if (data === '') {
        const image = ev.dataTransfer.items[0].getAsFile()
        await new Promise((resolve, reject) => {
            const reader = new FileReader()
            reader.onloadend = () => resolve(reader.result)
            reader.onerror = reject
            reader.readAsDataURL(image)
        }).then(res => {
            url = res;
        })
    } else {
        const div = $("<div>").append(data);
        url = $(div).find("img").attr('src');
    }
    console.log(url)
    document.querySelector("img#imagem").src = url;

    const result = document.querySelector(".result p");
    result.style.display = "none";
}

function recognizer(event) {
    var image = document.querySelector("#imagem").src;
    
    if (!(image.slice(0, 11) == "data:image/")) {
        eel.getDataFromUrl(image)((res) => {
            image = res;
        })
    } 
    eel.recognize(image)((res) => {
        const result = document.querySelector(".result p");
        result.innerHTML = `Tenho ${res[1]}% de certeza que é ${res[0]}`
        result.style.display = "flex";
    });
}