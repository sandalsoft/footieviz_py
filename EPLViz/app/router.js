import Ember from 'ember';

var Router = Ember.Router.extend({
  location: EPLVizENV.locationType
});

Router.map(function() {
  this.route('player');
  this.route('players');
});

export default Router;
