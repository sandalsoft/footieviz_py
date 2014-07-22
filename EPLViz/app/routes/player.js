import Ember from 'ember';
import PlayerAdapter from 'EPLViz/adapters/player';


export default Ember.Route.extend({
    model: function(params) {
        var adapter = PlayerAdapter.create();
        window.console.log(' params.player_id: ' + JSON.stringify( params.player_id));
        return adapter.find('Player', params.player_id);
    },//model
});
