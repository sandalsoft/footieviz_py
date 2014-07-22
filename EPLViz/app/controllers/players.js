import Ember from 'ember';

export default Ember.ArrayController.extend({
  totalPlayers: function() {
    return this.get('model.length');
    }.property('model'),

  actions: {

    filterBy: function(filterTerm) {
      window.console.log('filterTerm: ' + JSON.stringify(filterTerm));
    },// filterBy

  }// actions
});
