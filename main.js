//Render  an  interactive scatterplot of  the data:
//– Dimensions   for  x-axis  and y-axis  can be  selected.
//– Filtering  on MPG is  supported.
//– Hovered car name  is  shown as  the h4  header.

$(document).ready(function() {

console.log(document.getElementById('sel-x'))
var draw = function(xKey, yKey) {
    

var xValue = function(d) { return d[xKey]; }, yValue = function(d) { return d[yKey]; };

var margin = {top: 30, right: 20, bottom: 60, left: 30},
    width = 400 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;
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
    .x(function(d) { return x(d[xKey]); })
    .y(function(d) { return y(d[yKey]); });
    
// Adds the svg canvas 
var canvas = d3.select(".plot")

    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", 
              "translate(" + margin.left + "," + margin.top + ")");

// add the tooltip area to the webpage
var tooltip = d3.select("#hovered").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

// Get the data
d3.csv("car.csv", function(error, data) {
   data.forEach(function(d) {

        // csv data are input one row at a time
        var key = Object.keys(d)
        for(var i = 0; i < key.length; i++) {
        // change string into number format
            if (!isNaN(d[key[i]])){
                d[key[i]] = +d[key[i]];
                }
        }

    });
    
    // Try to assign values to axis x and axis y
    var selx = document.getElementById("sel-x");
    console.log(data)
    var options = Object.keys(data[0])  
    for(var i = 1; i < options.length-1; i++) {
    var opt = options[i];
    var el = document.createElement("option");
    el.textContent = opt;
    el.value = opt;
    selx.appendChild(el);
    }
    
    var sely = document.getElementById("sel-y");
    for(var i = 1; i < options.length-1; i++) {
    var opt = options[i];
    var el = document.createElement("option");
    el.textContent = opt;
    el.value = opt;
    sely.appendChild(el);
    }

    // Scale the range of the data
    x.domain([d3.min(data, xValue)-10, d3.max(data, xValue)+10]);
    y.domain([d3.min(data, yValue)-5, d3.max(data, yValue)+5]);
    // Add the scatterplot
    var scatterplot = canvas.selectAll("dot").data(data);
    scatterplot.enter().append("circle")
        .attr("class", "dot")
        .attr("r", 3.5)
        .attr("cx", function(d) { return x(d[xKey]); })
        .attr("cy", function(d) { return y(d[yKey]); })
        .on("mouseover", function(d) {
          tooltip.transition()
               .duration(200)
               .style("opacity", .9);
          tooltip.html(d.name)
               .style("left", (d3.event.pageX + 5) + "px")
               .style("top", (d3.event.pageY - 28) + "px");
      })
      .on("mouseout", function(d) {
          tooltip.transition()
               .duration(500)
               .style("opacity", 0);
      });
    scatterplot.exit().remove();    
    // Add the X Axis
    canvas.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
      .append("text")
        .attr("class", "x label")
        .attr("x", width)
        .attr("y", -6)
        .style("text-anchor", "end")
        .text(xKey);
      
    // Add the Y Axis
    canvas.append("g")
        .attr("class", "y axis")
        .call(yAxis)
      .append("text") 
        .attr("class", "y label")
        .attr("x", 30)
        .attr("y", -6)
        .attr("transform", "rotate(90)")
        .style("text-anchor", "end")
        .text(yKey);
})
}

draw('displacement', 'mpg');
// var xKey = 'displacement', yKey = 'mpg';
// document.getElementById("sel-x").change(draw('mpg', 'displacement'));
var update = $("#update");
var mpg_min = $("#mpg-min");
var mpg_max = $("#mpg-max");

update.click(function(){    

    update.css('color','red');
    
    });


});




