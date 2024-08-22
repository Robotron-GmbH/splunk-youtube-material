define([
            'jquery',
            'underscore',
            'api/SplunkVisualizationBase',
            'api/SplunkVisualizationUtils',
            'd3'
        ],
        function(
            $,
            _,
            SplunkVisualizationBase,
            SplunkVisualizationUtils,
            d3
        ) {
  
    return SplunkVisualizationBase.extend({
 
        initialize: function() {
            // Save this.$el for convenience
            this.$el = $(this.el);
             
            // Add a css selector class
            this.$el.addClass('kreis_prozess');
        },
 
        getInitialDataParams: function() {
            return ({
                outputMode: SplunkVisualizationBase.ROW_MAJOR_OUTPUT_MODE,
                count: 10000
            });
        },
  
        updateView: function(data, config) {
             
         	                  // Guard for empty data
					  if(data.rows.length < 1){
						return;
					}
					// Clear the div
					this.$el.empty();
					
					// Farbe des Hauptkreises
					var mainColor =
					config[this.getPropertyNamespaceInfo().propertyNamespace + 'mainColor'] || '#f7bc38'
					
					// Radius einstellen
					var radius = 
					parseFloat(config[this.getPropertyNamespaceInfo().propertyNamespace + 'radius']) || 75;
					
					// Set height and width
					var height = 300;
					var width = 1200;
					var abstand_kreise=240;
					 
					// SVG setup
					var svg  = d3.select(this.el).append('svg')
						.attr('width', width)
						.attr('height', height)
						.style('background', 'white')
						.append('g')
		
		
							
				svg.selectAll("circle")
				.data(data.rows)
				.enter()
				.append("circle")
					.attr("cx", function(d,i) { return radius + parseFloat(i)*abstand_kreise; })
					.attr("cy", radius)
					.attr("r", radius)
					.style('fill', mainColor);
				
				svg.selectAll("datum")
				.data(data.rows)
				.enter()
					.append("text")					
					.text(function(d,i) { return (d[0]); })
					.attr("x", function(d,i) { return (radius+parseFloat(i)*abstand_kreise); })
					.attr("y", radius)
					.attr('class', 'meter-center-text')
					.style("font-size", "25px")
					.style('text-anchor', 'middle')
					.attr("dominant-baseline", "central");
				
				svg.selectAll("standort")
				.data(data.rows)
				.enter()
					.append("text")					
					.text(function(d,i) { return (d[1]); })
					.attr("x", function(d,i) { return (radius+parseFloat(i)*abstand_kreise); })
					.attr("y", 25+2*radius)
					.attr('class', 'meter-center-text')
					.attr('alignment-baseline','central')
					.style("font-size", "16px")
					.style('text-anchor', 'middle');
		   
					
					svg.selectAll("circle_2")
					.data(data.rows)
					.enter()
					.append("circle")
						.attr("cx", function(d,i) { return (radius-abstand_kreise/2+parseFloat(i)*abstand_kreise);})
						.attr("cy", radius)
						.attr("r", (-2*radius+abstand_kreise)/2)
						.style('fill', "#22db67");


					svg.selectAll("zeitdauer")
					.data(data.rows)
					.enter()
						.append("text")					
						.text(function(d,i) { return (parseInt(d[2])); })
						.attr("x", function(d,i) { return (radius-abstand_kreise/2+parseFloat(i)*abstand_kreise); })
						.attr("y", radius)
						.attr('class', 'meter-center-text')
						.attr('alignment-baseline','central')
						.style("font-size", "20px")
						.style('text-anchor', 'middle');



        }
    });
});
