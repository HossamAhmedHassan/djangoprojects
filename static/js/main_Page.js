function submitForm(formIndex) {
    var formId = 'form-' + formIndex;
    var form = document.getElementById(formId);
    form.submit();
}   

function onloadActions(currentPage, paginationLength) {
    let currentPageNumber = document.getElementById(currentPage)
    console.log("SAd");
    if (currentPageNumber != null) {
        currentPageNumber.classList.add("active")
    }

    if (currentPage == 1) {
        let previous_button = document.getElementById("previous")
        previous_button.classList.add("disabled")
    }
    if (currentPage == paginationLength || paginationLength == 0) {
        let next_button = document.getElementById("next")
        next_button.classList.add("disabled")
    }
    onloadSearchActions()
}

function pagination(chosenOption, currentPage) {
    const url = new URL(window.location.href);
    if (chosenOption == "next") {
        currentPage += 1
        url.searchParams.set("currentPage", currentPage);
    } else if (chosenOption == "previous") {
        currentPage -= 1
        url.searchParams.set("currentPage", currentPage);
    } else {
        url.searchParams.set("currentPage", chosenOption);
    }
    window.history.replaceState({}, '', url.toString());
    location.reload()
}   

