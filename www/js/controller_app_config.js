app.controller_helpers = function(ctl){
  ctl.getQueryVariable = function(variable, default_value) {
    var query = window.location.search.substring(1);
    var vars = query.split('&');
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
        if (decodeURIComponent(pair[0]) == variable) {
            return decodeURIComponent(pair[1]);
        }
    }
    return default_value;
  };
};
var debug = false;
app.controller_config = function(ctl, $scope, $firebaseObject, $interval){

  try{
  ctl.config = {
    group_name: ["Merge Ponti"],
    
  }
	//ctl.GROUP_NAMES = ["Merge Ponti"];//ADD GROUPS HERE
	ctl.MAPS_API = "AIzaSyDjcY0l0eKswR1AADc2ow4WEnx69qzuLKw"; //REPLACE WITH YOUR APIKEY
  
  ctl.input_app_name = ctl.getQueryVariable('name'); // || 'ponti';
  if (!ctl.input_app_name) ctl.input_app_name = prompt("Write your application name...");
  if (!ctl.input_app_name) alert("So, you should found it...");
 
  firebase.database().ref(`inputapp/${ctl.input_app_name}`).once("value", function(snap){
    ctl.config = snap.val();
    
    //scarico un data di quel gruppo
    if(debug){
      firebase.database().ref(`/groups/${ctl.config.group_name}/member_list`).once("value",function(snap){
        var template_el=snap.val().split(",")[1];
        firebase.database().ref(`/data/${template_el}/data`).once("value",function(snapshot){
          var x=snapshot.val();
          var z=Object.keys(x);
          var input = []
          for(var i=0;i<z.length;i++){
            var temp = {};
            temp.input_type='text';
            temp.key=z[i];
            input.push(temp);
          }
          firebase.database().ref(`/views/${ctl.config.view_name}/tabs/0/elements/`).set(input);
        });
      });
    }

    //alert("STOP, DIMENTICA PERCHE' ");

    // CARICO LA STRUTTURA DEL TAB
    ctl.tabs_obj = $firebaseObject(
      firebase.database().ref(`/views/${ctl.config.view_name}`)
    );
    //ctl.det_view.tabs 
    ctl.tabs_obj.$bindTo($scope, "ctl.det_view");
    ctl.tabs_obj.$loaded(function(){
      console.log("laoded tabs", ctl.det_view.tabs);
    });
    
    // CARICO IL GRUPPO
    console.log("pp", `/groups/${ctl.config.group_name}`);
    ctl.group_obj = $firebaseObject(
      firebase.database().ref(`/groups/${ctl.config.group_name}`)
    );
    ctl.group_obj.$bindTo($scope, "ctl.group");
    ctl.group_obj.$loaded(function(){
      console.log("loaded group ", ctl.group);
      ctl.elementi = [];
      // CARICO OGNI ELEMENTO DEL GRUPPO
      for (var k in ctl.group.members){
        console.log("Carico", k, `data/${k}`);
        if (k.match(/\$/)) continue;
        console.log("Carico", k, `data/${k}`);
        firebase.database().ref(`/data/${k}`).once('value', function(snap){
          var tmp = snap.val();
          if (tmp) ctl.elementi.push( tmp );
        });
        // ctl.elementi.push( $firebaseObject( firebase.database().ref(`/data/${k}`) ) );
      };
      // ctl.apply = function(){ setTimeout(function () { $scope.$apply(); }, 50); }
      // console.log(`/groups/${ctl.config.group_name}/member_list`);
      // firebase.database().ref(`/groups/${ctl.config.group_name}/member_list`).once("value", function(snap){
      //   var elementi = snap.val().split(',');
      //   elementi.forEach(function(k){
      //     console.log("Carico", k, `data/${k}`);
      //     console.log("Carico", k, `data/${k}`);
      //     ctl.elementi.push( $firebaseObject( firebase.database().ref(`/data/${k}`) ) );
      //   });
      // });
    });
  });
  }catch(ex){}
  
  //$interval(function(){}, 1500);
};