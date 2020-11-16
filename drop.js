drop_area = document.getElementById("drop-area")

function set_border() {
    drop_area.style.border = "0.7rem dashed #3482d0";
}
function clear_border() {
    drop_area.style.border = "none";
}

function allowDrop(ev) {
    ev.preventDefault();
}
function drop(ev) {
    ev.preventDefault();
    const data = ev.dataTransfer.getData('text/html');

    const div = $("<div>").append(data);
    const url = $(div).find("img").attr('src');
    document.querySelector("img#imagem").src = url;
}

