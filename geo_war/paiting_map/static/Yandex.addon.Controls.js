L.Yandex.mergeOptions({
	controlsContainerStyle: {
		left: '45px',
		right: '57px',
		top: '3px',
		width: 'auto'
	}
});

L.Yandex.include({
	_addControl: function (name, parameters) {
		if (!this._map) { // ymaps API expects map to be in DOM
			return this.once('add',function () {
				this._addControl(name, parameters);
			});
		}
		var defaults = this._controlOptionsDefault;
		var options = L.extend({}, defaults, defaults[name], parameters.options);
		this._yandex.controls.add(name, options);
		if (typeof parameters === 'object') {
			var control = this._yandex.controls.get(name);
			['data','state'].forEach(function (manager) {
				if (manager in parameters) {
					control[manager].set(parameters[manager]);
				}
			});
		}
	},

	// Some default values to facilitate Yandex controls seamless integration
	_controlOptionsDefault: {
		size: 'small', float: 'right',
		typeSelector: { panoramasItemMode: 'off' }
	}
});

L.Yandex.addInitHook('on', 'load', function () {
	var options = this.options;
	if (options.controlsContainerStyle) {
		this._setStyle(this._yandex.controls.getContainer(), options.controlsContainerStyle);
	}
	for (var key in options) {
		if (ymaps.control.storage.get(key)) { // check if `key` is valid control name
			this._addControl(key, options[key]);
		}
	}

	if (!options.controlsSeparate) { return; }
	this._controls = L.DomUtil.create('div','leaflet-yandex-controls');
	this._controls.appendChild(this._yandex.panes.get('controls').getElement());
	this._controls.appendChild(this._yandex.panes.get('copyrights').getElement());
	this._setStyle(this._controls, {
		position: 'absolute',
		height: '100%',
		width: '100%',
		zIndex: this._isOverlay ? 950 : 900
	})
	function addControls () {
		this._map._controlContainer.appendChild(this._controls);
	}
	this.on('add',addControls);
	if (this._map) { addControls.call(this); }
	this.on('remove',function () {
		this._controls.remove();
	});
});