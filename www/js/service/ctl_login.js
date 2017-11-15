app.login = function(ctl, $scope, $location, $firebaseObject, $firebaseArray){
  
  app.check_login = function(){
    ctl.user = ctl.mainfirebase.auth().currentUser;
    //app.user = ctl.user;
    console.log("User", ctl.user);
    ctl.apply();
  };

  setTimeout(app.check_login, 250);
  setTimeout(app.check_login, 650);
  
  ctl.user_signin = function(){
    $('#login_section button').hide();
    $('#login_section md-progress-circular').show();
    ctl.mainfirebase.auth().signInWithEmailAndPassword(ctl.user_email, ctl.user_pass)
    .then(function(authData){
      ctl.user = ctl.mainfirebase.auth().currentUser;
      app.user = ctl.user;
      ctl.user_pass  = undefined;
      ctl.apply();
      $location.path( "/index" );
      $('#login_section button').show();
      $('#login_section md-progress-circular').hide();
    })
    .catch(function(error) {
      console.log(error);
      var errorCode = error.code;
      var errorMessage = error.message;
      $('#login_section button').show();
      $('#login_section md-progress-circular').hide();
      if (errorCode === 'auth/wrong-password') {
        alert('Wrong password.');
      } else {
        alert(errorMessage);
      }
    });
  };
  
  ctl.user_logout = function(){
    console.log("Logout");
    ctl.user = undefined;
    app.user = undefined;
    ctl.mainfirebase.auth().signOut();
    ctl.apply();
    $location.path( "/index" );
  };
  
};