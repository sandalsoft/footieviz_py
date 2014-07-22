import Ember from 'ember';

var Router = Ember.Router.extend({
  location: EPLVizENV.locationType
});

// Array.prototype.map.call(document.getElementsByClassName('ismInfo ismViewProfile JS_ISM_INFO'), function(link) {return document.createElement('a').href=link.hash.split('#')[1];});
// 
Router.map(function() {
   this.resource("players", function(){
    this.resource("player", { path: "/:player_id" });
  });
  this.route('players');
});

export default Router;
