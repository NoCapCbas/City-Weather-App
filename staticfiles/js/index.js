const container = document.querySelector('.container');
const search = document.querySelector('.search-box button');
const weatherBox = document.querySelector('.weather-box');
const weatherDetails = document.querySelector('.weather-details');
const error404 = document.querySelector('.not-found');
const wave01 = document.querySelector('.wave-01');
const wave02 = document.querySelector('.wave-02');
const wave03 = document.querySelector('.wave-03');

search.addEventListener('click', (event) => {
    event.preventDefault();
    // Grab form
    var weather_form = document.querySelector('#weather-form');

    var xhr = new XMLHttpRequest();
    url = '/getWeather/';

    // Isolate form data
    var formData = new FormData(weather_form);
    // Serialize the form data to query string
    var serializedData = new URLSearchParams(formData).toString();

    // Append the serialized data to the url
    url = url + '?' + serializedData;

    xhr.open('GET', url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onload = function(){
        if (xhr.status >= 200 && xhr.status < 400){
            // console.log('Handle Response Successful');
            // Handle response data
            error404.style.display = 'none';
            error404.classList.remove('fadeIn');

            const image_element = document.querySelector('.weather-box img');
            const temperature_element = document.querySelector('.weather-box .temperature');
            const description_element = document.querySelector('.weather-box .description');
            const humidity_element = document.querySelector('.weather-details .humidity span');
            const wind_element = document.querySelector('.weather-details .wind span');
            const country_element = document.querySelector('.weather-box .country');

            var returned_json = JSON.parse(xhr.responseText);
            // console.log(returned_json);
            var data = returned_json.data;
            if (returned_json['success'] == false){
                // console.log('Handle Weather API Response Error');
                // Handle response error
                wave01.classList.add('active');
                wave02.classList.add('active');
                wave03.classList.add('active');
                container.style.height = '400px';
                weatherBox.style.display = 'none';
                weatherDetails.style.display = 'none';
                error404.style.display = 'block';
                error404.classList.add('fadeIn');
                return;
            } else{
                wave01.classList.add('active');
                wave02.classList.add('active');
                wave03.classList.add('active');
                const temperature = data['main'].temp + '°F';
                const wind_speed = data['wind'].speed + 'Km/h';
                const humidity = data['main'].humidity + '%';
                const country = data['sys'].country;
                const weather = data['weather'][0]['main'];
                const weather_desc = data['weather'][0]['description'];
                const weather_icon = "http://openweathermap.org/img/w/" + data['weather'][0]['icon'] + ".png";

                temperature_element.textContent = temperature;
                description_element.textContent = weather_desc;
                humidity_element.textContent = humidity;
                wind_element.textContent = wind_speed;
                temperature_element.textContent = temperature;
                image_element.src = weather_icon;
                // country_element.textContent = country;

                container.style.height = '400px';
                weatherBox.style.display = 'flex';
                weatherDetails.style.display = 'flex';
                error404.style.display = 'none';
                error404.classList.remove('fadeIn');
            }
            
            

        } else {
            // console.log('Handle Response Error');
            // Handle response error
            wave01.classList.add('active');
            wave02.classList.add('active');
            wave03.classList.add('active');
            container.style.height = '400px';
            weatherBox.style.display = 'none';
            weatherDetails.style.display = 'none';
            error404.style.display = 'block';
            error404.classList.add('fadeIn');
            return;
        }
    }

    xhr.onerror = function(){
        // Handle request error
    }
    
    // Send request
    xhr.send();
})