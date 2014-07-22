import Ember from 'ember';

export default Ember.Object.extend({

  find: function(name, id) {
      var adapter = this.container.lookup('adapter:' + name);
    window.console.log('find() adapter: ' + JSON.stringify(adapter));

      return adapter.find(name, id);
  },

  findAll: function(name) {
      var adapter = this.container.lookup('adapter:' + name);
      window.console.log('adapter: ' + JSON.stringify(adapter));
      return adapter.findAll(name);
  },
});
