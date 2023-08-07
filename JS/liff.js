function initializeApp(data) {  //初始化LIFF
    var userid = data.context.userId;  //取得ID
}

function pushMsg(pname, pdatatime, proom) {
    if (pname == '' || pdatatime == '' || proom == '') {  //資料檢查
        alert('每個項目都必須輸入！');
        return;
    }
    var msg = "###";  //回傳訊息字串
    msg = msg + pname + "/";
    msg = msg + amount + "/";
    msg = msg + pdatatime + "/";
    msg = msg + proom;
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
    
    $('#sure').click(function (e) {  //按下確定鈕
        pushMsg($('#name').val(), $('#datetime').val(), $('#sel_room').val());
    });
});