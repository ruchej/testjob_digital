const newInputDataTMPL = `
<div class="col">
  <input id="{{id}}" type="number" step="0.01" class="form-control" placeholder="{{plh}}" data-el="plh">
</div>
`

const newRowDataTMPL = `
<div class="row g-3 mt-1 mb-1" data-type="table-row">
  {{col}}
</div>
`

function renderTemplate(tmpl, data){
   return tmpl.replace(/{{(\w+)}}/g, (match, part) => (part in data ? data[part] : part));
}

$(function() {
    $('#datepicker').datepicker( {
        defaultDate: new Date(),
        viewMode: 'month',
        format: 'dd.mm.yyyy',
    });
});

$("#datepicker").on('dp.hide', function (event) {
    setTimeout(function () {
        $("#datepicker").data('DateTimePicker').viewMode('months');
    }, 1);
});

// При изменении даты, обновим данные в таблице
$("#date_id").change(function(){ getData(); });

// Получим данные с сервера и обновим таблицы
function getData(){
    let date = $("#date_id").val().split(".");
    let month = date[1];
    let year = date[2];
    $.ajax({
        url: "/api/indicators/",
        method: "get",
        async: false,
        data: {
            year: year,
            month: month,
        },
        success: function(data){
            updateData(data.data);
            updateStatData(data.stats);
        }
    });
}
// Обновим основные данные в таблице
function updateData(data){
    let tableBody = $("#table_id").children("tbody");
    tableBody.children("tr").remove();
    for (let i = 0; i < data.length; i++){
        let row = `
 <tr role="row">
 <td>${data[i].fe}</td>
 <td>${data[i].si}</td>
 <td>${data[i].al}</td>
 <td>${data[i].ca}</td>
 <td>${data[i].s}</td>
 `
        tableBody.append(row);
    }
};

// Получаем объект формы с полями данных
let newData_idForm = $("#newData_id");
// Слушаем событие вставки из буфера обмена
newData_id.addEventListener('paste', handlePaste);
// Обработаем событие вставки из буфера обмена в нашу форму ввода данных
function handlePaste (e) {
    e.preventDefault();
    let paste = (e.clipboardData ||
        window.clipboardData).getData('text');
    let newData = paste.split("\n").map((e) => e.split("\t").map((e) => e.trim()));
    $(e.currentTarget).find("[data-type=table-row]").slice(1).remove()
    let rows = [];
    for (let i = 0; i < newData.length-1; i++){
        let cols = [];
        let elems = [
            {id: `fe_${i+2}`, plh: 'fe'},
            {id: `si_${i+2}`, plh: 'si'},
            {id: `al_${i+2}`, plh: 'al'},
            {id: `ca_${i+2}`, plh: 'ca'},
            {id: `s_${i+2}`, plh: 's'},
        ];
        for (j = 0; j < 5; j++){
            cols[j] = renderTemplate(newInputDataTMPL, elems[j]);
        };
        rows[i] = renderTemplate(newRowDataTMPL, {col: cols.join("\n")})
    };
    $(e.currentTarget).children("[data-type=table-row]").after(rows)
    let rowsInputs = $(e.currentTarget).find("[data-type=table-row]");
    for (let i = 0; i < rowsInputs.length; i++){
        let inputs = $(rowsInputs[i]).find("input[type=number]");
        for (let j = 0; j < inputs.length; j++){
            $(inputs[j]).val(newData[i][j])
        };
    };
};
// Отправим новые данные на сервер из формы добавления данных
function addNewData(){
    let date_id = $("#date_id");
    let dateNow = (new Date()).toLocaleDateString("ru")
    $(date_id).val(dateNow);

    let newData = [];
    let data = {};
    let rowsInputs = $("#newData_id").find("[data-type=table-row]");
    for (let i = 0; i < rowsInputs.length; i++){
        let inputs = $(rowsInputs[i]).find("input[type=number]");
        for (let j = 0; j < inputs.length; j++){
            data[$(inputs[j]).attr("data-el")] = +($(inputs[j]).val());
        };
        data['date'] = (new Date()).toISOString().slice(0,10);
        newData[i] = data;
    };
    $.ajax({
        url: "/api/indicators/",
        method: "post",
        async: false,
        data: newData,
        beforeSend: function (xhr) {
            xhr.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
        },
        success: function(){
            getData();
        }
    });
};

function updateStatData(data) {
    let statTable = $("#stattable_id").children("tbody");
    statTable.children("tr").remove();
    let row = `
 <tr role="row">
 <th scope="row">Мин</th>
 <td>${data.fe_min}</td>
 <td>${data.si_min}</td>
 <td>${data.al_min}</td>
 <td>${data.ca_min}</td>
 <td>${data.s_min}</td>
 <tr role="row">
 <th scope="row">Макс</th>
 <td>${data.fe_max}</td>
 <td>${data.si_max}</td>
 <td>${data.al_max}</td>
 <td>${data.ca_max}</td>
 <td>${data.s_max}</td>
 <tr role="row">
 <th scope="row">Сред</th>
 <td>${data.fe_avg}</td>
 <td>${data.si_avg}</td>
 <td>${data.al_avg}</td>
 <td>${data.ca_avg}</td>
 <td>${data.s_avg}</td>
 `
    statTable.append(row);
};


