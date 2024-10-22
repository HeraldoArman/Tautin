document.addEventListener('DOMContentLoaded', function() {
    const paragraf = document.querySelector('.deskripsi'); // Menggunakan querySelector dengan class
    if (paragraf) {
        console.log('Paragraf ditemukan!');
        const kalimat = paragraf.innerHTML;
        
        // Pisahkan teks menjadi kata-kata dan bungkus dengan <span>
        const kataBerSpan = kalimat.split(' ').map(kata => `<span>${kata}</span>`).join(' ');

        // Ganti konten paragraf dengan teks yang sudah diubah
        paragraf.innerHTML = kataBerSpan;
    } else {
        console.error('Paragraf tidak ditemukan!');
    }
});
