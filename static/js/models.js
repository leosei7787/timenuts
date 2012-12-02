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