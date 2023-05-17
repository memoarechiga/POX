function Random() {
    var rnd = Math.floor(Math.random() * 1000000000);
    document.getElementById('slug').value = rnd;
}

function Random2() {
    var rnd = Math.floor(Math.random() * 10000000);
    document.getElementById('ref_pago').value = rnd;
}