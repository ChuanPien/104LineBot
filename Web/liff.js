function pushMsg(continent, country, town, jobs, job, pay, exp) {
    //如果是空的就放入"#"
    if (pay != '') {
        pay = '#';
    }
    if (exp != '') {
        exp = '#';
    }

    //將所有字串加在一起並加上逗號便於之後分割
    var msg = "##,";  
    msg += continent + ",";
    msg += country + ",";
    msg += town + ",";
    msg += jobs + ",";
    msg += job + ",";
    msg += pay + ",";
    msg += exp;

    //回傳訊息字串
    liff.sendMessages([
        {
            type: 'text',
            text: msg
        }
    ])
        //傳完後關閉網頁
        .then(() => {
            liff.closeWindow();
        })
        .catch((err) => {
            console.log('error', err);
        });
}

//初始化LIFF
var liffID = '2000268560-PDBzXMGm'
$(document).ready(function () {
    liff.init({
        liffId: liffID
    }).then(function () {
        //檢查是否適用line開始網頁
        var isInClient = liff.isInClient();
        if (!isInClient) {
            alert("請用line開啟此網頁呦~");
        } else {
            var context = liff.getContext();
            console.log(context);

            $('#btn-send').click(function () {  //按下確定鈕
                //抓取全部資料
                pushMsg(
                    $("#continent-list :selected").text(),
                    $("#country-list :selected").text(),
                    $("#town-list :selected").text(),
                    $("#job-main-list :selected").text(),
                    $("#job-list :selected").text(),
                    $("#pay").text(),
                    $("#exp").text()
                );
            });
        }
    });
});
