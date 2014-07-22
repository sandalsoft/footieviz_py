import Ember from 'ember';

export default Ember.ArrayController.extend({
  totalPlayers: function() {
    return this.get('model.length');
    }.property('model'),
});
