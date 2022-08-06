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

$("#date_id").change(function(){ getData(); });
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

let newData_idForm = $("#newData_id");
newData_id.addEventListener('paste', handlePaste);

function handlePaste (e) {
    e.preventDefault();
    let paste = (e.clipboardData ||
        window.clipboardData).getData('text');
    let newData = paste.trim().split(/[\t\n]/);
    let inputs = $(e.currentTarget).find("input[type=number]");
    if (inputs.length == newData.length){
        for (let i = 0; i < inputs.length; i++){
            inputs[i].value = newData[i];
        };
    }
};

function addNewData(){
    let newData = {};
    $("#newData_id").find("input[type=number]").each(function(){
        newData[$(this).attr("id")] = +($(this).val());
    });
    let date_id = $("#date_id");
    let dateNow = (new Date()).toLocaleDateString("ru")
    $(date_id).val(dateNow);
    newData['date'] = (new Date()).toISOString().slice(0,10);
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


