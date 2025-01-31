// LEAFLET + LEAFLET VELOCITY PLUGIN
function initMap() {
  var World = L.tileLayer(
    'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
    {
      maxZoom: 19,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }
  );

  var baseLayers = {
    Default: World,
  };

  var map = L.map("map", {
    layers: [World]
  });

  var layerControl = L.control.layers(baseLayers);
  layerControl.addTo(map);
  map.setView([43.68, -79.64], 13);

  var markerLayer = L.layerGroup().addTo(map);


  return {
    map: map,
    layerControl: layerControl,
    markerLayer: markerLayer
  };
}

var mapStuff = initMap();
var map = mapStuff.map;
var layerControl = mapStuff.layerControl;
var markerLayer = mapStuff.markerLayer;

var planeIcon = L.icon({
  iconUrl: 'planeicon.png', // png is 1616x940
  iconSize: [33, 20], // Size of the icon (width, height)
  iconAnchor: [16, 10], // Point of the icon that corresponds to the marker's location
  popupAnchor: [0, -10] // Point from which the popup should open relative to the iconAnchor
});

$.getJSON("winddata.json", function (data) {
  var velocityLayer = L.velocityLayer({
    displayValues: true,
    displayOptions: {
      velocityType: "Global Wind",
      position: "bottomleft",
      emptyString: "No wind data"
    },
    data: data,
    maxVelocity: 15
  });

  layerControl.addOverlay(velocityLayer, "Wind Speed/Direction Overlay");
});
// LEAFLET + LEAFLET VELOCITY PLUGIN


// Update aircraft data
function getaircraftdata() {
  $.getJSON("aircraftdata.json", function (data) {
    console.log(data);

    let onething = data[0];
    console.log(onething);

    console.log(onething.callsign);

    markerLayer.clearLayers();
    // Add new markers for each aircraft
    data.forEach(function (aircraft) {
      var lat = aircraft.latitude;
      var lng = aircraft.longitude;
      var callsign = aircraft.callsign;
      var true_track = Math.round(aircraft.true_track);
      var velocity = Math.round(aircraft.velocity * 1.94384);
      var altitude = aircraft.baro_altitude;

      if (altitude == null)
        altitude = 0;
      else
        altitude = Math.round(altitude * 3.28084);

      if (lat && lng) {
        var marker = L.marker([lat, lng], { icon: planeIcon, rotationAngle: aircraft.true_track - 45 }).addTo(markerLayer);
        marker.bindPopup(`Callsign: ${callsign} <br> Heading: ${true_track} <br> Speed: ${velocity} kt <br> Altitude: ${altitude} ft`);
      }
    });
  });
}

getaircraftdata();
setInterval(getaircraftdata, 10000)// 10 seconds in milliseconds
layerControl.addOverlay(markerLayer, "Aircraft Markers");