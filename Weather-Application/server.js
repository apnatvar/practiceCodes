const express = require('express') // set up the express js server
const app = express() // initialising
const port = 8080 // selecting a port
const path = require("path")
const fetch = require("node-fetch") // to use fetch api. Might need to install this module before using.
const { nextTick } = require('process')
const { start } = require('repl')

let publicPath = path.resolve(__dirname, "public")
app.use(express.static(publicPath))

app.get('/', (req, res) => {
  res.sendFile(__dirname+'/index.html');
}) // launch the html file for the client

app.get('/weather-report/:lat/:long/:city/:country', getWeatherAndPollution) // call the function to prepare an API for the weather report if the client requests it.
app.get('/get-coord/:query', getCoordinates) // call the function to return coordinates of the place requested to the client
app.get('/get-name/:lat/:long', getName) // call the function for reverse geotagging to get the name from the co-ordinates
app.get('/get-pollution/:lat/:long', getPollution) // call the function to return pollutant information to the client.

app.listen(port, () => {
  console.log(`Listening at http://localhost:${port}/`) // announce which port is being used to listen to new connections
})

function getName(req, res) {
  let lat = parseFloat(req.params.lat).toFixed(2); // read longitude correct to 2 decimal places
  let long = parseFloat(req.params.long).toFixed(2); // read latitude correct to 2 decimal places
  let api_key = 'ffd49641aa83e2319c2fb22e4d710ac0'; 
  let url_name = 'http://api.openweathermap.org/geo/1.0/reverse?';
  fetch( `${url_name}lat=${lat}&lon=${long}&limit=2&appid=${api_key}` ) // request data from openweathermap.org
  // since it is a promise
  .then( response => { 
    return response.json(); // we resolve the data into json
  })
  .then( data => { // then process it to return to the client
    var to_return = {
      city: data[0].name,
      country: data[0].country
    };
    res.json(to_return);
  })
}

function getCoordinates(req, res) {
  let q = req.params.query; // get the city name and country code from the client
  let api_key = 'ffd49641aa83e2319c2fb22e4d710ac0';
  let url_coord = 'http://api.openweathermap.org/geo/1.0/direct?';
  fetch( `${url_coord}q=${q}&limit=1&appid=${api_key}` ) // request api from the geotagging API
  // since it is a promise
  .then( response => { 
    return response.json(); // we resolve the data into json
  })
  .then( data => { // then process it to return to the client
    var to_return = {
      lat: data[0].lat,
      lon: data[0].lon,
    };
    res.json(to_return);
  })
}

function getWeatherAndPollution(req, res) {
  let lat = parseFloat(req.params.lat).toFixed(2); // read latitude correct to 2 decimal places
  let long = parseFloat(req.params.long).toFixed(2); // read longitude correct to 2 decimal places
  let api_key = 'ffd49641aa83e2319c2fb22e4d710ac0';
  let url_weather = 'https://api.openweathermap.org/data/3.0/onecall?';
  fetch( `${url_weather}lat=${lat}&lon=${long}&appid=${api_key}` ) // fetch data from openweathermap.org
    // since it is a promise
    .then( response => { 
      return response.json(); // we resolve the data into json
    })
    .then( data => { // then process it to return to the client
      var to_return = [
        {
          day: "Today",
          city: req.params.city,
          country: req.params.country,
          rain: (data.daily[0].rain == null ? 0 : data.daily[0].rain), // if there is no rain, the rain parameter is absent from the api
          avg_temp: (data.daily[0].temp.max + data.daily[0].temp.min) / 2, // averaging daily minimum and maximum to have a baseline temperature for the day
          weather: data.daily[0].weather[0].main,
          weather_desc: data.daily[0].weather[0].description,
          wind_speed: data.daily[0].wind_speed
        },
        { 
          day: "Day 1",
          city: req.params.city,
          country: req.params.country,
          rain: (data.daily[1].rain == null ? 0 : data.daily[1].rain), // if there is no rain, the rain parameter is absent from the api
          avg_temp: (data.daily[1].temp.max + data.daily[1].temp.min) / 2,
          weather: data.daily[1].weather[0].main,
          weather_desc: data.daily[1].weather[0].description,
          wind_speed: data.daily[1].wind_speed
        },
        {
          day: "Day 2",
          city: req.params.city,
          country: req.params.country,
          rain: (data.daily[2].rain == null ? 0 : data.daily[2].rain), // if there is no rain, the rain parameter is absent from the api
          avg_temp: (data.daily[2].temp.max + data.daily[2].temp.min) / 2,
          weather: data.daily[2].weather[0].main,
          weather_desc: data.daily[2].weather[0].description,
          wind_speed: data.daily[2].wind_speed
        },
        {
          day: "Day 3",
          city: req.params.city,
          country: req.params.country,
          rain: (data.daily[3].rain == null ? 0 : data.daily[3].rain), // if there is no rain, the rain parameter is absent from the api
          avg_temp: (data.daily[3].temp.max + data.daily[3].temp.min) / 2,
          weather: data.daily[3].weather[0].main,
          weather_desc: data.daily[3].weather[0].description,
          wind_speed: data.daily[3].wind_speed
        }
      ]
      res.json(to_return);
    });
}

function getPollution(req, res){
  let lat = parseFloat(req.params.lat).toFixed(2); // read latitude correct to 2 decimal places
  let long = parseFloat(req.params.long).toFixed(2); // read longitude correct to 2 decimal places
  let api_key = 'ffd49641aa83e2319c2fb22e4d710ac0';
  let url_pollution = 'http://api.openweathermap.org/data/2.5/air_pollution/forecast?';

  var today = new Date(); // today's date
  // var dd = String(today.getDate()).padStart(2, '0');
  // var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
  // var yyyy = today.getFullYear();
  // today = new Date(mm + '/' + dd + '/' + yyyy);
  var start = Math.floor(today.getTime() / 1000); // today's date but in unix format
  var last_day = new Date(today.setDate(today.getDate() + 4)) // date 4 days later
  var end = Math.floor(last_day.getTime() / 1000); // date 4 days  later in unix format

  fetch( `${url_pollution}lat=${lat}&lon=${long}&start=${start}&end=${end}&appid=${api_key}` ) // fetch data from openweathermap.org
    // since it is a promise
    .then( response => { 
      return response.json(); // we resolve the data into json
    })
    .then( data => { // then process it to return to the client
      console.log(data.list);
      res.json(data.list);
    });
  }