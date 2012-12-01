var AppRouter = Backbone.Router.extend({

	routes : {
		'' : 'feed',
		'!feed' : 'feed'
		'!404' : 'show_404',
		'!profile/me' : 'me',
		'!profile/:id' : 'profile'
	},
	initialize : function() {

	},
	show_404 : function() {

	},
	feed : function() {

	},
	me : function() {

	},
	profile : function(id) {

	}
});

var app = new AppRouter();