require(["underscore","splunkjs/mvc/searchmanager",
"splunkjs/mvc","jquery",
"splunkjs/mvc/tableview","splunkjs/mvc/simplexml/ready!"], 
function(_,SearchManager,mvc,$,TableView) {


// Nur Zahlen erlauben mit bestimmten Grenzwerten----------------------------------------------------------------------------------------------------
$("#id_min_umsatz input").attr('type','number').attr("min",0)
$("#id_max_umsatz input").attr('type','number').attr("max",10000)




// Tabellenheader dymamisch mitziehen  --------------------------------------------------------------------------------------------------------------
$(window).scroll(function() {
var tablenames = ['auftragstabelle']; // Tablename
_.each(tablenames, // iterate over alle tables
	function (tablename) { 
		var table = $('#' + tablename + ' div.results-table');  // get full type name 
		var posTop = $(window).scrollTop(); // define distance
		if (typeof table.offset() !== 'undefined'){
		    var posTable = table.offset().top; // position of table at the top
		    var heightLastRow = table.find("table tr:last").height(); //

/*
			console.log("table",table)
			console.log("posTop",posTop)
			console.log("posTable",posTable)
			console.log("heightLastRow",heightLastRow)
*/
		    if (posTop > posTable && posTop < posTable + table.height() - heightLastRow) { // begin and end of the table has to be between the window
			table.find('thead > tr > th').css({
			    'position': 'relative',
			    'z-index': 11, // Priorität der Ebene
			    'top': posTop - posTable, // Position wo Header sein soll -
			});
		    } else {
			table.find('thead > tr > th').css({ 
			    'position': 'static',
			    'top': 0
			});
		    }
	}
});
});





// Spalte aus Tabelle unsichtbar machen ----------------------------------------------------------------------------------------------------
// Table drilldown
var table_drilldown = mvc.Components.getInstance("auftragstabelle");
table_drilldown.on("click", function(e) {
	console.log("Klick auf Tabelle")
	alert("Genaue Zeit:" + e.data["row._time"])
	})


// Hide table column
var CustomVisibleRenderer = TableView.BaseCellRenderer.extend({
	canRender: function(cell) { // define which cells you want to operate on
	    return _(['_time']).contains(cell.field);
	},

	render: function($td, cell) {  // what to do with the cells
	    $td.addClass('invisible-cell'); // add CSS Class to this cell
	    $td.text(cell.value); // write value in
	}
});

table_drilldown.getVisualization(function(tableView) {
	tableView.addCellRenderer(new CustomVisibleRenderer());
});







function handleAllOptionForMultipleInputs(inputs, defaultOptionValue) {
	_.each(inputs, function(inputWithAllOpt){
		var input = mvc.Components.getInstance(inputWithAllOpt);
		input.on("change", function(newValue){
			console.log(this.id + ": " + newValue + ", isArr: " + Array.isArray(newValue));
            // if no element is selected
			if (newValue.length === 0) {
				return;

            //if single values are selected; in other words, every element except All
			} else if (newValue.length > 1 && newValue.indexOf(defaultOptionValue) == 0) {
				newValue = newValue.filter(function(value){return value!=defaultOptionValue});

            //if the element 'All' is selected
			} else if (newValue.length > 1 && newValue.includes(defaultOptionValue)) {
				newValue = [defaultOptionValue];
			}

	    // send the newValue to the input
			this.val(newValue);
			if ($('#submit button').length !== 0) {
				FormUtils.handleValueChange(this);
			}
		});
	});
}
var inputsWithAllOpt = ["id_holz"];
handleAllOptionForMultipleInputs(inputsWithAllOpt, "*");


});



