function lock() {
    $.post('/api/box/lock')
}

function unlock() {
    $.post('/api/box/unlock')
}