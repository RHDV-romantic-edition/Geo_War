var myMap;
// Дождёмся загрузки API и готовности DOM.
ymaps.ready(init);
function init() {
    // Создание экземпляра карты и его привязка к контейнеру с заданным id ("map").
    myMap = new ymaps.Map('map', {
        center: [
            55.76, 37.64
        ], // Москва
        zoom: 15
    }, {searchControlProvider: 'yandex#search'});

    myMap.addListener('bounds_changed', function () {
        const zoom = map.getZoom();
        const loadFeatures = zoom > 17;

        if (loadFeatures) { // Zoom level is high enough
            var ne = map
                .getBounds()
                .getNorthEast();
            var sw = map
                .getBounds()
                .getSouthWest();

            // Call the what3words Grid API to obtain the grid squares within the current
            // visble bounding box
            what3words
                .api
                .gridSectionGeoJson({
                    southwest: {
                        lat: sw.lat(),
                        lng: sw.lng()
                    },
                    northeast: {
                        lat: ne.lat(),
                        lng: ne.lng()
                    }
                })
                .then(function (data) {
                    if (gridData !== undefined) {
                        for (var i = 0; i < gridData.length; i++) {
                            map
                                .data
                                .remove(gridData[i]);
                        }
                    }
                    gridData = map
                        .data
                        .addGeoJson(data);
                })
                .catch(console.error);
        }

        // Set the grid display style
        map
            .data
            .setStyle({visible: loadFeatures, strokeColor: '#777', strokeWeight: 0.5});
        // {"southwest":{"lng":37.62931,"lat":55.742373},"northeast":{"lng":37.629358,
        // "lat":55.7424}}
    });
    async function CheckDelta() {
        var Url = 'http://127.0.0.1:8000/home/get_delta/'
        var delta = 0
        axios
            .get(Url)
            .then((response) => {
                    delta = (response.data);
                    console.log('kek')
                    console.log(delta)
                    console.log('kek')

                    for (var cell in delta) {
                        cords = cell.split(';')
                        rectangle = new ymaps.Rectangle([
                                // Задаем координаты диагональных углов прямоугольника.
                                [
                                    parseFloat(cords[3]),
                                    parseFloat(cords[0])
                                ],
                                [
                                    parseFloat(cords[2]),
                                    parseFloat(cords[1])
                                ],
                                {
                                    //Свойства hintContent: '', balloonContent: 'Прямоугольник 1'
                                },
                                {
                                    // Опции. Цвет и прозрачность заливки.
                                    fillColor: data[cell],
                                    // Дополнительная прозрачность заливки.. Итоговая прозрачность будет не
                                    // #33(0.2), а 0.1(0.2*0.5).
                                    fillOpacity: 0.1,
                                    // Цвет обводки.
                                    strokeColor: '#0000FF',
                                    // Прозрачность обводки.
                                    strokeOpacity: 1,
                                    // Ширина линии.
                                    strokeWidth: 2,
                                    // Радиус скругления углов. Данная опция принимается только прямоугольником.
                                    borderRadius: 0
                                }
                            );

                            myMap.geoObjects.add(myRectangle)
                        }
                    }
                );
            }
        async function Update() {
            CheckDelta()
        }
        myMap
            .events
            .add('click', function (e) {
                var coords = e.get('coords');
                Url = 'http://127.0.0.1:8000/home/square_add/'
                axios({
                    method: 'post',
                    url: Url,
                    data: {
                        'cords': coords,
                        'team': "{{team}}"
                    },
                    xsrfHeaderName: "X-CSRFToken",
                    headers: {
                        "X-CSRFToken": "{{csrf_token}}"
                    }
                })
                    .then(response => {
                        //console.log(response)
                    })
                    .catch(error => {
                        //console.log(error.response)
                    });
            });
        var data = {{my_data|safe}};
        for (var cell in data) {
            cords = cell.split(';')
            //console.log(cell)

            rectangle = new ymaps.Rectangle([
                    // Задаем координаты диагональных углов прямоугольника.
                    [
                        parseFloat(cords[3]),
                        parseFloat(cords[0])
                    ],
                    [
                        parseFloat(cords[2]),
                        parseFloat(cords[1])
                    ],
                    {
                        //Свойства hintContent: '', balloonContent: 'Прямоугольник 1'
                    },
                    {
                        // Опции. Цвет и прозрачность заливки.
                        fillColor: data[cell],
                        // Дополнительная прозрачность заливки.. Итоговая прозрачность будет не
                        // #33(0.2), а 0.1(0.2*0.5).
                        fillOpacity: 0.1,
                        // Цвет обводки.
                        strokeColor: '#0000FF',
                        // Прозрачность обводки.
                        strokeOpacity: 1,
                        // Ширина линии.
                        strokeWidth: 2,
                        // Радиус скругления углов. Данная опция принимается только прямоугольником.
                        borderRadius: 0
                    }
                );

                myMap.geoObjects.add(myRectangle)
            }
            let timerId = setInterval(() => Update(), 500);
            //await Update() ////
        }