document.addEventListener("DOMContentLoaded", function () {  document.getElementById("getTestFormByCat").addEventListener("submit", function (event) {
    event.preventDefault();

    const cat1 = document.getElementById('cat1').value;
    const cat2 = document.getElementById('cat2').value;
    const cat3 = document.getElementById('cat3').value;
    const quizNumb = document.getElementById('quizNumb').value;

    const url = new URL('/gettest/', window.location.origin);
    // const url = new URL('https://kopa.ge/gettest/', window.location.origin);
    url.searchParams.append('cat1', cat1);
    url.searchParams.append('cat2', cat2);
    url.searchParams.append('cat3', cat3);
    url.searchParams.append('quizNumb', quizNumb);

    console.log(url);

    fetch(url, { method: 'GET' })
        .then(response => response.json())
        .then(data => {
            if (data.detail) {
                document.getElementById('responseApi').innerHTML = data.detail;
            } else {
                document.getElementById('responseApi').innerHTML = JSON.stringify(data);
            }
        })
        .catch(error => console.error('Error:', error));
});


});



document.addEventListener("DOMContentLoaded", function () {  document.getElementById("getTestFilter").addEventListener("submit", function (event) {
    event.preventDefault();
    console.log('getTestFilter')
    const catFilter = document.getElementById('catFilter').value;

    const url = new URL('/catFilter/', window.location.origin);
    // const url = new URL('https://kopa.ge/catFilter/', window.location.origin);
    url.searchParams.append('catFilter', catFilter);

    console.log(url);

    fetch(url, { method: 'GET' })
        .then(response => response.json())
        .then(data => {
            if (data.detail) {
                document.getElementById('responseApi').innerHTML = data.detail;
            } else {
                document.getElementById('responseApi').innerHTML = JSON.stringify(data);
            }
        })
        .catch(error => console.error('Error:', error));
});


});











