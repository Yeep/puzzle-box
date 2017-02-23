function showGallery(path, element) {
    $.get('/api/directory/' + path)
        .done(function(data) {
            for (var i = 0, len = data.length; i < len; i++) {
                $("<img>", {
                    "src": "data:image/jpeg;base64," + data[i].data,
                    "alt": data[i].name
                }).appendTo(element);
            }
        });
}