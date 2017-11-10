app
.config(function($locationProvider) {
  $locationProvider.hashPrefix('!');
})
.config(function($routeProvider) {
  console.log("QUI");
  $routeProvider.
    when('/index', {
      templateUrl: "/views/fragments/map.html"
    }).
    when('/login', {
      templateUrl: "/views/login.html"
    }).
    // when('/page_detail/:item_id', {
    //   templateUrl: "/views/page_detail.html"
    // }).
    otherwise('/index');
});
