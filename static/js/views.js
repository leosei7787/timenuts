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

window.FeedSkeletonView = Backbone.View.extend({
	tagName : 'section',
	initialize : function() {
	},
	template : _.template($('#tpl-feed-skeleton').html()),
	render : function(eventName) {
		$(this.el).html(this.template());
		return this;
	}
});

window.LoadingView = Backbone.View.extend({
	className : 'loading',
	render : function(eventName) {
		$(this.el).html('<img src="img/ajax-loader.gif" />');
		return this;
	}
});

window.ServiceView = Backbone.View.extend({
	className : 'service-block',
	template : _.template($('#tpl-service').html()),
	initialize : function() {
	},
	render : function(eventName) {
		if (this.model) {
			$(this.el).html(this.template(this.model.toJSON()));
		} else {
			$(this.el).html(new LoadingView.render().el);
		}
		return this;
	}
});

window.ServicesView = Backbone.View.extend({
	tagName : 'tbody',
	initialize : function() {
		this.collection.on('reset',this.render,this);
		this.collection.view = this;
	},
	render : function(eventName) {
		$(this.el).empty();
		if (this.collection.length) {
			_.each(this.collection.models,function(service,index) {
				$(this.el).append('<tr><td class="service" id="service-'+index+'"></td></tr>');
				$(this.el).find('#service-'+index).append(new ServiceView({
					model : service
				}).render().el);
			},this);
		} else {
			$(this.el).html('<tr><td class="service"></td></tr>');
			$(this.el).find('.service').html(new LoadingView({}).render().el);
			
		}
		return this;
	}
});

window.MeSmallView = Backbone.View.extend({
	id : 'small-me',
	className : 'block',
	template : _.template($('#tpl-small-me').html()),
	initialize : function() {
		this.model.on('change',this.render,this);
	},
	render : function(eventName) {
		if (this.model.get('Id')) {
			$(this.el).html(this.template(this.model.toJSON()));
		} else {
			$(this.el).html(new LoadingView({}).render().el);
		}
		return this;
	}
});

window.MeFullView = Backbone.View.extend({
	id : 'tpl-main-user-data',
	tagName : 'section',
	template : _.template($('#tpl-main-user-data').html()),
	initialize : function() {
		this.model.on('change',this.render,this);
	},
	render : function(eventName) {
		if (this.model.get('Id')) {
			$(this.el).html(this.template(this.model.toJSON()));
		} else {
			$(this.el).html(new LoadingView({}).render().el);
		}
		return this;
	}
});