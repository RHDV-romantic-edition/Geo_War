function getParams(selector) {
    var src = $(selector)
        .attr("src")
        .split("?");
    var args = src[src.length - 1]; // выбираем последнюю часть src после ?
    args = args.split("&"); // разбиваем параметры &
    var parameters;
    for (var i = args.length - 1; i >= 0; i--) { // заносим параметры в результирующий объект
        var parameter = args[i].split("=");
        parameters = parameter[1];
    }
    return parameters;
}

var myMap;
// Дождёмся загрузки API и готовности DOM.
ymaps.ready(init);

function init() {
    var team = getParams("#script") // Get Team Code (color)
    // Создание экземпляра карты и его привязка к контейнеру с заданным id ("map").
    myMap = new ymaps.Map('map', {
        center: [
            55.76, 37.64
        ], // Москва
        zoom: 10
    }, {searchControlProvider: 'yandex#search'});
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
                    'team': team
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
            var StartX = Math.floor(coords[0] / 0.0006) * 0.0006
            var StartY = Math.floor(coords[1] / 0.0006) * 0.0006
            console.log(team)
            rectangle = new ymaps.Rectangle([
                // Задаем координаты диагональных углов прямоугольника.
                [
                    StartX, StartY
                ],
                [
                    StartX + 0.0006,
                    StartY + 0.001
                ]
            ], {
                //Свойства hintContent: '',
                balloonContent: 'Прямоугольник 1'
            }, {
                // Опции. Цвет и прозрачность заливки.
                fillColor: data[cell],
                // Дополнительная прозрачность заливки.. Итоговая прозрачность будет не
                // #33(0.2), а 0.1(0.2*0.5).
                fillOpacity: 0.1,
                // Цвет обводки.
                strokeColor: '{{team}}',
                // Прозрачность обводки.
                strokeOpacity: 1,
                // Ширина линии.
                strokeWidth: 2,
                // Радиус скругления углов. Данная опция принимается только прямоугольником.
                borderRadius: 0
            });

            myMap
                .geoObjects
                .add(rectangle)
        });
    // {"southwest":{"lng":37.62931,"lat":55.742373},"northeast":{"lng":37.629358,
    // "lat":55.7424}}
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
                        ]
                    ], {
                        //Свойства hintContent: '',
                        balloonContent: 'Прямоугольник 1'
                    }, {
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
                    });

                    myMap
                        .geoObjects
                        .add(rectangle)
                }
            });
    }
    async function Update() {
        CheckDelta()
    }

    var data = {{my_data|safe}};
    for (var cell in data) {
        cords = cell.split(';')
        console.log('PRINTED')
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
            ]
        ], {
            //Свойства hintContent: '', balloonContent: 'Прямоугольник 1'
        }, {
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
        });

        myMap
            .geoObjects
            .add(rectangle)
    }
    let timerId = setInterval(() => Update(), 500);
    //await Update()
    // ----------------------------
}