const ajax = (options) => {
    let { type = 'GET', url, data, success = () => {}, error = () => {} } = options
    const xhr = new XMLHttpRequest()
    let params = ''
    const paramsArr = []
    for (key in data) {
        value = data[key]
        paramsArr.push(`${key}=${value}`)
    }
    if (paramsArr.length) {
        params = `?${paramsArr.join('&')}`
    }
    if (type === 'GET') {
        url += params
    }
    xhr.open(type, url)
    if (type === 'POST') {
        xhr.setRequestHeader('Content-Type', 'application/json;charset=utf-8')
        xhr.send(JSON.stringify(data))
    }
    if (type === 'GET') {
        xhr.send()
    }
    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
            if(xhr.status === 200) {
                console.log(xhr.responseText)
                success && success(xhr.responseText)
            } else {
                error && error(xhr.status)
            }
        }
    }
    xhr.onerror = () => {
        error && error(xhr.status)
    }
}

ajax({
    // type: 'GET',
    url: 'http://httpbin.org/get',
    data: {
        username: 'admin',
        password: '123'
    },
    // success: function (res) {
    //     alert(res)
    // },
})

ajax({
    type: 'POST',
    url: 'http://httpbin.org/post',
    data: {
        username: 'admin',
        password: '123'
    }
})