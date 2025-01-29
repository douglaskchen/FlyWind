import data from "./sample.json" with { type: 'json' };
console.log(data);


let onething = data[0];
console.log(onething);

console.log(onething.callsign);

var loc = window.location.pathname;
console.log(loc);






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
  
    return {
      map: map,
      layerControl: layerControl
    };
  }
  

  
  var mapStuff = initMap();
  var layerControl = mapStuff.layerControl;

  $.getJSON("./leaflet-velocity/demo/wind-global.json",function(data) {
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
  
    layerControl.addOverlay(velocityLayer, "Wind - Global");
  });