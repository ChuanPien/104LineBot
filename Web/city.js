$(document).ready(function () {
    //抓取json檔案
    $.getJSON("https://raw.githubusercontent.com/ChuanPien/104LineBot/main/Crawler/city.json", function (data) {

        var continent = data['洲'];
        var inner = '<option value="#">#</option>';         //宣告一個空的值
        //將['洲']中所有內容依序加入inner中
        for (var i = 0; i < continent.length; i++) {
            inner = inner + '<option value=' + i + '>' + continent[i].text + '</option>';
        }
        //將inner值傳給html中id為continent-list元素
        $("#continent-list").html(inner)

        $("#continent-list").change(function () {
            //如果[洲]是#，指派#給[國家][區]
            if ($("#continent-list :selected").text() == '#') {
                $("#country-list").html('<option value="#">#</option>');
                $("#town-list").html('<option value="#">#</option>');
            } else {        //若不是，則抓取json資料
                var index = $("#continent-list :selected").text();       //宣告index = (continent-list)目前選的值的文字
                var country = data[index];                               //抓取json中該值的資料放進country中
                var cinner = "";                                        //宣告一個空的值
                //將(country)中所有內容依序加入cinner中
                for (var i = 0; i < country.length; i++) {
                    cinner = cinner + '<option value=' + i + '>' + country[i].text + '</option>';
                }
                $("#country-list").html(cinner);    //將cinner值傳給html中id為country-list元素
                $("#country-list").change();        //當[洲]更改時，國家也會及時更新
            }
        });

        $("#country-list").change(function () {
            var index = $("#country-list :selected").text();        //宣告index = (country-list)目前選的值的文字
            var town = data[index];                                 //抓取json中該值的資料放進town中
            var tinner = "";                                        //宣告一個空的值
            //將(town)中所有內容依序加入tinner中
            for (var i = 0; i < town.length; i++) {
                tinner = tinner + '<option value=' + i + '>' + town[i].text + '</option>';
            }
            $("#town-list").html(tinner);        //將tinner值傳給html中id為town-list元素
            // $("#town-list").change();            //當[國家]更改時，Info也會及時更新
        });

        /*
        $("#town-list").change(function () {
            // 設定頁面下方總結資訊文字，"selected"抓取目前所選的值
            var Info1 = '洲 : ' + $("#continent-list :selected").text() + ' | ' + $("#continent-list :selected").val() + '<br>'
            var Info2 = '國家 : ' + $("#country-list :selected").text() + ' | ' + $("#country-list :selected").val() + '<br>'
            var Info3 = '地區 : ' + $("#town-list :selected").text() + ' | ' + $("#town-list :selected").val()
            //將(Info1 + Info2)值傳給html中id為info-text元素
            $('#city-info-text').html(Info1 + Info2 + Info3)
        });
        */

        //呼叫function
        $("#continent-list").change();
    });
});