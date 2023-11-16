function Open() {
	
	document.getElementById("navbar").style.display = "inline";
	Close_search()
	Tag_automate()
	//document.getElementById("navbar").style.transition="all 1.5s";
}

function Close() {
	document.getElementById("navbar").style.display = "none";
	document.getElementById("navbar").style.transition="all 1.5s";
}

function Open_search() {
	document.getElementById("navbar-search").style.display = "inline";
	Close()
	//document.getElementById("navbar").style.transition="all 1.5s";
}

function Close_search() {
	document.getElementById("navbar-search").style.display = "none";
	document.getElementById("navbar").style.transition="all 1.5s";
}