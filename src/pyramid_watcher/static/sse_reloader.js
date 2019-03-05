const debug = true;

const source = new EventSource('/livereload');
console.log('Loaded EventSource script');

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
        console.log('Time to reload', data.last_modified);
        // last_modified = data.last_modified;
    }
}, false);
