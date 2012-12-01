var AppRouter = Backbone.Router.extend({

	routes : {
		'' : 'feed',
		'!feed' : 'feed',
		'!404' : 'show_404',
		'!profile/me' : 'me',
		'!profile/:id' : 'profile'
	},
	initialize : function() {
		this.menuView = new MenuView();
		$('body').prepend(this.menuView.render().el);
		Backbone.history.start();


	},
	show_404 : function() {

	},
	feed : function() {
		this.services = new Services();
		this.services.fetch({
			success : function(collection, response) {
				console
				.log('Success in loading ' + collection + ' at '
					+ collection.url + ' with ' + response.length
					+ ' elements');
			},
			error : function(collection, response) {
				console.log('Error in loading : ' + collection.name + ' at '
					+ collection.url + ' with response ' + response);
			}
		});

		this.servicesView = new ServicesView({
			collection : this.services
		});

		// this.services.on('reset',function() {
		// 	this.servicesView.render();
		// });

		$('#feed-table').append(this.servicesView.render().el);
	},
	me : function() {

	},
	profile : function(id) {

	}
});

var app = new AppRouter();