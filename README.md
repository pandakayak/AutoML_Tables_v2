# AutoML_Tables_v2
AutoML_Tables_Chicago_taxi_fare (An application)


```html
<!DOCTYPE html>
<head>    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    
        <script>
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        </script>
    
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.4.0/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.4.0/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css"/>
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    
            <meta name="viewport" content="width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
            <style>
                #map_66631b96769c4ebdb07c477e972011fb {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
            </style>
        
</head>
<body>    
    
            <div class="folium-map" id="map_66631b96769c4ebdb07c477e972011fb" ></div>
        
</body>
<script>    
    
            var map_66631b96769c4ebdb07c477e972011fb = L.map(
                "map_66631b96769c4ebdb07c477e972011fb",
                {
                    center: [41.895140898, -87.624255632],
                    crs: L.CRS.EPSG3857,
                    zoom: 10,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );

            

        
    
            var tile_layer_ca0dcade1d2443db910f8253cba11309 = L.tileLayer(
                "https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}.png",
                {"attribution": "Map tiles by \u003ca href=\"http://stamen.com\"\u003eStamen Design\u003c/a\u003e, under \u003ca href=\"http://creativecommons.org/licenses/by/3.0\"\u003eCC BY 3.0\u003c/a\u003e. Data by \u0026copy; \u003ca href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\"http://www.openstreetmap.org/copyright\"\u003eODbL\u003c/a\u003e.", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
            var circle_marker_7b1331c699ca4bdfa2240f7f536330e8 = L.circleMarker(
                [41.980264315, -87.913624596],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 3.1285714285714286, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_0d91f19a35d24bafb65ad763f2596f41 = L.popup({"maxWidth": "100%"});

        
            var html_b6ce2b12327c493db3cd686bed4c2b60 = $(`<div id="html_b6ce2b12327c493db3cd686bed4c2b60" style="width: 100.0%; height: 100.0%;">Latitude : 41.980264315<br>                     Longitude : -87.913624596<br>                     frequency : 876<br></div>`)[0];
            popup_0d91f19a35d24bafb65ad763f2596f41.setContent(html_b6ce2b12327c493db3cd686bed4c2b60);
        

        circle_marker_7b1331c699ca4bdfa2240f7f536330e8.bindPopup(popup_0d91f19a35d24bafb65ad763f2596f41)
        ;

        
    
    
            var circle_marker_187138a6cd4e4b4f93f949784f9dd7f1 = L.circleMarker(
                [41.97907082, -87.903039661],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 9.128571428571428, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_918abe9c45864e2793e1767f68c39e39 = L.popup({"maxWidth": "100%"});

        
            var html_16a2a438fec84822a7d331d4072d811e = $(`<div id="html_16a2a438fec84822a7d331d4072d811e" style="width: 100.0%; height: 100.0%;">Latitude : 41.97907082<br>                     Longitude : -87.903039661<br>                     frequency : 2556<br></div>`)[0];
            popup_918abe9c45864e2793e1767f68c39e39.setContent(html_16a2a438fec84822a7d331d4072d811e);
        

        circle_marker_187138a6cd4e4b4f93f949784f9dd7f1.bindPopup(popup_918abe9c45864e2793e1767f68c39e39)
        ;

        
    
    
            var circle_marker_445684f918384ee998c08590eda90b2a = L.circleMarker(
                [41.982775009, -87.8773054],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_75f6e43acab644989c25d53a37eed326 = L.popup({"maxWidth": "100%"});

        
            var html_b94f1da2bbea4e21a2ce82b5c6713d5a = $(`<div id="html_b94f1da2bbea4e21a2ce82b5c6713d5a" style="width: 100.0%; height: 100.0%;">Latitude : 41.982775009<br>                     Longitude : -87.8773054<br>                     frequency : 2<br></div>`)[0];
            popup_75f6e43acab644989c25d53a37eed326.setContent(html_b94f1da2bbea4e21a2ce82b5c6713d5a);
        

        circle_marker_445684f918384ee998c08590eda90b2a.bindPopup(popup_75f6e43acab644989c25d53a37eed326)
        ;

        
    
    
            var circle_marker_919a7b833c1c4715bc15adda7eeb2faf = L.circleMarker(
                [42.007612593, -87.813781034],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.017857142857142856, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_c1bce6fa09694ef6810105560c941beb = L.popup({"maxWidth": "100%"});

        
            var html_e041798069a340bdb975ba28f8fdeea3 = $(`<div id="html_e041798069a340bdb975ba28f8fdeea3" style="width: 100.0%; height: 100.0%;">Latitude : 42.007612593<br>                     Longitude : -87.813781034<br>                     frequency : 5<br></div>`)[0];
            popup_c1bce6fa09694ef6810105560c941beb.setContent(html_e041798069a340bdb975ba28f8fdeea3);
        

        circle_marker_919a7b833c1c4715bc15adda7eeb2faf.bindPopup(popup_c1bce6fa09694ef6810105560c941beb)
        ;

        
    
    
            var circle_marker_f622a90322f845a19394e21ada31f1f3 = L.circleMarker(
                [41.94651142, -87.806020002],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.06428571428571428, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_1b28a7197f0244069dedf5dcc41e312b = L.popup({"maxWidth": "100%"});

        
            var html_2af7a7779286458bb0a49670f01a7054 = $(`<div id="html_2af7a7779286458bb0a49670f01a7054" style="width: 100.0%; height: 100.0%;">Latitude : 41.94651142<br>                     Longitude : -87.806020002<br>                     frequency : 18<br></div>`)[0];
            popup_1b28a7197f0244069dedf5dcc41e312b.setContent(html_2af7a7779286458bb0a49670f01a7054);
        

        circle_marker_f622a90322f845a19394e21ada31f1f3.bindPopup(popup_1b28a7197f0244069dedf5dcc41e312b)
        ;

        
    
    
            var circle_marker_730122d4a4a4481e951c3d18459228bf = L.circleMarker(
                [41.985015101, -87.804532006],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.15, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_4c6e4cfc1cad47d8ae48ee9615277523 = L.popup({"maxWidth": "100%"});

        
            var html_839a27e9c38946aaaafb91004cdabdfb = $(`<div id="html_839a27e9c38946aaaafb91004cdabdfb" style="width: 100.0%; height: 100.0%;">Latitude : 41.985015101<br>                     Longitude : -87.804532006<br>                     frequency : 42<br></div>`)[0];
            popup_4c6e4cfc1cad47d8ae48ee9615277523.setContent(html_839a27e9c38946aaaafb91004cdabdfb);
        

        circle_marker_730122d4a4a4481e951c3d18459228bf.bindPopup(popup_4c6e4cfc1cad47d8ae48ee9615277523)
        ;

        
    
    
            var circle_marker_4d96159661214eaf8f8bc1d585ad92e7 = L.circleMarker(
                [41.929297368, -87.798032181],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_fbd68456723a4b08ba5656806d7fa5e3 = L.popup({"maxWidth": "100%"});

        
            var html_76d7fa768c0142b5ac73647f67c8b77f = $(`<div id="html_76d7fa768c0142b5ac73647f67c8b77f" style="width: 100.0%; height: 100.0%;">Latitude : 41.929297368<br>                     Longitude : -87.798032181<br>                     frequency : 1<br></div>`)[0];
            popup_fbd68456723a4b08ba5656806d7fa5e3.setContent(html_76d7fa768c0142b5ac73647f67c8b77f);
        

        circle_marker_4d96159661214eaf8f8bc1d585ad92e7.bindPopup(popup_fbd68456723a4b08ba5656806d7fa5e3)
        ;

        
    
    
            var circle_marker_93b21e4fb60f43df852c4d05a55b824a = L.circleMarker(
                [41.978829526, -87.771166703],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.35714285714285715, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_67fbb62a01884e0c8b963611ddbd5093 = L.popup({"maxWidth": "100%"});

        
            var html_fce0aac6354d4e9d8d3c6e93f0cc43f9 = $(`<div id="html_fce0aac6354d4e9d8d3c6e93f0cc43f9" style="width: 100.0%; height: 100.0%;">Latitude : 41.978829526<br>                     Longitude : -87.771166703<br>                     frequency : 100<br></div>`)[0];
            popup_67fbb62a01884e0c8b963611ddbd5093.setContent(html_fce0aac6354d4e9d8d3c6e93f0cc43f9);
        

        circle_marker_93b21e4fb60f43df852c4d05a55b824a.bindPopup(popup_67fbb62a01884e0c8b963611ddbd5093)
        ;

        
    
    
            var circle_marker_0de8a599f7e7476d84389a870648f282 = L.circleMarker(
                [41.79259236, -87.769615453],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.9214285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_8ac8bf62792e498b90489b2e1fe7b0da = L.popup({"maxWidth": "100%"});

        
            var html_356fa883e79c457986ab9b2a0e13d46f = $(`<div id="html_356fa883e79c457986ab9b2a0e13d46f" style="width: 100.0%; height: 100.0%;">Latitude : 41.79259236<br>                     Longitude : -87.769615453<br>                     frequency : 258<br></div>`)[0];
            popup_8ac8bf62792e498b90489b2e1fe7b0da.setContent(html_356fa883e79c457986ab9b2a0e13d46f);
        

        circle_marker_0de8a599f7e7476d84389a870648f282.bindPopup(popup_8ac8bf62792e498b90489b2e1fe7b0da)
        ;

        
    
    
            var circle_marker_3db679d90cbb4550ac21947d7ca275ab = L.circleMarker(
                [41.779582888, -87.768510849],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_703d162eb0134e739f9ab0e2789da2c3 = L.popup({"maxWidth": "100%"});

        
            var html_34d61a62f0e94f83a508b0850f001d10 = $(`<div id="html_34d61a62f0e94f83a508b0850f001d10" style="width: 100.0%; height: 100.0%;">Latitude : 41.779582888<br>                     Longitude : -87.768510849<br>                     frequency : 2<br></div>`)[0];
            popup_703d162eb0134e739f9ab0e2789da2c3.setContent(html_34d61a62f0e94f83a508b0850f001d10);
        

        circle_marker_3db679d90cbb4550ac21947d7ca275ab.bindPopup(popup_703d162eb0134e739f9ab0e2789da2c3)
        ;

        
    
    
            var circle_marker_04ee91f6f3e04f078f170fd78218fd8e = L.circleMarker(
                [41.927260956, -87.765501609],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.11428571428571428, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_77bb69c569044e42829d135561aa07f3 = L.popup({"maxWidth": "100%"});

        
            var html_952336f7262840ebbb1985719cb6cdfa = $(`<div id="html_952336f7262840ebbb1985719cb6cdfa" style="width: 100.0%; height: 100.0%;">Latitude : 41.927260956<br>                     Longitude : -87.765501609<br>                     frequency : 32<br></div>`)[0];
            popup_77bb69c569044e42829d135561aa07f3.setContent(html_952336f7262840ebbb1985719cb6cdfa);
        

        circle_marker_04ee91f6f3e04f078f170fd78218fd8e.bindPopup(popup_77bb69c569044e42829d135561aa07f3)
        ;

        
    
    
            var circle_marker_cd213e612fce408bb75c18d26fc071eb = L.circleMarker(
                [41.954027649, -87.763399032],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.19285714285714287, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_22dbc8f57b0140b49dfafe8ee9c98d22 = L.popup({"maxWidth": "100%"});

        
            var html_6026c9393db648458ed403e045439169 = $(`<div id="html_6026c9393db648458ed403e045439169" style="width: 100.0%; height: 100.0%;">Latitude : 41.954027649<br>                     Longitude : -87.763399032<br>                     frequency : 54<br></div>`)[0];
            popup_22dbc8f57b0140b49dfafe8ee9c98d22.setContent(html_6026c9393db648458ed403e045439169);
        

        circle_marker_cd213e612fce408bb75c18d26fc071eb.bindPopup(popup_22dbc8f57b0140b49dfafe8ee9c98d22)
        ;

        
    
    
            var circle_marker_c8e71a2c19fe47fe906e3c159ffb187f = L.circleMarker(
                [41.970288894, -87.759857019],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.017857142857142856, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_3bd025b687a2441fbfc433317e7ff178 = L.popup({"maxWidth": "100%"});

        
            var html_1e90bc3e03294f5d94147a666e4a3dc3 = $(`<div id="html_1e90bc3e03294f5d94147a666e4a3dc3" style="width: 100.0%; height: 100.0%;">Latitude : 41.970288894<br>                     Longitude : -87.759857019<br>                     frequency : 5<br></div>`)[0];
            popup_3bd025b687a2441fbfc433317e7ff178.setContent(html_1e90bc3e03294f5d94147a666e4a3dc3);
        

        circle_marker_c8e71a2c19fe47fe906e3c159ffb187f.bindPopup(popup_3bd025b687a2441fbfc433317e7ff178)
        ;

        
    
    
            var circle_marker_89e698db91134169bf3779ad8cc76128 = L.circleMarker(
                [41.993930128, -87.758353588],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.04642857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_73b84c766af3408eb230211b47cf61d8 = L.popup({"maxWidth": "100%"});

        
            var html_8ed724fafbe24ff2881bccca218f4a8f = $(`<div id="html_8ed724fafbe24ff2881bccca218f4a8f" style="width: 100.0%; height: 100.0%;">Latitude : 41.993930128<br>                     Longitude : -87.758353588<br>                     frequency : 13<br></div>`)[0];
            popup_73b84c766af3408eb230211b47cf61d8.setContent(html_8ed724fafbe24ff2881bccca218f4a8f);
        

        circle_marker_89e698db91134169bf3779ad8cc76128.bindPopup(popup_73b84c766af3408eb230211b47cf61d8)
        ;

        
    
    
            var circle_marker_b555e82617ea4ad2a75b6e5803bf13b3 = L.circleMarker(
                [41.890608853, -87.756046711],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.075, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_1bafbb855e1c4683bc906453169a9b1a = L.popup({"maxWidth": "100%"});

        
            var html_4299c13423b64c04b510fe995911a820 = $(`<div id="html_4299c13423b64c04b510fe995911a820" style="width: 100.0%; height: 100.0%;">Latitude : 41.890608853<br>                     Longitude : -87.756046711<br>                     frequency : 21<br></div>`)[0];
            popup_1bafbb855e1c4683bc906453169a9b1a.setContent(html_4299c13423b64c04b510fe995911a820);
        

        circle_marker_b555e82617ea4ad2a75b6e5803bf13b3.bindPopup(popup_1bafbb855e1c4683bc906453169a9b1a)
        ;

        
    
    
            var circle_marker_e2edbe26d32a4862b3b59227ed6d7f34 = L.circleMarker(
                [41.785998518, -87.750934289],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 2.625, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_1183eeccd0214567823036c56dd3cdea = L.popup({"maxWidth": "100%"});

        
            var html_4a14d36629db4fc79da75b9cec4718d4 = $(`<div id="html_4a14d36629db4fc79da75b9cec4718d4" style="width: 100.0%; height: 100.0%;">Latitude : 41.785998518<br>                     Longitude : -87.750934289<br>                     frequency : 735<br></div>`)[0];
            popup_1183eeccd0214567823036c56dd3cdea.setContent(html_4a14d36629db4fc79da75b9cec4718d4);
        

        circle_marker_e2edbe26d32a4862b3b59227ed6d7f34.bindPopup(popup_1183eeccd0214567823036c56dd3cdea)
        ;

        
    
    
            var circle_marker_a11df222edc9480080a0840a8e502601 = L.circleMarker(
                [41.924347077, -87.734739754],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.039285714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_b3a8e2ec02474167a3bfaed8b047784f = L.popup({"maxWidth": "100%"});

        
            var html_2074621dc6e143838391014d23b32382 = $(`<div id="html_2074621dc6e143838391014d23b32382" style="width: 100.0%; height: 100.0%;">Latitude : 41.924347077<br>                     Longitude : -87.734739754<br>                     frequency : 11<br></div>`)[0];
            popup_b3a8e2ec02474167a3bfaed8b047784f.setContent(html_2074621dc6e143838391014d23b32382);
        

        circle_marker_a11df222edc9480080a0840a8e502601.bindPopup(popup_b3a8e2ec02474167a3bfaed8b047784f)
        ;

        
    
    
            var circle_marker_d1a4f647cd4e4d3086195f5ef68e237c = L.circleMarker(
                [41.957264108, -87.730898785],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_891ba24d1ec1458c82d22c6bbeba06d2 = L.popup({"maxWidth": "100%"});

        
            var html_f0972259ae8f4a7ebd9c2e2a06edf9b4 = $(`<div id="html_f0972259ae8f4a7ebd9c2e2a06edf9b4" style="width: 100.0%; height: 100.0%;">Latitude : 41.957264108<br>                     Longitude : -87.730898785<br>                     frequency : 1<br></div>`)[0];
            popup_891ba24d1ec1458c82d22c6bbeba06d2.setContent(html_f0972259ae8f4a7ebd9c2e2a06edf9b4);
        

        circle_marker_d1a4f647cd4e4d3086195f5ef68e237c.bindPopup(popup_891ba24d1ec1458c82d22c6bbeba06d2)
        ;

        
    
    
            var circle_marker_a5898dc1596c44828c74d06ed19eb84e = L.circleMarker(
                [41.949974454, -87.730684255],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_eb73c19593794de49aa281c381d142ef = L.popup({"maxWidth": "100%"});

        
            var html_9c54e721609f44f994bf76fefd2bd1f3 = $(`<div id="html_9c54e721609f44f994bf76fefd2bd1f3" style="width: 100.0%; height: 100.0%;">Latitude : 41.949974454<br>                     Longitude : -87.730684255<br>                     frequency : 3<br></div>`)[0];
            popup_eb73c19593794de49aa281c381d142ef.setContent(html_9c54e721609f44f994bf76fefd2bd1f3);
        

        circle_marker_a5898dc1596c44828c74d06ed19eb84e.bindPopup(popup_eb73c19593794de49aa281c381d142ef)
        ;

        
    
    
            var circle_marker_f924ba325e9a4c758c8b81b4c6d8fe55 = L.circleMarker(
                [41.878594358, -87.730232428],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_23b33a7d8cac482ca6e7f2ef5c761c82 = L.popup({"maxWidth": "100%"});

        
            var html_526dd052c37e48559b6e92dad0ffc576 = $(`<div id="html_526dd052c37e48559b6e92dad0ffc576" style="width: 100.0%; height: 100.0%;">Latitude : 41.878594358<br>                     Longitude : -87.730232428<br>                     frequency : 3<br></div>`)[0];
            popup_23b33a7d8cac482ca6e7f2ef5c761c82.setContent(html_526dd052c37e48559b6e92dad0ffc576);
        

        circle_marker_f924ba325e9a4c758c8b81b4c6d8fe55.bindPopup(popup_23b33a7d8cac482ca6e7f2ef5c761c82)
        ;

        
    
    
            var circle_marker_440743b8d8a94e07b2ad1aca66385ccc = L.circleMarker(
                [41.769778059, -87.726929842],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_df7545db64a14bf2875cd0bd431a64c8 = L.popup({"maxWidth": "100%"});

        
            var html_144946bfe42942619dfa5d0c698318be = $(`<div id="html_144946bfe42942619dfa5d0c698318be" style="width: 100.0%; height: 100.0%;">Latitude : 41.769778059<br>                     Longitude : -87.726929842<br>                     frequency : 3<br></div>`)[0];
            popup_df7545db64a14bf2875cd0bd431a64c8.setContent(html_144946bfe42942619dfa5d0c698318be);
        

        circle_marker_440743b8d8a94e07b2ad1aca66385ccc.bindPopup(popup_df7545db64a14bf2875cd0bd431a64c8)
        ;

        
    
    
            var circle_marker_8becf9578aa74585949ab4bc0859ea14 = L.circleMarker(
                [41.810879008, -87.726363325],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_ee6cd1859bd9444db57eafcd04635b09 = L.popup({"maxWidth": "100%"});

        
            var html_8b86806851fe4f28ae4724f3b7c011d7 = $(`<div id="html_8b86806851fe4f28ae4724f3b7c011d7" style="width: 100.0%; height: 100.0%;">Latitude : 41.810879008<br>                     Longitude : -87.726363325<br>                     frequency : 2<br></div>`)[0];
            popup_ee6cd1859bd9444db57eafcd04635b09.setContent(html_8b86806851fe4f28ae4724f3b7c011d7);
        

        circle_marker_8becf9578aa74585949ab4bc0859ea14.bindPopup(popup_ee6cd1859bd9444db57eafcd04635b09)
        ;

        
    
    
            var circle_marker_2393bdf33fbc4796969138bcdf525281 = L.circleMarker(
                [41.964647733, -87.725891015],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_3cb1926308bf4ebb9f1cb2b6751e7f4c = L.popup({"maxWidth": "100%"});

        
            var html_2ad6c189b11b42558477709e4021447e = $(`<div id="html_2ad6c189b11b42558477709e4021447e" style="width: 100.0%; height: 100.0%;">Latitude : 41.964647733<br>                     Longitude : -87.725891015<br>                     frequency : 1<br></div>`)[0];
            popup_3cb1926308bf4ebb9f1cb2b6751e7f4c.setContent(html_2ad6c189b11b42558477709e4021447e);
        

        circle_marker_2393bdf33fbc4796969138bcdf525281.bindPopup(popup_3cb1926308bf4ebb9f1cb2b6751e7f4c)
        ;

        
    
    
            var circle_marker_cf146d4655c2408080dc05cfe4c0e00f = L.circleMarker(
                [41.792981903, -87.724208194],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.025, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_5f5c850a330b4ff1b46d9650d4b1fe8c = L.popup({"maxWidth": "100%"});

        
            var html_bf04a689eda94daf899a431561b07cf0 = $(`<div id="html_bf04a689eda94daf899a431561b07cf0" style="width: 100.0%; height: 100.0%;">Latitude : 41.792981903<br>                     Longitude : -87.724208194<br>                     frequency : 7<br></div>`)[0];
            popup_5f5c850a330b4ff1b46d9650d4b1fe8c.setContent(html_bf04a689eda94daf899a431561b07cf0);
        

        circle_marker_cf146d4655c2408080dc05cfe4c0e00f.bindPopup(popup_5f5c850a330b4ff1b46d9650d4b1fe8c)
        ;

        
    
    
            var circle_marker_f619635ff8c7432392a64f5c6c85f339 = L.circleMarker(
                [41.983636307, -87.723583185],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.09642857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_246fea97e4b7495eabeed30e8248de3a = L.popup({"maxWidth": "100%"});

        
            var html_a54a890163a143f0a74df94a984a8e01 = $(`<div id="html_a54a890163a143f0a74df94a984a8e01" style="width: 100.0%; height: 100.0%;">Latitude : 41.983636307<br>                     Longitude : -87.723583185<br>                     frequency : 27<br></div>`)[0];
            popup_246fea97e4b7495eabeed30e8248de3a.setContent(html_a54a890163a143f0a74df94a984a8e01);
        

        circle_marker_f619635ff8c7432392a64f5c6c85f339.bindPopup(popup_246fea97e4b7495eabeed30e8248de3a)
        ;

        
    
    
            var circle_marker_81045e9d7bbc4a499d4b351fa2929450 = L.circleMarker(
                [41.953582125, -87.72345239],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.6321428571428571, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_3200c573887e4f09aeaf04a29120797a = L.popup({"maxWidth": "100%"});

        
            var html_4b03953e1e7f4e9eb63266bbc12c200b = $(`<div id="html_4b03953e1e7f4e9eb63266bbc12c200b" style="width: 100.0%; height: 100.0%;">Latitude : 41.953582125<br>                     Longitude : -87.72345239<br>                     frequency : 177<br></div>`)[0];
            popup_3200c573887e4f09aeaf04a29120797a.setContent(html_4b03953e1e7f4e9eb63266bbc12c200b);
        

        circle_marker_81045e9d7bbc4a499d4b351fa2929450.bindPopup(popup_3200c573887e4f09aeaf04a29120797a)
        ;

        
    
    
            var circle_marker_2f476a9b944d49089549ba247550ce93 = L.circleMarker(
                [41.969205937, -87.723168974],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.014285714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_c7800c0b24d74c73b27fe3f1bc28476e = L.popup({"maxWidth": "100%"});

        
            var html_1c76cdac78364c23b101c691b6b9cc9d = $(`<div id="html_1c76cdac78364c23b101c691b6b9cc9d" style="width: 100.0%; height: 100.0%;">Latitude : 41.969205937<br>                     Longitude : -87.723168974<br>                     frequency : 4<br></div>`)[0];
            popup_c7800c0b24d74c73b27fe3f1bc28476e.setContent(html_1c76cdac78364c23b101c691b6b9cc9d);
        

        circle_marker_2f476a9b944d49089549ba247550ce93.bindPopup(popup_c7800c0b24d74c73b27fe3f1bc28476e)
        ;

        
    
    
            var circle_marker_3ab01e53c1c3424898ef494aeb4ed6e1 = L.circleMarker(
                [41.968069, -87.721559063],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.4035714285714286, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_a572cbf6d7494a389b2fb87e94340d2e = L.popup({"maxWidth": "100%"});

        
            var html_7ac9768f9a2a46619f84ff234a56b63e = $(`<div id="html_7ac9768f9a2a46619f84ff234a56b63e" style="width: 100.0%; height: 100.0%;">Latitude : 41.968069<br>                     Longitude : -87.721559063<br>                     frequency : 113<br></div>`)[0];
            popup_a572cbf6d7494a389b2fb87e94340d2e.setContent(html_7ac9768f9a2a46619f84ff234a56b63e);
        

        circle_marker_3ab01e53c1c3424898ef494aeb4ed6e1.bindPopup(popup_a572cbf6d7494a389b2fb87e94340d2e)
        ;

        
    
    
            var circle_marker_128f684b19cf462198901066995c27d8 = L.circleMarker(
                [41.900069603, -87.720918238],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.17857142857142858, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_e7995ad92725445c8c378af4074e1809 = L.popup({"maxWidth": "100%"});

        
            var html_e597f40746e844ceb9865e14c7cb9267 = $(`<div id="html_e597f40746e844ceb9865e14c7cb9267" style="width: 100.0%; height: 100.0%;">Latitude : 41.900069603<br>                     Longitude : -87.720918238<br>                     frequency : 50<br></div>`)[0];
            popup_e7995ad92725445c8c378af4074e1809.setContent(html_e597f40746e844ceb9865e14c7cb9267);
        

        circle_marker_128f684b19cf462198901066995c27d8.bindPopup(popup_e7995ad92725445c8c378af4074e1809)
        ;

        
    
    
            var circle_marker_5e1aa5b13f234741902f81ceff9707f3 = L.circleMarker(
                [41.942859303, -87.717503858],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_5331b8e298c744b6a1bde79123bd97f5 = L.popup({"maxWidth": "100%"});

        
            var html_21efd131ba7843f0acc0a101e5b27748 = $(`<div id="html_21efd131ba7843f0acc0a101e5b27748" style="width: 100.0%; height: 100.0%;">Latitude : 41.942859303<br>                     Longitude : -87.717503858<br>                     frequency : 2<br></div>`)[0];
            popup_5331b8e298c744b6a1bde79123bd97f5.setContent(html_21efd131ba7843f0acc0a101e5b27748);
        

        circle_marker_5e1aa5b13f234741902f81ceff9707f3.bindPopup(popup_5331b8e298c744b6a1bde79123bd97f5)
        ;

        
    
    
            var circle_marker_1d3b80513e2a45af972b7833ec60c0d3 = L.circleMarker(
                [41.860190019, -87.7172201],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.05714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_71e5a30a65864631b9cb3d5bcf101530 = L.popup({"maxWidth": "100%"});

        
            var html_fd49dd19edc5464bb4940ac07ce42778 = $(`<div id="html_fd49dd19edc5464bb4940ac07ce42778" style="width: 100.0%; height: 100.0%;">Latitude : 41.860190019<br>                     Longitude : -87.7172201<br>                     frequency : 16<br></div>`)[0];
            popup_71e5a30a65864631b9cb3d5bcf101530.setContent(html_fd49dd19edc5464bb4940ac07ce42778);
        

        circle_marker_1d3b80513e2a45af972b7833ec60c0d3.bindPopup(popup_71e5a30a65864631b9cb3d5bcf101530)
        ;

        
    
    
            var circle_marker_0ee6dcaeb66f4c83a66481dbc22d46b2 = L.circleMarker(
                [41.839086906, -87.714003807],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.02857142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_747e0ba17f854cdab3d9023c9086bc20 = L.popup({"maxWidth": "100%"});

        
            var html_afc465a8d9ef481da7904b3a871456df = $(`<div id="html_afc465a8d9ef481da7904b3a871456df" style="width: 100.0%; height: 100.0%;">Latitude : 41.839086906<br>                     Longitude : -87.714003807<br>                     frequency : 8<br></div>`)[0];
            popup_747e0ba17f854cdab3d9023c9086bc20.setContent(html_afc465a8d9ef481da7904b3a871456df);
        

        circle_marker_0ee6dcaeb66f4c83a66481dbc22d46b2.bindPopup(popup_747e0ba17f854cdab3d9023c9086bc20)
        ;

        
    
    
            var circle_marker_fa807e3e24a945c9a392f5d769e2f9d8 = L.circleMarker(
                [41.963115755, -87.713229335],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_483e6f9eeb37402c962cf4244a066a51 = L.popup({"maxWidth": "100%"});

        
            var html_a1e72325d05147a18df635fb6cc519f7 = $(`<div id="html_a1e72325d05147a18df635fb6cc519f7" style="width: 100.0%; height: 100.0%;">Latitude : 41.963115755<br>                     Longitude : -87.713229335<br>                     frequency : 1<br></div>`)[0];
            popup_483e6f9eeb37402c962cf4244a066a51.setContent(html_a1e72325d05147a18df635fb6cc519f7);
        

        circle_marker_fa807e3e24a945c9a392f5d769e2f9d8.bindPopup(popup_483e6f9eeb37402c962cf4244a066a51)
        ;

        
    
    
            var circle_marker_bd3d79f7cd674fd888f830959496e4b5 = L.circleMarker(
                [41.950212096, -87.712814232],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_041f4b7cdfa64c4a88b44478e359c28a = L.popup({"maxWidth": "100%"});

        
            var html_c6202fcf8bec4493817e06b4e7e763b6 = $(`<div id="html_c6202fcf8bec4493817e06b4e7e763b6" style="width: 100.0%; height: 100.0%;">Latitude : 41.950212096<br>                     Longitude : -87.712814232<br>                     frequency : 1<br></div>`)[0];
            popup_041f4b7cdfa64c4a88b44478e359c28a.setContent(html_c6202fcf8bec4493817e06b4e7e763b6);
        

        circle_marker_bd3d79f7cd674fd888f830959496e4b5.bindPopup(popup_041f4b7cdfa64c4a88b44478e359c28a)
        ;

        
    
    
            var circle_marker_9490a8aa3c96473390b59cdcc69dda92 = L.circleMarker(
                [41.929329713, -87.711974254],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_d616772af8b54997955369620bbe28c2 = L.popup({"maxWidth": "100%"});

        
            var html_6e04634abbff4f77aa255080c8617a5f = $(`<div id="html_6e04634abbff4f77aa255080c8617a5f" style="width: 100.0%; height: 100.0%;">Latitude : 41.929329713<br>                     Longitude : -87.711974254<br>                     frequency : 1<br></div>`)[0];
            popup_d616772af8b54997955369620bbe28c2.setContent(html_6e04634abbff4f77aa255080c8617a5f);
        

        circle_marker_9490a8aa3c96473390b59cdcc69dda92.bindPopup(popup_d616772af8b54997955369620bbe28c2)
        ;

        
    
    
            var circle_marker_4236ac6f4ae74eea9636badc058fef1b = L.circleMarker(
                [41.938666196, -87.711210593],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.39285714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_5186a8643dd84aef8c7864fd94717bc8 = L.popup({"maxWidth": "100%"});

        
            var html_855f9f5d84774ebc848f4cfe0d873a85 = $(`<div id="html_855f9f5d84774ebc848f4cfe0d873a85" style="width: 100.0%; height: 100.0%;">Latitude : 41.938666196<br>                     Longitude : -87.711210593<br>                     frequency : 110<br></div>`)[0];
            popup_5186a8643dd84aef8c7864fd94717bc8.setContent(html_855f9f5d84774ebc848f4cfe0d873a85);
        

        circle_marker_4236ac6f4ae74eea9636badc058fef1b.bindPopup(popup_5186a8643dd84aef8c7864fd94717bc8)
        ;

        
    
    
            var circle_marker_79c22ba9951741ccbc50f6fd179291b3 = L.circleMarker(
                [41.921019607, -87.710359144],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_ca956ba5707a4705a5fe96a6696b6c78 = L.popup({"maxWidth": "100%"});

        
            var html_b66d3b06567448479d08e70c0f282f83 = $(`<div id="html_b66d3b06567448479d08e70c0f282f83" style="width: 100.0%; height: 100.0%;">Latitude : 41.921019607<br>                     Longitude : -87.710359144<br>                     frequency : 1<br></div>`)[0];
            popup_ca956ba5707a4705a5fe96a6696b6c78.setContent(html_b66d3b06567448479d08e70c0f282f83);
        

        circle_marker_79c22ba9951741ccbc50f6fd179291b3.bindPopup(popup_ca956ba5707a4705a5fe96a6696b6c78)
        ;

        
    
    
            var circle_marker_166a417d5ac541bd81988f4db127f8bf = L.circleMarker(
                [41.93749397, -87.709987338],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_d3d0a6ccdd7541f5847671251d54838a = L.popup({"maxWidth": "100%"});

        
            var html_42c08e73bb154196ba9c85d4929d5696 = $(`<div id="html_42c08e73bb154196ba9c85d4929d5696" style="width: 100.0%; height: 100.0%;">Latitude : 41.93749397<br>                     Longitude : -87.709987338<br>                     frequency : 1<br></div>`)[0];
            popup_d3d0a6ccdd7541f5847671251d54838a.setContent(html_42c08e73bb154196ba9c85d4929d5696);
        

        circle_marker_166a417d5ac541bd81988f4db127f8bf.bindPopup(popup_d3d0a6ccdd7541f5847671251d54838a)
        ;

        
    
    
            var circle_marker_818ef12e61e5497997a3ba3c39ed82b8 = L.circleMarker(
                [41.745757713, -87.708365704],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_e0a2d82bd7ef46a2a32ce8c6360b2820 = L.popup({"maxWidth": "100%"});

        
            var html_4d29174a03fd481cbbec737b8a393771 = $(`<div id="html_4d29174a03fd481cbbec737b8a393771" style="width: 100.0%; height: 100.0%;">Latitude : 41.745757713<br>                     Longitude : -87.708365704<br>                     frequency : 2<br></div>`)[0];
            popup_e0a2d82bd7ef46a2a32ce8c6360b2820.setContent(html_4d29174a03fd481cbbec737b8a393771);
        

        circle_marker_818ef12e61e5497997a3ba3c39ed82b8.bindPopup(popup_e0a2d82bd7ef46a2a32ce8c6360b2820)
        ;

        
    
    
            var circle_marker_85f32afe8e904aa984571c8257d41a74 = L.circleMarker(
                [41.878914496, -87.70589713],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.05714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_d66b7e245dd74f3b9da9784dbb666327 = L.popup({"maxWidth": "100%"});

        
            var html_1925973fddee449198a3c2ce237d24df = $(`<div id="html_1925973fddee449198a3c2ce237d24df" style="width: 100.0%; height: 100.0%;">Latitude : 41.878914496<br>                     Longitude : -87.70589713<br>                     frequency : 16<br></div>`)[0];
            popup_d66b7e245dd74f3b9da9784dbb666327.setContent(html_1925973fddee449198a3c2ce237d24df);
        

        circle_marker_85f32afe8e904aa984571c8257d41a74.bindPopup(popup_d66b7e245dd74f3b9da9784dbb666327)
        ;

        
    
    
            var circle_marker_b2b326c42813479fabc777760282b4f5 = L.circleMarker(
                [41.928391397, -87.704907236],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_e7b8f9a734194a82a7cd8da50a5e93ba = L.popup({"maxWidth": "100%"});

        
            var html_f3e90fd681b04a04afc8b613144f919e = $(`<div id="html_f3e90fd681b04a04afc8b613144f919e" style="width: 100.0%; height: 100.0%;">Latitude : 41.928391397<br>                     Longitude : -87.704907236<br>                     frequency : 2<br></div>`)[0];
            popup_e7b8f9a734194a82a7cd8da50a5e93ba.setContent(html_f3e90fd681b04a04afc8b613144f919e);
        

        circle_marker_b2b326c42813479fabc777760282b4f5.bindPopup(popup_e7b8f9a734194a82a7cd8da50a5e93ba)
        ;

        
    
    
            var circle_marker_eb96bd5c2cf04642bbb1800e855a6801 = L.circleMarker(
                [41.860762262, -87.700691903],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_fc27f9241ff54e079f945041586fadab = L.popup({"maxWidth": "100%"});

        
            var html_cbe210a8948844b3b159dbce6e00cb75 = $(`<div id="html_cbe210a8948844b3b159dbce6e00cb75" style="width: 100.0%; height: 100.0%;">Latitude : 41.860762262<br>                     Longitude : -87.700691903<br>                     frequency : 2<br></div>`)[0];
            popup_fc27f9241ff54e079f945041586fadab.setContent(html_cbe210a8948844b3b159dbce6e00cb75);
        

        circle_marker_eb96bd5c2cf04642bbb1800e855a6801.bindPopup(popup_fc27f9241ff54e079f945041586fadab)
        ;

        
    
    
            var circle_marker_e9253890095f4a0ca294a0f9a868d00d = L.circleMarker(
                [41.928431564, -87.699968591],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_141158c4f0da4ffe9efc4d4bc172ab7e = L.popup({"maxWidth": "100%"});

        
            var html_21149a7b7a524915a86ec4820fa40160 = $(`<div id="html_21149a7b7a524915a86ec4820fa40160" style="width: 100.0%; height: 100.0%;">Latitude : 41.928431564<br>                     Longitude : -87.699968591<br>                     frequency : 2<br></div>`)[0];
            popup_141158c4f0da4ffe9efc4d4bc172ab7e.setContent(html_21149a7b7a524915a86ec4820fa40160);
        

        circle_marker_e9253890095f4a0ca294a0f9a868d00d.bindPopup(popup_141158c4f0da4ffe9efc4d4bc172ab7e)
        ;

        
    
    
            var circle_marker_46714ff39a8a4aaeb37d99c75e08c988 = L.circleMarker(
                [41.921125914, -87.699754406],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.04642857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_f84ac675b5b54968a5ac7c0bfb89298f = L.popup({"maxWidth": "100%"});

        
            var html_6b21672cc0fc4424955f6e13d9410161 = $(`<div id="html_6b21672cc0fc4424955f6e13d9410161" style="width: 100.0%; height: 100.0%;">Latitude : 41.921125914<br>                     Longitude : -87.699754406<br>                     frequency : 13<br></div>`)[0];
            popup_f84ac675b5b54968a5ac7c0bfb89298f.setContent(html_6b21672cc0fc4424955f6e13d9410161);
        

        circle_marker_46714ff39a8a4aaeb37d99c75e08c988.bindPopup(popup_f84ac675b5b54968a5ac7c0bfb89298f)
        ;

        
    
    
            var circle_marker_188f083a154946ea8e5eb0b7e01133a6 = L.circleMarker(
                [41.92276062, -87.699155343],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1.1357142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_f204868538d84b14aacee3c050743b26 = L.popup({"maxWidth": "100%"});

        
            var html_e40079fe7bd047dfbbd0a41c69d0ce7c = $(`<div id="html_e40079fe7bd047dfbbd0a41c69d0ce7c" style="width: 100.0%; height: 100.0%;">Latitude : 41.92276062<br>                     Longitude : -87.699155343<br>                     frequency : 318<br></div>`)[0];
            popup_f204868538d84b14aacee3c050743b26.setContent(html_e40079fe7bd047dfbbd0a41c69d0ce7c);
        

        circle_marker_188f083a154946ea8e5eb0b7e01133a6.bindPopup(popup_f204868538d84b14aacee3c050743b26)
        ;

        
    
    
            var circle_marker_eeb1a96541fd4b94b5c854ae5bafdb7b = L.circleMarker(
                [41.817366208, -87.698860797],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.03214285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_8aeb81ed4fad4c5e8393ffa0ca5534a2 = L.popup({"maxWidth": "100%"});

        
            var html_890c91a14012446ba9962c07edbe0f92 = $(`<div id="html_890c91a14012446ba9962c07edbe0f92" style="width: 100.0%; height: 100.0%;">Latitude : 41.817366208<br>                     Longitude : -87.698860797<br>                     frequency : 9<br></div>`)[0];
            popup_8aeb81ed4fad4c5e8393ffa0ca5534a2.setContent(html_890c91a14012446ba9962c07edbe0f92);
        

        circle_marker_eeb1a96541fd4b94b5c854ae5bafdb7b.bindPopup(popup_8aeb81ed4fad4c5e8393ffa0ca5534a2)
        ;

        
    
    
            var circle_marker_468f908469ea4cd7bb3b266f874515ca = L.circleMarker(
                [41.771848515, -87.695666342],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.025, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_f996575f9f7f411e92a8b8943c005d6e = L.popup({"maxWidth": "100%"});

        
            var html_ca762c6c14ee454d88a804c76f3eb1fb = $(`<div id="html_ca762c6c14ee454d88a804c76f3eb1fb" style="width: 100.0%; height: 100.0%;">Latitude : 41.771848515<br>                     Longitude : -87.695666342<br>                     frequency : 7<br></div>`)[0];
            popup_f996575f9f7f411e92a8b8943c005d6e.setContent(html_ca762c6c14ee454d88a804c76f3eb1fb);
        

        circle_marker_468f908469ea4cd7bb3b266f874515ca.bindPopup(popup_f996575f9f7f411e92a8b8943c005d6e)
        ;

        
    
    
            var circle_marker_604083b96b084c18b13b3ac514b5754b = L.circleMarker(
                [42.001571027, -87.695012589],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.6214285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_0db94f9da2594df8a11b4f4cf118441b = L.popup({"maxWidth": "100%"});

        
            var html_52ff52f2ea5947a796534764369aba41 = $(`<div id="html_52ff52f2ea5947a796534764369aba41" style="width: 100.0%; height: 100.0%;">Latitude : 42.001571027<br>                     Longitude : -87.695012589<br>                     frequency : 174<br></div>`)[0];
            popup_0db94f9da2594df8a11b4f4cf118441b.setContent(html_52ff52f2ea5947a796534764369aba41);
        

        circle_marker_604083b96b084c18b13b3ac514b5754b.bindPopup(popup_0db94f9da2594df8a11b4f4cf118441b)
        ;

        
    
    
            var circle_marker_6bba36e844cc4fa98e706d507c2f6845 = L.circleMarker(
                [41.994059824, -87.694630719],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_75984633b61649e79f4821a39b0ea5f5 = L.popup({"maxWidth": "100%"});

        
            var html_db74223eb9df4f02864417af5f0ed2c3 = $(`<div id="html_db74223eb9df4f02864417af5f0ed2c3" style="width: 100.0%; height: 100.0%;">Latitude : 41.994059824<br>                     Longitude : -87.694630719<br>                     frequency : 2<br></div>`)[0];
            popup_75984633b61649e79f4821a39b0ea5f5.setContent(html_db74223eb9df4f02864417af5f0ed2c3);
        

        circle_marker_6bba36e844cc4fa98e706d507c2f6845.bindPopup(popup_75984633b61649e79f4821a39b0ea5f5)
        ;

        
    
    
            var circle_marker_93172f68636448f6a8469ab901e4dad3 = L.circleMarker(
                [41.920801704, -87.694532342],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.02142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_c3428a9388db489bb04a2c1050c522a7 = L.popup({"maxWidth": "100%"});

        
            var html_1111d64c43ce4fa589aec8067d3af5bb = $(`<div id="html_1111d64c43ce4fa589aec8067d3af5bb" style="width: 100.0%; height: 100.0%;">Latitude : 41.920801704<br>                     Longitude : -87.694532342<br>                     frequency : 6<br></div>`)[0];
            popup_c3428a9388db489bb04a2c1050c522a7.setContent(html_1111d64c43ce4fa589aec8067d3af5bb);
        

        circle_marker_93172f68636448f6a8469ab901e4dad3.bindPopup(popup_c3428a9388db489bb04a2c1050c522a7)
        ;

        
    
    
            var circle_marker_2992d713713d456b9c894a8d28230dec = L.circleMarker(
                [41.900560384, -87.69419737],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_c0af15428fa541aeb471d747530f2c7d = L.popup({"maxWidth": "100%"});

        
            var html_3e0133e1949a4cb09dd0c85796642c95 = $(`<div id="html_3e0133e1949a4cb09dd0c85796642c95" style="width: 100.0%; height: 100.0%;">Latitude : 41.900560384<br>                     Longitude : -87.69419737<br>                     frequency : 1<br></div>`)[0];
            popup_c0af15428fa541aeb471d747530f2c7d.setContent(html_3e0133e1949a4cb09dd0c85796642c95);
        

        circle_marker_2992d713713d456b9c894a8d28230dec.bindPopup(popup_c0af15428fa541aeb471d747530f2c7d)
        ;

        
    
    
            var circle_marker_74460008e9f646e597e8db371b08d5f1 = L.circleMarker(
                [41.979855309, -87.694096022],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_faa6f3a972fc4628810cfd599949eadc = L.popup({"maxWidth": "100%"});

        
            var html_12c11b967a684b73a774798de56f5ae1 = $(`<div id="html_12c11b967a684b73a774798de56f5ae1" style="width: 100.0%; height: 100.0%;">Latitude : 41.979855309<br>                     Longitude : -87.694096022<br>                     frequency : 1<br></div>`)[0];
            popup_faa6f3a972fc4628810cfd599949eadc.setContent(html_12c11b967a684b73a774798de56f5ae1);
        

        circle_marker_74460008e9f646e597e8db371b08d5f1.bindPopup(popup_faa6f3a972fc4628810cfd599949eadc)
        ;

        
    
    
            var circle_marker_fa81200156524ecb8a6c1b85acb90dc1 = L.circleMarker(
                [41.9725808, -87.694001061],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_332cfc5e4a374b3db2a11a697b85d2ac = L.popup({"maxWidth": "100%"});

        
            var html_649380de7faa4a128404839c2f204494 = $(`<div id="html_649380de7faa4a128404839c2f204494" style="width: 100.0%; height: 100.0%;">Latitude : 41.9725808<br>                     Longitude : -87.694001061<br>                     frequency : 2<br></div>`)[0];
            popup_332cfc5e4a374b3db2a11a697b85d2ac.setContent(html_649380de7faa4a128404839c2f204494);
        

        circle_marker_fa81200156524ecb8a6c1b85acb90dc1.bindPopup(popup_332cfc5e4a374b3db2a11a697b85d2ac)
        ;

        
    
    
            var circle_marker_e765601433a74c3f88ec57be8a01bcc0 = L.circleMarker(
                [42.001315924, -87.693637494],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_5a8fba4465e24dd2a9742de837555537 = L.popup({"maxWidth": "100%"});

        
            var html_11288c4c21fd4dffb41ae35b4f0a7c68 = $(`<div id="html_11288c4c21fd4dffb41ae35b4f0a7c68" style="width: 100.0%; height: 100.0%;">Latitude : 42.001315924<br>                     Longitude : -87.693637494<br>                     frequency : 1<br></div>`)[0];
            popup_5a8fba4465e24dd2a9742de837555537.setContent(html_11288c4c21fd4dffb41ae35b4f0a7c68);
        

        circle_marker_e765601433a74c3f88ec57be8a01bcc0.bindPopup(popup_5a8fba4465e24dd2a9742de837555537)
        ;

        
    
    
            var circle_marker_7325e5273d794fb2b454857ec8f26f9d = L.circleMarker(
                [41.915741193, -87.692256326],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_f2348daa8d3748828db6d380e119e6a8 = L.popup({"maxWidth": "100%"});

        
            var html_31ce4915adfc4882823ae1b97239d863 = $(`<div id="html_31ce4915adfc4882823ae1b97239d863" style="width: 100.0%; height: 100.0%;">Latitude : 41.915741193<br>                     Longitude : -87.692256326<br>                     frequency : 1<br></div>`)[0];
            popup_f2348daa8d3748828db6d380e119e6a8.setContent(html_31ce4915adfc4882823ae1b97239d863);
        

        circle_marker_7325e5273d794fb2b454857ec8f26f9d.bindPopup(popup_f2348daa8d3748828db6d380e119e6a8)
        ;

        
    
    
            var circle_marker_b5fd8e75b54d4abea52612a0e8c34a98 = L.circleMarker(
                [41.975170943, -87.687515515],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.75, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_546028807661401d85382057d6c07c7b = L.popup({"maxWidth": "100%"});

        
            var html_f3a3337d415844a2b59de10067dd0c44 = $(`<div id="html_f3a3337d415844a2b59de10067dd0c44" style="width: 100.0%; height: 100.0%;">Latitude : 41.975170943<br>                     Longitude : -87.687515515<br>                     frequency : 210<br></div>`)[0];
            popup_546028807661401d85382057d6c07c7b.setContent(html_f3a3337d415844a2b59de10067dd0c44);
        

        circle_marker_b5fd8e75b54d4abea52612a0e8c34a98.bindPopup(popup_546028807661401d85382057d6c07c7b)
        ;

        
    
    
            var circle_marker_e10516e52fd7466c9f3cf4e8b3cdcaa3 = L.circleMarker(
                [41.928619051, -87.685362024],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_b344f0b43abd48cd82f70928387d8929 = L.popup({"maxWidth": "100%"});

        
            var html_2d38077627b849d699b1a3affed81e65 = $(`<div id="html_2d38077627b849d699b1a3affed81e65" style="width: 100.0%; height: 100.0%;">Latitude : 41.928619051<br>                     Longitude : -87.685362024<br>                     frequency : 1<br></div>`)[0];
            popup_b344f0b43abd48cd82f70928387d8929.setContent(html_2d38077627b849d699b1a3affed81e65);
        

        circle_marker_e10516e52fd7466c9f3cf4e8b3cdcaa3.bindPopup(popup_b344f0b43abd48cd82f70928387d8929)
        ;

        
    
    
            var circle_marker_ce17c1a3c9bb4f93bf6e34f0194cc825 = L.circleMarker(
                [41.906707792, -87.684685949],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_2c44539743964fa398339d4982fa9e7e = L.popup({"maxWidth": "100%"});

        
            var html_0416ebccecb74e439340722b96cf3c2f = $(`<div id="html_0416ebccecb74e439340722b96cf3c2f" style="width: 100.0%; height: 100.0%;">Latitude : 41.906707792<br>                     Longitude : -87.684685949<br>                     frequency : 1<br></div>`)[0];
            popup_2c44539743964fa398339d4982fa9e7e.setContent(html_0416ebccecb74e439340722b96cf3c2f);
        

        circle_marker_ce17c1a3c9bb4f93bf6e34f0194cc825.bindPopup(popup_2c44539743964fa398339d4982fa9e7e)
        ;

        
    
    
            var circle_marker_35a3fcb7a0a94273b4271d5b203d3c81 = L.circleMarker(
                [41.899422254, -87.684490122],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_2fc041beacb642aab8aa7b8994361582 = L.popup({"maxWidth": "100%"});

        
            var html_ead71ad35084494a855c612a114b6c40 = $(`<div id="html_ead71ad35084494a855c612a114b6c40" style="width: 100.0%; height: 100.0%;">Latitude : 41.899422254<br>                     Longitude : -87.684490122<br>                     frequency : 2<br></div>`)[0];
            popup_2fc041beacb642aab8aa7b8994361582.setContent(html_ead71ad35084494a855c612a114b6c40);
        

        circle_marker_35a3fcb7a0a94273b4271d5b203d3c81.bindPopup(popup_2fc041beacb642aab8aa7b8994361582)
        ;

        
    
    
            var circle_marker_9623eef626b2406cbd9b1d0a5ccee6b4 = L.circleMarker(
                [42.001313249, -87.684198195],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_986fc580cb2a4f1e8136d1d83aa332d1 = L.popup({"maxWidth": "100%"});

        
            var html_5331e34381c0466694207c9e16cb4a00 = $(`<div id="html_5331e34381c0466694207c9e16cb4a00" style="width: 100.0%; height: 100.0%;">Latitude : 42.001313249<br>                     Longitude : -87.684198195<br>                     frequency : 1<br></div>`)[0];
            popup_986fc580cb2a4f1e8136d1d83aa332d1.setContent(html_5331e34381c0466694207c9e16cb4a00);
        

        circle_marker_9623eef626b2406cbd9b1d0a5ccee6b4.bindPopup(popup_986fc580cb2a4f1e8136d1d83aa332d1)
        ;

        
    
    
            var circle_marker_1a799ef94af949e6a2e63c2c4b528c0b = L.circleMarker(
                [41.884767784, -87.684147449],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_4619ad970da349a9842d8adbc9cce96a = L.popup({"maxWidth": "100%"});

        
            var html_3cd28ec038bb491190a4d9e50e5b5131 = $(`<div id="html_3cd28ec038bb491190a4d9e50e5b5131" style="width: 100.0%; height: 100.0%;">Latitude : 41.884767784<br>                     Longitude : -87.684147449<br>                     frequency : 1<br></div>`)[0];
            popup_4619ad970da349a9842d8adbc9cce96a.setContent(html_3cd28ec038bb491190a4d9e50e5b5131);
        

        circle_marker_1a799ef94af949e6a2e63c2c4b528c0b.bindPopup(popup_4619ad970da349a9842d8adbc9cce96a)
        ;

        
    
    
            var circle_marker_2c0afd30886b4855bb7b84d0c9e2d8e5 = L.circleMarker(
                [41.966834067, -87.684018371],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_e038ecb87ded484f91b28b4c393415ae = L.popup({"maxWidth": "100%"});

        
            var html_8195ce469782474bb349ff6e0da27155 = $(`<div id="html_8195ce469782474bb349ff6e0da27155" style="width: 100.0%; height: 100.0%;">Latitude : 41.966834067<br>                     Longitude : -87.684018371<br>                     frequency : 2<br></div>`)[0];
            popup_e038ecb87ded484f91b28b4c393415ae.setContent(html_8195ce469782474bb349ff6e0da27155);
        

        circle_marker_2c0afd30886b4855bb7b84d0c9e2d8e5.bindPopup(popup_e038ecb87ded484f91b28b4c393415ae)
        ;

        
    
    
            var circle_marker_670164394fad4e3194af04ad22423135 = L.circleMarker(
                [41.947791586, -87.683834942],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.7, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_8b76558fe8d448c28eed4009000b0164 = L.popup({"maxWidth": "100%"});

        
            var html_dc74703efc8543498a871b9501414463 = $(`<div id="html_dc74703efc8543498a871b9501414463" style="width: 100.0%; height: 100.0%;">Latitude : 41.947791586<br>                     Longitude : -87.683834942<br>                     frequency : 196<br></div>`)[0];
            popup_8b76558fe8d448c28eed4009000b0164.setContent(html_dc74703efc8543498a871b9501414463);
        

        circle_marker_670164394fad4e3194af04ad22423135.bindPopup(popup_8b76558fe8d448c28eed4009000b0164)
        ;

        
    
    
            var circle_marker_e920078be22943879b1eacf10be2bd8e = L.circleMarker(
                [41.957735565, -87.683718102],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.03571428571428571, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_57cf7644864a4c008eb9079b1ffb6667 = L.popup({"maxWidth": "100%"});

        
            var html_c57cd21c55624283b30efca889e83e6b = $(`<div id="html_c57cd21c55624283b30efca889e83e6b" style="width: 100.0%; height: 100.0%;">Latitude : 41.957735565<br>                     Longitude : -87.683718102<br>                     frequency : 10<br></div>`)[0];
            popup_57cf7644864a4c008eb9079b1ffb6667.setContent(html_c57cd21c55624283b30efca889e83e6b);
        

        circle_marker_e920078be22943879b1eacf10be2bd8e.bindPopup(popup_57cf7644864a4c008eb9079b1ffb6667)
        ;

        
    
    
            var circle_marker_fd5fee00359b4feea8c08d9840856c10 = L.circleMarker(
                [41.911972301, -87.683642922],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.025, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_ef497c0734154491a2ce2e47592a1412 = L.popup({"maxWidth": "100%"});

        
            var html_402cf921b1f74ee5ba39a93e20ada551 = $(`<div id="html_402cf921b1f74ee5ba39a93e20ada551" style="width: 100.0%; height: 100.0%;">Latitude : 41.911972301<br>                     Longitude : -87.683642922<br>                     frequency : 7<br></div>`)[0];
            popup_ef497c0734154491a2ce2e47592a1412.setContent(html_402cf921b1f74ee5ba39a93e20ada551);
        

        circle_marker_fd5fee00359b4feea8c08d9840856c10.bindPopup(popup_ef497c0734154491a2ce2e47592a1412)
        ;

        
    
    
            var circle_marker_bc7c8038a1144d9d80ca5ab897e33ce5 = L.circleMarker(
                [41.950442599, -87.68350623],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_b17af437a95f4a008e98c6212e9a23ac = L.popup({"maxWidth": "100%"});

        
            var html_b669e41e046a468787dbf6931eee0b64 = $(`<div id="html_b669e41e046a468787dbf6931eee0b64" style="width: 100.0%; height: 100.0%;">Latitude : 41.950442599<br>                     Longitude : -87.68350623<br>                     frequency : 1<br></div>`)[0];
            popup_b17af437a95f4a008e98c6212e9a23ac.setContent(html_b669e41e046a468787dbf6931eee0b64);
        

        circle_marker_bc7c8038a1144d9d80ca5ab897e33ce5.bindPopup(popup_b17af437a95f4a008e98c6212e9a23ac)
        ;

        
    
    
            var circle_marker_d3910868f4c548c7a5da8452cdd879bb = L.circleMarker(
                [41.833517886, -87.681355829],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.03571428571428571, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_e47809f7a8af43c8a636e471d7e94ca4 = L.popup({"maxWidth": "100%"});

        
            var html_5601a67f76a74340af7ee18b6602e803 = $(`<div id="html_5601a67f76a74340af7ee18b6602e803" style="width: 100.0%; height: 100.0%;">Latitude : 41.833517886<br>                     Longitude : -87.681355829<br>                     frequency : 10<br></div>`)[0];
            popup_e47809f7a8af43c8a636e471d7e94ca4.setContent(html_5601a67f76a74340af7ee18b6602e803);
        

        circle_marker_d3910868f4c548c7a5da8452cdd879bb.bindPopup(popup_e47809f7a8af43c8a636e471d7e94ca4)
        ;

        
    
    
            var circle_marker_1881f3beaa2a47ce95d5b4c5c3b7a5a4 = L.circleMarker(
                [41.945010151, -87.680928225],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_d8dd4975cf9441a7af4f9a1700d2b9f0 = L.popup({"maxWidth": "100%"});

        
            var html_6a8a7d3ba90e4419b19c55bc715d3dc7 = $(`<div id="html_6a8a7d3ba90e4419b19c55bc715d3dc7" style="width: 100.0%; height: 100.0%;">Latitude : 41.945010151<br>                     Longitude : -87.680928225<br>                     frequency : 1<br></div>`)[0];
            popup_d8dd4975cf9441a7af4f9a1700d2b9f0.setContent(html_6a8a7d3ba90e4419b19c55bc715d3dc7);
        

        circle_marker_1881f3beaa2a47ce95d5b4c5c3b7a5a4.bindPopup(popup_d8dd4975cf9441a7af4f9a1700d2b9f0)
        ;

        
    
    
            var circle_marker_91455c7c975b4f58ad1cb9284e63604a = L.circleMarker(
                [41.877383471, -87.680654116],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_58dfd5070aa44ae58b80c022f7acbf57 = L.popup({"maxWidth": "100%"});

        
            var html_ed953c3995d249129f9363ba4407fa89 = $(`<div id="html_ed953c3995d249129f9363ba4407fa89" style="width: 100.0%; height: 100.0%;">Latitude : 41.877383471<br>                     Longitude : -87.680654116<br>                     frequency : 1<br></div>`)[0];
            popup_58dfd5070aa44ae58b80c022f7acbf57.setContent(html_ed953c3995d249129f9363ba4407fa89);
        

        circle_marker_91455c7c975b4f58ad1cb9284e63604a.bindPopup(popup_58dfd5070aa44ae58b80c022f7acbf57)
        ;

        
    
    
            var circle_marker_076fd2fa7655432b8724526fffb32167 = L.circleMarker(
                [41.920451512, -87.679954768],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.025, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_7f223719f19d485a84f92049b8ac059e = L.popup({"maxWidth": "100%"});

        
            var html_7182acdda76a442c95b69f7741419bc9 = $(`<div id="html_7182acdda76a442c95b69f7741419bc9" style="width: 100.0%; height: 100.0%;">Latitude : 41.920451512<br>                     Longitude : -87.679954768<br>                     frequency : 7<br></div>`)[0];
            popup_7f223719f19d485a84f92049b8ac059e.setContent(html_7182acdda76a442c95b69f7741419bc9);
        

        circle_marker_076fd2fa7655432b8724526fffb32167.bindPopup(popup_7f223719f19d485a84f92049b8ac059e)
        ;

        
    
    
            var circle_marker_01261649c49c460c99ad0930d4af00b6 = L.circleMarker(
                [41.899506548, -87.679600287],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.06428571428571428, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_87f8faec64424f7c89e08a771ac61838 = L.popup({"maxWidth": "100%"});

        
            var html_65f28c32068140249878372721e5d669 = $(`<div id="html_65f28c32068140249878372721e5d669" style="width: 100.0%; height: 100.0%;">Latitude : 41.899506548<br>                     Longitude : -87.679600287<br>                     frequency : 18<br></div>`)[0];
            popup_87f8faec64424f7c89e08a771ac61838.setContent(html_65f28c32068140249878372721e5d669);
        

        circle_marker_01261649c49c460c99ad0930d4af00b6.bindPopup(popup_87f8faec64424f7c89e08a771ac61838)
        ;

        
    
    
            var circle_marker_56064a46f65b48e8b92cc68611934265 = L.circleMarker(
                [41.892276708, -87.679397479],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_9aa89d8525604de5a4bdb31a575f5e55 = L.popup({"maxWidth": "100%"});

        
            var html_46a0b47f163a41cd879a0c2bf6581c39 = $(`<div id="html_46a0b47f163a41cd879a0c2bf6581c39" style="width: 100.0%; height: 100.0%;">Latitude : 41.892276708<br>                     Longitude : -87.679397479<br>                     frequency : 1<br></div>`)[0];
            popup_9aa89d8525604de5a4bdb31a575f5e55.setContent(html_46a0b47f163a41cd879a0c2bf6581c39);
        

        circle_marker_56064a46f65b48e8b92cc68611934265.bindPopup(popup_9aa89d8525604de5a4bdb31a575f5e55)
        ;

        
    
    
            var circle_marker_b56b99bb31ed40eca4042ce28f90c73e = L.circleMarker(
                [41.965141709, -87.676578071],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_0ecec73c234943c194f554a5a05c6dfb = L.popup({"maxWidth": "100%"});

        
            var html_c062936f22544f6aaf59d8d82ae0d75c = $(`<div id="html_c062936f22544f6aaf59d8d82ae0d75c" style="width: 100.0%; height: 100.0%;">Latitude : 41.965141709<br>                     Longitude : -87.676578071<br>                     frequency : 3<br></div>`)[0];
            popup_0ecec73c234943c194f554a5a05c6dfb.setContent(html_c062936f22544f6aaf59d8d82ae0d75c);
        

        circle_marker_b56b99bb31ed40eca4042ce28f90c73e.bindPopup(popup_0ecec73c234943c194f554a5a05c6dfb)
        ;

        
    
    
            var circle_marker_aac83242959f421195d588ebd814d87a = L.circleMarker(
                [41.957843375, -87.676373281],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_c2f251f93f7e4e8587c7b3bb526840c6 = L.popup({"maxWidth": "100%"});

        
            var html_1fd671a56c1e410daef974589c8c1977 = $(`<div id="html_1fd671a56c1e410daef974589c8c1977" style="width: 100.0%; height: 100.0%;">Latitude : 41.957843375<br>                     Longitude : -87.676373281<br>                     frequency : 2<br></div>`)[0];
            popup_c2f251f93f7e4e8587c7b3bb526840c6.setContent(html_1fd671a56c1e410daef974589c8c1977);
        

        circle_marker_aac83242959f421195d588ebd814d87a.bindPopup(popup_c2f251f93f7e4e8587c7b3bb526840c6)
        ;

        
    
    
            var circle_marker_48c23165816041d999f19f00a69ad93b = L.circleMarker(
                [41.901206994, -87.676355989],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 2.3857142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_2dbc01d3557f46f496cf15108bf4be80 = L.popup({"maxWidth": "100%"});

        
            var html_62c015f8ed2e465c9e874acf9c08dd8e = $(`<div id="html_62c015f8ed2e465c9e874acf9c08dd8e" style="width: 100.0%; height: 100.0%;">Latitude : 41.901206994<br>                     Longitude : -87.676355989<br>                     frequency : 668<br></div>`)[0];
            popup_2dbc01d3557f46f496cf15108bf4be80.setContent(html_62c015f8ed2e465c9e874acf9c08dd8e);
        

        circle_marker_48c23165816041d999f19f00a69ad93b.bindPopup(popup_2dbc01d3557f46f496cf15108bf4be80)
        ;

        
    
    
            var circle_marker_e4e3279a80e44f88b26327762ce5ed13 = L.circleMarker(
                [41.950545696, -87.676182496],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_083ee986a821428c824156c130a84e71 = L.popup({"maxWidth": "100%"});

        
            var html_e84b8a6d96da4b4eb9b6a91cf0f5198f = $(`<div id="html_e84b8a6d96da4b4eb9b6a91cf0f5198f" style="width: 100.0%; height: 100.0%;">Latitude : 41.950545696<br>                     Longitude : -87.676182496<br>                     frequency : 3<br></div>`)[0];
            popup_083ee986a821428c824156c130a84e71.setContent(html_e84b8a6d96da4b4eb9b6a91cf0f5198f);
        

        circle_marker_e4e3279a80e44f88b26327762ce5ed13.bindPopup(popup_083ee986a821428c824156c130a84e71)
        ;

        
    
    
            var circle_marker_5ce86cb645b042aea1fdd3cc9a96b9e1 = L.circleMarker(
                [41.906025969, -87.675311622],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.29285714285714287, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_6500a574beec4725ac0ffafa2c7739c6 = L.popup({"maxWidth": "100%"});

        
            var html_abf7db8d90b3481c890164cca9a20ba3 = $(`<div id="html_abf7db8d90b3481c890164cca9a20ba3" style="width: 100.0%; height: 100.0%;">Latitude : 41.906025969<br>                     Longitude : -87.675311622<br>                     frequency : 82<br></div>`)[0];
            popup_6500a574beec4725ac0ffafa2c7739c6.setContent(html_abf7db8d90b3481c890164cca9a20ba3);
        

        circle_marker_5ce86cb645b042aea1fdd3cc9a96b9e1.bindPopup(popup_6500a574beec4725ac0ffafa2c7739c6)
        ;

        
    
    
            var circle_marker_fcd29c25de764da0b55a3e1ef58dae98 = L.circleMarker(
                [41.916005274, -87.675095116],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.07142857142857142, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_bd39830d07c8443b9dabc527bdd8fc98 = L.popup({"maxWidth": "100%"});

        
            var html_3afc2b4ef6f24c95b29d230bae9b14b9 = $(`<div id="html_3afc2b4ef6f24c95b29d230bae9b14b9" style="width: 100.0%; height: 100.0%;">Latitude : 41.916005274<br>                     Longitude : -87.675095116<br>                     frequency : 20<br></div>`)[0];
            popup_bd39830d07c8443b9dabc527bdd8fc98.setContent(html_3afc2b4ef6f24c95b29d230bae9b14b9);
        

        circle_marker_fcd29c25de764da0b55a3e1ef58dae98.bindPopup(popup_bd39830d07c8443b9dabc527bdd8fc98)
        ;

        
    
    
            var circle_marker_f99a03d7e9694b78b902267cc561a694 = L.circleMarker(
                [41.870415, -87.675085621],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.20357142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_e04c95b95cdf40e9a9e88e5112cf9ee5 = L.popup({"maxWidth": "100%"});

        
            var html_bdcfe716862c44838b0ad16ec684974e = $(`<div id="html_bdcfe716862c44838b0ad16ec684974e" style="width: 100.0%; height: 100.0%;">Latitude : 41.870415<br>                     Longitude : -87.675085621<br>                     frequency : 57<br></div>`)[0];
            popup_e04c95b95cdf40e9a9e88e5112cf9ee5.setContent(html_bdcfe716862c44838b0ad16ec684974e);
        

        circle_marker_f99a03d7e9694b78b902267cc561a694.bindPopup(popup_e04c95b95cdf40e9a9e88e5112cf9ee5)
        ;

        
    
    
            var circle_marker_0d3f80780ebb4508b93ae0290b14ec4f = L.circleMarker(
                [41.713148612, -87.675075312],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_d29e517fbeda49f5a900d1d6ecf82afc = L.popup({"maxWidth": "100%"});

        
            var html_2be1fb0c08494efab2f3cbc13919d657 = $(`<div id="html_2be1fb0c08494efab2f3cbc13919d657" style="width: 100.0%; height: 100.0%;">Latitude : 41.713148612<br>                     Longitude : -87.675075312<br>                     frequency : 2<br></div>`)[0];
            popup_d29e517fbeda49f5a900d1d6ecf82afc.setContent(html_2be1fb0c08494efab2f3cbc13919d657);
        

        circle_marker_0d3f80780ebb4508b93ae0290b14ec4f.bindPopup(popup_d29e517fbeda49f5a900d1d6ecf82afc)
        ;

        
    
    
            var circle_marker_88366766c4964b9aa99f17989cb70c8c = L.circleMarker(
                [41.912364354, -87.675062757],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.03571428571428571, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_92793fdd0c0241b6be47e9a46505d735 = L.popup({"maxWidth": "100%"});

        
            var html_902815ecb7554b739da93c746f4ca4cf = $(`<div id="html_902815ecb7554b739da93c746f4ca4cf" style="width: 100.0%; height: 100.0%;">Latitude : 41.912364354<br>                     Longitude : -87.675062757<br>                     frequency : 10<br></div>`)[0];
            popup_92793fdd0c0241b6be47e9a46505d735.setContent(html_902815ecb7554b739da93c746f4ca4cf);
        

        circle_marker_88366766c4964b9aa99f17989cb70c8c.bindPopup(popup_92793fdd0c0241b6be47e9a46505d735)
        ;

        
    
    
            var circle_marker_f2a88d6bc38541f4aed01c93d9d2089e = L.circleMarker(
                [41.899589796, -87.674719134],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.03571428571428571, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_4fa93c4e6721448ca990387075c0e1ef = L.popup({"maxWidth": "100%"});

        
            var html_f1e7d558e54148b88afecfa942822fc1 = $(`<div id="html_f1e7d558e54148b88afecfa942822fc1" style="width: 100.0%; height: 100.0%;">Latitude : 41.899589796<br>                     Longitude : -87.674719134<br>                     frequency : 10<br></div>`)[0];
            popup_4fa93c4e6721448ca990387075c0e1ef.setContent(html_f1e7d558e54148b88afecfa942822fc1);
        

        circle_marker_f2a88d6bc38541f4aed01c93d9d2089e.bindPopup(popup_4fa93c4e6721448ca990387075c0e1ef)
        ;

        
    
    
            var circle_marker_d22abd7f303243f9a861ae48bcf51703 = L.circleMarker(
                [41.892355048, -87.674506788],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.014285714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_80a0cbf1b57c4ebebd356750ac9a75a1 = L.popup({"maxWidth": "100%"});

        
            var html_48a1e4352f2a42548963960ced19aaa9 = $(`<div id="html_48a1e4352f2a42548963960ced19aaa9" style="width: 100.0%; height: 100.0%;">Latitude : 41.892355048<br>                     Longitude : -87.674506788<br>                     frequency : 4<br></div>`)[0];
            popup_80a0cbf1b57c4ebebd356750ac9a75a1.setContent(html_48a1e4352f2a42548963960ced19aaa9);
        

        circle_marker_d22abd7f303243f9a861ae48bcf51703.bindPopup(popup_80a0cbf1b57c4ebebd356750ac9a75a1)
        ;

        
    
    
            var circle_marker_6fc94045ee8b44139c6620c8803ebb91 = L.circleMarker(
                [41.929272532, -87.673807238],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_c2d1a0e2d84949d8a184ac18a9b6cc8c = L.popup({"maxWidth": "100%"});

        
            var html_b4d2b37abde14a14b30476add0c30547 = $(`<div id="html_b4d2b37abde14a14b30476add0c30547" style="width: 100.0%; height: 100.0%;">Latitude : 41.929272532<br>                     Longitude : -87.673807238<br>                     frequency : 1<br></div>`)[0];
            popup_c2d1a0e2d84949d8a184ac18a9b6cc8c.setContent(html_b4d2b37abde14a14b30476add0c30547);
        

        circle_marker_6fc94045ee8b44139c6620c8803ebb91.bindPopup(popup_c2d1a0e2d84949d8a184ac18a9b6cc8c)
        ;

        
    
    
            var circle_marker_a20fb2382db1489db1a4ee3d2aede6ff = L.circleMarker(
                [42.001698194, -87.673574032],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.017857142857142856, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_6cbb2f91a08f4c3e80a8ea9a8cf013d3 = L.popup({"maxWidth": "100%"});

        
            var html_3562f4a2d3e24159b099db28cde59701 = $(`<div id="html_3562f4a2d3e24159b099db28cde59701" style="width: 100.0%; height: 100.0%;">Latitude : 42.001698194<br>                     Longitude : -87.673574032<br>                     frequency : 5<br></div>`)[0];
            popup_6cbb2f91a08f4c3e80a8ea9a8cf013d3.setContent(html_3562f4a2d3e24159b099db28cde59701);
        

        circle_marker_a20fb2382db1489db1a4ee3d2aede6ff.bindPopup(popup_6cbb2f91a08f4c3e80a8ea9a8cf013d3)
        ;

        
    
    
            var circle_marker_729c619eac804a748d7a6b848a61a493 = L.circleMarker(
                [41.863118103, -87.672920435],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_5e455f79f884470d9d51465d9434a367 = L.popup({"maxWidth": "100%"});

        
            var html_a1873b1c735d436493a7c24d4d71fe05 = $(`<div id="html_a1873b1c735d436493a7c24d4d71fe05" style="width: 100.0%; height: 100.0%;">Latitude : 41.863118103<br>                     Longitude : -87.672920435<br>                     frequency : 1<br></div>`)[0];
            popup_5e455f79f884470d9d51465d9434a367.setContent(html_a1873b1c735d436493a7c24d4d71fe05);
        

        circle_marker_729c619eac804a748d7a6b848a61a493.bindPopup(popup_5e455f79f884470d9d51465d9434a367)
        ;

        
    
    
            var circle_marker_6a750f13bc4c45c299ad330a86629882 = L.circleMarker(
                [42.009018227, -87.672723959],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_1d75d733a5c94b36a2e18072ef71d4ee = L.popup({"maxWidth": "100%"});

        
            var html_1e5bddabbca441e8bc3077f3f6ec5a3c = $(`<div id="html_1e5bddabbca441e8bc3077f3f6ec5a3c" style="width: 100.0%; height: 100.0%;">Latitude : 42.009018227<br>                     Longitude : -87.672723959<br>                     frequency : 1<br></div>`)[0];
            popup_1d75d733a5c94b36a2e18072ef71d4ee.setContent(html_1e5bddabbca441e8bc3077f3f6ec5a3c);
        

        circle_marker_6a750f13bc4c45c299ad330a86629882.bindPopup(popup_1d75d733a5c94b36a2e18072ef71d4ee)
        ;

        
    
    
            var circle_marker_3cab09e573eb40f3a513f94cfd9633e0 = L.circleMarker(
                [41.829922304, -87.672502646],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.06428571428571428, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_f327898c438b498cadc41daad242b9ca = L.popup({"maxWidth": "100%"});

        
            var html_15b33119f2aa4742a750c090c490d5b3 = $(`<div id="html_15b33119f2aa4742a750c090c490d5b3" style="width: 100.0%; height: 100.0%;">Latitude : 41.829922304<br>                     Longitude : -87.672502646<br>                     frequency : 18<br></div>`)[0];
            popup_f327898c438b498cadc41daad242b9ca.setContent(html_15b33119f2aa4742a750c090c490d5b3);
        

        circle_marker_3cab09e573eb40f3a513f94cfd9633e0.bindPopup(popup_f327898c438b498cadc41daad242b9ca)
        ;

        
    
    
            var circle_marker_f9a7906d540a4f51bac14d96e0169376 = L.circleMarker(
                [41.87866742, -87.671653621],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.26785714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_80f35d698e374ba5a27a7701b9352105 = L.popup({"maxWidth": "100%"});

        
            var html_64aa95168481412a878eb55257f4c8e5 = $(`<div id="html_64aa95168481412a878eb55257f4c8e5" style="width: 100.0%; height: 100.0%;">Latitude : 41.87866742<br>                     Longitude : -87.671653621<br>                     frequency : 75<br></div>`)[0];
            popup_80f35d698e374ba5a27a7701b9352105.setContent(html_64aa95168481412a878eb55257f4c8e5);
        

        circle_marker_f9a7906d540a4f51bac14d96e0169376.bindPopup(popup_80f35d698e374ba5a27a7701b9352105)
        ;

        
    
    
            var circle_marker_0ca673444d5645fca496ae7acfb2ebbd = L.circleMarker(
                [41.91922505, -87.671445766],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.02142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_f1e7034c09604fdbb952f2374bdadc9d = L.popup({"maxWidth": "100%"});

        
            var html_ae03ed7bbd0944b791ccf3d742605da5 = $(`<div id="html_ae03ed7bbd0944b791ccf3d742605da5" style="width: 100.0%; height: 100.0%;">Latitude : 41.91922505<br>                     Longitude : -87.671445766<br>                     frequency : 6<br></div>`)[0];
            popup_f1e7034c09604fdbb952f2374bdadc9d.setContent(html_ae03ed7bbd0944b791ccf3d742605da5);
        

        circle_marker_0ca673444d5645fca496ae7acfb2ebbd.bindPopup(popup_f1e7034c09604fdbb952f2374bdadc9d)
        ;

        
    
    
            var circle_marker_61842f052512477494df6658fab0bca4 = L.circleMarker(
                [41.979795551, -87.671445547],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.06428571428571428, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_df1f358978ae476a802f9b1d46d90422 = L.popup({"maxWidth": "100%"});

        
            var html_21c62a1f6fc74a3280512caf38fb6f20 = $(`<div id="html_21c62a1f6fc74a3280512caf38fb6f20" style="width: 100.0%; height: 100.0%;">Latitude : 41.979795551<br>                     Longitude : -87.671445547<br>                     frequency : 18<br></div>`)[0];
            popup_df1f358978ae476a802f9b1d46d90422.setContent(html_21c62a1f6fc74a3280512caf38fb6f20);
        

        circle_marker_61842f052512477494df6658fab0bca4.bindPopup(popup_df1f358978ae476a802f9b1d46d90422)
        ;

        
    
    
            var circle_marker_c77ef009e01141c9b9bf88f1d2c3cac1 = L.circleMarker(
                [41.950605232, -87.671332488],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_d0ded30a398e437a9b7057f2abd68d4f = L.popup({"maxWidth": "100%"});

        
            var html_04d6996065444a058bc871f964b3d90c = $(`<div id="html_04d6996065444a058bc871f964b3d90c" style="width: 100.0%; height: 100.0%;">Latitude : 41.950605232<br>                     Longitude : -87.671332488<br>                     frequency : 2<br></div>`)[0];
            popup_d0ded30a398e437a9b7057f2abd68d4f.setContent(html_04d6996065444a058bc871f964b3d90c);
        

        circle_marker_c77ef009e01141c9b9bf88f1d2c3cac1.bindPopup(popup_d0ded30a398e437a9b7057f2abd68d4f)
        ;

        
    
    
            var circle_marker_6d1198b0dcfb442db23c4f778c006347 = L.circleMarker(
                [41.972437081, -87.671109526],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_3b1bff92e6aa4579898e53d9f999c531 = L.popup({"maxWidth": "100%"});

        
            var html_7faf3a3d018c41f48234f797c6900810 = $(`<div id="html_7faf3a3d018c41f48234f797c6900810" style="width: 100.0%; height: 100.0%;">Latitude : 41.972437081<br>                     Longitude : -87.671109526<br>                     frequency : 1<br></div>`)[0];
            popup_3b1bff92e6aa4579898e53d9f999c531.setContent(html_7faf3a3d018c41f48234f797c6900810);
        

        circle_marker_6d1198b0dcfb442db23c4f778c006347.bindPopup(popup_3b1bff92e6aa4579898e53d9f999c531)
        ;

        
    
    
            var circle_marker_7ce425efa58441de95fb5ecce59beb9b = L.circleMarker(
                [41.941488234, -87.671107656],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_b0662ad838fb41f28b1107e933e5dfec = L.popup({"maxWidth": "100%"});

        
            var html_41610a157823405cbeea9b0e74dbefa0 = $(`<div id="html_41610a157823405cbeea9b0e74dbefa0" style="width: 100.0%; height: 100.0%;">Latitude : 41.941488234<br>                     Longitude : -87.671107656<br>                     frequency : 2<br></div>`)[0];
            popup_b0662ad838fb41f28b1107e933e5dfec.setContent(html_41610a157823405cbeea9b0e74dbefa0);
        

        circle_marker_7ce425efa58441de95fb5ecce59beb9b.bindPopup(popup_b0662ad838fb41f28b1107e933e5dfec)
        ;

        
    
    
            var circle_marker_58a11d1f361c4aaa87768f94245757ad = L.circleMarker(
                [41.935988906, -87.670966384],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_201db1b39cbe490eabdc5d52bbef2755 = L.popup({"maxWidth": "100%"});

        
            var html_db184a1add2343d880292421c8ccea5b = $(`<div id="html_db184a1add2343d880292421c8ccea5b" style="width: 100.0%; height: 100.0%;">Latitude : 41.935988906<br>                     Longitude : -87.670966384<br>                     frequency : 2<br></div>`)[0];
            popup_201db1b39cbe490eabdc5d52bbef2755.setContent(html_db184a1add2343d880292421c8ccea5b);
        

        circle_marker_58a11d1f361c4aaa87768f94245757ad.bindPopup(popup_201db1b39cbe490eabdc5d52bbef2755)
        ;

        
    
    
            var circle_marker_b92b46f285ed46f197ca003264960344 = L.circleMarker(
                [41.908378669, -87.670945075],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.06428571428571428, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_32322f430d6a4ecea3cc5450b9984412 = L.popup({"maxWidth": "100%"});

        
            var html_9f2e8dc6d5ec43fc926597007b1843ba = $(`<div id="html_9f2e8dc6d5ec43fc926597007b1843ba" style="width: 100.0%; height: 100.0%;">Latitude : 41.908378669<br>                     Longitude : -87.670945075<br>                     frequency : 18<br></div>`)[0];
            popup_32322f430d6a4ecea3cc5450b9984412.setContent(html_9f2e8dc6d5ec43fc926597007b1843ba);
        

        circle_marker_b92b46f285ed46f197ca003264960344.bindPopup(popup_32322f430d6a4ecea3cc5450b9984412)
        ;

        
    
    
            var circle_marker_b597395daa404005a5477346bcaa33d2 = L.circleMarker(
                [41.912431869, -87.670189148],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_879b5d676c834958b84301ed125dc39e = L.popup({"maxWidth": "100%"});

        
            var html_e60227f16dae422d850e376a300092f3 = $(`<div id="html_e60227f16dae422d850e376a300092f3" style="width: 100.0%; height: 100.0%;">Latitude : 41.912431869<br>                     Longitude : -87.670189148<br>                     frequency : 2<br></div>`)[0];
            popup_879b5d676c834958b84301ed125dc39e.setContent(html_e60227f16dae422d850e376a300092f3);
        

        circle_marker_b597395daa404005a5477346bcaa33d2.bindPopup(popup_879b5d676c834958b84301ed125dc39e)
        ;

        
    
    
            var circle_marker_0e4503b48e084507afc91db8dd940c50 = L.circleMarker(
                [41.963374382, -87.67018455],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_d880f5de6ddf4882b775af1df4ab3735 = L.popup({"maxWidth": "100%"});

        
            var html_51b809360e0a4e12a05a0293a4cfce71 = $(`<div id="html_51b809360e0a4e12a05a0293a4cfce71" style="width: 100.0%; height: 100.0%;">Latitude : 41.963374382<br>                     Longitude : -87.67018455<br>                     frequency : 1<br></div>`)[0];
            popup_d880f5de6ddf4882b775af1df4ab3735.setContent(html_51b809360e0a4e12a05a0293a4cfce71);
        

        circle_marker_0e4503b48e084507afc91db8dd940c50.bindPopup(popup_d880f5de6ddf4882b775af1df4ab3735)
        ;

        
    
    
            var circle_marker_26de03497a5747269ca222e5cf8a8b3b = L.circleMarker(
                [42.009622881, -87.670166857],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.7321428571428571, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_659051a6eda446f1883f89baa1469610 = L.popup({"maxWidth": "100%"});

        
            var html_c533a7a2c2da4c02a4c6f7f143b111e3 = $(`<div id="html_c533a7a2c2da4c02a4c6f7f143b111e3" style="width: 100.0%; height: 100.0%;">Latitude : 42.009622881<br>                     Longitude : -87.670166857<br>                     frequency : 205<br></div>`)[0];
            popup_659051a6eda446f1883f89baa1469610.setContent(html_c533a7a2c2da4c02a4c6f7f143b111e3);
        

        circle_marker_26de03497a5747269ca222e5cf8a8b3b.bindPopup(popup_659051a6eda446f1883f89baa1469610)
        ;

        
    
    
            var circle_marker_45b2b977a79b4cbcb670b434d8b3d79d = L.circleMarker(
                [41.89967018, -87.669837798],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.039285714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_af3f1ef514054ed3adcd9052afa1b9ba = L.popup({"maxWidth": "100%"});

        
            var html_d66ed8f33adc450a879217ca4a48c710 = $(`<div id="html_d66ed8f33adc450a879217ca4a48c710" style="width: 100.0%; height: 100.0%;">Latitude : 41.89967018<br>                     Longitude : -87.669837798<br>                     frequency : 11<br></div>`)[0];
            popup_af3f1ef514054ed3adcd9052afa1b9ba.setContent(html_d66ed8f33adc450a879217ca4a48c710);
        

        circle_marker_45b2b977a79b4cbcb670b434d8b3d79d.bindPopup(popup_af3f1ef514054ed3adcd9052afa1b9ba)
        ;

        
    
    
            var circle_marker_d50b54bad65b4fb69fdf84963e716382 = L.circleMarker(
                [41.689729914, -87.669054403],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_616b1c8bbd824505afd3418b1a73c725 = L.popup({"maxWidth": "100%"});

        
            var html_02429275d31143c5be084de5d0f62082 = $(`<div id="html_02429275d31143c5be084de5d0f62082" style="width: 100.0%; height: 100.0%;">Latitude : 41.689729914<br>                     Longitude : -87.669054403<br>                     frequency : 3<br></div>`)[0];
            popup_616b1c8bbd824505afd3418b1a73c725.setContent(html_02429275d31143c5be084de5d0f62082);
        

        circle_marker_d50b54bad65b4fb69fdf84963e716382.bindPopup(popup_616b1c8bbd824505afd3418b1a73c725)
        ;

        
    
    
            var circle_marker_a3e6068904744bad9f987e614f9e22dd = L.circleMarker(
                [41.945170453, -87.668794439],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_542da5076d724c1286304a02fe69f834 = L.popup({"maxWidth": "100%"});

        
            var html_95c7579d6b9d4f5d9fa1f7977a710983 = $(`<div id="html_95c7579d6b9d4f5d9fa1f7977a710983" style="width: 100.0%; height: 100.0%;">Latitude : 41.945170453<br>                     Longitude : -87.668794439<br>                     frequency : 3<br></div>`)[0];
            popup_542da5076d724c1286304a02fe69f834.setContent(html_95c7579d6b9d4f5d9fa1f7977a710983);
        

        circle_marker_a3e6068904744bad9f987e614f9e22dd.bindPopup(popup_542da5076d724c1286304a02fe69f834)
        ;

        
    
    
            var circle_marker_54b0f20f0ce14ec186f07cdf52dc750f = L.circleMarker(
                [41.850266366, -87.667569312],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.17142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_610001bfb05f4086aee22beaf2e41533 = L.popup({"maxWidth": "100%"});

        
            var html_4874e28175e141f39a4488bac33ab2a3 = $(`<div id="html_4874e28175e141f39a4488bac33ab2a3" style="width: 100.0%; height: 100.0%;">Latitude : 41.850266366<br>                     Longitude : -87.667569312<br>                     frequency : 48<br></div>`)[0];
            popup_610001bfb05f4086aee22beaf2e41533.setContent(html_4874e28175e141f39a4488bac33ab2a3);
        

        circle_marker_54b0f20f0ce14ec186f07cdf52dc750f.bindPopup(popup_610001bfb05f4086aee22beaf2e41533)
        ;

        
    
    
            var circle_marker_35a19a8e06cb46c183e713d7e8633968 = L.circleMarker(
                [41.957530922, -87.66661144],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.014285714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_fdee529330214a2e9b995eaf79205ace = L.popup({"maxWidth": "100%"});

        
            var html_3bed4dafe000444195bd105adbd99d94 = $(`<div id="html_3bed4dafe000444195bd105adbd99d94" style="width: 100.0%; height: 100.0%;">Latitude : 41.957530922<br>                     Longitude : -87.66661144<br>                     frequency : 4<br></div>`)[0];
            popup_fdee529330214a2e9b995eaf79205ace.setContent(html_3bed4dafe000444195bd105adbd99d94);
        

        circle_marker_35a19a8e06cb46c183e713d7e8633968.bindPopup(popup_fdee529330214a2e9b995eaf79205ace)
        ;

        
    
    
            var circle_marker_d38620d60c814bf2a3c2514724494b7e = L.circleMarker(
                [41.775928827, -87.666596265],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_d845189f2e704204a4fb892288a00099 = L.popup({"maxWidth": "100%"});

        
            var html_825d50bb048543b897994febe0267129 = $(`<div id="html_825d50bb048543b897994febe0267129" style="width: 100.0%; height: 100.0%;">Latitude : 41.775928827<br>                     Longitude : -87.666596265<br>                     frequency : 2<br></div>`)[0];
            popup_d845189f2e704204a4fb892288a00099.setContent(html_825d50bb048543b897994febe0267129);
        

        circle_marker_d38620d60c814bf2a3c2514724494b7e.bindPopup(popup_d845189f2e704204a4fb892288a00099)
        ;

        
    
    
            var circle_marker_9116378a863e4566b160f2a2d2af985e = L.circleMarker(
                [41.950673358, -87.666536281],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.03214285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_0db1c5ce7d4a4da69b800d18979efad2 = L.popup({"maxWidth": "100%"});

        
            var html_eb1bcf0cb2ad41ccb6e386d2e3cd3b2a = $(`<div id="html_eb1bcf0cb2ad41ccb6e386d2e3cd3b2a" style="width: 100.0%; height: 100.0%;">Latitude : 41.950673358<br>                     Longitude : -87.666536281<br>                     frequency : 9<br></div>`)[0];
            popup_0db1c5ce7d4a4da69b800d18979efad2.setContent(html_eb1bcf0cb2ad41ccb6e386d2e3cd3b2a);
        

        circle_marker_9116378a863e4566b160f2a2d2af985e.bindPopup(popup_0db1c5ce7d4a4da69b800d18979efad2)
        ;

        
    
    
            var circle_marker_09ce0a27753f4e6e937b886c7348bf95 = L.circleMarker(
                [41.941555829, -87.666288887],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_c6b5614ec9134e8fa4ef2c16abe22e2d = L.popup({"maxWidth": "100%"});

        
            var html_3ce74f2c9ebe439983c4283014d25806 = $(`<div id="html_3ce74f2c9ebe439983c4283014d25806" style="width: 100.0%; height: 100.0%;">Latitude : 41.941555829<br>                     Longitude : -87.666288887<br>                     frequency : 1<br></div>`)[0];
            popup_c6b5614ec9134e8fa4ef2c16abe22e2d.setContent(html_3ce74f2c9ebe439983c4283014d25806);
        

        circle_marker_09ce0a27753f4e6e937b886c7348bf95.bindPopup(popup_c6b5614ec9134e8fa4ef2c16abe22e2d)
        ;

        
    
    
            var circle_marker_f2e1c76a9e9c47aa8d6f35f3a571dfea = L.circleMarker(
                [41.936086535, -87.666110694],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_f66308a77eb74824961a7996c91f90bc = L.popup({"maxWidth": "100%"});

        
            var html_db61ccb4928b4def9162a4faa007bf97 = $(`<div id="html_db61ccb4928b4def9162a4faa007bf97" style="width: 100.0%; height: 100.0%;">Latitude : 41.936086535<br>                     Longitude : -87.666110694<br>                     frequency : 2<br></div>`)[0];
            popup_f66308a77eb74824961a7996c91f90bc.setContent(html_db61ccb4928b4def9162a4faa007bf97);
        

        circle_marker_f2e1c76a9e9c47aa8d6f35f3a571dfea.bindPopup(popup_f66308a77eb74824961a7996c91f90bc)
        ;

        
    
    
            var circle_marker_239bfe26d6824b3fa2bec03d1295a5f8 = L.circleMarker(
                [41.928763006, -87.665676837],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_da449ab84a534e068238068323892731 = L.popup({"maxWidth": "100%"});

        
            var html_13379bd8eff343ba91c0e288fbbea350 = $(`<div id="html_13379bd8eff343ba91c0e288fbbea350" style="width: 100.0%; height: 100.0%;">Latitude : 41.928763006<br>                     Longitude : -87.665676837<br>                     frequency : 3<br></div>`)[0];
            popup_da449ab84a534e068238068323892731.setContent(html_13379bd8eff343ba91c0e288fbbea350);
        

        circle_marker_239bfe26d6824b3fa2bec03d1295a5f8.bindPopup(popup_da449ab84a534e068238068323892731)
        ;

        
    
    
            var circle_marker_3edbc27825be46fd96a8263a69a7a1f4 = L.circleMarker(
                [41.906650766, -87.66533766],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.07857142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_311a4478062343ac84e849b198591459 = L.popup({"maxWidth": "100%"});

        
            var html_17280e793a7c410ab89cee894db7daac = $(`<div id="html_17280e793a7c410ab89cee894db7daac" style="width: 100.0%; height: 100.0%;">Latitude : 41.906650766<br>                     Longitude : -87.66533766<br>                     frequency : 22<br></div>`)[0];
            popup_311a4478062343ac84e849b198591459.setContent(html_17280e793a7c410ab89cee894db7daac);
        

        circle_marker_3edbc27825be46fd96a8263a69a7a1f4.bindPopup(popup_311a4478062343ac84e849b198591459)
        ;

        
    
    
            var circle_marker_e73be03d1a46428b8e6562ef6c6d886e = L.circleMarker(
                [41.994442248, -87.665224776],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.014285714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_0f9907f288e4463985894f529c3b055d = L.popup({"maxWidth": "100%"});

        
            var html_3e1e2a08d271480da4d489617e1f29ce = $(`<div id="html_3e1e2a08d271480da4d489617e1f29ce" style="width: 100.0%; height: 100.0%;">Latitude : 41.994442248<br>                     Longitude : -87.665224776<br>                     frequency : 4<br></div>`)[0];
            popup_0f9907f288e4463985894f529c3b055d.setContent(html_3e1e2a08d271480da4d489617e1f29ce);
        

        circle_marker_e73be03d1a46428b8e6562ef6c6d886e.bindPopup(popup_0f9907f288e4463985894f529c3b055d)
        ;

        
    
    
            var circle_marker_ca86ae33a2974ac5b98aa5ae970167ea = L.circleMarker(
                [41.899737388, -87.664953917],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.039285714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_ff416fa4b96c4e538169fdce429cb145 = L.popup({"maxWidth": "100%"});

        
            var html_47016f761a6a439cb0455450d5b779d2 = $(`<div id="html_47016f761a6a439cb0455450d5b779d2" style="width: 100.0%; height: 100.0%;">Latitude : 41.899737388<br>                     Longitude : -87.664953917<br>                     frequency : 11<br></div>`)[0];
            popup_ff416fa4b96c4e538169fdce429cb145.setContent(html_47016f761a6a439cb0455450d5b779d2);
        

        circle_marker_ca86ae33a2974ac5b98aa5ae970167ea.bindPopup(popup_ff416fa4b96c4e538169fdce429cb145)
        ;

        
    
    
            var circle_marker_8901fd7c5b094570acbac6ce7cddffb3 = L.circleMarker(
                [41.987225558, -87.664937724],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_ef4d91b86c884c728df9de6e32400eb0 = L.popup({"maxWidth": "100%"});

        
            var html_a1813d7e8b9a4a838eb2731ad126f88e = $(`<div id="html_a1813d7e8b9a4a838eb2731ad126f88e" style="width: 100.0%; height: 100.0%;">Latitude : 41.987225558<br>                     Longitude : -87.664937724<br>                     frequency : 3<br></div>`)[0];
            popup_ef4d91b86c884c728df9de6e32400eb0.setContent(html_a1813d7e8b9a4a838eb2731ad126f88e);
        

        circle_marker_8901fd7c5b094570acbac6ce7cddffb3.bindPopup(popup_ef4d91b86c884c728df9de6e32400eb0)
        ;

        
    
    
            var circle_marker_506ebb85e9e848cfbfd4a0f35c97d75c = L.circleMarker(
                [41.892493167, -87.664745836],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_88dfcb7926344741a6082afd598915d4 = L.popup({"maxWidth": "100%"});

        
            var html_74c35b01edf04aca89dbe5a186a6d1c1 = $(`<div id="html_74c35b01edf04aca89dbe5a186a6d1c1" style="width: 100.0%; height: 100.0%;">Latitude : 41.892493167<br>                     Longitude : -87.664745836<br>                     frequency : 3<br></div>`)[0];
            popup_88dfcb7926344741a6082afd598915d4.setContent(html_74c35b01edf04aca89dbe5a186a6d1c1);
        

        circle_marker_506ebb85e9e848cfbfd4a0f35c97d75c.bindPopup(popup_88dfcb7926344741a6082afd598915d4)
        ;

        
    
    
            var circle_marker_1c4b7ecc9944491f8239fabbcdb81ec7 = L.circleMarker(
                [41.979912445, -87.664188242],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.017857142857142856, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_a3db15a2297f4ecca061dfc6e843d2e9 = L.popup({"maxWidth": "100%"});

        
            var html_145be683455b43858b192545c0a573a4 = $(`<div id="html_145be683455b43858b192545c0a573a4" style="width: 100.0%; height: 100.0%;">Latitude : 41.979912445<br>                     Longitude : -87.664188242<br>                     frequency : 5<br></div>`)[0];
            popup_a3db15a2297f4ecca061dfc6e843d2e9.setContent(html_145be683455b43858b192545c0a573a4);
        

        circle_marker_1c4b7ecc9944491f8239fabbcdb81ec7.bindPopup(popup_a3db15a2297f4ecca061dfc6e843d2e9)
        ;

        
    
    
            var circle_marker_a9a995cc3d7840cfaa49338f9309d859 = L.circleMarker(
                [41.921877461, -87.66407824],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.039285714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_4e36dfd34df64c4497c87fa7f4ee201c = L.popup({"maxWidth": "100%"});

        
            var html_4633f6093a3e44de84eb3ab0ab157ba8 = $(`<div id="html_4633f6093a3e44de84eb3ab0ab157ba8" style="width: 100.0%; height: 100.0%;">Latitude : 41.921877461<br>                     Longitude : -87.66407824<br>                     frequency : 11<br></div>`)[0];
            popup_4e36dfd34df64c4497c87fa7f4ee201c.setContent(html_4633f6093a3e44de84eb3ab0ab157ba8);
        

        circle_marker_a9a995cc3d7840cfaa49338f9309d859.bindPopup(popup_4e36dfd34df64c4497c87fa7f4ee201c)
        ;

        
    
    
            var circle_marker_4bef1454fcd3441db75b7535a3928376 = L.circleMarker(
                [42.009412547, -87.663958214],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_3d0e244aa2e84fb7b80f7e2bb3520da0 = L.popup({"maxWidth": "100%"});

        
            var html_6c31a4829cf94f958eb0c8feb7cfef67 = $(`<div id="html_6c31a4829cf94f958eb0c8feb7cfef67" style="width: 100.0%; height: 100.0%;">Latitude : 42.009412547<br>                     Longitude : -87.663958214<br>                     frequency : 1<br></div>`)[0];
            popup_3d0e244aa2e84fb7b80f7e2bb3520da0.setContent(html_6c31a4829cf94f958eb0c8feb7cfef67);
        

        circle_marker_4bef1454fcd3441db75b7535a3928376.bindPopup(popup_3d0e244aa2e84fb7b80f7e2bb3520da0)
        ;

        
    
    
            var circle_marker_18974ba5597b441f841e181f9d0338b0 = L.circleMarker(
                [41.972667956, -87.663865496],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.03571428571428571, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_53d6d157afed4285be71e585db745016 = L.popup({"maxWidth": "100%"});

        
            var html_7bbd11ef067e45b2b0d919ed3bbf72e9 = $(`<div id="html_7bbd11ef067e45b2b0d919ed3bbf72e9" style="width: 100.0%; height: 100.0%;">Latitude : 41.972667956<br>                     Longitude : -87.663865496<br>                     frequency : 10<br></div>`)[0];
            popup_53d6d157afed4285be71e585db745016.setContent(html_7bbd11ef067e45b2b0d919ed3bbf72e9);
        

        circle_marker_18974ba5597b441f841e181f9d0338b0.bindPopup(popup_53d6d157afed4285be71e585db745016)
        ;

        
    
    
            var circle_marker_55d18d1ac06a4732867a976ceb2c3321 = L.circleMarker(
                [41.874005383, -87.66351755],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 3.2071428571428573, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_4f7cee3eed354c54ba950df40f0cb846 = L.popup({"maxWidth": "100%"});

        
            var html_70f5d36bd2994077bc161d13e6267855 = $(`<div id="html_70f5d36bd2994077bc161d13e6267855" style="width: 100.0%; height: 100.0%;">Latitude : 41.874005383<br>                     Longitude : -87.66351755<br>                     frequency : 898<br></div>`)[0];
            popup_4f7cee3eed354c54ba950df40f0cb846.setContent(html_70f5d36bd2994077bc161d13e6267855);
        

        circle_marker_55d18d1ac06a4732867a976ceb2c3321.bindPopup(popup_4f7cee3eed354c54ba950df40f0cb846)
        ;

        
    
    
            var circle_marker_994808e58cb745b2b9e9509158001dd0 = L.circleMarker(
                [41.9867118, -87.663416405],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1.457142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_f2d75b4b61494953b5c7b63fbaf1a01a = L.popup({"maxWidth": "100%"});

        
            var html_52b6d6f5a6bc4e648731b728529e9879 = $(`<div id="html_52b6d6f5a6bc4e648731b728529e9879" style="width: 100.0%; height: 100.0%;">Latitude : 41.9867118<br>                     Longitude : -87.663416405<br>                     frequency : 408<br></div>`)[0];
            popup_f2d75b4b61494953b5c7b63fbaf1a01a.setContent(html_52b6d6f5a6bc4e648731b728529e9879);
        

        circle_marker_994808e58cb745b2b9e9509158001dd0.bindPopup(popup_f2d75b4b61494953b5c7b63fbaf1a01a)
        ;

        
    
    
            var circle_marker_b3e36d7f23cb4bac9111fd9ee0593de4 = L.circleMarker(
                [42.004517488, -87.663327859],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_41698e95eff64d9a8c45e16c4a71c5b4 = L.popup({"maxWidth": "100%"});

        
            var html_aeca14ed78ec480987a549667076b5ae = $(`<div id="html_aeca14ed78ec480987a549667076b5ae" style="width: 100.0%; height: 100.0%;">Latitude : 42.004517488<br>                     Longitude : -87.663327859<br>                     frequency : 1<br></div>`)[0];
            popup_41698e95eff64d9a8c45e16c4a71c5b4.setContent(html_aeca14ed78ec480987a549667076b5ae);
        

        circle_marker_b3e36d7f23cb4bac9111fd9ee0593de4.bindPopup(popup_41698e95eff64d9a8c45e16c4a71c5b4)
        ;

        
    
    
            var circle_marker_5263c1a3ff204614a710565e94639508 = L.circleMarker(
                [41.965445784, -87.66319585],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_860c34a4982b4bac9f5bedbaf832c577 = L.popup({"maxWidth": "100%"});

        
            var html_626ebeb985294ddda0c364e8250af516 = $(`<div id="html_626ebeb985294ddda0c364e8250af516" style="width: 100.0%; height: 100.0%;">Latitude : 41.965445784<br>                     Longitude : -87.66319585<br>                     frequency : 3<br></div>`)[0];
            popup_860c34a4982b4bac9f5bedbaf832c577.setContent(html_626ebeb985294ddda0c364e8250af516);
        

        circle_marker_5263c1a3ff204614a710565e94639508.bindPopup(popup_860c34a4982b4bac9f5bedbaf832c577)
        ;

        
    
    
            var circle_marker_3d35c8ed56594a56b3b41e1a5070a80e = L.circleMarker(
                [42.000320306, -87.6631268],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_8822b6184d704d058122e178fb72db11 = L.popup({"maxWidth": "100%"});

        
            var html_62f47bbd9aa6446482426a852a2fddfa = $(`<div id="html_62f47bbd9aa6446482426a852a2fddfa" style="width: 100.0%; height: 100.0%;">Latitude : 42.000320306<br>                     Longitude : -87.6631268<br>                     frequency : 1<br></div>`)[0];
            popup_8822b6184d704d058122e178fb72db11.setContent(html_62f47bbd9aa6446482426a852a2fddfa);
        

        circle_marker_3d35c8ed56594a56b3b41e1a5070a80e.bindPopup(popup_8822b6184d704d058122e178fb72db11)
        ;

        
    
    
            var circle_marker_6104cd879d244f0998998b68d3b9d38a = L.circleMarker(
                [41.874176625, -87.661861124],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_9799a3bb95c74139acc4779d33b4808d = L.popup({"maxWidth": "100%"});

        
            var html_2c4caaad801e43f49e5f29e294dbde15 = $(`<div id="html_2c4caaad801e43f49e5f29e294dbde15" style="width: 100.0%; height: 100.0%;">Latitude : 41.874176625<br>                     Longitude : -87.661861124<br>                     frequency : 1<br></div>`)[0];
            popup_9799a3bb95c74139acc4779d33b4808d.setContent(html_2c4caaad801e43f49e5f29e294dbde15);
        

        circle_marker_6104cd879d244f0998998b68d3b9d38a.bindPopup(popup_9799a3bb95c74139acc4779d33b4808d)
        ;

        
    
    
            var circle_marker_5553f67261a440b9b7c7b13f80c077a9 = L.circleMarker(
                [41.949060526, -87.661642904],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.03571428571428571, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_89977f8411d84b2fb8af6faaf56bf950 = L.popup({"maxWidth": "100%"});

        
            var html_64f18e231c1b4e6e9a2c583b097b5b9e = $(`<div id="html_64f18e231c1b4e6e9a2c583b097b5b9e" style="width: 100.0%; height: 100.0%;">Latitude : 41.949060526<br>                     Longitude : -87.661642904<br>                     frequency : 10<br></div>`)[0];
            popup_89977f8411d84b2fb8af6faaf56bf950.setContent(html_64f18e231c1b4e6e9a2c583b097b5b9e);
        

        circle_marker_5553f67261a440b9b7c7b13f80c077a9.bindPopup(popup_89977f8411d84b2fb8af6faaf56bf950)
        ;

        
    
    
            var circle_marker_3b71e2c0d572475ebf50343d6d38add2 = L.circleMarker(
                [41.945282331, -87.661545096],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_9d6e3dccca4942b79d28dfb47c7388e7 = L.popup({"maxWidth": "100%"});

        
            var html_86205423c0fc4c17abe9f44d9b690c32 = $(`<div id="html_86205423c0fc4c17abe9f44d9b690c32" style="width: 100.0%; height: 100.0%;">Latitude : 41.945282331<br>                     Longitude : -87.661545096<br>                     frequency : 3<br></div>`)[0];
            popup_9d6e3dccca4942b79d28dfb47c7388e7.setContent(html_86205423c0fc4c17abe9f44d9b690c32);
        

        circle_marker_3b71e2c0d572475ebf50343d6d38add2.bindPopup(popup_9d6e3dccca4942b79d28dfb47c7388e7)
        ;

        
    
    
            var circle_marker_f62223d4b1ef4f3aabadde7732812600 = L.circleMarker(
                [41.936159071, -87.661265218],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.039285714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_62789033568b4eaa8b1ed2e449d2cbfe = L.popup({"maxWidth": "100%"});

        
            var html_d4b073ffb8f8423bb4bdace45dd8819a = $(`<div id="html_d4b073ffb8f8423bb4bdace45dd8819a" style="width: 100.0%; height: 100.0%;">Latitude : 41.936159071<br>                     Longitude : -87.661265218<br>                     frequency : 11<br></div>`)[0];
            popup_62789033568b4eaa8b1ed2e449d2cbfe.setContent(html_d4b073ffb8f8423bb4bdace45dd8819a);
        

        circle_marker_f62223d4b1ef4f3aabadde7732812600.bindPopup(popup_62789033568b4eaa8b1ed2e449d2cbfe)
        ;

        
    
    
            var circle_marker_36458064749b4367b2e40c8d4e41a172 = L.circleMarker(
                [41.928945904, -87.66089257],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_47351c2dd79c45ea8f9ee736a56f909f = L.popup({"maxWidth": "100%"});

        
            var html_be97b018c7044f47a2be4abb90b130a0 = $(`<div id="html_be97b018c7044f47a2be4abb90b130a0" style="width: 100.0%; height: 100.0%;">Latitude : 41.928945904<br>                     Longitude : -87.66089257<br>                     frequency : 2<br></div>`)[0];
            popup_47351c2dd79c45ea8f9ee736a56f909f.setContent(html_be97b018c7044f47a2be4abb90b130a0);
        

        circle_marker_36458064749b4367b2e40c8d4e41a172.bindPopup(popup_47351c2dd79c45ea8f9ee736a56f909f)
        ;

        
    
    
            var circle_marker_579115e85fed4e029561daff881da4ac = L.circleMarker(
                [41.952719111, -87.660503502],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_d6f4b4cabab8467d947da918c289c53b = L.popup({"maxWidth": "100%"});

        
            var html_dd2ea3c24b224884813abe34666016d7 = $(`<div id="html_dd2ea3c24b224884813abe34666016d7" style="width: 100.0%; height: 100.0%;">Latitude : 41.952719111<br>                     Longitude : -87.660503502<br>                     frequency : 3<br></div>`)[0];
            popup_d6f4b4cabab8467d947da918c289c53b.setContent(html_dd2ea3c24b224884813abe34666016d7);
        

        circle_marker_579115e85fed4e029561daff881da4ac.bindPopup(popup_d6f4b4cabab8467d947da918c289c53b)
        ;

        
    
    
            var circle_marker_02f73aba66294dfebafdc3f5796f5dfa = L.circleMarker(
                [41.958055933, -87.660389456],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.07857142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_fc1b9cf5c61a434ca80af5ee1b325f29 = L.popup({"maxWidth": "100%"});

        
            var html_94de9196b85343e8a16a1964cda3c1ce = $(`<div id="html_94de9196b85343e8a16a1964cda3c1ce" style="width: 100.0%; height: 100.0%;">Latitude : 41.958055933<br>                     Longitude : -87.660389456<br>                     frequency : 22<br></div>`)[0];
            popup_fc1b9cf5c61a434ca80af5ee1b325f29.setContent(html_94de9196b85343e8a16a1964cda3c1ce);
        

        circle_marker_02f73aba66294dfebafdc3f5796f5dfa.bindPopup(popup_fc1b9cf5c61a434ca80af5ee1b325f29)
        ;

        
    
    
            var circle_marker_e6f1fef4f11d4c41814deed6da544d4a = L.circleMarker(
                [41.892536872, -87.659864318],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.02857142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_8667f1bdb5824991a0dbe60dfaa6b547 = L.popup({"maxWidth": "100%"});

        
            var html_6347f7509cc14a25b6016fa359e24ada = $(`<div id="html_6347f7509cc14a25b6016fa359e24ada" style="width: 100.0%; height: 100.0%;">Latitude : 41.892536872<br>                     Longitude : -87.659864318<br>                     frequency : 8<br></div>`)[0];
            popup_8667f1bdb5824991a0dbe60dfaa6b547.setContent(html_6347f7509cc14a25b6016fa359e24ada);
        

        circle_marker_e6f1fef4f11d4c41814deed6da544d4a.bindPopup(popup_8667f1bdb5824991a0dbe60dfaa6b547)
        ;

        
    
    
            var circle_marker_0264f8bbaf8a42caad0e23b13917a86f = L.circleMarker(
                [41.856333217, -87.659564239],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_58824ed21088458fbcac607bbd0b83ca = L.popup({"maxWidth": "100%"});

        
            var html_5c838188f876428eb38435ee344cd251 = $(`<div id="html_5c838188f876428eb38435ee344cd251" style="width: 100.0%; height: 100.0%;">Latitude : 41.856333217<br>                     Longitude : -87.659564239<br>                     frequency : 1<br></div>`)[0];
            popup_58824ed21088458fbcac607bbd0b83ca.setContent(html_5c838188f876428eb38435ee344cd251);
        

        circle_marker_0264f8bbaf8a42caad0e23b13917a86f.bindPopup(popup_58824ed21088458fbcac607bbd0b83ca)
        ;

        
    
    
            var circle_marker_2a0e869b0d9d414685b52fa0b34beb62 = L.circleMarker(
                [41.80901825, -87.659166599],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.04285714285714286, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_cf58c0b1c66e4a07af0037927193e396 = L.popup({"maxWidth": "100%"});

        
            var html_da14689ef2cb40c09fb4fdecfb54f410 = $(`<div id="html_da14689ef2cb40c09fb4fdecfb54f410" style="width: 100.0%; height: 100.0%;">Latitude : 41.80901825<br>                     Longitude : -87.659166599<br>                     frequency : 12<br></div>`)[0];
            popup_cf58c0b1c66e4a07af0037927193e396.setContent(html_da14689ef2cb40c09fb4fdecfb54f410);
        

        circle_marker_2a0e869b0d9d414685b52fa0b34beb62.bindPopup(popup_cf58c0b1c66e4a07af0037927193e396)
        ;

        
    
    
            var circle_marker_f019a182dfd244a9ad933bdc4374c66c = L.circleMarker(
                [42.004764559, -87.659122427],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_4a8e47f017da4deda14a1ccb3a17c7cd = L.popup({"maxWidth": "100%"});

        
            var html_a5f035047a964c80afdbfb1bf6f0f2b9 = $(`<div id="html_a5f035047a964c80afdbfb1bf6f0f2b9" style="width: 100.0%; height: 100.0%;">Latitude : 42.004764559<br>                     Longitude : -87.659122427<br>                     frequency : 2<br></div>`)[0];
            popup_4a8e47f017da4deda14a1ccb3a17c7cd.setContent(html_a5f035047a964c80afdbfb1bf6f0f2b9);
        

        circle_marker_f019a182dfd244a9ad933bdc4374c66c.bindPopup(popup_4a8e47f017da4deda14a1ccb3a17c7cd)
        ;

        
    
    
            var circle_marker_a99dd0efd96b434fba2cc357cfdf48e6 = L.circleMarker(
                [41.982745595, -87.657966347],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_24a2f4b34e1c4d49b0ea67586637c290 = L.popup({"maxWidth": "100%"});

        
            var html_afcdeaf9d0e745e1b31240f1e31c2073 = $(`<div id="html_afcdeaf9d0e745e1b31240f1e31c2073" style="width: 100.0%; height: 100.0%;">Latitude : 41.982745595<br>                     Longitude : -87.657966347<br>                     frequency : 1<br></div>`)[0];
            popup_24a2f4b34e1c4d49b0ea67586637c290.setContent(html_afcdeaf9d0e745e1b31240f1e31c2073);
        

        circle_marker_a99dd0efd96b434fba2cc357cfdf48e6.bindPopup(popup_24a2f4b34e1c4d49b0ea67586637c290)
        ;

        
    
    
            var circle_marker_187d198747cb4448937dbded0b485f5d = L.circleMarker(
                [41.978875058, -87.657871263],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_8ae7863a7bf84cb296a81bcf011e5bae = L.popup({"maxWidth": "100%"});

        
            var html_2ee176a34a6249fda2bd462f5f0fc116 = $(`<div id="html_2ee176a34a6249fda2bd462f5f0fc116" style="width: 100.0%; height: 100.0%;">Latitude : 41.978875058<br>                     Longitude : -87.657871263<br>                     frequency : 1<br></div>`)[0];
            popup_8ae7863a7bf84cb296a81bcf011e5bae.setContent(html_2ee176a34a6249fda2bd462f5f0fc116);
        

        circle_marker_187d198747cb4448937dbded0b485f5d.bindPopup(popup_8ae7863a7bf84cb296a81bcf011e5bae)
        ;

        
    
    
            var circle_marker_23c24bb281b0445db158b6cac86c5418 = L.circleMarker(
                [41.993440946, -87.657417742],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_0fb4c5e04b13472d9a8e6ad27e4c4f72 = L.popup({"maxWidth": "100%"});

        
            var html_4021ad614e3a404c8fd7fec2624dee0c = $(`<div id="html_4021ad614e3a404c8fd7fec2624dee0c" style="width: 100.0%; height: 100.0%;">Latitude : 41.993440946<br>                     Longitude : -87.657417742<br>                     frequency : 2<br></div>`)[0];
            popup_0fb4c5e04b13472d9a8e6ad27e4c4f72.setContent(html_4021ad614e3a404c8fd7fec2624dee0c);
        

        circle_marker_23c24bb281b0445db158b6cac86c5418.bindPopup(popup_0fb4c5e04b13472d9a8e6ad27e4c4f72)
        ;

        
    
    
            var circle_marker_7c0637b3db5c47aab3fdd4539ab49fc7 = L.circleMarker(
                [41.972709547, -87.657341107],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.025, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_a38a6cb65781478fa9fb0648f56cd9e3 = L.popup({"maxWidth": "100%"});

        
            var html_77f65e4377df49428bc9a81cf787da9d = $(`<div id="html_77f65e4377df49428bc9a81cf787da9d" style="width: 100.0%; height: 100.0%;">Latitude : 41.972709547<br>                     Longitude : -87.657341107<br>                     frequency : 7<br></div>`)[0];
            popup_a38a6cb65781478fa9fb0648f56cd9e3.setContent(html_77f65e4377df49428bc9a81cf787da9d);
        

        circle_marker_7c0637b3db5c47aab3fdd4539ab49fc7.bindPopup(popup_a38a6cb65781478fa9fb0648f56cd9e3)
        ;

        
    
    
            var circle_marker_b1407d2dd6124c9b84f57ce75c12fa82 = L.circleMarker(
                [41.991234532, -87.65730427],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_95e8335592cf4ae9a41859c6131d6cf1 = L.popup({"maxWidth": "100%"});

        
            var html_fef3d785b5534c5c88718c778a2c80f3 = $(`<div id="html_fef3d785b5534c5c88718c778a2c80f3" style="width: 100.0%; height: 100.0%;">Latitude : 41.991234532<br>                     Longitude : -87.65730427<br>                     frequency : 1<br></div>`)[0];
            popup_95e8335592cf4ae9a41859c6131d6cf1.setContent(html_fef3d785b5534c5c88718c778a2c80f3);
        

        circle_marker_b1407d2dd6124c9b84f57ce75c12fa82.bindPopup(popup_95e8335592cf4ae9a41859c6131d6cf1)
        ;

        
    
    
            var circle_marker_ec7e3a82a63f41f58170ab840de0944b = L.circleMarker(
                [41.988704022, -87.657234828],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_ff0e814cf9bc4d0a864542359228bdeb = L.popup({"maxWidth": "100%"});

        
            var html_3a47cdffc9b4403db34778e10817d893 = $(`<div id="html_3a47cdffc9b4403db34778e10817d893" style="width: 100.0%; height: 100.0%;">Latitude : 41.988704022<br>                     Longitude : -87.657234828<br>                     frequency : 2<br></div>`)[0];
            popup_ff0e814cf9bc4d0a864542359228bdeb.setContent(html_3a47cdffc9b4403db34778e10817d893);
        

        circle_marker_ec7e3a82a63f41f58170ab840de0944b.bindPopup(popup_ff0e814cf9bc4d0a864542359228bdeb)
        ;

        
    
    
            var circle_marker_3f702b2376b24bc986673910a5d0672a = L.circleMarker(
                [41.88528132, -87.6572332],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 2.1, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_808fedc7f2d547ceb84d45e1ac204d40 = L.popup({"maxWidth": "100%"});

        
            var html_2ef61e53c5bc49bc937b2c3b73e1703b = $(`<div id="html_2ef61e53c5bc49bc937b2c3b73e1703b" style="width: 100.0%; height: 100.0%;">Latitude : 41.88528132<br>                     Longitude : -87.6572332<br>                     frequency : 588<br></div>`)[0];
            popup_808fedc7f2d547ceb84d45e1ac204d40.setContent(html_2ef61e53c5bc49bc937b2c3b73e1703b);
        

        circle_marker_3f702b2376b24bc986673910a5d0672a.bindPopup(popup_808fedc7f2d547ceb84d45e1ac204d40)
        ;

        
    
    
            var circle_marker_00f85c62cd7f4cb6987e064a8f92a950 = L.circleMarker(
                [41.879066994, -87.657005027],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.5392857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_4f90b7ff11db41118f41a0565a73d446 = L.popup({"maxWidth": "100%"});

        
            var html_b7b98f16877447d49dc0fe572651639f = $(`<div id="html_b7b98f16877447d49dc0fe572651639f" style="width: 100.0%; height: 100.0%;">Latitude : 41.879066994<br>                     Longitude : -87.657005027<br>                     frequency : 151<br></div>`)[0];
            popup_4f90b7ff11db41118f41a0565a73d446.setContent(html_b7b98f16877447d49dc0fe572651639f);
        

        circle_marker_00f85c62cd7f4cb6987e064a8f92a950.bindPopup(popup_4f90b7ff11db41118f41a0565a73d446)
        ;

        
    
    
            var circle_marker_034dc05cf9254f0ea35f3e8ea526c48f = L.circleMarker(
                [41.949139771, -87.656803909],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.14642857142857144, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_b5018a5745c74c65acb85dc5f21808dd = L.popup({"maxWidth": "100%"});

        
            var html_4a586fd9bb964db98e6e1deb959cd740 = $(`<div id="html_4a586fd9bb964db98e6e1deb959cd740" style="width: 100.0%; height: 100.0%;">Latitude : 41.949139771<br>                     Longitude : -87.656803909<br>                     frequency : 41<br></div>`)[0];
            popup_b5018a5745c74c65acb85dc5f21808dd.setContent(html_4a586fd9bb964db98e6e1deb959cd740);
        

        circle_marker_034dc05cf9254f0ea35f3e8ea526c48f.bindPopup(popup_b5018a5745c74c65acb85dc5f21808dd)
        ;

        
    
    
            var circle_marker_97be516f11f74a8b8c29897cde0cb6f8 = L.circleMarker(
                [41.94258518, -87.656644092],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.1392857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_155a91e92c4d4826a8aec35558abcdf7 = L.popup({"maxWidth": "100%"});

        
            var html_2e4f8dc262f0418a8a6462aa2b94a8bb = $(`<div id="html_2e4f8dc262f0418a8a6462aa2b94a8bb" style="width: 100.0%; height: 100.0%;">Latitude : 41.94258518<br>                     Longitude : -87.656644092<br>                     frequency : 39<br></div>`)[0];
            popup_155a91e92c4d4826a8aec35558abcdf7.setContent(html_2e4f8dc262f0418a8a6462aa2b94a8bb);
        

        circle_marker_97be516f11f74a8b8c29897cde0cb6f8.bindPopup(popup_155a91e92c4d4826a8aec35558abcdf7)
        ;

        
    
    
            var circle_marker_7f8de50fd95841fc92a2930ab9d55303 = L.circleMarker(
                [41.936237179, -87.656411531],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.08571428571428572, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_845af748b7de41a9b99ca7ad141ed182 = L.popup({"maxWidth": "100%"});

        
            var html_f59ecf2161024935b34a2f2ad5f8c939 = $(`<div id="html_f59ecf2161024935b34a2f2ad5f8c939" style="width: 100.0%; height: 100.0%;">Latitude : 41.936237179<br>                     Longitude : -87.656411531<br>                     frequency : 24<br></div>`)[0];
            popup_845af748b7de41a9b99ca7ad141ed182.setContent(html_f59ecf2161024935b34a2f2ad5f8c939);
        

        circle_marker_7f8de50fd95841fc92a2930ab9d55303.bindPopup(popup_845af748b7de41a9b99ca7ad141ed182)
        ;

        
    
    
            var circle_marker_ee8ea3cea4a0481b93c1589541aee5fe = L.circleMarker(
                [41.744205146, -87.656305986],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.02142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_8ac7083ddefe4ec6baa30d7370e92bf2 = L.popup({"maxWidth": "100%"});

        
            var html_ca5dc76e422a43f78bf920084752851f = $(`<div id="html_ca5dc76e422a43f78bf920084752851f" style="width: 100.0%; height: 100.0%;">Latitude : 41.744205146<br>                     Longitude : -87.656305986<br>                     frequency : 6<br></div>`)[0];
            popup_8ac7083ddefe4ec6baa30d7370e92bf2.setContent(html_ca5dc76e422a43f78bf920084752851f);
        

        circle_marker_ee8ea3cea4a0481b93c1589541aee5fe.bindPopup(popup_8ac7083ddefe4ec6baa30d7370e92bf2)
        ;

        
    
    
            var circle_marker_3451153240554714a10e00093c50074d = L.circleMarker(
                [41.928967266, -87.656156831],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.04285714285714286, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_8c7b6256a639483fa7df6a6158d86eef = L.popup({"maxWidth": "100%"});

        
            var html_622d7a86c6e84fb9a04fa27c6fe96c4c = $(`<div id="html_622d7a86c6e84fb9a04fa27c6fe96c4c" style="width: 100.0%; height: 100.0%;">Latitude : 41.928967266<br>                     Longitude : -87.656156831<br>                     frequency : 12<br></div>`)[0];
            popup_8c7b6256a639483fa7df6a6158d86eef.setContent(html_622d7a86c6e84fb9a04fa27c6fe96c4c);
        

        circle_marker_3451153240554714a10e00093c50074d.bindPopup(popup_8c7b6256a639483fa7df6a6158d86eef)
        ;

        
    
    
            var circle_marker_6765b48e03dc4f538410f9603123c47e = L.circleMarker(
                [41.944226601, -87.655998182],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.392857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_be6e5f5bfe79444db932e7e356051439 = L.popup({"maxWidth": "100%"});

        
            var html_7d31862bf86e426bbd14f0647153ba3f = $(`<div id="html_7d31862bf86e426bbd14f0647153ba3f" style="width: 100.0%; height: 100.0%;">Latitude : 41.944226601<br>                     Longitude : -87.655998182<br>                     frequency : 1510<br></div>`)[0];
            popup_be6e5f5bfe79444db932e7e356051439.setContent(html_7d31862bf86e426bbd14f0647153ba3f);
        

        circle_marker_6765b48e03dc4f538410f9603123c47e.bindPopup(popup_be6e5f5bfe79444db932e7e356051439)
        ;

        
    
    
            var circle_marker_135ca74c3e0545af9785cd1a02cd1e70 = L.circleMarker(
                [41.921701492, -87.655911848],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.014285714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_9ec20928aee2450d87d7325f131184c7 = L.popup({"maxWidth": "100%"});

        
            var html_43ce12f331214693aafa0f4ebe7682a3 = $(`<div id="html_43ce12f331214693aafa0f4ebe7682a3" style="width: 100.0%; height: 100.0%;">Latitude : 41.921701492<br>                     Longitude : -87.655911848<br>                     frequency : 4<br></div>`)[0];
            popup_9ec20928aee2450d87d7325f131184c7.setContent(html_43ce12f331214693aafa0f4ebe7682a3);
        

        circle_marker_135ca74c3e0545af9785cd1a02cd1e70.bindPopup(popup_9ec20928aee2450d87d7325f131184c7)
        ;

        
    
    
            var circle_marker_ed6dc75fb6c549bb8b8ceca4ea60e385 = L.circleMarker(
                [41.96581197, -87.655878786],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1.7642857142857142, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_7ee85d512c9d4a5b9f2f8ddb8ddfbc91 = L.popup({"maxWidth": "100%"});

        
            var html_472a2c7026e543238e3ba767030ade9a = $(`<div id="html_472a2c7026e543238e3ba767030ade9a" style="width: 100.0%; height: 100.0%;">Latitude : 41.96581197<br>                     Longitude : -87.655878786<br>                     frequency : 494<br></div>`)[0];
            popup_7ee85d512c9d4a5b9f2f8ddb8ddfbc91.setContent(html_472a2c7026e543238e3ba767030ade9a);
        

        circle_marker_ed6dc75fb6c549bb8b8ceca4ea60e385.bindPopup(popup_7ee85d512c9d4a5b9f2f8ddb8ddfbc91)
        ;

        
    
    
            var circle_marker_41fe6515534f48908ef749cf7ebb43f9 = L.circleMarker(
                [41.946294536, -87.654298084],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.4142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_6f0bc12788d34843a8eb8b2e2c1cc260 = L.popup({"maxWidth": "100%"});

        
            var html_c56befceffd24530967a9a16650444c6 = $(`<div id="html_c56befceffd24530967a9a16650444c6" style="width: 100.0%; height: 100.0%;">Latitude : 41.946294536<br>                     Longitude : -87.654298084<br>                     frequency : 116<br></div>`)[0];
            popup_6f0bc12788d34843a8eb8b2e2c1cc260.setContent(html_c56befceffd24530967a9a16650444c6);
        

        circle_marker_41fe6515534f48908ef749cf7ebb43f9.bindPopup(popup_6f0bc12788d34843a8eb8b2e2c1cc260)
        ;

        
    
    
            var circle_marker_a3f8412c32724ea99a12b445e054ffe4 = L.circleMarker(
                [41.871689474, -87.654092652],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_d2d6b10fd34f4caeb61af6d079975884 = L.popup({"maxWidth": "100%"});

        
            var html_855d81fd83bd4a3da37088e337f42719 = $(`<div id="html_855d81fd83bd4a3da37088e337f42719" style="width: 100.0%; height: 100.0%;">Latitude : 41.871689474<br>                     Longitude : -87.654092652<br>                     frequency : 3<br></div>`)[0];
            popup_d2d6b10fd34f4caeb61af6d079975884.setContent(html_855d81fd83bd4a3da37088e337f42719);
        

        circle_marker_a3f8412c32724ea99a12b445e054ffe4.bindPopup(popup_d2d6b10fd34f4caeb61af6d079975884)
        ;

        
    
    
            var circle_marker_374012a4dee543a3aff28048a5256469 = L.circleMarker(
                [41.914747305, -87.654007029],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.19285714285714287, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_afd67c4800a44406a884f9d55104a328 = L.popup({"maxWidth": "100%"});

        
            var html_14093c4250df4bc9afe5baa3cb2d59ea = $(`<div id="html_14093c4250df4bc9afe5baa3cb2d59ea" style="width: 100.0%; height: 100.0%;">Latitude : 41.914747305<br>                     Longitude : -87.654007029<br>                     frequency : 54<br></div>`)[0];
            popup_afd67c4800a44406a884f9d55104a328.setContent(html_14093c4250df4bc9afe5baa3cb2d59ea);
        

        circle_marker_374012a4dee543a3aff28048a5256469.bindPopup(popup_afd67c4800a44406a884f9d55104a328)
        ;

        
    
    
            var circle_marker_f57ce0f876634c06a8008184dbad5ec6 = L.circleMarker(
                [41.985472422, -87.653793529],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_f9a17d924ece4491856543dd3bed9bd8 = L.popup({"maxWidth": "100%"});

        
            var html_3ea28cebde88402581ec9a011993a4c9 = $(`<div id="html_3ea28cebde88402581ec9a011993a4c9" style="width: 100.0%; height: 100.0%;">Latitude : 41.985472422<br>                     Longitude : -87.653793529<br>                     frequency : 2<br></div>`)[0];
            popup_f9a17d924ece4491856543dd3bed9bd8.setContent(html_3ea28cebde88402581ec9a011993a4c9);
        

        circle_marker_f57ce0f876634c06a8008184dbad5ec6.bindPopup(popup_f9a17d924ece4491856543dd3bed9bd8)
        ;

        
    
    
            var circle_marker_073a2df0bfd54b6d8e3abdf11a000c2b = L.circleMarker(
                [41.89830587, -87.653613982],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.32142857142857145, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_4c7e3136c90947bf829863bc6575da03 = L.popup({"maxWidth": "100%"});

        
            var html_87a5c52fc3724d5ab0bb03cfcc8eece2 = $(`<div id="html_87a5c52fc3724d5ab0bb03cfcc8eece2" style="width: 100.0%; height: 100.0%;">Latitude : 41.89830587<br>                     Longitude : -87.653613982<br>                     frequency : 90<br></div>`)[0];
            popup_4c7e3136c90947bf829863bc6575da03.setContent(html_87a5c52fc3724d5ab0bb03cfcc8eece2);
        

        circle_marker_073a2df0bfd54b6d8e3abdf11a000c2b.bindPopup(popup_4c7e3136c90947bf829863bc6575da03)
        ;

        
    
    
            var circle_marker_35e264ad929244d6ae5b33b4bd38a36d = L.circleMarker(
                [41.952822916, -87.653243992],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.05, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_d846129a67aa4e8fa30e5b9e876ddd1d = L.popup({"maxWidth": "100%"});

        
            var html_6bea6ae030954b4caf16665e7a8c1b62 = $(`<div id="html_6bea6ae030954b4caf16665e7a8c1b62" style="width: 100.0%; height: 100.0%;">Latitude : 41.952822916<br>                     Longitude : -87.653243992<br>                     frequency : 14<br></div>`)[0];
            popup_d846129a67aa4e8fa30e5b9e876ddd1d.setContent(html_6bea6ae030954b4caf16665e7a8c1b62);
        

        circle_marker_35e264ad929244d6ae5b33b4bd38a36d.bindPopup(popup_d846129a67aa4e8fa30e5b9e876ddd1d)
        ;

        
    
    
            var circle_marker_732e2142b3a04a20b3ae77603726b373 = L.circleMarker(
                [41.958154876, -87.653021789],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.10714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_730d04600ebb47129fa26b40bb395331 = L.popup({"maxWidth": "100%"});

        
            var html_74442644d2374c0489367525ffb92c64 = $(`<div id="html_74442644d2374c0489367525ffb92c64" style="width: 100.0%; height: 100.0%;">Latitude : 41.958154876<br>                     Longitude : -87.653021789<br>                     frequency : 30<br></div>`)[0];
            popup_730d04600ebb47129fa26b40bb395331.setContent(html_74442644d2374c0489367525ffb92c64);
        

        circle_marker_732e2142b3a04a20b3ae77603726b373.bindPopup(popup_730d04600ebb47129fa26b40bb395331)
        ;

        
    
    
            var circle_marker_5d546a0aab7a4454be61dbfb662d4e93 = L.circleMarker(
                [41.892658108, -87.652534484],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.24285714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_9df93af5f7164f62aca2ad4cc8ccd586 = L.popup({"maxWidth": "100%"});

        
            var html_f3667cc40f0e4e3a8443868b3226d8ae = $(`<div id="html_f3667cc40f0e4e3a8443868b3226d8ae" style="width: 100.0%; height: 100.0%;">Latitude : 41.892658108<br>                     Longitude : -87.652534484<br>                     frequency : 68<br></div>`)[0];
            popup_9df93af5f7164f62aca2ad4cc8ccd586.setContent(html_f3667cc40f0e4e3a8443868b3226d8ae);
        

        circle_marker_5d546a0aab7a4454be61dbfb662d4e93.bindPopup(popup_9df93af5f7164f62aca2ad4cc8ccd586)
        ;

        
    
    
            var circle_marker_905685bcce0143308536edf98e3102a4 = L.circleMarker(
                [41.980157574, -87.652274017],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.014285714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_46fca7e4e72d489a91ecd01c5a0cdfa5 = L.popup({"maxWidth": "100%"});

        
            var html_819a91c2bb874eb0800017a805099b76 = $(`<div id="html_819a91c2bb874eb0800017a805099b76" style="width: 100.0%; height: 100.0%;">Latitude : 41.980157574<br>                     Longitude : -87.652274017<br>                     frequency : 4<br></div>`)[0];
            popup_46fca7e4e72d489a91ecd01c5a0cdfa5.setContent(html_819a91c2bb874eb0800017a805099b76);
        

        circle_marker_905685bcce0143308536edf98e3102a4.bindPopup(popup_46fca7e4e72d489a91ecd01c5a0cdfa5)
        ;

        
    
    
            var circle_marker_d85507785b54451c98462c0601bc7a6d = L.circleMarker(
                [41.949220914, -87.651970395],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.16428571428571428, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_23de8d3e6b8c45f5a6bee623bf8e71b5 = L.popup({"maxWidth": "100%"});

        
            var html_0d96df414bf84f65870c59ad2651966c = $(`<div id="html_0d96df414bf84f65870c59ad2651966c" style="width: 100.0%; height: 100.0%;">Latitude : 41.949220914<br>                     Longitude : -87.651970395<br>                     frequency : 46<br></div>`)[0];
            popup_23de8d3e6b8c45f5a6bee623bf8e71b5.setContent(html_0d96df414bf84f65870c59ad2651966c);
        

        circle_marker_d85507785b54451c98462c0601bc7a6d.bindPopup(popup_23de8d3e6b8c45f5a6bee623bf8e71b5)
        ;

        
    
    
            var circle_marker_1169ac6cda7e4c64924a6f6e05fda6b1 = L.circleMarker(
                [41.942691844, -87.651770507],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.44285714285714284, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_fc88808441ad476e929669648112ce4a = L.popup({"maxWidth": "100%"});

        
            var html_23116c1424dd4319b9c68950a1d489e7 = $(`<div id="html_23116c1424dd4319b9c68950a1d489e7" style="width: 100.0%; height: 100.0%;">Latitude : 41.942691844<br>                     Longitude : -87.651770507<br>                     frequency : 124<br></div>`)[0];
            popup_fc88808441ad476e929669648112ce4a.setContent(html_23116c1424dd4319b9c68950a1d489e7);
        

        circle_marker_1169ac6cda7e4c64924a6f6e05fda6b1.bindPopup(popup_fc88808441ad476e929669648112ce4a)
        ;

        
    
    
            var circle_marker_54786a7908b64991aeb8b03db281d2d6 = L.circleMarker(
                [41.936310131, -87.651562592],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.18571428571428572, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_f87a2c9a852b49daab6ff61490317b59 = L.popup({"maxWidth": "100%"});

        
            var html_a754ea98d0e24f438a78d8dc5c02c90a = $(`<div id="html_a754ea98d0e24f438a78d8dc5c02c90a" style="width: 100.0%; height: 100.0%;">Latitude : 41.936310131<br>                     Longitude : -87.651562592<br>                     frequency : 52<br></div>`)[0];
            popup_f87a2c9a852b49daab6ff61490317b59.setContent(html_a754ea98d0e24f438a78d8dc5c02c90a);
        

        circle_marker_54786a7908b64991aeb8b03db281d2d6.bindPopup(popup_f87a2c9a852b49daab6ff61490317b59)
        ;

        
    
    
            var circle_marker_cb550e16405942158f3e2d7ccfb6d63e = L.circleMarker(
                [41.929046937, -87.651310877],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.2, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_f49f435a4d7b4757809b6591564d8139 = L.popup({"maxWidth": "100%"});

        
            var html_1f2a1481418f47f8b90e934fc851efa5 = $(`<div id="html_1f2a1481418f47f8b90e934fc851efa5" style="width: 100.0%; height: 100.0%;">Latitude : 41.929046937<br>                     Longitude : -87.651310877<br>                     frequency : 56<br></div>`)[0];
            popup_f49f435a4d7b4757809b6591564d8139.setContent(html_1f2a1481418f47f8b90e934fc851efa5);
        

        circle_marker_cb550e16405942158f3e2d7ccfb6d63e.bindPopup(popup_f49f435a4d7b4757809b6591564d8139)
        ;

        
    
    
            var circle_marker_09cd2d5bfcdb425e84d72c551303fbf5 = L.circleMarker(
                [41.921778188, -87.651061884],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.125, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_f4a788ccf7d64faba6152fced9e5563e = L.popup({"maxWidth": "100%"});

        
            var html_e548671fd04c44229e734b8f21e3d6e8 = $(`<div id="html_e548671fd04c44229e734b8f21e3d6e8" style="width: 100.0%; height: 100.0%;">Latitude : 41.921778188<br>                     Longitude : -87.651061884<br>                     frequency : 35<br></div>`)[0];
            popup_f4a788ccf7d64faba6152fced9e5563e.setContent(html_e548671fd04c44229e734b8f21e3d6e8);
        

        circle_marker_09cd2d5bfcdb425e84d72c551303fbf5.bindPopup(popup_f4a788ccf7d64faba6152fced9e5563e)
        ;

        
    
    
            var circle_marker_ad500b2f60894680b6d76794730b58f7 = L.circleMarker(
                [41.972929317, -87.650290074],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.03214285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_4d7a4dce965d47f3bbe7814fa5acd6c5 = L.popup({"maxWidth": "100%"});

        
            var html_55ee2b89f06a413ea02ee4eb51b4978d = $(`<div id="html_55ee2b89f06a413ea02ee4eb51b4978d" style="width: 100.0%; height: 100.0%;">Latitude : 41.972929317<br>                     Longitude : -87.650290074<br>                     frequency : 9<br></div>`)[0];
            popup_4d7a4dce965d47f3bbe7814fa5acd6c5.setContent(html_55ee2b89f06a413ea02ee4eb51b4978d);
        

        circle_marker_ad500b2f60894680b6d76794730b58f7.bindPopup(popup_4d7a4dce965d47f3bbe7814fa5acd6c5)
        ;

        
    
    
            var circle_marker_364fed8b9238432bab7262480eddac9f = L.circleMarker(
                [41.904935302, -87.649907226],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.9035714285714286, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_cc9e272a0d8046dbbfe2de7717c6da41 = L.popup({"maxWidth": "100%"});

        
            var html_80ba0724da2d403daed5924d2775e574 = $(`<div id="html_80ba0724da2d403daed5924d2775e574" style="width: 100.0%; height: 100.0%;">Latitude : 41.904935302<br>                     Longitude : -87.649907226<br>                     frequency : 253<br></div>`)[0];
            popup_cc9e272a0d8046dbbfe2de7717c6da41.setContent(html_80ba0724da2d403daed5924d2775e574);
        

        circle_marker_364fed8b9238432bab7262480eddac9f.bindPopup(popup_cc9e272a0d8046dbbfe2de7717c6da41)
        ;

        
    
    
            var circle_marker_c192557f0ecb4f05bf6edea9a5920b80 = L.circleMarker(
                [41.922686284, -87.649488729],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 3.217857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_162426a0070a44fba6cdfda7070ce97f = L.popup({"maxWidth": "100%"});

        
            var html_872d37a11935466eb45bb94a451054cd = $(`<div id="html_872d37a11935466eb45bb94a451054cd" style="width: 100.0%; height: 100.0%;">Latitude : 41.922686284<br>                     Longitude : -87.649488729<br>                     frequency : 901<br></div>`)[0];
            popup_162426a0070a44fba6cdfda7070ce97f.setContent(html_872d37a11935466eb45bb94a451054cd);
        

        circle_marker_c192557f0ecb4f05bf6edea9a5920b80.bindPopup(popup_162426a0070a44fba6cdfda7070ce97f)
        ;

        
    
    
            var circle_marker_097137b7de774e5897b502dd4247f0ef = L.circleMarker(
                [41.717493036, -87.648895072],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.02142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_057d5996ca964fdba49fe0f5d2a5c217 = L.popup({"maxWidth": "100%"});

        
            var html_2704bf59113d4660a3ccb3ecd1d05cc1 = $(`<div id="html_2704bf59113d4660a3ccb3ecd1d05cc1" style="width: 100.0%; height: 100.0%;">Latitude : 41.717493036<br>                     Longitude : -87.648895072<br>                     frequency : 6<br></div>`)[0];
            popup_057d5996ca964fdba49fe0f5d2a5c217.setContent(html_2704bf59113d4660a3ccb3ecd1d05cc1);
        

        circle_marker_097137b7de774e5897b502dd4247f0ef.bindPopup(popup_057d5996ca964fdba49fe0f5d2a5c217)
        ;

        
    
    
            var circle_marker_b5fa89e8e7b14bc6a05a61cdb224ab65 = L.circleMarker(
                [41.836150155, -87.648787952],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.08214285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_24344f405d444f19bdb4d142067d9ce2 = L.popup({"maxWidth": "100%"});

        
            var html_b6d282d680d041d1b844140c1d743357 = $(`<div id="html_b6d282d680d041d1b844140c1d743357" style="width: 100.0%; height: 100.0%;">Latitude : 41.836150155<br>                     Longitude : -87.648787952<br>                     frequency : 23<br></div>`)[0];
            popup_24344f405d444f19bdb4d142067d9ce2.setContent(html_b6d282d680d041d1b844140c1d743357);
        

        circle_marker_b5fa89e8e7b14bc6a05a61cdb224ab65.bindPopup(popup_24344f405d444f19bdb4d142067d9ce2)
        ;

        
    
    
            var circle_marker_476d80c40a9b4be9bcc2fd57887a11b5 = L.circleMarker(
                [41.946489764, -87.647113634],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.03571428571428571, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_b09cee38a037422b8399ddf6024739f7 = L.popup({"maxWidth": "100%"});

        
            var html_db5feecb79ba4f5093a5fd37f84b4290 = $(`<div id="html_db5feecb79ba4f5093a5fd37f84b4290" style="width: 100.0%; height: 100.0%;">Latitude : 41.946489764<br>                     Longitude : -87.647113634<br>                     frequency : 10<br></div>`)[0];
            popup_b09cee38a037422b8399ddf6024739f7.setContent(html_db5feecb79ba4f5093a5fd37f84b4290);
        

        circle_marker_476d80c40a9b4be9bcc2fd57887a11b5.bindPopup(popup_b09cee38a037422b8399ddf6024739f7)
        ;

        
    
    
            var circle_marker_b5e6295acfe04cfc9a515da98f506ba8 = L.circleMarker(
                [41.942577185, -87.647078509],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.2, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_b860558342a1452dad3b0b7b863293b3 = L.popup({"maxWidth": "100%"});

        
            var html_6e471f48211b4ec0976054881b64f697 = $(`<div id="html_6e471f48211b4ec0976054881b64f697" style="width: 100.0%; height: 100.0%;">Latitude : 41.942577185<br>                     Longitude : -87.647078509<br>                     frequency : 56<br></div>`)[0];
            popup_b860558342a1452dad3b0b7b863293b3.setContent(html_6e471f48211b4ec0976054881b64f697);
        

        circle_marker_b5e6295acfe04cfc9a515da98f506ba8.bindPopup(popup_b860558342a1452dad3b0b7b863293b3)
        ;

        
    
    
            var circle_marker_83eb99c4011b4129b8dd1b6adac5d214 = L.circleMarker(
                [41.938232293, -87.646782081],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.11428571428571428, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_471ca37edbd34097be7c86893343570d = L.popup({"maxWidth": "100%"});

        
            var html_e1b71155bd694174a9c1eb76b0aea323 = $(`<div id="html_e1b71155bd694174a9c1eb76b0aea323" style="width: 100.0%; height: 100.0%;">Latitude : 41.938232293<br>                     Longitude : -87.646782081<br>                     frequency : 32<br></div>`)[0];
            popup_471ca37edbd34097be7c86893343570d.setContent(html_e1b71155bd694174a9c1eb76b0aea323);
        

        circle_marker_83eb99c4011b4129b8dd1b6adac5d214.bindPopup(popup_471ca37edbd34097be7c86893343570d)
        ;

        
    
    
            var circle_marker_5c2be08f0e874a2eadced5f26cf7e7d3 = L.circleMarker(
                [41.934659157, -87.646729729],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.1, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_0282a035ffc4409eb68292ba601a6bf9 = L.popup({"maxWidth": "100%"});

        
            var html_876904aba6d1430fba2848f22cd3fce7 = $(`<div id="html_876904aba6d1430fba2848f22cd3fce7" style="width: 100.0%; height: 100.0%;">Latitude : 41.934659157<br>                     Longitude : -87.646729729<br>                     frequency : 28<br></div>`)[0];
            popup_0282a035ffc4409eb68292ba601a6bf9.setContent(html_876904aba6d1430fba2848f22cd3fce7);
        

        circle_marker_5c2be08f0e874a2eadced5f26cf7e7d3.bindPopup(popup_0282a035ffc4409eb68292ba601a6bf9)
        ;

        
    
    
            var circle_marker_cfcb2deaa0bb44eb9d90b1c43ebd61c2 = L.circleMarker(
                [41.929077655, -87.646293476],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.20357142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_8a7fd1f47a6d4a468be09abbbf08969b = L.popup({"maxWidth": "100%"});

        
            var html_7eafd2d162054875ab28f478f4278ff5 = $(`<div id="html_7eafd2d162054875ab28f478f4278ff5" style="width: 100.0%; height: 100.0%;">Latitude : 41.929077655<br>                     Longitude : -87.646293476<br>                     frequency : 57<br></div>`)[0];
            popup_8a7fd1f47a6d4a468be09abbbf08969b.setContent(html_7eafd2d162054875ab28f478f4278ff5);
        

        circle_marker_cfcb2deaa0bb44eb9d90b1c43ebd61c2.bindPopup(popup_8a7fd1f47a6d4a468be09abbbf08969b)
        ;

        
    
    
            var circle_marker_bcbf8f0754ea4257bcefa92b65b9599d = L.circleMarker(
                [41.921854911, -87.646210977],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.23214285714285715, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_2557b5ac1dc84dc9a6fb108fc0e01430 = L.popup({"maxWidth": "100%"});

        
            var html_bc23b822050249ae8d2cbd6ce5a74c2e = $(`<div id="html_bc23b822050249ae8d2cbd6ce5a74c2e" style="width: 100.0%; height: 100.0%;">Latitude : 41.921854911<br>                     Longitude : -87.646210977<br>                     frequency : 65<br></div>`)[0];
            popup_2557b5ac1dc84dc9a6fb108fc0e01430.setContent(html_bc23b822050249ae8d2cbd6ce5a74c2e);
        

        circle_marker_bcbf8f0754ea4257bcefa92b65b9599d.bindPopup(popup_2557b5ac1dc84dc9a6fb108fc0e01430)
        ;

        
    
    
            var circle_marker_ad2bd4c577284e2eb93fb903af76dadb = L.circleMarker(
                [41.953400044, -87.646007066],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.060714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_10f20b1d29864721b5b3996156d345f5 = L.popup({"maxWidth": "100%"});

        
            var html_12cfddca9be949d6a4626e65ad9b8dde = $(`<div id="html_12cfddca9be949d6a4626e65ad9b8dde" style="width: 100.0%; height: 100.0%;">Latitude : 41.953400044<br>                     Longitude : -87.646007066<br>                     frequency : 17<br></div>`)[0];
            popup_10f20b1d29864721b5b3996156d345f5.setContent(html_12cfddca9be949d6a4626e65ad9b8dde);
        

        circle_marker_ad2bd4c577284e2eb93fb903af76dadb.bindPopup(popup_10f20b1d29864721b5b3996156d345f5)
        ;

        
    
    
            var circle_marker_30c5cbefbc4544af855e53f9cdad2337 = L.circleMarker(
                [41.914585709, -87.645966207],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.075, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_f256197d46ca4d0abab7b1ff452f275b = L.popup({"maxWidth": "100%"});

        
            var html_ac912886e57a42818cc2c5a292436ae8 = $(`<div id="html_ac912886e57a42818cc2c5a292436ae8" style="width: 100.0%; height: 100.0%;">Latitude : 41.914585709<br>                     Longitude : -87.645966207<br>                     frequency : 21<br></div>`)[0];
            popup_f256197d46ca4d0abab7b1ff452f275b.setContent(html_ac912886e57a42818cc2c5a292436ae8);
        

        circle_marker_30c5cbefbc4544af855e53f9cdad2337.bindPopup(popup_f256197d46ca4d0abab7b1ff452f275b)
        ;

        
    
    
            var circle_marker_db550c6f873f4d3bbf931998b7ff0892 = L.circleMarker(
                [41.962178629, -87.645378762],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.1357142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_044ff11665ed4ba18aff60e41e8d1ca4 = L.popup({"maxWidth": "100%"});

        
            var html_33ea819cb41b4e0da55605fd0fb85a5b = $(`<div id="html_33ea819cb41b4e0da55605fd0fb85a5b" style="width: 100.0%; height: 100.0%;">Latitude : 41.962178629<br>                     Longitude : -87.645378762<br>                     frequency : 38<br></div>`)[0];
            popup_044ff11665ed4ba18aff60e41e8d1ca4.setContent(html_33ea819cb41b4e0da55605fd0fb85a5b);
        

        circle_marker_db550c6f873f4d3bbf931998b7ff0892.bindPopup(popup_044ff11665ed4ba18aff60e41e8d1ca4)
        ;

        
    
    
            var circle_marker_b7e37702aeef47c8b9a788105ce86f0a = L.circleMarker(
                [41.949829346, -87.64396537],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.2857142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_b60e4015fb354bc99043ecee56535d24 = L.popup({"maxWidth": "100%"});

        
            var html_58d67af65d1444bd86a119c77177d70d = $(`<div id="html_58d67af65d1444bd86a119c77177d70d" style="width: 100.0%; height: 100.0%;">Latitude : 41.949829346<br>                     Longitude : -87.64396537<br>                     frequency : 80<br></div>`)[0];
            popup_b60e4015fb354bc99043ecee56535d24.setContent(html_58d67af65d1444bd86a119c77177d70d);
        

        circle_marker_b7e37702aeef47c8b9a788105ce86f0a.bindPopup(popup_b60e4015fb354bc99043ecee56535d24)
        ;

        
    
    
            var circle_marker_5c64307da8994949af64da59bd54e09c = L.circleMarker(
                [41.943237122, -87.643470956],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.039285714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_f40ea2613916429293fcd5831c174fc7 = L.popup({"maxWidth": "100%"});

        
            var html_2dc586e799f644e2b1feada5b9aebf06 = $(`<div id="html_2dc586e799f644e2b1feada5b9aebf06" style="width: 100.0%; height: 100.0%;">Latitude : 41.943237122<br>                     Longitude : -87.643470956<br>                     frequency : 11<br></div>`)[0];
            popup_f40ea2613916429293fcd5831c174fc7.setContent(html_2dc586e799f644e2b1feada5b9aebf06);
        

        circle_marker_5c64307da8994949af64da59bd54e09c.bindPopup(popup_f40ea2613916429293fcd5831c174fc7)
        ;

        
    
    
            var circle_marker_9065de58d3554ef09ba784b39f2975fd = L.circleMarker(
                [41.934539716, -87.643022804],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.04285714285714286, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_82e2ed55778a463b8d22443b9db7cbb2 = L.popup({"maxWidth": "100%"});

        
            var html_80648bb80dcb4696a4052826d2d3f5eb = $(`<div id="html_80648bb80dcb4696a4052826d2d3f5eb" style="width: 100.0%; height: 100.0%;">Latitude : 41.934539716<br>                     Longitude : -87.643022804<br>                     frequency : 12<br></div>`)[0];
            popup_82e2ed55778a463b8d22443b9db7cbb2.setContent(html_80648bb80dcb4696a4052826d2d3f5eb);
        

        circle_marker_9065de58d3554ef09ba784b39f2975fd.bindPopup(popup_82e2ed55778a463b8d22443b9db7cbb2)
        ;

        
    
    
            var circle_marker_e328e655bd1d4589bf32fa4b40f41415 = L.circleMarker(
                [41.867902418, -87.642958665],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.35, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_ea4e22d81e184c4d8cc46829d6344589 = L.popup({"maxWidth": "100%"});

        
            var html_2bd71ce12e304c8d90298bdf3bc0f633 = $(`<div id="html_2bd71ce12e304c8d90298bdf3bc0f633" style="width: 100.0%; height: 100.0%;">Latitude : 41.867902418<br>                     Longitude : -87.642958665<br>                     frequency : 98<br></div>`)[0];
            popup_ea4e22d81e184c4d8cc46829d6344589.setContent(html_2bd71ce12e304c8d90298bdf3bc0f633);
        

        circle_marker_e328e655bd1d4589bf32fa4b40f41415.bindPopup(popup_ea4e22d81e184c4d8cc46829d6344589)
        ;

        
    
    
            var circle_marker_8a47bd44d94c43cc8a5d9e892a5d4c0a = L.circleMarker(
                [41.885300022, -87.642808466],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 4.735714285714286, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_d0b3a10f1ba549ecbf431ce836ff4cc9 = L.popup({"maxWidth": "100%"});

        
            var html_6a431d2cbd984471b04ba894f3a9cde1 = $(`<div id="html_6a431d2cbd984471b04ba894f3a9cde1" style="width: 100.0%; height: 100.0%;">Latitude : 41.885300022<br>                     Longitude : -87.642808466<br>                     frequency : 1326<br></div>`)[0];
            popup_d0b3a10f1ba549ecbf431ce836ff4cc9.setContent(html_6a431d2cbd984471b04ba894f3a9cde1);
        

        circle_marker_8a47bd44d94c43cc8a5d9e892a5d4c0a.bindPopup(popup_d0b3a10f1ba549ecbf431ce836ff4cc9)
        ;

        
    
    
            var circle_marker_d471338873e447ba85768a16eff7c91b = L.circleMarker(
                [41.879255084, -87.642648998],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 7.746428571428571, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_b5f2f71ec8cb42c29077560b47a6c819 = L.popup({"maxWidth": "100%"});

        
            var html_33c8ef97b7c2434b9584b96d18b65432 = $(`<div id="html_33c8ef97b7c2434b9584b96d18b65432" style="width: 100.0%; height: 100.0%;">Latitude : 41.879255084<br>                     Longitude : -87.642648998<br>                     frequency : 2169<br></div>`)[0];
            popup_b5f2f71ec8cb42c29077560b47a6c819.setContent(html_33c8ef97b7c2434b9584b96d18b65432);
        

        circle_marker_d471338873e447ba85768a16eff7c91b.bindPopup(popup_b5f2f71ec8cb42c29077560b47a6c819)
        ;

        
    
    
            var circle_marker_145c2ea7f6fc4c5b9266f1517fb33948 = L.circleMarker(
                [41.926811182, -87.642605247],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.11071428571428571, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_70abbc592a6b4b258b17f0de37b25d6b = L.popup({"maxWidth": "100%"});

        
            var html_a13495ecc68649a9b5c5804fc6144e1c = $(`<div id="html_a13495ecc68649a9b5c5804fc6144e1c" style="width: 100.0%; height: 100.0%;">Latitude : 41.926811182<br>                     Longitude : -87.642605247<br>                     frequency : 31<br></div>`)[0];
            popup_70abbc592a6b4b258b17f0de37b25d6b.setContent(html_a13495ecc68649a9b5c5804fc6144e1c);
        

        circle_marker_145c2ea7f6fc4c5b9266f1517fb33948.bindPopup(popup_70abbc592a6b4b258b17f0de37b25d6b)
        ;

        
    
    
            var circle_marker_df873379c18e4dd7b0e3e99ada34721d = L.circleMarker(
                [41.777196255, -87.642497527],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.02142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_3467b1f04e964ae5a57b0d6b82e747e0 = L.popup({"maxWidth": "100%"});

        
            var html_b4fd0cdd48634724a51cafa8c9c8e88f = $(`<div id="html_b4fd0cdd48634724a51cafa8c9c8e88f" style="width: 100.0%; height: 100.0%;">Latitude : 41.777196255<br>                     Longitude : -87.642497527<br>                     frequency : 6<br></div>`)[0];
            popup_3467b1f04e964ae5a57b0d6b82e747e0.setContent(html_b4fd0cdd48634724a51cafa8c9c8e88f);
        

        circle_marker_df873379c18e4dd7b0e3e99ada34721d.bindPopup(popup_3467b1f04e964ae5a57b0d6b82e747e0)
        ;

        
    
    
            var circle_marker_9cc7f26fafae47eb8808d4a1fb5aa281 = L.circleMarker(
                [41.93057857, -87.642206313],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.07857142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_9046d36d41f24cadb67072b869d53caf = L.popup({"maxWidth": "100%"});

        
            var html_77dbd5d415744c9c80413ddcffd2e755 = $(`<div id="html_77dbd5d415744c9c80413ddcffd2e755" style="width: 100.0%; height: 100.0%;">Latitude : 41.93057857<br>                     Longitude : -87.642206313<br>                     frequency : 22<br></div>`)[0];
            popup_9046d36d41f24cadb67072b869d53caf.setContent(html_77dbd5d415744c9c80413ddcffd2e755);
        

        circle_marker_9cc7f26fafae47eb8808d4a1fb5aa281.bindPopup(popup_9046d36d41f24cadb67072b869d53caf)
        ;

        
    
    
            var circle_marker_774166b6c3b941a38510440ccdc5ce9e = L.circleMarker(
                [41.897983898, -87.641491533],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.12142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_d03ca10ea2a948c9ab32ebd4b11a3630 = L.popup({"maxWidth": "100%"});

        
            var html_35425e3cc2ce4814ac12fe28173216da = $(`<div id="html_35425e3cc2ce4814ac12fe28173216da" style="width: 100.0%; height: 100.0%;">Latitude : 41.897983898<br>                     Longitude : -87.641491533<br>                     frequency : 34<br></div>`)[0];
            popup_d03ca10ea2a948c9ab32ebd4b11a3630.setContent(html_35425e3cc2ce4814ac12fe28173216da);
        

        circle_marker_774166b6c3b941a38510440ccdc5ce9e.bindPopup(popup_d03ca10ea2a948c9ab32ebd4b11a3630)
        ;

        
    
    
            var circle_marker_126f205a45764e7a9743b6d71184b916 = L.circleMarker(
                [41.921778356, -87.641459759],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.10357142857142858, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_5c1a5838eb5c42debda97e0269939f1b = L.popup({"maxWidth": "100%"});

        
            var html_1232d489be364f98a3a9ca23edea5852 = $(`<div id="html_1232d489be364f98a3a9ca23edea5852" style="width: 100.0%; height: 100.0%;">Latitude : 41.921778356<br>                     Longitude : -87.641459759<br>                     frequency : 29<br></div>`)[0];
            popup_5c1a5838eb5c42debda97e0269939f1b.setContent(html_1232d489be364f98a3a9ca23edea5852);
        

        circle_marker_126f205a45764e7a9743b6d71184b916.bindPopup(popup_5c1a5838eb5c42debda97e0269939f1b)
        ;

        
    
    
            var circle_marker_a207e9672b50423a8f517a6b3f6075ee = L.circleMarker(
                [41.916473316, -87.641183657],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_263be52fd5ba46fb9895afe965165bad = L.popup({"maxWidth": "100%"});

        
            var html_84b83555f161435cb4ad2dd30ce7ca7e = $(`<div id="html_84b83555f161435cb4ad2dd30ce7ca7e" style="width: 100.0%; height: 100.0%;">Latitude : 41.916473316<br>                     Longitude : -87.641183657<br>                     frequency : 2<br></div>`)[0];
            popup_263be52fd5ba46fb9895afe965165bad.setContent(html_84b83555f161435cb4ad2dd30ce7ca7e);
        

        circle_marker_a207e9672b50423a8f517a6b3f6075ee.bindPopup(popup_263be52fd5ba46fb9895afe965165bad)
        ;

        
    
    
            var circle_marker_4e9021a89764408b8a037a7a873e1181 = L.circleMarker(
                [41.912868922, -87.641070746],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_cacc1995f7944551838e0a949165f249 = L.popup({"maxWidth": "100%"});

        
            var html_ba70734640e147caaef62f1e7335da82 = $(`<div id="html_ba70734640e147caaef62f1e7335da82" style="width: 100.0%; height: 100.0%;">Latitude : 41.912868922<br>                     Longitude : -87.641070746<br>                     frequency : 1<br></div>`)[0];
            popup_cacc1995f7944551838e0a949165f249.setContent(html_ba70734640e147caaef62f1e7335da82);
        

        circle_marker_4e9021a89764408b8a037a7a873e1181.bindPopup(popup_cacc1995f7944551838e0a949165f249)
        ;

        
    
    
            var circle_marker_12e8be446de94411bc731d466ea57dbc = L.circleMarker(
                [41.907412816, -87.640901525],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.03571428571428571, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_9a209ac05f1640c8a8c7116003083479 = L.popup({"maxWidth": "100%"});

        
            var html_79f078b149fc4aae927d772a4c4ae453 = $(`<div id="html_79f078b149fc4aae927d772a4c4ae453" style="width: 100.0%; height: 100.0%;">Latitude : 41.907412816<br>                     Longitude : -87.640901525<br>                     frequency : 10<br></div>`)[0];
            popup_9a209ac05f1640c8a8c7116003083479.setContent(html_79f078b149fc4aae927d772a4c4ae453);
        

        circle_marker_12e8be446de94411bc731d466ea57dbc.bindPopup(popup_9a209ac05f1640c8a8c7116003083479)
        ;

        
    
    
            var circle_marker_6c9bd9734ce0402eb86ac060c5ce20af = L.circleMarker(
                [41.943155086, -87.640698076],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.19285714285714287, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_d486aabbf4b44b2181cf37df8050334c = L.popup({"maxWidth": "100%"});

        
            var html_7ff68d3d824845499a073d5f5bc86583 = $(`<div id="html_7ff68d3d824845499a073d5f5bc86583" style="width: 100.0%; height: 100.0%;">Latitude : 41.943155086<br>                     Longitude : -87.640698076<br>                     frequency : 54<br></div>`)[0];
            popup_d486aabbf4b44b2181cf37df8050334c.setContent(html_7ff68d3d824845499a073d5f5bc86583);
        

        circle_marker_6c9bd9734ce0402eb86ac060c5ce20af.bindPopup(popup_d486aabbf4b44b2181cf37df8050334c)
        ;

        
    
    
            var circle_marker_be52055697664b0ca48d8ffde1b8741f = L.circleMarker(
                [41.934762456, -87.639853859],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.16785714285714284, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_91fb428d4dcb4aaea38f0d9fe51d2f71 = L.popup({"maxWidth": "100%"});

        
            var html_b8b1641f7ba24c1d82aa930449a7c2ca = $(`<div id="html_b8b1641f7ba24c1d82aa930449a7c2ca" style="width: 100.0%; height: 100.0%;">Latitude : 41.934762456<br>                     Longitude : -87.639853859<br>                     frequency : 47<br></div>`)[0];
            popup_91fb428d4dcb4aaea38f0d9fe51d2f71.setContent(html_b8b1641f7ba24c1d82aa930449a7c2ca);
        

        circle_marker_be52055697664b0ca48d8ffde1b8741f.bindPopup(popup_91fb428d4dcb4aaea38f0d9fe51d2f71)
        ;

        
    
    
            var circle_marker_ca00b2da17d84ad3852034cdbfda3af1 = L.circleMarker(
                [41.938391258, -87.63857492],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.18571428571428572, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_a40ea2d2a76f45b59582c9ba9b8c91c7 = L.popup({"maxWidth": "100%"});

        
            var html_a8cc82748eab401ab56bfaad541b2bdd = $(`<div id="html_a8cc82748eab401ab56bfaad541b2bdd" style="width: 100.0%; height: 100.0%;">Latitude : 41.938391258<br>                     Longitude : -87.63857492<br>                     frequency : 52<br></div>`)[0];
            popup_a40ea2d2a76f45b59582c9ba9b8c91c7.setContent(html_a8cc82748eab401ab56bfaad541b2bdd);
        

        circle_marker_ca00b2da17d84ad3852034cdbfda3af1.bindPopup(popup_a40ea2d2a76f45b59582c9ba9b8c91c7)
        ;

        
    
    
            var circle_marker_f9aaff6e71244a8bae10df68e12ed63c = L.circleMarker(
                [41.90156691, -87.638404012],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.03571428571428571, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_1e3c4be92ae84b83b5c4834b98f633c3 = L.popup({"maxWidth": "100%"});

        
            var html_15efe95fd7314392acf0fd1a17487662 = $(`<div id="html_15efe95fd7314392acf0fd1a17487662" style="width: 100.0%; height: 100.0%;">Latitude : 41.90156691<br>                     Longitude : -87.638404012<br>                     frequency : 10<br></div>`)[0];
            popup_1e3c4be92ae84b83b5c4834b98f633c3.setContent(html_15efe95fd7314392acf0fd1a17487662);
        

        circle_marker_f9aaff6e71244a8bae10df68e12ed63c.bindPopup(popup_1e3c4be92ae84b83b5c4834b98f633c3)
        ;

        
    
    
            var circle_marker_506084b9529d41a7943b3ef1a585200b = L.circleMarker(
                [41.89321636, -87.63784421],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 4.546428571428572, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_91a378b125294f50b41f6eee5947d197 = L.popup({"maxWidth": "100%"});

        
            var html_7c75add867744432ad374dd1911350a9 = $(`<div id="html_7c75add867744432ad374dd1911350a9" style="width: 100.0%; height: 100.0%;">Latitude : 41.89321636<br>                     Longitude : -87.63784421<br>                     frequency : 1273<br></div>`)[0];
            popup_91a378b125294f50b41f6eee5947d197.setContent(html_7c75add867744432ad374dd1911350a9);
        

        circle_marker_506084b9529d41a7943b3ef1a585200b.bindPopup(popup_91a378b125294f50b41f6eee5947d197)
        ;

        
    
    
            var circle_marker_b90ace54440f4b9583c2f6b028d76919 = L.circleMarker(
                [41.92926299, -87.635890954],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.17857142857142858, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_156539f0829f4214805e1e3715e70922 = L.popup({"maxWidth": "100%"});

        
            var html_7d1b156125b74ba5944a2afdf85226a0 = $(`<div id="html_7d1b156125b74ba5944a2afdf85226a0" style="width: 100.0%; height: 100.0%;">Latitude : 41.92926299<br>                     Longitude : -87.635890954<br>                     frequency : 50<br></div>`)[0];
            popup_156539f0829f4214805e1e3715e70922.setContent(html_7d1b156125b74ba5944a2afdf85226a0);
        

        circle_marker_b90ace54440f4b9583c2f6b028d76919.bindPopup(popup_156539f0829f4214805e1e3715e70922)
        ;

        
    
    
            var circle_marker_a027fb8ff2414492accaa85a390ee66e = L.circleMarker(
                [41.90749193, -87.63576009],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1.3142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_922aacd068fc4c3cae09f90f3c436d3c = L.popup({"maxWidth": "100%"});

        
            var html_2b4c42752e7f49359c557bdb3f3d6991 = $(`<div id="html_2b4c42752e7f49359c557bdb3f3d6991" style="width: 100.0%; height: 100.0%;">Latitude : 41.90749193<br>                     Longitude : -87.63576009<br>                     frequency : 368<br></div>`)[0];
            popup_922aacd068fc4c3cae09f90f3c436d3c.setContent(html_2b4c42752e7f49359c557bdb3f3d6991);
        

        circle_marker_a027fb8ff2414492accaa85a390ee66e.bindPopup(popup_922aacd068fc4c3cae09f90f3c436d3c)
        ;

        
    
    
            var circle_marker_6ef1d0860456473ab0beec46b035e3a5 = L.circleMarker(
                [41.673819904, -87.635739777],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.017857142857142856, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_b698010ea7de4793b32c29b0c7e345cd = L.popup({"maxWidth": "100%"});

        
            var html_e246979e4df3437b926567c25b3ba4a6 = $(`<div id="html_e246979e4df3437b926567c25b3ba4a6" style="width: 100.0%; height: 100.0%;">Latitude : 41.673819904<br>                     Longitude : -87.635739777<br>                     frequency : 5<br></div>`)[0];
            popup_b698010ea7de4793b32c29b0c7e345cd.setContent(html_e246979e4df3437b926567c25b3ba4a6);
        

        circle_marker_6ef1d0860456473ab0beec46b035e3a5.bindPopup(popup_b698010ea7de4793b32c29b0c7e345cd)
        ;

        
    
    
            var circle_marker_3398fb362cef4ab9b3ef045135a44b95 = L.circleMarker(
                [41.851017824, -87.635091856],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.02142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_07a57b34f27f477790dee65a0538db56 = L.popup({"maxWidth": "100%"});

        
            var html_bf4026aac86640628adc823a11f482c6 = $(`<div id="html_bf4026aac86640628adc823a11f482c6" style="width: 100.0%; height: 100.0%;">Latitude : 41.851017824<br>                     Longitude : -87.635091856<br>                     frequency : 6<br></div>`)[0];
            popup_07a57b34f27f477790dee65a0538db56.setContent(html_bf4026aac86640628adc823a11f482c6);
        

        circle_marker_3398fb362cef4ab9b3ef045135a44b95.bindPopup(popup_07a57b34f27f477790dee65a0538db56)
        ;

        
    
    
            var circle_marker_d386b1e009f04b44a5c2d5735d35edc4 = L.circleMarker(
                [41.934650448, -87.634647877],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.014285714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_3bbd2e904e9048a1b518e283950fedee = L.popup({"maxWidth": "100%"});

        
            var html_5d806f6785504b63aaf6f7c0465b346b = $(`<div id="html_5d806f6785504b63aaf6f7c0465b346b" style="width: 100.0%; height: 100.0%;">Latitude : 41.934650448<br>                     Longitude : -87.634647877<br>                     frequency : 4<br></div>`)[0];
            popup_3bbd2e904e9048a1b518e283950fedee.setContent(html_5d806f6785504b63aaf6f7c0465b346b);
        

        circle_marker_d386b1e009f04b44a5c2d5735d35edc4.bindPopup(popup_3bbd2e904e9048a1b518e283950fedee)
        ;

        
    
    
            var circle_marker_e3932489943c4526b642f69e9c837b49 = L.circleMarker(
                [41.922082541, -87.634156093],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.4642857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_1bf4817a09174435be2a71b51e507d72 = L.popup({"maxWidth": "100%"});

        
            var html_1e8cee89feb74e7eb515784acde49b4c = $(`<div id="html_1e8cee89feb74e7eb515784acde49b4c" style="width: 100.0%; height: 100.0%;">Latitude : 41.922082541<br>                     Longitude : -87.634156093<br>                     frequency : 130<br></div>`)[0];
            popup_1bf4817a09174435be2a71b51e507d72.setContent(html_1e8cee89feb74e7eb515784acde49b4c);
        

        circle_marker_e3932489943c4526b642f69e9c837b49.bindPopup(popup_1bf4817a09174435be2a71b51e507d72)
        ;

        
    
    
            var circle_marker_15834db554e447fcadcf9533e4f40085 = L.circleMarker(
                [41.842076117, -87.633973422],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.18214285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_5ca1ae0c5f2347e9b570d63d79ab8da4 = L.popup({"maxWidth": "100%"});

        
            var html_a7accfcd551447fa9972d8bc04052a65 = $(`<div id="html_a7accfcd551447fa9972d8bc04052a65" style="width: 100.0%; height: 100.0%;">Latitude : 41.842076117<br>                     Longitude : -87.633973422<br>                     frequency : 51<br></div>`)[0];
            popup_5ca1ae0c5f2347e9b570d63d79ab8da4.setContent(html_a7accfcd551447fa9972d8bc04052a65);
        

        circle_marker_15834db554e447fcadcf9533e4f40085.bindPopup(popup_5ca1ae0c5f2347e9b570d63d79ab8da4)
        ;

        
    
    
            var circle_marker_a22cd1a43d1240338cfb9cebd96a048b = L.circleMarker(
                [41.899602111, -87.633308037],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 8.95, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_b827ee08f7204061bd02fa59532322b4 = L.popup({"maxWidth": "100%"});

        
            var html_414a98ad3faf4f75a7533a93677a5d7b = $(`<div id="html_414a98ad3faf4f75a7533a93677a5d7b" style="width: 100.0%; height: 100.0%;">Latitude : 41.899602111<br>                     Longitude : -87.633308037<br>                     frequency : 2506<br></div>`)[0];
            popup_b827ee08f7204061bd02fa59532322b4.setContent(html_414a98ad3faf4f75a7533a93677a5d7b);
        

        circle_marker_a22cd1a43d1240338cfb9cebd96a048b.bindPopup(popup_b827ee08f7204061bd02fa59532322b4)
        ;

        
    
    
            var circle_marker_073dabc37ca54f87b96502bc5b57c90c = L.circleMarker(
                [41.834480698, -87.632959635],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.014285714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_af30b44b45314663b54bc47025681e86 = L.popup({"maxWidth": "100%"});

        
            var html_ad049ad5ba2e47618b501d5cbb6a620e = $(`<div id="html_ad049ad5ba2e47618b501d5cbb6a620e" style="width: 100.0%; height: 100.0%;">Latitude : 41.834480698<br>                     Longitude : -87.632959635<br>                     frequency : 4<br></div>`)[0];
            popup_af30b44b45314663b54bc47025681e86.setContent(html_ad049ad5ba2e47618b501d5cbb6a620e);
        

        circle_marker_073dabc37ca54f87b96502bc5b57c90c.bindPopup(popup_af30b44b45314663b54bc47025681e86)
        ;

        
    
    
            var circle_marker_7c3acbcc5b954dfab1969da3e3899c39 = L.circleMarker(
                [41.880994471, -87.632746489],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 24.103571428571428, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_d388dab7f4354885b8b85a0ffb75ad71 = L.popup({"maxWidth": "100%"});

        
            var html_e6c91413194b4361af3eb544cb3252e3 = $(`<div id="html_e6c91413194b4361af3eb544cb3252e3" style="width: 100.0%; height: 100.0%;">Latitude : 41.880994471<br>                     Longitude : -87.632746489<br>                     frequency : 6749<br></div>`)[0];
            popup_d388dab7f4354885b8b85a0ffb75ad71.setContent(html_e6c91413194b4361af3eb544cb3252e3);
        

        circle_marker_7c3acbcc5b954dfab1969da3e3899c39.bindPopup(popup_d388dab7f4354885b8b85a0ffb75ad71)
        ;

        
    
    
            var circle_marker_2cbe0f06709f44a4af96bb6cd2308822 = L.circleMarker(
                [41.827437232, -87.632558769],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.03214285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_5bf7f60b6d214ba2999236bc6e1c61b0 = L.popup({"maxWidth": "100%"});

        
            var html_b45971ca83764edc8f93f4de8414e329 = $(`<div id="html_b45971ca83764edc8f93f4de8414e329" style="width: 100.0%; height: 100.0%;">Latitude : 41.827437232<br>                     Longitude : -87.632558769<br>                     frequency : 9<br></div>`)[0];
            popup_5bf7f60b6d214ba2999236bc6e1c61b0.setContent(html_b45971ca83764edc8f93f4de8414e329);
        

        circle_marker_2cbe0f06709f44a4af96bb6cd2308822.bindPopup(popup_5bf7f60b6d214ba2999236bc6e1c61b0)
        ;

        
    
    
            var circle_marker_6bd0fe4e87924d198a444ae1b1efd2d4 = L.circleMarker(
                [41.80908443, -87.632424524],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_abe02a41006b470eab58cb8df88e04c3 = L.popup({"maxWidth": "100%"});

        
            var html_c6a7247c3c0a471389ce48042544b7d3 = $(`<div id="html_c6a7247c3c0a471389ce48042544b7d3" style="width: 100.0%; height: 100.0%;">Latitude : 41.80908443<br>                     Longitude : -87.632424524<br>                     frequency : 3<br></div>`)[0];
            popup_abe02a41006b470eab58cb8df88e04c3.setContent(html_c6a7247c3c0a471389ce48042544b7d3);
        

        circle_marker_6bd0fe4e87924d198a444ae1b1efd2d4.bindPopup(popup_abe02a41006b470eab58cb8df88e04c3)
        ;

        
    
    
            var circle_marker_74eddd08df504472974691e317ba65e9 = L.circleMarker(
                [41.900265687, -87.63210922],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1.0642857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_c344faa1e4014f4c82b7fe523957820c = L.popup({"maxWidth": "100%"});

        
            var html_79f2d43463dd48329bb65db97ff17bfe = $(`<div id="html_79f2d43463dd48329bb65db97ff17bfe" style="width: 100.0%; height: 100.0%;">Latitude : 41.900265687<br>                     Longitude : -87.63210922<br>                     frequency : 298<br></div>`)[0];
            popup_c344faa1e4014f4c82b7fe523957820c.setContent(html_79f2d43463dd48329bb65db97ff17bfe);
        

        circle_marker_74eddd08df504472974691e317ba65e9.bindPopup(popup_c344faa1e4014f4c82b7fe523957820c)
        ;

        
    
    
            var circle_marker_0c5150f685a84ec697654ea04681f970 = L.circleMarker(
                [41.892042136, -87.63186395],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 7.482142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_7e10cf34c5764a439385afe1d8a02717 = L.popup({"maxWidth": "100%"});

        
            var html_63045533cad74b76833bac090a217331 = $(`<div id="html_63045533cad74b76833bac090a217331" style="width: 100.0%; height: 100.0%;">Latitude : 41.892042136<br>                     Longitude : -87.63186395<br>                     frequency : 2095<br></div>`)[0];
            popup_7e10cf34c5764a439385afe1d8a02717.setContent(html_63045533cad74b76833bac090a217331);
        

        circle_marker_0c5150f685a84ec697654ea04681f970.bindPopup(popup_7e10cf34c5764a439385afe1d8a02717)
        ;

        
    
    
            var circle_marker_b720a983d81f4e1c88b458ce98994dfc = L.circleMarker(
                [41.914616286, -87.631717366],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1.167857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_f064eb21720f42cfbcefe5a7bd90e1d3 = L.popup({"maxWidth": "100%"});

        
            var html_6b70da94e02a41c0b0ef135e68fe206a = $(`<div id="html_6b70da94e02a41c0b0ef135e68fe206a" style="width: 100.0%; height: 100.0%;">Latitude : 41.914616286<br>                     Longitude : -87.631717366<br>                     frequency : 327<br></div>`)[0];
            popup_f064eb21720f42cfbcefe5a7bd90e1d3.setContent(html_6b70da94e02a41c0b0ef135e68fe206a);
        

        circle_marker_b720a983d81f4e1c88b458ce98994dfc.bindPopup(popup_f064eb21720f42cfbcefe5a7bd90e1d3)
        ;

        
    
    
            var circle_marker_cbe86a6c14b244daa9471d609fc8d659 = L.circleMarker(
                [41.87101588, -87.631406525],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.19642857142857142, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_7341035bfe2e42f985818b00387512d0 = L.popup({"maxWidth": "100%"});

        
            var html_fe43934863094d7b8e78c1a4482d0013 = $(`<div id="html_fe43934863094d7b8e78c1a4482d0013" style="width: 100.0%; height: 100.0%;">Latitude : 41.87101588<br>                     Longitude : -87.631406525<br>                     frequency : 55<br></div>`)[0];
            popup_7341035bfe2e42f985818b00387512d0.setContent(html_fe43934863094d7b8e78c1a4482d0013);
        

        circle_marker_cbe86a6c14b244daa9471d609fc8d659.bindPopup(popup_7341035bfe2e42f985818b00387512d0)
        ;

        
    
    
            var circle_marker_ade3a2dd47be4014be1e257315a396ec = L.circleMarker(
                [41.909495669, -87.630963601],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.4, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_85ca260d1da840f4ab2b1a69cd86bb4b = L.popup({"maxWidth": "100%"});

        
            var html_9aa281c2c48f4e33936facabc4ce5456 = $(`<div id="html_9aa281c2c48f4e33936facabc4ce5456" style="width: 100.0%; height: 100.0%;">Latitude : 41.909495669<br>                     Longitude : -87.630963601<br>                     frequency : 112<br></div>`)[0];
            popup_85ca260d1da840f4ab2b1a69cd86bb4b.setContent(html_9aa281c2c48f4e33936facabc4ce5456);
        

        circle_marker_ade3a2dd47be4014be1e257315a396ec.bindPopup(popup_85ca260d1da840f4ab2b1a69cd86bb4b)
        ;

        
    
    
            var circle_marker_e2aa586cea7e411db877e45d0c776d32 = L.circleMarker(
                [41.905857769, -87.630865027],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1.0714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_cb51b54aaa7e46718fbf27bd4231ce48 = L.popup({"maxWidth": "100%"});

        
            var html_d7ea2344df5944148142176e88341796 = $(`<div id="html_d7ea2344df5944148142176e88341796" style="width: 100.0%; height: 100.0%;">Latitude : 41.905857769<br>                     Longitude : -87.630865027<br>                     frequency : 300<br></div>`)[0];
            popup_cb51b54aaa7e46718fbf27bd4231ce48.setContent(html_d7ea2344df5944148142176e88341796);
        

        circle_marker_e2aa586cea7e411db877e45d0c776d32.bindPopup(popup_cb51b54aaa7e46718fbf27bd4231ce48)
        ;

        
    
    
            var circle_marker_fcd84b175e4246608f670958ccf9ec6e = L.circleMarker(
                [41.861280847, -87.630580061],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_74c4d70581384b86944c492e0d532951 = L.popup({"maxWidth": "100%"});

        
            var html_e8448a639de14dc09a8eb4ed4e298c61 = $(`<div id="html_e8448a639de14dc09a8eb4ed4e298c61" style="width: 100.0%; height: 100.0%;">Latitude : 41.861280847<br>                     Longitude : -87.630580061<br>                     frequency : 3<br></div>`)[0];
            popup_74c4d70581384b86944c492e0d532951.setContent(html_e8448a639de14dc09a8eb4ed4e298c61);
        

        circle_marker_fcd84b175e4246608f670958ccf9ec6e.bindPopup(popup_74c4d70581384b86944c492e0d532951)
        ;

        
    
    
            var circle_marker_9eec9f44ed97462a8c3b25990f544ad9 = L.circleMarker(
                [41.900221297, -87.629105186],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1.2821428571428573, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_ec0696910056456cabae69d207e0ee6d = L.popup({"maxWidth": "100%"});

        
            var html_59185d79f3224a2e9b02059d106f5011 = $(`<div id="html_59185d79f3224a2e9b02059d106f5011" style="width: 100.0%; height: 100.0%;">Latitude : 41.900221297<br>                     Longitude : -87.629105186<br>                     frequency : 359<br></div>`)[0];
            popup_ec0696910056456cabae69d207e0ee6d.setContent(html_59185d79f3224a2e9b02059d106f5011);
        

        circle_marker_9eec9f44ed97462a8c3b25990f544ad9.bindPopup(popup_ec0696910056456cabae69d207e0ee6d)
        ;

        
    
    
            var circle_marker_a3a1da034d8b41478dcc8575ed56c334 = L.circleMarker(
                [41.892072635, -87.628874157],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 3.4857142857142858, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_cee04e3477ed424abdbf518c5f99b590 = L.popup({"maxWidth": "100%"});

        
            var html_a58dcda29e324ff9bfcf615386e3d89e = $(`<div id="html_a58dcda29e324ff9bfcf615386e3d89e" style="width: 100.0%; height: 100.0%;">Latitude : 41.892072635<br>                     Longitude : -87.628874157<br>                     frequency : 976<br></div>`)[0];
            popup_cee04e3477ed424abdbf518c5f99b590.setContent(html_a58dcda29e324ff9bfcf615386e3d89e);
        

        circle_marker_a3a1da034d8b41478dcc8575ed56c334.bindPopup(popup_cee04e3477ed424abdbf518c5f99b590)
        ;

        
    
    
            var circle_marker_d2b0a489fe7f47608c40b68e098fabb5 = L.circleMarker(
                [41.841928026, -87.62836651],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_25b80b388e1d4d00b44dd5b596a4a14f = L.popup({"maxWidth": "100%"});

        
            var html_ce01b566ef324e5cab0a8ff188c6ef79 = $(`<div id="html_ce01b566ef324e5cab0a8ff188c6ef79" style="width: 100.0%; height: 100.0%;">Latitude : 41.841928026<br>                     Longitude : -87.62836651<br>                     frequency : 1<br></div>`)[0];
            popup_25b80b388e1d4d00b44dd5b596a4a14f.setContent(html_ce01b566ef324e5cab0a8ff188c6ef79);
        

        circle_marker_d2b0a489fe7f47608c40b68e098fabb5.bindPopup(popup_25b80b388e1d4d00b44dd5b596a4a14f)
        ;

        
    
    
            var circle_marker_e941c1add48c4bd799e3531199fca616 = L.circleMarker(
                [41.907520075, -87.6266589],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1.0607142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_39ab231aa7d845e49a3306572a54a855 = L.popup({"maxWidth": "100%"});

        
            var html_13806f76d6584216a072871897610e90 = $(`<div id="html_13806f76d6584216a072871897610e90" style="width: 100.0%; height: 100.0%;">Latitude : 41.907520075<br>                     Longitude : -87.6266589<br>                     frequency : 297<br></div>`)[0];
            popup_39ab231aa7d845e49a3306572a54a855.setContent(html_13806f76d6584216a072871897610e90);
        

        circle_marker_e941c1add48c4bd799e3531199fca616.bindPopup(popup_39ab231aa7d845e49a3306572a54a855)
        ;

        
    
    
            var circle_marker_576c1a260175408e9af95d6755e4310c = L.circleMarker(
                [41.892507781, -87.626214906],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 9.096428571428572, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_c062f8e2cca348209c49aaef31fb5db7 = L.popup({"maxWidth": "100%"});

        
            var html_91dd4776e2bb419ca32b1755c793eee4 = $(`<div id="html_91dd4776e2bb419ca32b1755c793eee4" style="width: 100.0%; height: 100.0%;">Latitude : 41.892507781<br>                     Longitude : -87.626214906<br>                     frequency : 2547<br></div>`)[0];
            popup_c062f8e2cca348209c49aaef31fb5db7.setContent(html_91dd4776e2bb419ca32b1755c793eee4);
        

        circle_marker_576c1a260175408e9af95d6755e4310c.bindPopup(popup_c062f8e2cca348209c49aaef31fb5db7)
        ;

        
    
    
            var circle_marker_088ca6cbb48b42a8a48bc7d3cdca7fb4 = L.circleMarker(
                [41.899155613, -87.626210532],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 4.610714285714286, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_9520e985f4334f2e90e5c82eb0349ca1 = L.popup({"maxWidth": "100%"});

        
            var html_407f42fedba5423d899665472ddb70ce = $(`<div id="html_407f42fedba5423d899665472ddb70ce" style="width: 100.0%; height: 100.0%;">Latitude : 41.899155613<br>                     Longitude : -87.626210532<br>                     frequency : 1291<br></div>`)[0];
            popup_9520e985f4334f2e90e5c82eb0349ca1.setContent(html_407f42fedba5423d899665472ddb70ce);
        

        circle_marker_088ca6cbb48b42a8a48bc7d3cdca7fb4.bindPopup(popup_9520e985f4334f2e90e5c82eb0349ca1)
        ;

        
    
    
            var circle_marker_f2829d53cf144c7fbdff2422d76942bb = L.circleMarker(
                [41.902788048, -87.62614559],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1.4142857142857144, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_b8e0b0946869439e94a0d1772f5bda6d = L.popup({"maxWidth": "100%"});

        
            var html_503992dbc1c8495f9f4ddaaeca74ced5 = $(`<div id="html_503992dbc1c8495f9f4ddaaeca74ced5" style="width: 100.0%; height: 100.0%;">Latitude : 41.902788048<br>                     Longitude : -87.62614559<br>                     frequency : 396<br></div>`)[0];
            popup_b8e0b0946869439e94a0d1772f5bda6d.setContent(html_503992dbc1c8495f9f4ddaaeca74ced5);
        

        circle_marker_f2829d53cf144c7fbdff2422d76942bb.bindPopup(popup_b8e0b0946869439e94a0d1772f5bda6d)
        ;

        
    
    
            var circle_marker_5a6f6cd5543947b18ba2023e1d0135b4 = L.circleMarker(
                [41.878865584, -87.625192142],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.564285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_94af570966bc44a6b3980aef83b3c70c = L.popup({"maxWidth": "100%"});

        
            var html_c2aa6b26c257427b9209c2036933a6fd = $(`<div id="html_c2aa6b26c257427b9209c2036933a6fd" style="width: 100.0%; height: 100.0%;">Latitude : 41.878865584<br>                     Longitude : -87.625192142<br>                     frequency : 1558<br></div>`)[0];
            popup_94af570966bc44a6b3980aef83b3c70c.setContent(html_c2aa6b26c257427b9209c2036933a6fd);
        

        circle_marker_5a6f6cd5543947b18ba2023e1d0135b4.bindPopup(popup_94af570966bc44a6b3980aef83b3c70c)
        ;

        
    
    
            var circle_marker_219b38a807a14b2493ee67c27515b642 = L.circleMarker(
                [41.849246754, -87.624135298],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1.3107142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_2b4401b61a604384904bdf1385960f76 = L.popup({"maxWidth": "100%"});

        
            var html_d86071be6d1049f994136e21665841a1 = $(`<div id="html_d86071be6d1049f994136e21665841a1" style="width: 100.0%; height: 100.0%;">Latitude : 41.849246754<br>                     Longitude : -87.624135298<br>                     frequency : 367<br></div>`)[0];
            popup_2b4401b61a604384904bdf1385960f76.setContent(html_d86071be6d1049f994136e21665841a1);
        

        circle_marker_219b38a807a14b2493ee67c27515b642.bindPopup(popup_2b4401b61a604384904bdf1385960f76)
        ;

        
    
    
            var circle_marker_33c782207a1a442ab1b2ab4723201556 = L.circleMarker(
                [41.706587882, -87.623366512],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.04642857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_5339ce48e4384e3da8d41e2c91c97bbf = L.popup({"maxWidth": "100%"});

        
            var html_0e9fe9810f90491eb24781d1c875f219 = $(`<div id="html_0e9fe9810f90491eb24781d1c875f219" style="width: 100.0%; height: 100.0%;">Latitude : 41.706587882<br>                     Longitude : -87.623366512<br>                     frequency : 13<br></div>`)[0];
            popup_5339ce48e4384e3da8d41e2c91c97bbf.setContent(html_0e9fe9810f90491eb24781d1c875f219);
        

        circle_marker_33c782207a1a442ab1b2ab4723201556.bindPopup(popup_5339ce48e4384e3da8d41e2c91c97bbf)
        ;

        
    
    
            var circle_marker_b499a6a60ba44e97a42af4bb46fd0bc6 = L.circleMarker(
                [41.870607372, -87.622172937],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1.9107142857142858, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_b97cae90448641239b42171c3d8f9c18 = L.popup({"maxWidth": "100%"});

        
            var html_51495567f67c474791a19d416c0083ce = $(`<div id="html_51495567f67c474791a19d416c0083ce" style="width: 100.0%; height: 100.0%;">Latitude : 41.870607372<br>                     Longitude : -87.622172937<br>                     frequency : 535<br></div>`)[0];
            popup_b97cae90448641239b42171c3d8f9c18.setContent(html_51495567f67c474791a19d416c0083ce);
        

        circle_marker_b499a6a60ba44e97a42af4bb46fd0bc6.bindPopup(popup_b97cae90448641239b42171c3d8f9c18)
        ;

        
    
    
            var circle_marker_a4fadb70517643f0931a3a0d530d1206 = L.circleMarker(
                [41.84201118, -87.622036461],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_08a77aeed659417294946009a0a1f7cc = L.popup({"maxWidth": "100%"});

        
            var html_944ae350b4f74811b314e9e8c5613676 = $(`<div id="html_944ae350b4f74811b314e9e8c5613676" style="width: 100.0%; height: 100.0%;">Latitude : 41.84201118<br>                     Longitude : -87.622036461<br>                     frequency : 1<br></div>`)[0];
            popup_08a77aeed659417294946009a0a1f7cc.setContent(html_944ae350b4f74811b314e9e8c5613676);
        

        circle_marker_a4fadb70517643f0931a3a0d530d1206.bindPopup(popup_08a77aeed659417294946009a0a1f7cc)
        ;

        
    
    
            var circle_marker_38a5db07230c465884c048f37431e6b6 = L.circleMarker(
                [41.877406123, -87.621971652],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 4.314285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_b6732bc161f844c2a7d5685b4c42a531 = L.popup({"maxWidth": "100%"});

        
            var html_2ef99525bd25488891d218da0f37fa9d = $(`<div id="html_2ef99525bd25488891d218da0f37fa9d" style="width: 100.0%; height: 100.0%;">Latitude : 41.877406123<br>                     Longitude : -87.621971652<br>                     frequency : 1208<br></div>`)[0];
            popup_b6732bc161f844c2a7d5685b4c42a531.setContent(html_2ef99525bd25488891d218da0f37fa9d);
        

        circle_marker_38a5db07230c465884c048f37431e6b6.bindPopup(popup_b6732bc161f844c2a7d5685b4c42a531)
        ;

        
    
    
            var circle_marker_fb636db7e5554b3ba9ee091f6760f8f7 = L.circleMarker(
                [41.884987192, -87.620992913],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 13.65, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_14f135e2733f47c39583e12c435abf4c = L.popup({"maxWidth": "100%"});

        
            var html_a959c7cc2a034d479241ace5fd788d61 = $(`<div id="html_a959c7cc2a034d479241ace5fd788d61" style="width: 100.0%; height: 100.0%;">Latitude : 41.884987192<br>                     Longitude : -87.620992913<br>                     frequency : 3822<br></div>`)[0];
            popup_14f135e2733f47c39583e12c435abf4c.setContent(html_a959c7cc2a034d479241ace5fd788d61);
        

        circle_marker_fb636db7e5554b3ba9ee091f6760f8f7.bindPopup(popup_14f135e2733f47c39583e12c435abf4c)
        ;

        
    
    
            var circle_marker_ddd4af89abe14e42b1ab4e761d4365f5 = L.circleMarker(
                [41.898331794, -87.620762865],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 3.6535714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_0b5d23467f5347d199541cbdfe872bb8 = L.popup({"maxWidth": "100%"});

        
            var html_fb5e57f7052f400d98daf47e6901c7a7 = $(`<div id="html_fb5e57f7052f400d98daf47e6901c7a7" style="width: 100.0%; height: 100.0%;">Latitude : 41.898331794<br>                     Longitude : -87.620762865<br>                     frequency : 1023<br></div>`)[0];
            popup_0b5d23467f5347d199541cbdfe872bb8.setContent(html_fb5e57f7052f400d98daf47e6901c7a7);
        

        circle_marker_ddd4af89abe14e42b1ab4e761d4365f5.bindPopup(popup_0b5d23467f5347d199541cbdfe872bb8)
        ;

        
    
    
            var circle_marker_71ee8da7dffa4fa9a1419216d6677ddb = L.circleMarker(
                [41.857183858, -87.620334624],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.75, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_f5d1dfb9b92745288b31140219d65094 = L.popup({"maxWidth": "100%"});

        
            var html_ee8a96d101de44f4a7694e5411181771 = $(`<div id="html_ee8a96d101de44f4a7694e5411181771" style="width: 100.0%; height: 100.0%;">Latitude : 41.857183858<br>                     Longitude : -87.620334624<br>                     frequency : 210<br></div>`)[0];
            popup_f5d1dfb9b92745288b31140219d65094.setContent(html_ee8a96d101de44f4a7694e5411181771);
        

        circle_marker_71ee8da7dffa4fa9a1419216d6677ddb.bindPopup(popup_f5d1dfb9b92745288b31140219d65094)
        ;

        
    
    
            var circle_marker_a8a128c333984387908712c6c81f9d62 = L.circleMarker(
                [41.89503345, -87.619710672],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 3.8857142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_b6cd7847e10d4a398e43de872fee9f94 = L.popup({"maxWidth": "100%"});

        
            var html_fc4b8997a6eb4e4da1bc59b1a401627c = $(`<div id="html_fc4b8997a6eb4e4da1bc59b1a401627c" style="width: 100.0%; height: 100.0%;">Latitude : 41.89503345<br>                     Longitude : -87.619710672<br>                     frequency : 1088<br></div>`)[0];
            popup_b6cd7847e10d4a398e43de872fee9f94.setContent(html_fc4b8997a6eb4e4da1bc59b1a401627c);
        

        circle_marker_a8a128c333984387908712c6c81f9d62.bindPopup(popup_b6cd7847e10d4a398e43de872fee9f94)
        ;

        
    
    
            var circle_marker_4572e19dddb14eb08d5c06c4f2395748 = L.circleMarker(
                [41.890922026, -87.618868355],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.860714285714286, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_ae252c5b08064c848dd5d837933da6fd = L.popup({"maxWidth": "100%"});

        
            var html_5e8fb752b5304a808dca7534a33805a4 = $(`<div id="html_5e8fb752b5304a808dca7534a33805a4" style="width: 100.0%; height: 100.0%;">Latitude : 41.890922026<br>                     Longitude : -87.618868355<br>                     frequency : 1641<br></div>`)[0];
            popup_ae252c5b08064c848dd5d837933da6fd.setContent(html_5e8fb752b5304a808dca7534a33805a4);
        

        circle_marker_4572e19dddb14eb08d5c06c4f2395748.bindPopup(popup_ae252c5b08064c848dd5d837933da6fd)
        ;

        
    
    
            var circle_marker_44e04318b11a4b3198528bfa717d55e1 = L.circleMarker(
                [41.835117986, -87.618677767],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.225, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_bc829802be4b4ef3999f8aa47910e7fa = L.popup({"maxWidth": "100%"});

        
            var html_fd379540877b4ad0be3996741b8d8ecc = $(`<div id="html_fd379540877b4ad0be3996741b8d8ecc" style="width: 100.0%; height: 100.0%;">Latitude : 41.835117986<br>                     Longitude : -87.618677767<br>                     frequency : 63<br></div>`)[0];
            popup_bc829802be4b4ef3999f8aa47910e7fa.setContent(html_fd379540877b4ad0be3996741b8d8ecc);
        

        circle_marker_44e04318b11a4b3198528bfa717d55e1.bindPopup(popup_bc829802be4b4ef3999f8aa47910e7fa)
        ;

        
    
    
            var circle_marker_8d3d58b85e17408b90b4b4d3cf0a0e0b = L.circleMarker(
                [41.792357223, -87.61793138],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.017857142857142856, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_6f1c916464994a42808554b00b1fa257 = L.popup({"maxWidth": "100%"});

        
            var html_a7e90dfc021b458d95592aa010a66dbf = $(`<div id="html_a7e90dfc021b458d95592aa010a66dbf" style="width: 100.0%; height: 100.0%;">Latitude : 41.792357223<br>                     Longitude : -87.61793138<br>                     frequency : 5<br></div>`)[0];
            popup_6f1c916464994a42808554b00b1fa257.setContent(html_a7e90dfc021b458d95592aa010a66dbf);
        

        circle_marker_8d3d58b85e17408b90b4b4d3cf0a0e0b.bindPopup(popup_6f1c916464994a42808554b00b1fa257)
        ;

        
    
    
            var circle_marker_28f4e2090ccd490daba4f976d605c2a2 = L.circleMarker(
                [41.812948939, -87.617859676],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.08928571428571429, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_da1a2fa0a04a4a2b8957bdd67318fe9e = L.popup({"maxWidth": "100%"});

        
            var html_c6e4a57bfec64b1e86fcd938ab567fa3 = $(`<div id="html_c6e4a57bfec64b1e86fcd938ab567fa3" style="width: 100.0%; height: 100.0%;">Latitude : 41.812948939<br>                     Longitude : -87.617859676<br>                     frequency : 25<br></div>`)[0];
            popup_da1a2fa0a04a4a2b8957bdd67318fe9e.setContent(html_c6e4a57bfec64b1e86fcd938ab567fa3);
        

        circle_marker_28f4e2090ccd490daba4f976d605c2a2.bindPopup(popup_da1a2fa0a04a4a2b8957bdd67318fe9e)
        ;

        
    
    
            var circle_marker_ed0a387aef5440e9b31ad73d72a9bef0 = L.circleMarker(
                [41.859349715, -87.617358006],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 3.0535714285714284, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_6558a73f80d44b80b0ddc026e3b6e9bc = L.popup({"maxWidth": "100%"});

        
            var html_1e2ba1a4319d4f7ebe938fd80582b195 = $(`<div id="html_1e2ba1a4319d4f7ebe938fd80582b195" style="width: 100.0%; height: 100.0%;">Latitude : 41.859349715<br>                     Longitude : -87.617358006<br>                     frequency : 855<br></div>`)[0];
            popup_6558a73f80d44b80b0ddc026e3b6e9bc.setContent(html_1e2ba1a4319d4f7ebe938fd80582b195);
        

        circle_marker_ed0a387aef5440e9b31ad73d72a9bef0.bindPopup(popup_6558a73f80d44b80b0ddc026e3b6e9bc)
        ;

        
    
    
            var circle_marker_063dca22842e4f05a3551b1bd8ff5adf = L.circleMarker(
                [41.763246799, -87.616134111],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.04285714285714286, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_f36c719ca89d4e71958fad68e56de764 = L.popup({"maxWidth": "100%"});

        
            var html_5cfa52a447c44eafa31a5276392406cc = $(`<div id="html_5cfa52a447c44eafa31a5276392406cc" style="width: 100.0%; height: 100.0%;">Latitude : 41.763246799<br>                     Longitude : -87.616134111<br>                     frequency : 12<br></div>`)[0];
            popup_f36c719ca89d4e71958fad68e56de764.setContent(html_5cfa52a447c44eafa31a5276392406cc);
        

        circle_marker_063dca22842e4f05a3551b1bd8ff5adf.bindPopup(popup_f36c719ca89d4e71958fad68e56de764)
        ;

        
    
    
            var circle_marker_254ddf12ccd24eb2bd500d1d7b854a89 = L.circleMarker(
                [41.740205756, -87.615969523],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.03571428571428571, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_80dc63ea218d4f8cae4ec9a88443680a = L.popup({"maxWidth": "100%"});

        
            var html_55ef52bc474a4b5b969b049435716b99 = $(`<div id="html_55ef52bc474a4b5b969b049435716b99" style="width: 100.0%; height: 100.0%;">Latitude : 41.740205756<br>                     Longitude : -87.615969523<br>                     frequency : 10<br></div>`)[0];
            popup_80dc63ea218d4f8cae4ec9a88443680a.setContent(html_55ef52bc474a4b5b969b049435716b99);
        

        circle_marker_254ddf12ccd24eb2bd500d1d7b854a89.bindPopup(popup_80dc63ea218d4f8cae4ec9a88443680a)
        ;

        
    
    
            var circle_marker_75d81b1b8cc84758b8f0c7541d2c36d3 = L.circleMarker(
                [41.891971508, -87.612945414],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 2.039285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_049223fad6a1405cb62179d3186efbe2 = L.popup({"maxWidth": "100%"});

        
            var html_a28cc9f876e84a9db4beb9c13a154622 = $(`<div id="html_a28cc9f876e84a9db4beb9c13a154622" style="width: 100.0%; height: 100.0%;">Latitude : 41.891971508<br>                     Longitude : -87.612945414<br>                     frequency : 571<br></div>`)[0];
            popup_049223fad6a1405cb62179d3186efbe2.setContent(html_a28cc9f876e84a9db4beb9c13a154622);
        

        circle_marker_75d81b1b8cc84758b8f0c7541d2c36d3.bindPopup(popup_049223fad6a1405cb62179d3186efbe2)
        ;

        
    
    
            var circle_marker_81badf6fb92f4e6982e637885fd77860 = L.circleMarker(
                [41.834673598, -87.610834737],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_1e0632b98a224343889eae989f4139ce = L.popup({"maxWidth": "100%"});

        
            var html_6d63251330f74880887acf19edb38559 = $(`<div id="html_6d63251330f74880887acf19edb38559" style="width: 100.0%; height: 100.0%;">Latitude : 41.834673598<br>                     Longitude : -87.610834737<br>                     frequency : 1<br></div>`)[0];
            popup_1e0632b98a224343889eae989f4139ce.setContent(html_6d63251330f74880887acf19edb38559);
        

        circle_marker_81badf6fb92f4e6982e637885fd77860.bindPopup(popup_1e0632b98a224343889eae989f4139ce)
        ;

        
    
    
            var circle_marker_be84ad303ce142d9a6751249a3ff3a4f = L.circleMarker(
                [41.748210512, -87.610074966],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_eef98e84be0145c9ad77d44db1d25979 = L.popup({"maxWidth": "100%"});

        
            var html_cdc7321cf26d4f3cad005085a3296618 = $(`<div id="html_cdc7321cf26d4f3cad005085a3296618" style="width: 100.0%; height: 100.0%;">Latitude : 41.748210512<br>                     Longitude : -87.610074966<br>                     frequency : 1<br></div>`)[0];
            popup_eef98e84be0145c9ad77d44db1d25979.setContent(html_cdc7321cf26d4f3cad005085a3296618);
        

        circle_marker_be84ad303ce142d9a6751249a3ff3a4f.bindPopup(popup_eef98e84be0145c9ad77d44db1d25979)
        ;

        
    
    
            var circle_marker_4aeb0d06b1f1482a99224cbd7eb6f8aa = L.circleMarker(
                [41.82371281, -87.602350437],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.02857142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_0c51c3d414f3404baba70775f86d74a5 = L.popup({"maxWidth": "100%"});

        
            var html_d151066fa45845119ac0e8fde72d660c = $(`<div id="html_d151066fa45845119ac0e8fde72d660c" style="width: 100.0%; height: 100.0%;">Latitude : 41.82371281<br>                     Longitude : -87.602350437<br>                     frequency : 8<br></div>`)[0];
            popup_0c51c3d414f3404baba70775f86d74a5.setContent(html_d151066fa45845119ac0e8fde72d660c);
        

        circle_marker_4aeb0d06b1f1482a99224cbd7eb6f8aa.bindPopup(popup_0c51c3d414f3404baba70775f86d74a5)
        ;

        
    
    
            var circle_marker_34ad7cbed7994e1c860bf1208b5e15c2 = L.circleMarker(
                [41.7904694, -87.601285122],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.04285714285714286, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_0ebd66a26dd1468f986419e208f860c5 = L.popup({"maxWidth": "100%"});

        
            var html_bb6b7904b98c4d44a2615781dc22144d = $(`<div id="html_bb6b7904b98c4d44a2615781dc22144d" style="width: 100.0%; height: 100.0%;">Latitude : 41.7904694<br>                     Longitude : -87.601285122<br>                     frequency : 12<br></div>`)[0];
            popup_0ebd66a26dd1468f986419e208f860c5.setContent(html_bb6b7904b98c4d44a2615781dc22144d);
        

        circle_marker_34ad7cbed7994e1c860bf1208b5e15c2.bindPopup(popup_0ebd66a26dd1468f986419e208f860c5)
        ;

        
    
    
            var circle_marker_67363769c0314ab9a7514e9f672be877 = L.circleMarker(
                [41.706125752, -87.598255838],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.017857142857142856, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_c4da904c403d49b0acc61fd9ab6bce1d = L.popup({"maxWidth": "100%"});

        
            var html_62e3573fa1214b119cb267f7fe9146a4 = $(`<div id="html_62e3573fa1214b119cb267f7fe9146a4" style="width: 100.0%; height: 100.0%;">Latitude : 41.706125752<br>                     Longitude : -87.598255838<br>                     frequency : 5<br></div>`)[0];
            popup_c4da904c403d49b0acc61fd9ab6bce1d.setContent(html_62e3573fa1214b119cb267f7fe9146a4);
        

        circle_marker_67363769c0314ab9a7514e9f672be877.bindPopup(popup_c4da904c403d49b0acc61fd9ab6bce1d)
        ;

        
    
    
            var circle_marker_bb290e042d1b4230a7d8f2818fd0d96e = L.circleMarker(
                [41.808916283, -87.596183344],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.18571428571428572, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_e61bcaa882134c3091bc9717c1f7d119 = L.popup({"maxWidth": "100%"});

        
            var html_4badce1918a24330bf5d04b79881650f = $(`<div id="html_4badce1918a24330bf5d04b79881650f" style="width: 100.0%; height: 100.0%;">Latitude : 41.808916283<br>                     Longitude : -87.596183344<br>                     frequency : 52<br></div>`)[0];
            popup_e61bcaa882134c3091bc9717c1f7d119.setContent(html_4badce1918a24330bf5d04b79881650f);
        

        circle_marker_bb290e042d1b4230a7d8f2818fd0d96e.bindPopup(popup_e61bcaa882134c3091bc9717c1f7d119)
        ;

        
    
    
            var circle_marker_0474dfc712004082bb8a1d942bca59e8 = L.circleMarker(
                [41.77887686, -87.594925439],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.10357142857142858, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_0bb451d1dc4145c6b4e930ac8f3b215d = L.popup({"maxWidth": "100%"});

        
            var html_be55b4ffe4024e62ad1f53fa0150f980 = $(`<div id="html_be55b4ffe4024e62ad1f53fa0150f980" style="width: 100.0%; height: 100.0%;">Latitude : 41.77887686<br>                     Longitude : -87.594925439<br>                     frequency : 29<br></div>`)[0];
            popup_0bb451d1dc4145c6b4e930ac8f3b215d.setContent(html_be55b4ffe4024e62ad1f53fa0150f980);
        

        circle_marker_0474dfc712004082bb8a1d942bca59e8.bindPopup(popup_0bb451d1dc4145c6b4e930ac8f3b215d)
        ;

        
    
    
            var circle_marker_5eaa04c688854c30a56622cbaaee0cf3 = L.circleMarker(
                [41.794090253, -87.592310855],
                {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.4357142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_aee3ba8d34ca43f69d694b5b0729afcc = L.popup({"maxWidth": "100%"});

        
            var html_0275621ca9e7468994fc19298d07cf30 = $(`<div id="html_0275621ca9e7468994fc19298d07cf30" style="width: 100.0%; height: 100.0%;">Latitude : 41.794090253<br>                     Longitude : -87.592310855<br>                     frequency : 122<br></div>`)[0];
            popup_aee3ba8d34ca43f69d694b5b0729afcc.setContent(html_0275621ca9e7468994fc19298d07cf30);
        

        circle_marker_5eaa04c688854c30a56622cbaaee0cf3.bindPopup(popup_aee3ba8d34ca43f69d694b5b0729afcc)
        ;

        
    
    
            var circle_marker_8294adfd7033421c83202b7666982c22 = L.circleMarker(
                [41.797965209, -87.589607031],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_baf1a8cbad3741f5907bb0b8fec18f0f = L.popup({"maxWidth": "100%"});

        
            var html_97f29f24d328417092a019d2b41fa89e = $(`<div id="html_97f29f24d328417092a019d2b41fa89e" style="width: 100.0%; height: 100.0%;">Latitude : 41.797965209<br>                     Longitude : -87.589607031<br>                     frequency : 1<br></div>`)[0];
            popup_baf1a8cbad3741f5907bb0b8fec18f0f.setContent(html_97f29f24d328417092a019d2b41fa89e);
        

        circle_marker_8294adfd7033421c83202b7666982c22.bindPopup(popup_baf1a8cbad3741f5907bb0b8fec18f0f)
        ;

        
    
    
            var circle_marker_358efa32c4004953ad14a5a8ee1c6559 = L.circleMarker(
                [41.805911699, -87.587479258],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.02142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_5526dfab9288478584e4437ae5736c52 = L.popup({"maxWidth": "100%"});

        
            var html_f08884cf48f94334aed50d6a15ab5129 = $(`<div id="html_f08884cf48f94334aed50d6a15ab5129" style="width: 100.0%; height: 100.0%;">Latitude : 41.805911699<br>                     Longitude : -87.587479258<br>                     frequency : 6<br></div>`)[0];
            popup_5526dfab9288478584e4437ae5736c52.setContent(html_f08884cf48f94334aed50d6a15ab5129);
        

        circle_marker_358efa32c4004953ad14a5a8ee1c6559.bindPopup(popup_5526dfab9288478584e4437ae5736c52)
        ;

        
    
    
            var circle_marker_2e2a23e0d8884c82b637c6e0344b7861 = L.circleMarker(
                [41.744199535, -87.586348318],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.017857142857142856, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_d70c3e61b5184a7db3af8834a6b15052 = L.popup({"maxWidth": "100%"});

        
            var html_0b47fdbc7bde46b993f0d9312ee26cd6 = $(`<div id="html_0b47fdbc7bde46b993f0d9312ee26cd6" style="width: 100.0%; height: 100.0%;">Latitude : 41.744199535<br>                     Longitude : -87.586348318<br>                     frequency : 5<br></div>`)[0];
            popup_d70c3e61b5184a7db3af8834a6b15052.setContent(html_0b47fdbc7bde46b993f0d9312ee26cd6);
        

        circle_marker_2e2a23e0d8884c82b637c6e0344b7861.bindPopup(popup_d70c3e61b5184a7db3af8834a6b15052)
        ;

        
    
    
            var circle_marker_28d58acea7614ddf9f0aa97af3ae3d74 = L.circleMarker(
                [41.790506261, -87.583143717],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.17142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_2fa5b68fba8d4e039bef72c2de36a32b = L.popup({"maxWidth": "100%"});

        
            var html_16b1ec189e7049aa97938dc6354291a1 = $(`<div id="html_16b1ec189e7049aa97938dc6354291a1" style="width: 100.0%; height: 100.0%;">Latitude : 41.790506261<br>                     Longitude : -87.583143717<br>                     frequency : 48<br></div>`)[0];
            popup_2fa5b68fba8d4e039bef72c2de36a32b.setContent(html_16b1ec189e7049aa97938dc6354291a1);
        

        circle_marker_28d58acea7614ddf9f0aa97af3ae3d74.bindPopup(popup_2fa5b68fba8d4e039bef72c2de36a32b)
        ;

        
    
    
            var circle_marker_34aab489f98447f1baff94e204fc32a2 = L.circleMarker(
                [41.797153425, -87.582365702],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_6a4c2bf15d17449c9a1a1af4519ab783 = L.popup({"maxWidth": "100%"});

        
            var html_7b41c07432d1444eab6ad5f53113be10 = $(`<div id="html_7b41c07432d1444eab6ad5f53113be10" style="width: 100.0%; height: 100.0%;">Latitude : 41.797153425<br>                     Longitude : -87.582365702<br>                     frequency : 3<br></div>`)[0];
            popup_6a4c2bf15d17449c9a1a1af4519ab783.setContent(html_7b41c07432d1444eab6ad5f53113be10);
        

        circle_marker_34aab489f98447f1baff94e204fc32a2.bindPopup(popup_6a4c2bf15d17449c9a1a1af4519ab783)
        ;

        
    
    
            var circle_marker_f368c78335e14612a4948089e9334257 = L.circleMarker(
                [41.761577908, -87.572781987],
                {"bubblingMouseEvents": true, "color": "orange", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.05357142857142857, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_534a112d92d74cbcbefdf88764d1935d = L.popup({"maxWidth": "100%"});

        
            var html_e483fae462134576acaa814a7fe4b7d3 = $(`<div id="html_e483fae462134576acaa814a7fe4b7d3" style="width: 100.0%; height: 100.0%;">Latitude : 41.761577908<br>                     Longitude : -87.572781987<br>                     frequency : 15<br></div>`)[0];
            popup_534a112d92d74cbcbefdf88764d1935d.setContent(html_e483fae462134576acaa814a7fe4b7d3);
        

        circle_marker_f368c78335e14612a4948089e9334257.bindPopup(popup_534a112d92d74cbcbefdf88764d1935d)
        ;

        
    
    
            var circle_marker_73c182265dbb4303a2989fcdbf0f512d = L.circleMarker(
                [41.729676423, -87.572717134],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.014285714285714285, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_4f436d3ec8c447cd97b6034e829aeffe = L.popup({"maxWidth": "100%"});

        
            var html_709d42f4542f4857b650f3d1282e486d = $(`<div id="html_709d42f4542f4857b650f3d1282e486d" style="width: 100.0%; height: 100.0%;">Latitude : 41.729676423<br>                     Longitude : -87.572717134<br>                     frequency : 4<br></div>`)[0];
            popup_4f436d3ec8c447cd97b6034e829aeffe.setContent(html_709d42f4542f4857b650f3d1282e486d);
        

        circle_marker_73c182265dbb4303a2989fcdbf0f512d.bindPopup(popup_4f436d3ec8c447cd97b6034e829aeffe)
        ;

        
    
    
            var circle_marker_e12428cc8aed4bd4999c3f30dbe8f0f4 = L.circleMarker(
                [41.690633347, -87.570058269],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_dd979e15fd84483fbdbfac581e13b64e = L.popup({"maxWidth": "100%"});

        
            var html_75dfacc2d149478c8df18928d2c937c7 = $(`<div id="html_75dfacc2d149478c8df18928d2c937c7" style="width: 100.0%; height: 100.0%;">Latitude : 41.690633347<br>                     Longitude : -87.570058269<br>                     frequency : 3<br></div>`)[0];
            popup_dd979e15fd84483fbdbfac581e13b64e.setContent(html_75dfacc2d149478c8df18928d2c937c7);
        

        circle_marker_e12428cc8aed4bd4999c3f30dbe8f0f4.bindPopup(popup_dd979e15fd84483fbdbfac581e13b64e)
        ;

        
    
    
            var circle_marker_f75bd238574541f59b759b27af5c912d = L.circleMarker(
                [41.741242728, -87.551428197],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.010714285714285714, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_d2d13b3ee7604a6291c05ce9075468c8 = L.popup({"maxWidth": "100%"});

        
            var html_c2d2ce863b754edbbf5a86a5119ff690 = $(`<div id="html_c2d2ce863b754edbbf5a86a5119ff690" style="width: 100.0%; height: 100.0%;">Latitude : 41.741242728<br>                     Longitude : -87.551428197<br>                     frequency : 3<br></div>`)[0];
            popup_d2d13b3ee7604a6291c05ce9075468c8.setContent(html_c2d2ce863b754edbbf5a86a5119ff690);
        

        circle_marker_f75bd238574541f59b759b27af5c912d.bindPopup(popup_d2d13b3ee7604a6291c05ce9075468c8)
        ;

        
    
    
            var circle_marker_659b5e9bfd264da28b3d72634e173f5f = L.circleMarker(
                [41.663670652, -87.540935513],
                {"bubblingMouseEvents": true, "color": "green", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.0035714285714285713, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_1dfd1f1b32064d218106ff1b6ef2ae52 = L.popup({"maxWidth": "100%"});

        
            var html_bed154e77b444951b960ee5d0adfbd34 = $(`<div id="html_bed154e77b444951b960ee5d0adfbd34" style="width: 100.0%; height: 100.0%;">Latitude : 41.663670652<br>                     Longitude : -87.540935513<br>                     frequency : 1<br></div>`)[0];
            popup_1dfd1f1b32064d218106ff1b6ef2ae52.setContent(html_bed154e77b444951b960ee5d0adfbd34);
        

        circle_marker_659b5e9bfd264da28b3d72634e173f5f.bindPopup(popup_1dfd1f1b32064d218106ff1b6ef2ae52)
        ;

        
    
    
            var circle_marker_415853b72d5645e28379f384a7b7c5fa = L.circleMarker(
                [41.707311449, -87.534902901],
                {"bubblingMouseEvents": true, "color": "yellow", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "yellow", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 0.007142857142857143, "stroke": true, "weight": 3}
            ).addTo(map_66631b96769c4ebdb07c477e972011fb);
        
    
        var popup_5395e1b905494463a7f57efcae2a0e41 = L.popup({"maxWidth": "100%"});

        
            var html_2b7d7c500cf54262aa27a0ca4fd8fff8 = $(`<div id="html_2b7d7c500cf54262aa27a0ca4fd8fff8" style="width: 100.0%; height: 100.0%;">Latitude : 41.707311449<br>                     Longitude : -87.534902901<br>                     frequency : 2<br></div>`)[0];
            popup_5395e1b905494463a7f57efcae2a0e41.setContent(html_2b7d7c500cf54262aa27a0ca4fd8fff8);
        

        circle_marker_415853b72d5645e28379f384a7b7c5fa.bindPopup(popup_5395e1b905494463a7f57efcae2a0e41)
        ;

        
    
</script>
```
