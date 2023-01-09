function deleteAccount(element){
    let button = document.getElementById('delete_account')

    const DISABLED_BUTTON_CLASS = ['btn', 'disabled', 'mb-20']
    const NOT_DISABLED_BUTTON_CLASS = ['btn', 'btn-default', 'mb-35']

    if (element.checked){
        button.classList.remove(...DISABLED_BUTTON_CLASS)
        button.classList.add(...NOT_DISABLED_BUTTON_CLASS)
    }
    else{
        button.classList.remove(...NOT_DISABLED_BUTTON_CLASS)
        button.classList.add(...DISABLED_BUTTON_CLASS)
    }
    console.log(button)
}
