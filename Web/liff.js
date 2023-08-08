function pushMsg(continent, country, town, jobs, job) {
    // if (continent == '' || country == '' || town == '' || jobs == '' || job == '') {  //資料檢查
    //     alert('每個項目都必須輸入！');
    //     return;
    // }
    var msg = "#/";  
    msg += continent + "/";
    msg += country + "/";
    msg += town + "/";
    msg += jobs + "/";
    msg += job;

    //回傳訊息字串
    liff.sendMessages([
        {
            type: 'text',
            text: msg
        }
    ])
        .then(() => {
            liff.closeWindow();
        })
        .catch((err) => {
            console.log('error', err);
        });
}

var liffID = '2000268560-PDBzXMGm'
$(document).ready(function () {
    liff.init({
        liffId: liffID
    }).then(function () {  //初始化LIFF
        var isInClient = liff.isInClient();
        if (!isInClient) {
            alert("請用line開啟此網頁呦~");
        } else {
            var context = liff.getContext();
            console.log(context);

            $('#btn').click(function () {  //按下確定鈕
                pushMsg($("#continent-list :selected").text(), $("#country-list :selected").text(), $("#town-list :selected").text(), $("#job-main-list :selected").text(), $("#job-list :selected").text());
            });
        }
    });
});
