
   var mymap;
   var maplink;
   var coords;
   var mrkCurrentLocation;


    $(document).ready(function(){


        mymap = L.map('map').setView([-0.456, 34.899],14);
        mapLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>';
        L.tileLayer(
            'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; ' + mapLink + ' Contributors',
            maxZoom: 18,
            }).addTo(mymap);

        mymap.on('contextmenu', function(e){
          var dtCurrentTime = new Date();
          L.marker(e.latlng).addTo(mymap).bindPopup(e.latlng.toString()+ "<br><hr>"+dtCurrentTime.toString());
        });

        mymap.on('keypress', function(e){
             console.log(e);
        });



              // mymap.on('keypress', function(e){
        //   if (e.originalEvent.key == 'l'){
        //     mymap.locate();
        //   }
        // })
        // mymap.on('locationfound', function(e){
        //   if (mrkCurrentLocation){
        //     mrkCurrentLocation.remove();
        //   }
        //   L.circle(e.latlng, {radius=e.accuracy/2}).addTo(mymap);
        //   mymap.setView(e.latlng,14);
        // });

        mymap.on('locationerror', function(e){
          alert("location not found.")
        });

        $.getJSON('census.geojson', function(data){
              console.log(data);
        });

        mymap.on('click', function (e) {
             coords= e.latlng.lat + ", " + e.latlng.lng;
              data={lat:e.latlng.lat,lng:e.latlng.lng};
              console.log(e.latlng.lat)
           $.get('https://api.darksky.net/forecast/98dc6f6407c5665584ea47af7d7fd81d/-0.54657,35.738769', function(data){
                    console.log(data);});
        

           $.ajax({
            contentType: 'application/json',
            url:'/data',
            dataType : 'json',
            data: JSON.stringify(data),
            type: 'POST',
            success: function(response){
                console.log(response);
                  
            },
            error: function(error){
                console.log(error);
            }

           });


          });


        });