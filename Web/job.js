$(document).ready(function () {
    //抓取json檔案
    $.getJSON("https://raw.githubusercontent.com/ChuanPien/LineBot_Updating/main/Crawler/job.json", function (data) {

        var job_mains = data['工作'];
        var inner = '<option value="#">#</option>';         //宣告一個空的值
        //將['工作']中所有內容依序加入inner中
        for (var i = 0; i < job_mains.length; i++) {
            inner = inner + '<option value=' + i + '>' + job_mains[i].text + '</option>';
        }
        //將inner值傳給html中id為job-main-list元素
        $("#job-main-list").html(inner)

        $("#job-main-list").change(function () {
            //如果[主類]是#，指派#給[細項]
            if ($("#job-main-list :selected").text() == '#'){
                $("#job-list").html('<option value="#">#</option>');
            }else{          //若不是，則抓取json資料
                var index = $("#job-main-list :selected").text();       //宣告index = (job-main-list)目前選的值的文字
                var jobs = data[index];                                 //抓取json中該值的資料放進jobs中
                var Sinner = "";                                        //宣告一個空的值
                //將(jobs)中所有內容依序加入Sinner中
                for (var i = 0; i < jobs.length; i++) {
                    Sinner = Sinner + '<option value=' + i + '>' + jobs[i].text + '</option>';
                }
                $("#job-list").html(Sinner);            //將Sinner值傳給html中id為job-list元素
                // $("#job-list").change();            //當[類別]更改時，Info也會及時更新
            }
            
        });

        /*
        $("#job-list").change(function () {
            // 設定頁面下方總結資訊文字，"selected"抓取目前所選的值
            var Info1 = '類別 : ' + $("#job-main-list :selected").text() + ' | ' + $("#job-main-list :selected").val() + '<br>'
            var Info2 = '職缺 : ' + $("#job-list :selected").text() + ' | ' + $("#job-list :selected").val()
            //將(Info1 + Info2)值傳給html中id為info-text元素
            $('#job-info-text').html(Info1 + Info2)
        });
        */

        //呼叫function
        $("#job-main-list").change();       
        // $("#job-list").change();
    });
});