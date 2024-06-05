document.addEventListener("DOMContentLoaded", function () {
    const token = localStorage.getItem('token');

    if (!token) {
        console.error('Token not found in local storage');
    }
    else{
         apiRequest('/api/user-profile/', 'GET')
            .then(profileData => {
                // console.log('Authenticated!');
                // console.log('User Profile Data:', profileData);
                document.getElementById('token').innerHTML =
                    document.getElementById('token').innerHTML +
                    '           wellcome   '+
                    '            \n    '+
                    'email=' + profileData['email'] +
                    '            \n    '+
                    'username= ' + profileData['username']
            });
                    console.log('DOMContentLoaded')
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
                document.getElementById('token').innerHTML =
                    `Network response was not ok: ${response.statusText}`
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

                    console.log('loginForm')

    });


    // get test

                function displayTestText(data) {
                    // Find the legend element
                    const testTextElement = document.getElementById('testText');

                    // Get the first element of the array
                    const firstElement = data;

                    // Get the testText from the first element
                    const testText = firstElement.testText;

                    // Wrap the testText in a <span> with bold font and desired font size
                    const styledText = `<span style="font-weight: bold; font-size: 16px;">${testText.replace(/\r\n/g, '<br>')}</span>`;

                    // Insert the styled testText into the legend element
                    testTextElement.innerHTML = styledText;

                    if (data.testImage) {
                        const img = document.createElement('img');
                        img.src = data.testImage;
                        img.alt = 'Image';
                        img.style.maxWidth = '300px'; // Optional: limit the image size
                        document.getElementById('testImageContainer').appendChild(img);
                    }
                }

                // Function to create radio buttons based on answers
                function createRadioButtons(data) {
                    // Find the HTML element to insert the radio buttons into
                    const radioButtonsContainer = document.getElementById('radioButtonsContainer');

                    // Get the first element of the array
                    const firstElement = data;

                    // Get the answers array from the first element
                    const answers = firstElement.answers;

                    // Create radio buttons for each answer
                    answers.forEach((answer, index) => {
                        radioButtonsContainer.appendChild(document.createElement('br'));
                        // Create a radio button input element
                        const radioInput = document.createElement('input');
                        radioInput.type = 'radio';
                        radioInput.id = `answerChoice${index + 1}${answer['is_correct']}`;
                        radioInput.name = 'contact';
                        radioInput.value = answer.id;
                        radioButtonsContainer.appendChild(document.createTextNode('\u00A0'));
                        radioButtonsContainer.appendChild(document.createTextNode('\u00A0'));
                        // Create a label element
                        const label = document.createElement('label');
                        label.setAttribute('for', `answerChoice${index + 1}`);
                        label.innerText = answer.answer_text;

                        // Append the radio button and label to the container
                        radioButtonsContainer.appendChild(radioInput);
                        radioButtonsContainer.appendChild(document.createTextNode('\u00A0'));
                        radioButtonsContainer.appendChild(document.createTextNode('\u00A0'));
                        radioButtonsContainer.appendChild(label);

                        // Check if answers_image exists and create an img element if it does
                        if (answer.answers_image) {
                            const img = document.createElement('img');
                            img.src = answer.answers_image;
                            img.alt = `Image for ${answer.answer_text}`;
                            img.style.maxWidth = '100px'; // Optional: limit the image size
                            radioButtonsContainer.appendChild(img);
                        }

                        // Add a line break for better readability
                        radioButtonsContainer.appendChild(document.createElement('br'));
                    });
                }

    //getTest
   document.getElementById("getTestForm").addEventListener("submit", function (event) {
    event.preventDefault();
    const logical = document.getElementById('logicChekbox').checked;
    const math = document.getElementById('mathChekbox').checked;

    const url = new URL('/gettest/', window.location.origin);
    url.searchParams.append('logical', logical);
    url.searchParams.append('math', math);

    fetch(url, { method: 'GET' })
        .then(response => response.json())
        .then(data => {
            if (data.detail) {
                document.getElementById('responseApi').innerHTML = data.detail;
            } else {
                document.getElementById('testText').innerHTML = '';
                document.getElementById('radioButtonsContainer').innerHTML = '';
                document.getElementById('testImageContainer').innerHTML = '';
                document.getElementById('responseApi').innerHTML = JSON.stringify(data);

                displayTestText(data);
                createRadioButtons(data);
                console.log('getTestForm');
            }
        })
        .catch(error => console.error('Error:', error));
});





    //create user
    document.getElementById('userIdentForm').addEventListener('submit', async function(event) {
        event.preventDefault();
        const userData = {
            username: document.getElementById('usernameCreate').value,
            password: document.getElementById('passwordCreate').value,
            email: document.getElementById('email').value,
            first_name: document.getElementById('firstname').value,
            last_name: document.getElementById('lastname').value,
        };
        const userIdentData = {
            full_name: document.getElementById('full_name').value,
            personal_number: document.getElementById('personal_number').value,
            birth_date: document.getElementById('birth_date').value,
            user: userData,
        };
           apiRequest(`/users/`, 'POST', userIdentData)
            .then(data => {
                document.getElementById('token').innerHTML =
                    JSON.stringify(data);
            });
    });



//submit answer
    document.getElementById("submitAnswer").addEventListener("click", function () {
        event.preventDefault();
        // Get all radio buttons with name "contact"
        var radioButtons = document.getElementsByName('contact');

        // Loop through radio buttons to find the checked one
        for (var i = 0; i < radioButtons.length; i++) {
            if (radioButtons[i].checked) {
                if (radioButtons[i].id.includes('true'))
                    {alert(" სწორია ");}
                else{
                    {alert(" არასწორი პასუხი ");}
                }
            }
        }
     });



});





