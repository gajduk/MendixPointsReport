var page = require('webpage').create();
function startsWith(thisStr,searchStr) {
	return thisStr.slice(0, 0 + searchStr.length) === searchStr;
}
page.onConsoleMessage = function(msg, lineNum, sourceId) {
  if ( startsWith(msg,"userStatsResult=") ) {
  	console.log(msg.substring(16));
  	phantom.exit();
  }
};
page.open('https://developer.mendixcloud.com/link/community', function(status) {
  setTimeout(function() {
  	page.injectJs("mxgetmyuser.js");
  },5000)
  
});