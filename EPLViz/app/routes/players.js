import Ember from 'ember';
import PlayerAdapter from 'EPLViz/adapters/player';

export default Ember.Route.extend({ 

  model: function() {
    var adapter = PlayerAdapter.create();
    return adapter.findAll('Player');
  },
 
  // afterModel: function(model) {
  //   window.console.log('model: ' + JSON.stringify(model));
  // }

});
