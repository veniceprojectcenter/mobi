app.init_addObject = function(ctl,NavigatorGeolocation){
	
  ctl.getCurrentPosition = function(ctl,NavigatorGeolocation){
		NavigatorGeolocation.getCurrentPosition()
    .then(function(position) {
     //ctl.current_pos =[position.coords.latitude, position.coords.longitude];
     ctl.current_pos ={lat: position.coords.latitude , lng: position.coords.longitude }
    });
	}

  ctl.prepareForm = function(ctl,group_name){
    app.ctl=ctl;
    try{
      ctl.getCurrentPosition(ctl,NavigatorGeolocation);
    }catch(ex){
      ctl.current_pos.lat=0;
      ctl.current_pos.lng=0;
    };
    console.log("prepareForm");
    ctl.dati = {};
    for(var i=0; i < ctl.det_view.tabs[0].elements.length; i++){
      ctl.dati[ctl.det_view.tabs[0].elements[i].key]=""; 
    }
    ctl.dati.lat = ctl.current_pos.lat;
    ctl.dati.lng = ctl.current_pos.lng;
  }

  ctl.showEditModal = function(event,modal,obj){;
    console.log("[SHOWEDITMODAL]: ",modal);
    console.log("[SHOWEDITMODAL]: ",obj);
    ctl.dati=obj.data;
    ctl.dati.ckid = obj.birth_certificate.ckID;
    ctl.birth_certificate=obj.birth_certificate;
    console.log("[SHOWEDITMODAL]: ",ctl.birth_certificate.ckID);
    $(modal).show();
    $("#tabs").tabs();
    $(".add.button").hide();
    ctl.apply();
  }

  ctl.showModal = function(modal){
    ctl.prepareForm(ctl,ctl.config.group_name);
    console.log("modal: ",modal);
    //$(modal).append(ctl.form);
    $(modal).show();
    $("#tabs").tabs(function(){ console.log("GHE SBORO")});
    $(".add.button").hide();
    ctl.apply();
  }

  ctl.hideModal = function(modal){
    $(modal).hide();
    //$(modal).find("form").remove();
    $(".add.button").show();
    ctl.apply();
  }

  ctl.addObject = function(ctl,group_name,dati,files){
    var error=1;
    console.log("dati -->",dati);
    app.ctl = ctl;
    alert("debugg");
    if(group_name == '' || group_name == null || group_name == undefined){
      error=1;
      alert("Error: no group_name given");
    }

    if(dati.length < 1 ) error=1;

    for(var k in dati){
      console.log("cos'è k?: ",k);
      console.log("dati[k]: ",dati[k]);
      if(dati[k] == '' || dati[k] == null || dati[k] == undefined || dati[k]=="" || dati[k]==" " ){
        alert("Warning: "+k+" is empty");
        error=1; 
      }
    }

    if(error==1) return;

    alert("error code: "+error);
    var fb = ctl.mainfirebase.database();
    var new_obj={test : "dovrei essere sovrascritto"};
    var new_value;

    if(ctl.birth_certificate==null){

      new_value = fb.ref('/data').push();
      dati.ckid = new_value.key;
      console.log("Creo chiave ", dati.ckid);
      ctl.file_uploaded=[];

      if(files!= undefined || files!=null && files.length > 0 ){
        for(var k=0 ; k < ctl.files.length; k++ ){
          console.log("files[k]: ",files[k]);
          ctl.file_uploaded.push(ctl.uploadStorage(group_name,dati.ckid,files[k]));
          console.log("ctl.file_uploaded[l-1]: ",ctl.file_uploaded[ctl.file_uploaded.length-1]);
        } 
        dati.images=ctl.file_uploaded.join(",");
        console.log("dati.images: ", dati.images);
      }

      new_obj = {
      birth_certificate: {
        birthID:  (new Date).toJSON(),
        ckid:     dati.ckid,
        dor:      (new Date).toJSON(),
        lat:      ctl.current_pos.lat || 0.0,
        lng:      ctl.current_pos.lng || 0.0,
        recorder: ctl.user.email,
        type:     group_name
      }, 
      data: dati
    };


    }else{
      new_value = fb.ref('/data/'+dati.ckid+"/data");
      console.log("aggiorno chiave ", dati.ckid);
      new_obj = dati;
    }
    new_value.set ( new_obj,
     function(e){
      if (e){ 
        alert("FATAL ERROR");
        throw { ok: false, err: (e.code || e)};
      }
      if(ctl.birth_certificate==null){
        fb.ref('groups/' + group_name + '/members').push({
          [dati.ckid]: dati.ckid
        });
        fb.ref('groups/' + group_name + '/member_list').once('value', function(dataSnapshot) {
          var member_list = dataSnapshot.val();
          console.log('Result key groups/' + group_name + '/member_list');
          // console.log("Dati", member_ids);
          if (!member_list) throw "errore nel trovare il membro";//({ ok: false, err: 'Error getting members'});
          member_list = member_list + ',' + dati.ckid;
          fb.ref('groups/' + group_name + '/member_list').set(member_list);
          fb.ref('geojson/' + group_name + '/features').once('value', function(featSnapshot) {
            var new_id = featSnapshot.numChildren();
            console.log('Result key geojson/' + group_name + '/features');
            console.log("FEATURES", new_id);
            // new_id = new_id + 10000;
            console.log("NEW ID", new_id);
            var points = (ctl.current_pos.lng==null || ctl.current_pos.lng == undefined) ? [0.0,0.0] : 
            [ctl.current_pos.lng, ctl.current_pos.lat];
            fb.ref('geojson/' + group_name + '/features/' + new_id).set({
              geometry: {
                coordinates: points,
                type: 'Point'
              }, 
              properties: {
                  ckid: dati.ckid,
                  descr: dati.ckid,
                  title: dati.ckid,
                  type: group_name
                }, type: 'Feature'
              });
            });
          });
      }
      alert("object with ckid: "+dati.ckid+" created!");
      });
  }

  ctl.create = function(){
    console.log("[CTL.CREATE]: ",ctl.config.group_name,ctl.dati,ctl.files);
    ctl.addObject(ctl,ctl.config.group_name,ctl.dati,ctl.files);
  }

  ctl.update = function(){
    console.log("[CTL.UPDATE]: ",ctl.config.group_name,ctl.dati);
    fb.ref('data/' + ctl.dati.ckid).once('value', function(dataSnapshot){});

  }

  ctl.uploadStorage = function(group_name,ckid,file){
    var fileref = ctl.mainfirebase.storage().ref();
    var new_name = file.name;
    if(new_name.startsWith("image")){
      var temp_name = file.name.split(".");
      new_name=temp_name[0]+new Date().getTime()+"."+temp_name[1];
    };
    fileref = fileref.child("images/"+group_name+"/"+ckid+"/"+new_name);
    var blob = new Blob([file],{ type: file.type });
    fileref.put(blob).then(function(snapshot) {
      if(snapshot.state == "success"){
        console.log('Uploaded a blob or file!');
        alert("Uploaded a blob or file!, name: "+new_name);
        //console.log("[caricato sicuro!]: ",snapshot);
        //console.log("storage: ", fileref.location.bucket+"/"+fileref.location.u);
      }
    });
    return "https://firebasestorage.googleapis.com/v0/b/"+fileref.location.bucket+"/o/"+encodeURIComponent(fileref.location.u)+"?alt=media";
  }
 
}