// function pushMsg(continent, country, town, jobs, job) {
//     if (continent == '' || country == '' || town == '' || jobs == '' || job == '') {  //資料檢查
//         alert('每個項目都必須輸入！');
//         return;
//     }
//     var msg = "###";  //回傳訊息字串
//     msg += continent + "/";
//     msg += country + "/";
//     msg += town + "/";
//     msg += jobs + "/";
//     msg += job;
//     liff.sendMessages([  //推播訊息
//         {
//             type: 'text',
//             text: msg
//         }
//     ])
//         .then(() => {
//             liff.closeWindow();  //關閉視窗
//         });
// }
var liffID = '2000268560-PDBzXMGm'
$(document).ready(function () {
    liff.init({
        liffId: liffID
    }).then(function (data) {  //初始化LIFF
        console.log("LIFF Start")
        initializeApp(data);

        // $('#btn').click(function () {  //按下確定鈕
        //     pushMsg($("#continent-list :selected").text(), $("#country-list :selected").text(), $("#town-list :selected").text(), $("#job-main-list :selected").text(), $("#job-list :selected").text());
        // });
    });
});
