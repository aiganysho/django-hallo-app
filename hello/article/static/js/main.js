async function makeRequest(url, method='GET') {
    let response = await fetch(url, {method});
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}


articleLike = async function(event){
    event.preventDefault()
    let a = event.currentTarget
    let url = a.getAttribute('href')
    try{
        let result = await makeRequest(url)
        let id = a.dataset.counter_article
        let p = document.getElementById(id)
        p.innerText = result
        let counter = document.getElementById(id)
        counter.innerText = result
        console.log(result);
        a.innerHTML = '<i class="fas fa-heart"></i>'
        a.onclick = articleUnlike
        a.setAttribute('href', url.replace('article_like', "article_unlike"))
    }
    catch (error){
        console.log(error)
    }
}


articleUnlike = async function(event){
    event.preventDefault()
    let a = event.currentTarget
    let url = a.getAttribute('href')
    try{
        let result = await makeRequest(url)
        let id = a.dataset.counter_article
        let p = document.getElementById(id)
        p.innerText = result
        let counter = document.getElementById(id)
        counter.innerText = result
        console.log(result);
        a.innerHTML = '<i class="far fa-heart"></i>'
        a.onclick = articleLike
        a.setAttribute('href', url.replace("article_unlike", 'article_like'))
    }
    catch (error){
        console.log(error)
    }
}



commentLike = async function(event){
    event.preventDefault()
    let a = event.currentTarget
    let url = a.getAttribute('href')
    try{
        let result = await makeRequest(url)
        let id = a.dataset.counter_comment
        let p = document.getElementById(id)
        p.innerText = result
        let counter = document.getElementById(id)
        counter.innerText = result
        console.log(result);
        a.innerHTML = '<i class="fas fa-heart"></i>'
        a.onclick = commentUnlike
        a.setAttribute('href', url.replace('comment_like', "comment_unlike"))
    }
    catch (error){
        console.log(error)
    }
}


commentUnlike = async function(event){
    event.preventDefault()
    let a = event.currentTarget
    let url = a.getAttribute('href')
    try{
        let result = await makeRequest(url)
        let id = a.dataset.counter_comment
        let p = document.getElementById(id)
        p.innerText = result
        let counter = document.getElementById(id)
        counter.innerText = result
        console.log(result);
        a.innerHTML = '<i class="far fa-heart"></i>'
        a.onclick = commentLike
        a.setAttribute('href', url.replace("comment_unlike", 'comment_like'))
    }
    catch (error){
        console.log(error)
    }
}








