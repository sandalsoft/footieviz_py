import Ember from 'ember';
import ajax from 'ic-ajax';

export default Ember.Object.extend({
    namespace: '/1/classes',
    host: 'https://api.parse.com',
    data: {
      limit: 999,
    },
    method: 'GET',

    findAll: function(name) {
        var url = this.get('host') + this.get('namespace') + '/' + name;
        return ajax({
            url: url,
            headers: {
                'X-Parse-Application-Id': 'hIj40pzSmdiJiWO6obXxHedMFaaPiZxMRlnTZNCZ',
                'X-Parse-REST-API-Key': 'GfmWDxkfGvZj2nzAygTNQd9rriwkOUHQ3UodtXYO',
            },
            data: this.get('data'),
            method: this.get('method'),
        }).then(function(response) {
            return response.results;
        });
    },

    find: function(name, id) {
        var url = this.get('host') + this.get('namespace') + '/' + name + '/' + id;
        return ajax({
            url: url,
            headers: {
                'X-Parse-Application-Id': 'hIj40pzSmdiJiWO6obXxHedMFaaPiZxMRlnTZNCZ',
                'X-Parse-REST-API-Key': 'GfmWDxkfGvZj2nzAygTNQd9rriwkOUHQ3UodtXYO',
            },
            data: this.get('data'),
            method: this.get('method'),
        });
    },

     findQuery: function(name, id) {
        var url = this.get('host') + this.get('namespace') + '/' + name + '/' + id;
        return ajax({
            url: url,
            headers: {
                'X-Parse-Application-Id': 'hIj40pzSmdiJiWO6obXxHedMFaaPiZxMRlnTZNCZ',
                'X-Parse-REST-API-Key': 'GfmWDxkfGvZj2nzAygTNQd9rriwkOUHQ3UodtXYO',
            },
            data: this.get('data'),
            method: this.get('method'),
        });
    }


});
