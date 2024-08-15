require(["splunkjs/mvc/searchmanager","splunkjs/mvc","jquery","splunkjs/mvc/simplexml/ready!"], function(SearchManager,mvc,$) {


	console.log("Jetzt gehts los"); 


// Color the circles and return the absolute value
function einfarben(ID,wert){
	wert=parseInt(wert)
	$(ID).html(wert);

	if (wert>30){
		$(ID).prop("style","color: orange");
	}
	if (wert>100){
		$(ID).prop("style","color: red");
	}
	if (wert<=30){
		$(ID).prop("style","color: green");
	}	
}



// on click on chart, set token
$("#saege1").on("click", function() {
  	console.log("Auf Zahl saegewerk geklickt: "+$( this ).text() ); 
	var submittedTokens = mvc.Components.getInstance('submitted'); 
	submittedTokens.set('token_chart_maschine', "1"); 
	submittedTokens.unset('token_chart_lager'); 
});


// on click on chart, set token
$("#saege2").on("click", function() {
	console.log("Auf Zahl saegewerk geklickt: "+$( this ).text() ); 
  var submittedTokens = mvc.Components.getInstance('submitted'); 
  submittedTokens.set('token_chart_maschine', "1"); 
  submittedTokens.unset('token_chart_lager'); 
});


// on click on chart, set token
$("#saege3").on("click", function() {
	console.log("Auf Zahl saegewerk geklickt: "+$( this ).text() ); 
  var submittedTokens = mvc.Components.getInstance('submitted'); 
  submittedTokens.set('token_chart_maschine', "1"); 
  submittedTokens.unset('token_chart_lager'); 
});


$("#lagerzahl").on("click", function() {
	console.log("Auf Zahl saegewerk geklickt: "+$( this ).text() ); 
  var submittedTokens = mvc.Components.getInstance('submitted'); 
  submittedTokens.set('token_chart_lager', "1"); 
  submittedTokens.unset('token_chart_maschine'); 
});




// Seachmanager for SPL Searches
var standort_search = new SearchManager({
id: "standort_search_ID",
search: 'index=prozesskette| stats latest(Auftragsnummer) as Auftragsnummer by Prozessschritt| join Auftragsnummer [search index=auftrag | table Kunde, Holz, Produkt, Gewicht, AuftragsID, time |  stats values(*) as * by AuftragsID| rename AuftragsID as Auftragsnummer]| join Auftragsnummer [search index=auftrag |  stats sum(Umsatz) as Umsatz, sum(Gewicht) as Gewicht by AuftragsID| rename AuftragsID as Auftragsnummer]| table Prozessschritt,Kunde, Holz, Produkt, Gewicht, AuftragsID, time',
earliest_time:"-3m",
latest_time:"now"
});


var lager_search = new SearchManager({
	id: "search_lageranzahl",
	search: 'index="prozesskette" Prozessschritt=L* | table _time Prozessschritt Lager| sort  _time| stats latest(*) as * by Prozessschritt|  addcoltotals label=Summe labelfield=Prozessschritt',
	earliest_time:"-3m",
	latest_time:"now"
});


var standort_results = standort_search.data("preview");

standort_results.on("data", function() {

	console.log("Data (rows) 0: ", standort_results.data());

	// Holz für Sägen
	aktueller_stand_saege1=standort_results.data().rows[0][3]; // ALpha
	aktueller_stand_saege2=standort_results.data().rows[1][3]; // Beta
	aktueller_stand_saege3=standort_results.data().rows[6][3]; // Gamma
	$("#saege1").html(aktueller_stand_saege1);
	$("#saege2").html(aktueller_stand_saege2);
	$("#saege3").html(aktueller_stand_saege3);

	//Umsatz in Verpackung
	aktueller_stand_gewicht1=standort_results.data().rows[14][4];
	aktueller_stand_gewicht2=standort_results.data().rows[15][4];
	aktueller_stand_gewicht3=standort_results.data().rows[16][4];
	aktueller_stand_gewicht4=standort_results.data().rows[17][4];
	aktueller_stand_gewicht5=standort_results.data().rows[18][4];
	einfarben("#gewicht1",aktueller_stand_gewicht1)
	einfarben("#gewicht2",aktueller_stand_gewicht2)
	einfarben("#gewicht3",aktueller_stand_gewicht3)
	einfarben("#gewicht4",aktueller_stand_gewicht4)
	einfarben("#gewicht5",aktueller_stand_gewicht5)




});

var lager_results = lager_search.data("preview");
lager_results.on("data", function() {
	// change size of the blue bar
	var Total=lager_results.data().rows[4][1];
	console.log("Total",Total,lager_results.data())
	$("#lagerzahl").width(100+13*parseInt(Total));
	$("#lagerzahl").html(Total);

});

// Execute the Search all X seconds
var Total;
var index=0
interval=setInterval(function(){
	standort_search.startSearch()
	lager_search   .startSearch()

	index=index+1	
	if(index>10){clearInterval(interval);};
}, 10000);




});



