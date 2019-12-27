new Vue({
    el:'#app',
    data:{
        num: "",
        entered: false,
        team: 'Red'
    },
    methods:{
        enter:function(){
            this.entered=true;
            console.log(this.entered);

            //...............................
            var map = L.map('map').setView([0, 0], 19);
            L.yandex('yandex#map').addTo(map);
            map.addEventListener("click", function(e){
                console.log(e.latlng);
            });

            function drawGrid() 
            {
                const zoom = map.getZoom();
                const loadFeatures = zoom > 17;

                if (loadFeatures) { // Zoom level is high enough
                var ne = map.getBounds().getNorthEast();
                var sw = map.getBounds().getSouthWest();

                // Call the what3words Grid API to obtain the grid squares within the current visble bounding box
                what3words.api
                    .gridSectionGeoJson({
                    southwest: {
                        lat: sw.lat, lng: sw.lng
                    },
                    northeast: {
                        lat: ne.lat, lng: ne.lng
                    }
                    }).then(function(data) {
                    // If the grid layer is already present, remove it as it will need to be replaced by the new grid section
                    if (typeof grid_layer !== 'undefined') {
                        map.removeLayer(grid_layer);
                    }

                    // Create a new GeoJSON layer, based on the GeoJSON returned from the what3words API
                    grid_layer = L.geoJSON(data, {
                        style: function() {
                        return {
                            color: '#777',
                            stroke: true,
                            weight: 0.5
                        };
                        }
                    }).addTo(map);
                    }).catch(console.error);
                } 
                else 
                {
                // If the grid layer already exists, remove it as the zoom level no longer requires the grid to be displayed
                if (typeof grid_layer !== 'undefined') 
                {
                    map.removeLayer(grid_layer);
                }
                }
            }

            map.whenReady(drawGrid);
            map.on('move', drawGrid);
            //.........................................
   
    },
        clr:function(){
            document.documentElement.style.setProperty('--btn-color', this.team);
        }
},
    computed:{

    },

}); 
//document.querySelector('.team-select').addEventListener("click", function(){
    
// /*color: blue violet blueviolet green lightgreen lightblue yellow red coral orange cyan hotpink;  */
