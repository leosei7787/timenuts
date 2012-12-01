window.MenuView = Backbone.View.extend({
	tagName : 'header',
	initialize : function() {
	},
	template : _.template($('#tpl-menu').html()),
	render : function(eventName) {

		$(this.el).html(this.template());

		return this;
	}
});