$(document).ready(function () {
	
    function fontSize(o) {
    	
        var maximo = 17,
        	padrao = parseInt(o.css("fontSize"), 10),
        	atual = padrao;
        
        $('.fontMais').click(function() {
        	if (atual > maximo) return false;
            o.css("fontSize", ++atual);
        });
        
        $('.fontMenos').click(function(e) {
        	atual = padrao;
        	o.css("fontSize", atual);
        });

    };
	
    fontSize($(".layout-cell-pad-main div"));
    fontSize($(".layout-cell-pad-main p"));
    fontSize($(".layout-cell-pad-main li"));
    fontSize($(".layout-cell-pad-main span"));
    fontSize($(".layout-cell-pad-main a"));
	fontSize($(".layout-cell-pad-main td"));
	
});