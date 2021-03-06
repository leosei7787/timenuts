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
	events : {
		'click .apply' : 'apply'
	},
	initialize : function() {
	},
	render : function(eventName) {
		if (this.model) {
			$(this.el).html(this.template(this.model.toJSON()));
		} else {
			$(this.el).html(new LoadingView.render().el);
		}
		return this;
	},
	apply : function(event){
		var _url = '/data/apply?ServiceId='+event.currentTarget.id.replace(/apply-/g, '')
		$.ajax({
			url: _url,
			type: 'POST'
		});

		$('#'+event.currentTarget.id).attr('disabled','disabled');
		$('#'+event.currentTarget.id).addClass('btn-success');

	}
});

window.ServicesView = Backbone.View.extend({
	tagName : 'tbody',
	initialize : function() {
		this.collection.on('reset',this.render,this);
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

window.HistoryservicesView = Backbone.View.extend({
	template : _.template($('#tpl-given-services').html()),
	initialize : function() {
		this.collection.on('reset',this.render,this);
	},
	render : function(eventName) {
		$(this.el).empty();
		$(this.el).html(this.template({
			title : this.options.title
		}));
		if (this.collection.length) {
			_.each(this.collection.models,function(service,index) {
				$(this.el).find('tbody').append('<tr><td class="service" id="'+this.options.title.split(' ')[0]+'-'+index+'"></td></tr>');
				$(this.el).find('#'+this.options.title.split(' ')[0]+'-'+index).append(new ServiceView({
					model : service
				}).render().el);
			},this);
		} else {
			$(this.el).find('tbody').html('<tr><td class="service"></td></tr>');
			$(this.el).find('.service').html(new LoadingView({}).render().el);

		}
		$('#right-col').append($(this.el));

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

window.UserFullView = Backbone.View.extend({
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