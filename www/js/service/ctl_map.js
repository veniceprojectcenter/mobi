app.init_map = function(ctl, $firebaseArray, NgMap){

	// https://cityknowledge30.firebaseio.com/geojson 
	NgMap.getMap().then(function(map) {
    ctl.map = map;
  });
	ctl.map_center = [45.438109, 12.327966]; //Venice
	ctl.zoom_level = 13; //default zoom level
	ctl.current_pos = [45.438109, 12.327966];
	ctl.markers = [];

	ctl.import_geojson = function(geojson){
    ctl.map.data.addGeoJson(geojson);
	}

  ctl.read_geojson = function(group_names, $firebaseArray){
    for(group_name in group_names){ 
      ctl.mainfirebase.database().ref("/geojson/"+group_name)
      .once("value").then(function(snapshot){
        console.log("DATA: ",snapshot.val());
        ctl.geojson = snapshot.val();
        ctl.import_geojson(ctl.geojson)
      });
    }
  }
  //app.markers = ctl.markers;

  ctl.import_members = function(group_names){
    console.log("[import_members] group_names: ",group_names);
    for(var i=0; i < group_names.length ; i++){ 
    var ref = ctl.mainfirebase.database().ref("/groups/"+group_names[i]);
      console.log("GROUPNAME: ",group_names[i]);
      ref.on("value", function(snapshot) {
        console.log("orderByChild");
        console.log("snapshot.val(), ", snapshot.val());
        console.log("snapshot.key, ", snapshot.key);
        ctl.members = snapshot.val().member_list.split(",");
        app.members = ctl.members;
        ctl.import_markers(ctl.members);
      });
    }
  }

  ctl.import_markers = function(members){
    for(var i=0;i<members.length; i++){
      var ref = ctl.mainfirebase.database().ref("/data/"+members[i]);
      ref.on("value",function(snapshot){
        ctl.markers.push(snapshot.val());
        ctl.apply();
      });
    }
  }

  //app.import_markers = ctl.import_markers;
}
