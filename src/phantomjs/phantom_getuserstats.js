var system = require('system');
var args = system.args;
if (args.length !== 2) {
  console.error('DisplayName of user expected as only argument.');
  phantom.exit(1);
}
var page = require('webpage').create();
page.onCallback = function(data) {
	if ( data )  {
		console.log(JSON.stringify(data));
  		phantom.exit();
	}
	else  {
		console.error("failed while querying data.");
  		phantom.exit(1);
	}
};
page.onConsoleMessage = function(msg, lineNum, sourceId) {
//  console.debug('CONSOLE: ' + msg + ' (from line #' + lineNum + ' in "' + sourceId + '")');
};
//console.debug("started "+args[1]);
var attributes = ["TotalCommunityPoints","TotalForumPoints","TotalAppstorePoints","TotalPlatformPoints","TotalLearningPoints"];
var attributesSimpleNames = ["Community","Forum","Appstore","Platform","Learning"];
page.open('https://developer.mendixcloud.com/link/community', function(status) {
  if (status === "success") {
	 // console.debug("opened");
	  setTimeout(function() {
//	  	console.debug("injecting");
	   	page.evaluate(function(displayName,attributes,attributesSimpleNames) {
   			mx.data.get( {
			    xpath: "//Gamification.User[DisplayName='"+displayName+"']",
			    filter: {
			        sort: [["Name", "asc"]],
			        offset: 0,
			        amount: 1,
			        attributes: attributes
			    },
			    callback: function(objs) {
			   		if (typeof window.callPhantom === 'function') {
			   			try {
			   				var res = {};
			   				for ( var i = 0 ; i < attributes.length ; ++i ) {
			   					res[attributesSimpleNames[i]] = +objs[0].get(attributes[i]);
			   				}
			   				window.callPhantom(res);
			   			}
			   			catch (ignored_error){
			   				window.callPhantom(); 
			   			}
			   		}
			    }
			});
	   	},args[1],attributes,attributesSimpleNames);
//	   	console.debug("done injecting");
	  },3000)
	}
	else {
		console.error("Could not open page.");
  		phantom.exit(1);
	}
});