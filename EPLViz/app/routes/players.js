import Ember from 'ember';

export default Ember.Route.extend({

  model: function() {
    window.console.log('hi' + JSON.stringify(' there'));
    return this.store.findAll('player');
    },
  afterModel: function(model) {
    window.console.log('model: ' + JSON.stringify(model));
  }
});
