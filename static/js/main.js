var AppRouter = Backbone.Router.extend({

	routes : {
		'' : 'feed',
		'!feed' : 'feed'
		'!404' : 'show_404',
		'!profile/me' : 'me',
		'!profile/:id' : 'profile'
	},
	initialize : function() {
		this.menuView = new MenuView();
		$('body').prepend(this.menuView.render().el);

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