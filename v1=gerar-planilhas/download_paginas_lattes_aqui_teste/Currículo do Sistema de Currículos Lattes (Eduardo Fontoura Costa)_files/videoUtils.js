function mostrarPreviaVideo(video_link){
	
	if (video_link != null && video_link != ''){
		
		if (video_link.toUpperCase().indexOf("HTTP") < 0){
			video_link = "http://" + video_link;
		}
		
		window.open(video_link, '_blank');
		return;
	}
	
}