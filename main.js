$(document).ready(function() {

var margin = {top: 30, right: 20, bottom: 30, left: 50},
    width = 600 - margin.left - margin.right,
    height = 270 - margin.top - margin.bottom;
// Parse the date / time
var parseDate = d3.time.format("%d-%b-%y").parse;
// Set the ranges
var x = d3.scale.linear().range([0, width]);
var y = d3.scale.linear().range([height, 0]);
// Define the axes
var xAxis = d3.svg.axis().scale(x)
    .orient("bottom").ticks(5);
var yAxis = d3.svg.axis().scale(y)
    .orient("left").ticks(5);
// Define the line
var valueline = d3.svg.line()
    .x(function(d) { return x(d.acceleration); })
    .y(function(d) { return y(d.mpg); });
    
// Adds the svg canvas
var svg = d3.select("body")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", 
              "translate(" + margin.left + "," + margin.top + ")");
// Get the data
d3.csv("car.csv", function(error, data) {
   
   data.forEach(function(d) {
		d.acceleration = +d.acceleration;
        d.mpg = +d.mpg;
    });
    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.acceleration; }));
    y.domain([0, d3.max(data, function(d) { return d.mpg; })]);
    // Add the valueline path.
    svg.append("path")
        .attr("class", "line")
        .data(data);
    // Add the scatterplot
    svg.selectAll("dot")
        .data(data)
      .enter().append("circle")
        .attr("r", 3.5)
        .attr("cx", function(d) { return x(d.acceleration); })
        .attr("cy", function(d) { return y(d.mpg); });
    // Add the X Axis
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);
    // Add the Y Axis
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis);
});



d3.csv("car.csv", function(d) {
 return {
    mpg : d.mpg,
    cylinders : d.cylinders,
    displacement : d.displacement,
    horsepower : d.horsepower,
    weight : d.weight,
    acceleration : d.acceleration,
    model_year : d["model.year"],
    origin : d.origin
  };
}, function(dataset) {
	d = dataset;
	data  = dataset;
  	var select = document.getElementById("sel-x");
	var options = Object.keys(dataset[0])
	for(var i = 0; i < options.length-1; i++) {
    var opt = options[i];
    var el = document.createElement("option");
    el.textContent = opt;
    el.value = opt;
    select.appendChild(el);
    }
    
    var select2 = document.getElementById("sel-y");
	//var options = ["mpg",	"cylinders",	"displacement",	"horsepower",	"weight",	"acceleration",	"model.year"];
	for(var i = 0; i < options.length-1; i++) {
    var opt = options[i];
    var el = document.createElement("option");
    el.textContent = opt;
    el.value = opt;
    select2.appendChild(el);
	}
	
	

});
});

