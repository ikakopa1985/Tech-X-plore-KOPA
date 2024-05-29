document.addEventListener("DOMContentLoaded", function () {
    const token = localStorage.getItem('token');

    if (!token) {
        console.error('Token not found in local storage');

    }
    else{
         apiRequest('/api/user-profile/', 'GET')
            .then(profileData => {
                console.log('Authenticated!');
                console.log('User Profile Data:', profileData);
                document.getElementById('token').innerHTML =
                    document.getElementById('token').innerHTML +
                    '           wellcome   '+
                    '            \n    '+
                    'email=' + profileData['email'] +
                    '            \n    '+
                    'username= ' + profileData['username']
            });
    }

    function apiRequest(url, method, data = null, tokenRequired = true) {
        const headers = { 'Content-Type': 'application/json' };
        if (tokenRequired && token) {
            headers['Authorization'] = `Bearer ${token}`;
        }

        return fetch(url, {
            method: method,
            headers: headers,
            body: data ? JSON.stringify(data) : null
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Network response was not ok: ${response.statusText}`);
            }
            return response.json();
        })
        .catch(error => {
            console.error('There was a problem with your fetch operation:', error);
            throw error;
        });
    }

    // Login form
    document.getElementById("loginForm").addEventListener("submit", function (event) {
        event.preventDefault();
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        apiRequest('/api/token/', 'POST', { username, password }, false)
            .then(data => {
                localStorage.setItem('token', data.access);
                document.getElementById('token').innerHTML = `Token: ${data.access}`;
                // const token = data.access
                return apiRequest('/api/user-profile/', 'GET');
            })
            .then(profileData => {
                console.log('Authenticated!');
                console.log('User Profile Data:', profileData);
                document.getElementById('token').innerHTML =
                    document.getElementById('token').innerHTML +
                    '            \n    '+
                    'email=' + profileData['email'] +
                    '            \n    '+
                    'username= ' + profileData['username']
            });
         // window.location.reload();
    });

    // Pagination
    document.getElementById("paginBut").addEventListener("click", function () {
        const page = document.getElementById("paginKeyword").value;
        apiRequest(`/testlist`, 'GET')
            .then(data => {
                document.getElementById('responseApi').innerHTML = JSON.stringify(data);
            });
    });

});


