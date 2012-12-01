//Models
window.Lieu = Backbone.Model
.extend({
	url : function() {
		return '/services'
	},
	initialize : function() {
		this.passeFiltre = true;
		this.changeEtat = false;
		this.initPhotos();
	}
});