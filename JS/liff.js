function initializeApp(data) {  //初始化LIFF
    var userid = data.context.userId;  //取得ID
}

function pushMsg(continent, country, town, jobs, job) {
    if (continent == '' || country == '' || town == '' || jobs == '' || job == '') {  //資料檢查
        alert('每個項目都必須輸入！');
        return;
    }
    var msg = "###";  //回傳訊息字串
    msg += continent + "/";
    msg += country + "/";
    msg += town + "/";
    msg += jobs + "/";
    msg += job;
    liff.sendMessages([  //推播訊息
        { type: 'text',
          text: msg
        }
    ])
        .then(() => {
            liff.closeWindow();  //關閉視窗
        });
}

$(document).ready(function () {
    liff.init(function (data) {  //初始化LIFF
        initializeApp(data);
    });
    
    $('#btn').click(function () {  //按下確定鈕
        pushMsg($("#continent-list :selected").text(), $("#country-list :selected").text(), $("#town-list :selected").text(), $("#job-main-list :selected").text(), $("#job-list :selected").text());
    });
});