$(function()
{
$('.btnUSD').click(function(){
    alert("Pasando valores a Dolares");
    let arr = $('.Price');
    let clearArr = new Array();
    for(let i = 0;i<arr.length;i++){
        let price = $(arr[i]).html();
        price = price.replace('$','');
        price = price.replace('.','');
        clearArr.push(price);
    };
    $.getJSON('https://mindicador.cl/api', function(data) {
        let dailyIndicators = data;
        let vUSD = (dailyIndicators.dolar.valor);
        let arrNewValues = new Array();
        for(let i = 0;i<arr.length;i++){
            arrNewValues.push('$'+(parseInt(clearArr[i])*vUSD/1000000).toFixed(2));
            $('.Price').text(arrNewValues[i]);
            arr[i].classList.replace('Price','newPrice');
        }
        }).fail(function() {
        console.log('Error al consumir la API!');  
    });
})
$('.btnCLP').click(function(){
    alert("pasando valores a Pesos Chilenos")
    location.reload();
})

});


