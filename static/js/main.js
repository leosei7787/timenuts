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
		$('#content').empty();

		this.feedSkeletonView = new FeedSkeletonView();
		$('#content').append(this.feedSkeletonView.render().el);

		this.me = new Me();
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

		this.meView = new MeSmallView({
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
		$('#content').empty();

		this.meFull = new MeFull();
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

		$('#content').append(this.meFullView.render().el);

	},
	profile : function(_id) {
		$('#content').empty();

		this.userFull = new UserFull({
			id : _id
		});
		this.userFull.fetch({
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

		this.userFullView = new UserFullView({
			model : this.userFull
		});

		$('#content').append(this.userFullView.render().el);
	}
});

var app = new AppRouter();