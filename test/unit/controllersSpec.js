describe('EavesApp controllers', function() {
 
    beforeEach(module('eavesApp'));
  describe('MentionCtrl', function(){
 
    it('should create "mention" model with 2 mentions', inject(function($controller) {
      var scope = {},
        ctrl = new MentionCtrl(scope);
 
      expect(scope.mentions.length).toBe(2);
    });
  });
});
