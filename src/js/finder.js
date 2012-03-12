$(function() {
    $(".nutrient-range-finder").each(function(idx, elem) {
	var minText = $(".left-text",elem);
	var minVal = minText.val();
	var unit = minVal.split(" ")[1];
	var minVal = parseFloat(minVal.split(" ")[0]);
	var maxText = $(".right-text",elem);
	var maxVal = parseFloat(maxText.val().split(" ")[0]);
	$(".data-finder",elem).slider({
	    range:true,
	    min: 0,
	    max: 400,
	    values: [0,400],
	    slide: function(event, ui) {
		minText.val(""+(ui.values[0]/400.0*maxVal).toFixed(2)+" "+unit);
		maxText.val(""+(ui.values[1]/400.0*maxVal).toFixed(2)+" "+unit);
	    }
	});
    });
});