(function($){

$.citacoes = function(holder) {
	
	var citacao = {
		getCaminhoImagem:function(base) {
			var caminhoImg = "";
			if (base == 1){
				caminhoImg =  "images/v2/isi.gif";
			}else if( base == 2){
				caminhoImg =  "images/v2/scielo.png";
			}else if( base == 3){
				caminhoImg =  "images/v2/scopus.png";
			}
			return caminhoImg;
		},
		ajaxComplete:function() {
			holder.removeClass("citacoes").addClass("citado");
		},
		ajaxSuccess:function(data) {		
			if (data == null) return;
			
			var citacoes = data.citacoes;
			
			if (citacoes == null || citacoes.length == 0) {
				return;
			}
			
			var rotulo = $("<b />").addClass("label-citacoes").html("Citações:").appendTo(holder);
			
			$.each(citacoes, function(i, it){
				
				var anchorAttr = {
					href: it.url,
					target: "_blank",
					"class": "citacaoTip",
					"original-title": "Citações a partir de 1996"
				};
				
				var caminhoImg = citacao.getCaminhoImagem(it.base);
					
				var anchor = $("<a />").attr(anchorAttr);
				
				var imagem = $("<img />").attr("src",caminhoImg);
				
				var quantidadeCitacoes = $("<span class='numero-citacao' />").attr("data-tipo-ordenacao",it.base).html(it.qtd);
				
				imagem.appendTo(anchor);
				
				if (i > 0 ) {
					var separador = $("<span />").html("|").addClass("separador-citacoes");
					anchor.prepend(separador);
				}
				
				anchor.append(quantidadeCitacoes).appendTo(holder);
				
			});
			
			$('.citacaoTip').tipsy({gravity: 's'});
			
		},
		ajaxRequest:function() {
		
			$.ajax({
				type: "GET",
				dataType: "json",
				url: holder.attr("cvURI"),
				success: citacao.ajaxSuccess,
				complete: citacao.ajaxComplete
			});
		
		},
		init:function() {
			citacao.ajaxRequest();
		}
	};
	
	citacao.init();
	
};

$.fn.verificarCitacoes = function() {

	return this.each(function(index){
		var holder = $(this);
		$.citacoes(holder);
	});
	
};

})(jQuery);