const debug = false;

const source = new EventSource('/livereload');

let last_modified;

const sse_lister = (evt) => {
    console.log('Received:', evt);
}

source.addEventListener('open', e => {
    if (debug) {
        console.log('opened');
    }
}, false);

source.addEventListener('error', e => {
    if (e.readyState === EventSource.CLOSED) {
        console.log('closed');
    }
}, false);

source.addEventListener('new_request', e => {
    const data = JSON.parse(e.data);
    if (data && data.last_modified) {
        // First time through, get and store the value, but don't reload.
        if (!last_modified) {
            last_modified = data.last_modified;
        } else {
            if (data.last_modified !== last_modified) {
                // We've done one pass through and things have
                // changed, so...let's reload.
                window.location.reload(true);
            }
        }
    }
}, false);
