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