document.addEventListener('DOMContentLoaded', function() {
    const paragraf = document.querySelector('.deskripsi'); 
    if (paragraf) {
        console.log('Paragraf ditemukan!');
        const kalimat = paragraf.innerHTML;
        

        const kataBerSpan = kalimat.split(' ').map(kata => `<span>${kata}</span>`).join(' ');

        paragraf.innerHTML = kataBerSpan;
    } else {
        console.error('Paragraf tidak ditemukan!');
    }
});

document.querySelectorAll('.copy-icon').forEach(icon => {
    icon.addEventListener('click', function() {
        let linkText = icon.previousElementSibling.textContent;
        let tempInput = document.createElement('input');

        tempInput.value = linkText;
        document.body.appendChild(tempInput);
        tempInput.select();
        document.execCommand('copy');

        document.body.removeChild(tempInput);

        icon.classList.add('active');
        setTimeout(function() {
            icon.classList.remove('active');
        }, 3000);
    });
});