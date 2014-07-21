import Ember from 'ember';
// import Parse from 'vendor/parse-js-sdk/lib/parse';

export default Ember.Route.extend({

  model: function(params) {
    return this.store.find('player', params.player_id);
    // window.console.log('hi: ' + JSON.stringify('there'));
    // Parse.initialize("hIj40pzSmdiJiWO6obXxHedMFaaPiZxMRlnTZNCZ", "WzFLNl6ukCFcHnJuPZ5opF6QGDpDNOMjHno1Hkf2");
    // var Player = Parse.Object.extend("Player");
    // window.console.log('Player: ' + JSON.stringify(Player));
    // var q = Parse.Query(Player);
    // q.get('gcpiU3zzOx', {
    //   success: function(player) {
    //     return player;
    //   },
    //   error: function(object, error) {
    //     window.console.log('error: ' + JSON.stringify(error));
    //   } 
    // });
  },//model
});
