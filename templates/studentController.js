angular.module('studentApp', [])
  .controller('studentAppController',['$scope', function($scope) {
    var studentList = this;
	$scope.students = ['John','George','James'];
 
	
  }]);