var eavesApp = angular.module('eavesApp', []);

eavesApp.controller('MentionCtrl', function ($scope, $http) {

    $http.get('/mentions').success(function (data) {
        $scope.mentions = data;
    });

    $scope.addMention = function() {
        $scope.mentions.push({text: $scope.mentionText, read:false});
        $scope.mentionText = "";
    };
    $scope.unread = function() {
        var count = 0;
        angular.forEach($scope.mentions, function(mention) {
            count += mention.read ? 1 : 0;
        });
        return count;
    };
    $scope.orderProp = 'name';
});
