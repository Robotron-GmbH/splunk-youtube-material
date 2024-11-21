//# sourceURL=online_help.js
/**
 * Functions for Online help messages as a popup regarding specific types of areas to be described
 */
define([
    "splunkjs/mvc",
    "../../app/Saegewerk/show_popup",
    "splunk.i18n",
    "jquery"
], function (
    mvc,
    showPopup,
    i18n,
    $) {
        
    var defaultTokenModel = mvc.Components.getInstance('default');
    var i18n_help = i18n._("Help");

    function online_help(dashboard_name) {
        var icon = '<svg xmlns="http://www.w3.org/2000/svg" style="width:16px;height:16px;fill:#999999" viewBox="0 0 32 32"><path d="M 16 4 C 9.3844277 4 4 9.3844277 4 16 C 4 22.615572 9.3844277 28 16 28 C 22.615572 28 28 22.615572 28 16 C 28 9.3844277 22.615572 4 16 4 z M 16 6 C 21.534692 6 26 10.465308 26 16 C 26 21.534692 21.534692 26 16 26 C 10.465308 26 6 21.534692 6 16 C 6 10.465308 10.465308 6 16 6 z M 16 10 C 13.802666 10 12 11.802666 12 14 L 14 14 C 14 12.883334 14.883334 12 16 12 C 17.116666 12 18 12.883334 18 14 C 18 14.767423 17.508714 15.44544 16.78125 15.6875 L 16.375 15.8125 C 15.559939 16.083523 15 16.862393 15 17.71875 L 15 19 L 17 19 L 17 17.71875 L 17.40625 17.59375 C 18.944786 17.08181 20 15.620577 20 14 C 20 11.802666 18.197334 10 16 10 z M 15 20 L 15 22 L 17 22 L 17 20 L 15 20 z" overflow="visible"></path></svg>';
        var icon_table = '<svg xmlns="http://www.w3.org/2000/svg" style="width:16px;height:16px;fill:#c6ecb8" viewBox="0 0 32 32"><path d="M 16 4 C 9.3844277 4 4 9.3844277 4 16 C 4 22.615572 9.3844277 28 16 28 C 22.615572 28 28 22.615572 28 16 C 28 9.3844277 22.615572 4 16 4 z M 16 6 C 21.534692 6 26 10.465308 26 16 C 26 21.534692 21.534692 26 16 26 C 10.465308 26 6 21.534692 6 16 C 6 10.465308 10.465308 6 16 6 z M 16 10 C 13.802666 10 12 11.802666 12 14 L 14 14 C 14 12.883334 14.883334 12 16 12 C 17.116666 12 18 12.883334 18 14 C 18 14.767423 17.508714 15.44544 16.78125 15.6875 L 16.375 15.8125 C 15.559939 16.083523 15 16.862393 15 17.71875 L 15 19 L 17 19 L 17 17.71875 L 17.40625 17.59375 C 18.944786 17.08181 20 15.620577 20 14 C 20 11.802666 18.197334 10 16 10 z M 15 20 L 15 22 L 17 22 L 17 20 L 15 20 z" overflow="visible"></path></svg>';
        var oh_results;
        var service = mvc.createService();

        function appendListener(selector, helptext) {
            $(selector).on('click', function () {
                showPopup(i18n_help, helptext, '<button class="btn btn-default" data-dismiss="modal">OK</button>');
            });
        };
        // Creates a oneshot search - This mode returns the results of the search once completed
        service.oneshotSearch("| inputlookup online_help.csv | search Dashboard=" + dashboard_name, {
            output_mode: "JSON"
        }, function (err, results) {
            if (err) {
                console.error(err)
            } else {
                setTimeout(function () {
                    oh_results=results;
                    for (var i = 0; i < results.results.length; i++) {
                        ID = results.results[i].ID; // test, test2
                        hilfetext_header = ((defaultTokenModel.get("env:locale") !== undefined) ? defaultTokenModel.get("env:locale") : '');
                        console.log("Hilfetextheader",defaultTokenModel.get("locale_i18n"))
                        Hilfetext = results.results[i]["Hilfetext" + hilfetext_header]; // test, test2
                        Type = results.results[i].Type;
                        if ((Type === "Input") && ID && Hilfetext && Type) {
                            help = ID + "_help";
                            Jqid = "#" + ID;
                            var selector = $("<span id='" + help + "' class='online_help_icon'><a>" + icon + "</a></span>").appendTo(Jqid + " label");
                            appendListener(selector, Hilfetext);
                        } else 
                        if ((Type === "Dashboard") && ID && Hilfetext && Type) {
                            help = ID + "_help";
                            Jqid = "#" + ID;
                            var selector = $("<span id='" + help + "' class='online_help_icon'><sup><a>" + icon + "</a></sup></span>").appendTo("h2.dashboard-title");
                            appendListener(selector, Hilfetext);
                        } else 
                        if ((Type === "Button") && ID && Hilfetext && Type) {
                            help = ID + "_help";
                            Jqid = "#" + ID;
                            var selector = $("<span id='" + help + "' class='online_help_icon'><sup><a>" + icon + "</a></sup></span>").insertAfter(Jqid);
                            appendListener(selector, Hilfetext);
                        } else 
                        if ((Type === "Button_Right") && ID && Hilfetext && Type) {
                            help = ID + "_help";
                            Jqid = "#" + ID;
                            var selector = $("<span id='" + help + "' class='online_help_icon' style='float:right'><sup><a>" + icon + "</a></sup></span>").insertBefore(Jqid);
                            appendListener(selector, Hilfetext);
                        } else 
                        if ((Type === "Element") && ID && Hilfetext && Type) {
                            help = ID + "_help";
                            Jqid = "#" + ID;
                            var selector = $("<span id='" + help + "' class='online_help_icon'><a>" + icon + "</a></span>").appendTo(Jqid + " .panel-head h3");
                            appendListener(selector, Hilfetext);
                        } else 
                        if ((Type === "HTML-Element") && ID && Hilfetext && Type) {
                            help = ID + "_help";
                            Jqid = "#" + ID;
                            var selector = $("<span id='" + help + "' class='online_help_icon'><a>" + icon + "</a></span>").appendTo(Jqid + " .panel-body h3");
                            appendListener(selector, Hilfetext);
                        } else 
                        if ((Type === "Timezone") && ID && Hilfetext && Type) {
                            help = ID + "_help";
                            Jqid = "#" + ID;
                            service.oneshotSearch('| makeresults | eval timezone=strftime(now(), "%Z (%z)") | table timezone', {
                                output_mode: "JSON"
                            }, function (err, results) {
                                if (err) {
                                    console.error(err)
                                } else  {
                                    Hilfetext = Hilfetext + " " + results.results[0].timezone
                                    var selector = $("<span id='" + help + "' class='online_help_icon'><a>" + icon + "</a></span>").appendTo(Jqid + " label");
                                    appendListener(selector, Hilfetext);
                                }
                            });
                        }
                    }
                }, 3000);
            }
        });
        var help={
            setNewHelp:function(id){
                for(var i=0;i<oh_results.results.length;i++){
                    if(oh_results.results[i].ID===id){
                        help = id + "_help";
                        Jqid = "#" + id;
                        var selector = $("<span id='" + help + "' class='online_help_icon'><a>" + icon_table + "</a></span>").appendTo(Jqid);
                        appendListener(selector, Hilfetext);
                        break;
                    }
                } 
            }
        };

        return help;
    }

    return online_help;

});
