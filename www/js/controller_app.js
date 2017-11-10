angular.module('app').controller('MainCtrl',
 function(
  $scope, $routeParams, $translate, $http, $timeout, $location,
  $mdSidenav,$firebaseObject, $firebaseArray, $firebaseAuth, NgMap,
  NavigatorGeolocation,
  $interval
  ) {
  var ctl = this;
  app.$scope = $scope;
  // http://localhost:5000/?name=ponti
  app.controller_helpers(ctl);
  app.controller_config(ctl, $scope, $firebaseObject, $interval);
  
  // ctl.firebase = firebase;
  
  /*helper initialization*/
  app.app_helper(ctl);
  /*function for applying external javascript in an angular envroiment */
  ctl.apply = function(){ setTimeout(function () { $scope.$apply(); }, 50); };
  /* login functions */
  app.login(ctl, $scope, $location, $firebaseObject, $firebaseArray);
  app.check_login();
  /*map initialization*/
  app.init_map(ctl, $firebaseArray, NgMap);
  app.init_addObject(ctl,NavigatorGeolocation);
  ctl.getCurrentPosition(ctl,NavigatorGeolocation);
  //ctl.prepareForm(ctl,ctl.GROUP_NAMES[0]);

  /*functions per il sidenav */
  $scope.toggleLeft = buildToggler('left');
  $scope.toggleRight = buildToggler('right');

  function buildToggler(componentId) {
    return function() {
      $mdSidenav(componentId).toggle();
    };
  }
  
});
