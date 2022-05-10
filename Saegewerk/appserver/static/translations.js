require(["underscore","splunkjs/mvc/searchmanager",
"splunkjs/mvc","jquery","splunk.i18n",
"splunkjs/mvc/tableview","splunkjs/mvc/simplexml/ready!"], 
function(_,SearchManager,mvc,$,i18n,TableView) {

// Create token namespaces
var defaultTokenModel = mvc.Components.getInstance('default');
var submittedTokenModel = mvc.Components.getInstance('submitted');

function setToken(name, value) {
	defaultTokenModel.set(name, value);
	submittedTokenModel.set(name, value);
}
// Token translation
	$.each(defaultTokenModel.attributes, function( key, value ) {
		if (key.match("^i18n_")) {  // finde alle Token die mit i18n_Anfangen
			setToken(key, i18n._(value)); //Überschreibe den Token mit der aktuellen übersetzung
			console.log("Übersetzung",key,i18n._(value))
	}
	});

});



