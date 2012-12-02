var AppRouter = Backbone.Router.extend({

	routes : {
		'' : 'feed',
		'!feed' : 'feed',
		'!404' : 'show_404',
		'!profile/me' : 'me',
		'!profile/:id' : 'profile'
	},
	initialize : function() {
		Backbone.history.start();
	},
	show_404 : function() {
	},
	feed : function() {
		$('body').empty();
		this.menuView = new MenuView();
		$('body').prepend(this.menuView.render().el);

		this.feedSkeletonView = new FeedSkeletonView();
		$('body').append(this.feedSkeletonView.render().el);

		this.me = new User();
		this.me.fetch({
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

		this.meView = new UserSmallView({
			model : this.me
		});

		$('#left-col').append(this.meView.render().el);

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

		$('#feed-table').append(this.servicesView.render().el);
	},
	me : function() {
		$('body').empty();
		this.menuView = new MenuView();
		$('body').prepend(this.menuView.render().el);

		this.meFull = new UserFull();
		this.meFull.fetch({
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

		this.meFullView = new UserFullView({
			model : this.meFull
		});

		$('body').append(this.meFullView.render().el);

	},
	profile : function(id) {

	}
});

var app = new AppRouter();