const url = new URL(window.location.href);
const urlParams = new URLSearchParams(url.search);
let searchInput = document.getElementById("search")

function onloadSearchActions() {
    searchInput.focus()
    if (urlParams.has("searchValue")) {
        searchInput.value = urlParams.get('searchValue');
        console.log(urlParams.get('searchValue'));
        searchInput.blur()
    }
}
function searchFormSubmit(searchValue) {
    url.searchParams.set("searchValue", searchValue);
    url.searchParams.set("currentPage", 1);
    window.history.replaceState({}, '', url.toString());
    location.reload()
}
function searchFunction(value) {

    if (value == "") {
        urlParams.delete("searchValue");
        url.search = urlParams.toString();
        window.history.replaceState({}, '', url.toString());
        location.reload()
    }

    if (typeof searchTimeout != 'undefined') {
        clearTimeout(searchTimeout)
    }

    searchTimeout = setTimeout(function () { searchFormSubmit(value) }, 1800)
}
