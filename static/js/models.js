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

window.User = Backbone.Model.extend({
	url : function() {
		return '/data/user?Type=small'
	}
});

window.UserFull = Backbone.Model.extend({
	url : function() {
		return '/data/user?Type=full'
	}
});