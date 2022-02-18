//# sourceURL=show_popup.js
/** 
 * specification for show/hide modal, which is divided into primary sections header, body and footer with dialog and content 
 */

define([
		"jquery"
	], function (
		$) {
            
	function showPopup(title, body, footer, popupId) {
        var modalId = 'myModal';
        if (popupId != null) {
            modalId = popupId;
        }
	    var popupElem=$('<div/>', {id: modalId,class: 'modal fade',tabindex: '-1',role: 'dialog','aria-labelledby': 'myModalLabel'});
	    var modalDialog=$('<div/>', {class: 'modal-dialog',role: 'document'}).appendTo(popupElem);
	    var modalContent=$('<div/>', {class: 'modal-content'}).appendTo(modalDialog);
	    var modalHeader=$('<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&amp;times;</span></button></div>').appendTo(modalContent);
	    var modalBody=$('<div/>', {class: 'modal-body', style: 'overflow: auto;'}).appendTo(modalContent);
	    var modalFooter=$('<div/>', {class: 'modal-footer'}).appendTo(modalContent);
	    if (title) {
	        $('<h4 class="modal-title" id="myModalLabel"></h4>').html(title).appendTo(modalHeader);
	    }
	    if (body) {
	        modalBody.html(body);
	    }
	    if (footer) {
	        modalFooter.html(footer);
	    }
	
	    popupElem.modal("show");
	    
	    popupElem.on('hidden', function () {
	        popupElem.remove();
	    });
	}
    
    return showPopup;
});
