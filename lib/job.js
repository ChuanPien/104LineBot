// 定義 fetchJSONData 函式來從 JSON 檔案獲取數據
function fetchJSONData(jsonFilePath, callback) {
    fetch(jsonFilePath)
        .then((response) => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then((data) => {
            if (!data) {
                throw new Error('JSON data is undefined');
            }
            callback(data);
        })
        .catch((error) => console.error('Fetch Error:', error));
}

// 定義 generateSelectOptions 函式來動態生成下拉菜單選項
function generateSelectOptions(selectElement, jsonData) {
    // 確保 jsonData 不為未定義
    if (!jsonData) {
        return;
    }

    // 清空下拉選項
    selectElement.innerHTML = '';

    // 動態生成下拉選項
    jsonData.forEach((optionData) => {
        const optionElement = document.createElement('option');
        optionElement.value = optionData.value;
        optionElement.textContent = optionData.text;
        selectElement.appendChild(optionElement);
    });
}


// 定義 displaySelectedResult 函式來顯示選中的結果
function displaySelectedResult() {
    // 確保 options 有選項
    const selectOptions = document.getElementById('selectOptions');
    if (selectOptions.options.length === 0) {
        return;
    }

    // 確保 selectedIndex 在 options 的範圍內
    const selectedIndex = selectOptions.selectedIndex;
    if (selectedIndex < 0 || selectedIndex >= selectOptions.options.length) {
        return;
    }

    // 獲取選中的選項文本
    const selectedOption = selectOptions.value;
    const selectedText = selectOptions.options[selectedIndex].text;

    // 在頁面上顯示選中的選項文本
    const selectedResult = document.getElementById('selectedResult');
    selectedResult.textContent = `你选择了选项 ${selectedText}`;
}


// 確保程式碼在 DOM 載入完成後運行
document.addEventListener('DOMContentLoaded', function () {
    // 初始化時生成第一個下拉菜單的選項
    const selectCategory = document.getElementById('selectCategory');
    fetchJSONData('http://localhost:3000/data', (data) => {
        generateSelectOptions(selectCategory, data["工作"]);
    });

    // 添加事件監聽器來捕獲第一個下拉菜單的變化
    selectCategory.addEventListener('change', (event) => {
        const selectedCategory = event.target.value;
        const selectOptions = document.getElementById('selectOptions');

        fetchJSONData('http://localhost:3000/data', (data) => {
            const options = data[selectedCategory];
            generateSelectOptions(selectOptions, options); // 動態生成第二個下拉菜單的選項
            displaySelectedResult(); // 更新顯示選中結果
        });
    });

    // 初始化時生成第二個下拉菜單的選項
    const selectOptions = document.getElementById('selectOptions');
    fetchJSONData('http://localhost:3000/data', (data) => {
        const initialCategory = selectCategory.value;
        const initialOptions = data[initialCategory];
        generateSelectOptions(selectOptions, initialOptions);
    });

    // 初始化時顯示預設選項的結果
    displaySelectedResult();
});
