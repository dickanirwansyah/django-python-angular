var myApp = angular.module('imageuploadFrontendApp', ['ngResource']);

myApp.config(function($resourceProvider){
    $resourceProvider.defaults.stripTrailingSlashes = false;
});

myApp.controller('MainCtrl', function($scope){

   console.log("Congratulations You Are In MainCtrl!");

});