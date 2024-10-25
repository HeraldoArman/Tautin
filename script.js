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

document.querySelectorAll('.copy-icon').forEach(icon => {
    icon.addEventListener('click', function() {
        // Cari elemen .short-link terdekat dengan ikon yang diklik
        let linkText = icon.previousElementSibling.textContent;
        
        // Buat elemen input sementara
        let tempInput = document.createElement('input');
        tempInput.value = linkText;
        document.body.appendChild(tempInput);
        
        // Pilih teks dan salin ke clipboard
        tempInput.select();
        document.execCommand('copy');
        
        // Hapus elemen input sementara
        document.body.removeChild(tempInput);
        
        // Tambahkan kelas "active" ke ikon dan tampilkan teks
        icon.classList.add('active');
        
        // Hapus kelas "active" setelah 1 detik
        setTimeout(function() {
            icon.classList.remove('active');
        }, 3000);
    });
});