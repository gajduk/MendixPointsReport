mx.data.get( {
    xpath: "//Gamification.User[DisplayName='Andrej Gajduk']",
    filter: {
        sort: [["Name", "asc"]],
        offset: 0,
        amount: 2
    },
    callback: function(objs) {
    	console.log("result received");
    	console.log(objs.length);
    	console.log("userStatsResult="+JSON.stringify(objs));
    }
});
console.log("Invoked mxgetmyuser");
