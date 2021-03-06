// utility functions for open layers
"use strict";

function MapWrapper() {
	this.trainIcon = L.icon({
			iconUrl : '/static/common/img/open-train.png',
			iconSize : [26, 26]
		});
	this.createTrainMarker = function(stop) {
		var popup = L.marker([stop.lat, stop.lon],{
			icon : this.trainIcon
		}).addTo(this.map).bindPopup('(' + stop.seqId + ') ' + stop.name + " @" + stop.time);
		if (stop.stopId == this.zoomStopId) {
			popup.openPopup();
		}
	};
	this.createReportMarker = function(report) {
		var text = 'report'; 
		var popup = L.marker([report.lat, report.lon],{
			icon : this.trainIcon
		}).addTo(this.map).bindPopup(text);
	};
	this.createLine = function(shapes,options) {
		var polyline = L.polyline(shapes, options).addTo(this.map);
	};
}

function otCreateMap(mapDiv, options) {
	options = options || {};
	var map = L.map(mapDiv).setView([options.lat,options.lon], 13);
	L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
		maxZoom : 18,
		attribution : 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a>'
	}).addTo(map);
	var result = new MapWrapper();
	if (options.zoomStopId) {
		result.zoomStopId = options.zoomStopId;
	}
	result.map = map;
	return result;
}


