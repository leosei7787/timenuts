//Models
window.Service = Backbone.Model.extend({
	url : function() {
		return '/data/services'
	},
	initialize : function() {
	}
});

window.Services = Backbone.Collection.extend({
	model : Service,
	url : '/data/services'
});

window.Doneservices = Backbone.Collection.extend({
	model : Service,
	url : '/data/doneservices'
});

window.Requests = Backbone.Collection.extend({
	model : Service,
	url : '/data/requests'
});

window.Me = Backbone.Model.extend({
	url : function() {
		return '/data/me?Type=small'
	}
});

window.MeFull = Backbone.Model.extend({
	url : function() {
		return '/data/me?Type=full'
	}
});

window.UserFull = Backbone.Model.extend({
	url : function() {
		return '/data/user?Id='+this.get('id')+'&Type=full'
	}
});

window.UserDoneservices = Backbone.Collection.extend({
	model : Service,
	url : function() {
		console.log(this);
		return '/data/doneservices/'+this.userid;
	},
	initialize : function() {
		this.userid = '';

		// this.userid = this.options.get(userid);
	}
});

window.UserRequests = Backbone.Collection.extend({
	model : Service,
	url : function() {
		return	'/data/requests/'+this.userid;
	},
	initialize : function() {
		this.userid = '';
		// this.userid = this.options.get(userid);
	}
});