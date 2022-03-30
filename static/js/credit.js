$(document).ready(function () {

    show_charge_history(1);
    show_use_history(1);
});

function show_d1() {
    $('#d1').show()
    $('#d2').hide()
    $('#d3').hide()
    $('#c1').hide()
    $('#c2').show()
    $('#c3').show()
}

function show_d2() {
    $('#d1').hide()
    $('#d2').show()
    $('#d3').hide()
    $('#c1').show()
    $('#c2').hide()
    $('#c3').show()

}

function show_d3() {
    $('#d1').hide()
    $('#d2').hide()
    $('#d3').show()
    $('#c1').show()
    $('#c2').show()
    $('#c3').hide()
}

function charge_point() {
    // $.ajax({
    //     type: post,
    //     url: "/api/v1/credit/charge",
    //     contentType: "application/json",
    //     success: function (response) {
    //         console.log(response)
    //     }})
    axios({
        url: "/api/v1/credit/charge",
        method: 'post'
    })
        .then(function (response) {
            alert(response['data']['msg'])
        })

}

function use_point() {
    axios({
        url: "/api/v1/credit/use",
        method: 'post',
        data: {'credit': 100}
    })
        .then(function (response) {
            alert(response['data']['msg'])
        })

}

function show_use_history(pageNum) {
    axios({
        url: "/api/v1/credit/use/history",
        method: 'post',
        data: {'page': pageNum}
    })
        .then(function (response) {
            use_data = response['data']['p']
            let t_page = response['data']["t"];
            for (let i = 0; i < use_data.length; i++) {

                let credit = use_data[i]['credit']
                let date_info = use_data[i]['credit_date']

                let date = new Date(date_info);
                let year = date.getFullYear();
                let month = date.getMonth() + 1;
                let day = date.getDay();
                let hours = date.getHours();
                let minutes = date.getMinutes();
                let seconds = date.getSeconds();
                let all_date = year + '년 ' + month + '월 ' + day + '일 ' + hours + '시 ' + minutes + '분 ' + seconds + '초'

                let temp_html = `
                            
                            <tr class="temp">
                            <td style="margin-right: 6vw">${all_date}</td>
                            <td style = "margin-right: 1vw">${credit}</td>
                    
                            </tr>
                            `

                $('#d3-3').append(temp_html);
            }
            for (let j = 0; j < t_page['total_page']; j++) {
                let num = j + 1;
                if (num === pageNum) {
                    let temp_html = ` <a style="color: red">${num}</a>`
                    $('#pagination_use').append(temp_html);
                }
            }
        })

}

function show_charge_history(pageNum) {
    axios({
        url: "/api/v1/credit/charge/history",
        method: 'post',
        data: {'page': pageNum}
    })
        .then(function (response) {
            use_data = response['data']['p']
            ;
            let t_page = response['data']["t"];

            for (let i = 0; i < use_data.length; i++) {

                let credit = use_data[i]['credit']
                let date_info = use_data[i]['credit_date']
                let date = new Date(date_info);
                let year = date.getFullYear();
                let month = date.getMonth() + 1;
                let day = date.getDay();
                let hours = date.getHours();
                let minutes = date.getMinutes();
                let seconds = date.getSeconds();
                let all_date = year + '년 ' + month + '월 ' + day + '일 ' + hours + '시 ' + minutes + '분 ' + seconds + '초'

                let temp_html = `
                            
                            <tr class="temp">
                            <td style="margin-right: 6vw">${all_date}</td>
                            <td style = "margin-right: 1vw">${credit}</td>

                            </tr>
                            `

                $('#d2-2').append(temp_html);
            }
            for (let j = 0; j < t_page['total_page']; j++) {
                let num = j + 1;
                if (num === pageNum) {
                    let temp_html = ` <a style="color: red">${num}</a>`
                    $('#pagination_charge').append(temp_html);
                }
            }

        })
}