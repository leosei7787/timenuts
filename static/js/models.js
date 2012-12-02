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
		return '/data/user'
	}
});

window.Users = Backbone.Collection.extend({
	url : function() {
		return '/data/user'
	}
});