var MAP_WIDTH = 800;
var MAP_HEIGHT = 600;

/*var projection = d3.geo.albersUsa()
    .scale(1000)
    .translate([MAP_WIDTH / 2, MAP_HEIGHT	 / 2]);

var path = d3.geo.path()
    .projection(projection);
*/

var path = d3.geo.path();
var svg = d3.select("body").append("svg")
    .attr("width", MAP_WIDTH)
    .attr("height", MAP_HEIGHT);

d3.json("/resources/USCounties.json", function(error, topology) {
  if (error) throw error;
  svg.selectAll("path")
      .data(topojson.feature(topology, topology.objects.counties).features)
    .enter().append("path")
      .attr("d", path);

  d3.csv("/Housing Data/CountyMedianHousingPrices.csv", function) {
  	
  }
});