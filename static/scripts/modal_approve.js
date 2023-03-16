$('.modal_delete').click(function(){
	// console.log("clicked")
	// console.log($(this).data('url'))
$.ajax({
	url:$(this).data('url'),
	success:function(self){
	$('.mymodal').html(self)
	}
})
})