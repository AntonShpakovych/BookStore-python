function readMore(){
    const READ_MORE = 'Read More'
    const READ_LESS = 'Read Less'
   
    let link = document.getElementById('read_more')
    let full_description = document.getElementById('full_description')
    let short_description = document.getElementById('short_description')
    
    if (full_description.classList.contains('hidde')){
        full_description.classList.remove('hidde')
        short_description.classList.add('hidde')
        link.textContent = READ_LESS
    }
    else{
        full_description.classList.add('hidde')
        short_description.classList.remove('hidde')
        link.textContent = READ_MORE
    }
}
