var xmlHTTP = new XMLHttpRequest();

function showRelated(){
	var myCSRF = getCookie('csrftoken');

	searchText = document.getElementById('search').value;
    if(searchText != undefined){
	   if(searchText.length >= 2){
            xmlHTTP.open("POST", 'http://localhost:8000/AJAX', true);
	        xmlHTTP.setRequestHeader("X-CSRFToken", myCSRF);
	        xmlHTTP.onreadystatechange = function() {
    	       if (this.readyState == 4 && this.status == 200) {
                document.getElementById('searchBox').innerHTML = '';
      		    document.getElementById('searchBox').innerHTML = this.responseText;
      	       }
  	        };
	        xmlHTTP.send(searchText);
        }else{
        document.getElementById('searchBox').innerHTML = '';
        }
    }
}

function addCart(itemName){
	var cartCookie = getCookie('carro');
	var q = document.getElementById('cart_quantity').value;

	cartCookie = cartCookie + itemName + '|' + q + '|';
	console.log(cartCookie);
	document.cookie = 'carro=' + cartCookie + ";path=/";
}

function getCookie(cookieName){
	var name = cookieName + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i < ca.length; i++){
        var c = ca[i];
        while (c.charAt(0) == ' '){
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0){
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function eraseProd(item){
    var cartCookie = getCookie('carro');

    console.log(cartCookie)
    cartCookie = cartCookie.split('|');
    for (i = 0; i < cartCookie.length; i++){
        if( cartCookie[i] === item){
            cartCookie.splice(i,2);
            break;
        }
    }
    cartCookie = cartCookie.join('|');
    document.cookie = 'carro=' + cartCookie + ";path=/";
    updateTable();
}

function updateTable(){
    var myCSRF = getCookie('csrftoken');

    xmlHTTP.open("POST", 'http://localhost:8000/cart/see/', true);
    xmlHTTP.setRequestHeader("X-CSRFToken", myCSRF);
    xmlHTTP.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            cleanTable();
            createNewTable(JSON.parse(this.responseText));
        }
    };
    xmlHTTP.send('update');
}

function cleanTable(){
    var myTable = document.getElementById('myTable');
    var tableLength = document.getElementById('myTable').rows.length;

    for (i = tableLength; i > 1; i--){
        myTable.deleteRow(1);
    }
}

function createNewTable(myMatrix){
    var myTable = document.getElementById('myTable');
    var r_matrix = myMatrix['matrix'];
		var t_price = myMatrix['total_p'];


    for (i = 0; i < r_matrix.length; i++){

        var row = myTable.insertRow(i + 1);
        row.insertCell(0).innerHTML = '<img src="/static/img/' + r_matrix[i][0] + '.jpg "' + "class='p_image'>" + '<p>' + r_matrix[i][0] + '</p>';
        row.insertCell(1).innerHTML = r_matrix[i][1] + '€';
        row.insertCell(2).innerHTML = r_matrix[i][2];
		row.insertCell(3).innerHTML = r_matrix[i][1] * r_matrix[i][2] + '€';
        row.insertCell(4).innerHTML = "<button onclick=" + 'eraseProd("'  + r_matrix[i][0].replace(new RegExp(" ", 'g'), "-") + '");' +  '>' +
                    '<img src="/static/img/trash.png" '  +  'style="width: 20px; height: 20px;" /></button>';
    }
		var last_row = myTable.insertRow(r_matrix.length + 1);
		var cell = last_row.insertCell(0);
		cell.innerHTML = 'Total: ' + t_price + '€';
		cell.colSpan = 5;
}
