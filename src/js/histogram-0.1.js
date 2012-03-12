/* -*- espresso-indent-level: 2; -*- */
/*
 * The Histogram UI plugin takes a div element and creates within it a range
 * finder with max and min values, and generates a histogram to display a
 * high-level overview of the data being selected.
 *
 * Dependencies: UI Slider
 *
 * Options:
 *   bins (Optional): The number of bins to create for the histogram. Defaults to 10.
 *   data (Required): An array of values used to build the histogram.
 *   enabled (Optional): A boolean indicating whether the histogram should respond to user input. Defaults to true.
 *   label (Optional): A label to include with the histogram. Defaults to null.
 *   select (Optional): A callback that takes event and ui for retrieving information about the selection event
 *   snap (Optional): Indicates whether the range selectors should snap to the edge of the histogram bars. Defaults to false.
 *   unit (Optional): A unit label to be included in the text boxes for measured data. Defaults to null.
 *
 * Methods:
 *   bin(index): Returns the div representing a specific bin
 *   value(bound, [value]): Returns the current value of the bound (0 = left, 1 = right) or, if value is present, will set the value of the bound.
 */
(function($) {
  
  // A dictionary of method names and methods that represent the functional
  // component of the histogram widget
  var methods = {
    // Initialization method to turn a DOM element into a histogram widget
    init: function(options) {
      // Settings object to store some state information
      var settings = {
	'bins': 10,
	'data': null,
	'label': null,
	'enabled': true,
	'select': null,
	'snap': false,
	'unit': null
      };

      // Augment the existing settings with the passed options
      if(options) {
	$.extend(settings,options);
      }

      // Make sure we have data
      if(settings.data==null) {
	$.error("No data passed to histogram.");
      }

      // Build the histogram object
      this.addClass("ui-histogram");
      var bins = [];
      for(var i=0;i<settings.bins;i++)
	bins.push(new Array());
      var min=settings.data[0];
      var max=settings.data[0];
      for(var i=1;i<settings.data.length;i++) {
	if(min>settings.data[i]) min = settings.data[i];
	if(max<settings.data[i]) max = settings.data[i];
      }
      max++;
      var delta = max-min;
      for(var i=0;i<settings.data.length;i++) {
	var v = settings.bins*(settings.data[i]-min)/delta;
	bins[Math.floor(v)].push(settings.data[i]);
      }
      if(settings.label) {
	this.append("<span class=\"label\">"+settings.label+"</span>");
      }
      this.append("<input class=\"left-text\" type=\"text\" value=\""+min+(settings.unit ? " "+settings.unit : "")+"\" />");
      var gram = this.append("<div></div>").find("div");
      this.append("<input class=\"right-text\" type=\"text\" value=\""+max+(settings.unit ? " "+settings.unit : "")+"\" />");
      var maxHeight=0;
      for(var i=0;i<bins.length;i++) {
	var height = Math.floor(100*bins[i].length/settings.data.length);
	if(maxHeight < height) maxHeight = height;
      }
      for(var i=0;i<bins.length;i++) {
	var height = Math.floor(100*bins[i].length/settings.data.length);
	if(height==0 && bins[i].length > 0)
	  height = 1;
	var left = Math.floor(100*i/bins.length);
	var next;
	if(i<bins.length-1) {
	  next = Math.floor(100*(i+1)/bins.length);
	}
	else {
	  next = 100;
	}
	gram.append("<div class=\"ui-histogram-bin\" style=\"left: "+left+"%; height: "+Math.floor(height/maxHeight*100)+"%; width: "+(next-left)+"%;\"></div>");
      }
      var $this = $(this);
      this.data('histogram',{'settings':settings,'min':min,'max':max});
      var left = this.find(".left-text");
      var right = this.find(".right-text");
      var opts = {
	'range':true,
	'min':min,
	'max':max,
	'values':[min,max],
	'slide': function(event, ui) {
	  left.val(ui.values[0]+(settings.unit ? " "+settings.unit : ""));
	  right.val(ui.values[1]+(settings.unit ? " "+settings.unit : ""));
	  if(settings.select)
	    settings.select(event, ui);
	}
      };
      if(settings.snap) {
	opts.step = (max-min)/settings.bins;
      }
      gram.slider(opts);
      left.change(function(e) {
	var x = parseFloat(left.val());
	if(x==NaN) {
	  x = 0;
	}
	else if(x > parseFloat(right.val())) {
	  x = parseFloat(right.val());
	}
	gram.slider('values',0,x);
	left.val(gram.slider('values',0)+(settings.unit ? " "+settings.unit : ""));
      });
      right.change(function(e) {
	var x = parseFloat(right.val());
	if(x==NaN) {
	  x = 0;
	}
	else if(x < parseFloat(left.val())) {
	  x = parseFloat(left.val());
	}
	gram.slider('values',1,x);
	right.val(gram.slider('values',1)+(settings.unit ? " "+settings.unit : ""));
      });
      return this;
    },

    // Returns the DOM element for a particular bin number as a jQuery object
    bin: function(num) {
      var items = this.find(".ui-histogram-bin");
      return items.eq(num);
    },

    // The value method takes a which and optional value parameter
    // It gets the value of the handle specified by which if there is no
    // value, otherwise it sets the position of the handle to value
    value: function(which, value) {
      if(!value) {
	return this.find(".ui-slider").first().slider('values',which);
      }
      else {
	var settings = this.data('histogram').settings;
	this.find("div").first().slider('values',which,value);
	var item;
	if(which == 0) {
	  item = this.find("input").eq(0);
	}
	else if(which == 1) {
	  item = this.find("input").eq(1);
	}
	item.val(value+(settings.unit ? " "+settings.unit : ""));
      }
    }
  };

  // Configure the histogram plugin for jQuery
  $.fn.histogram = function(method) {
    // Test if the method is a known method
    if(methods[method]) {
      // Apply the method using the remaining arguments
      return methods[method].apply(this,
				   Array.prototype.slice.call(arguments, 1));
    }
    // Check if the method is really an object. If so, call the init method.
    else if(typeof method === 'object' || !method) {
      return methods.init.apply(this, arguments);
    }
    // Some error in the calling code, abort.
    else {
      $.error("Method "+method+" does not exist on jQuery.histogram");
    }
  };
})( jQuery );
