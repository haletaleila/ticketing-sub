import React, { Component,   useRef, useEffect } from "react";
import PropTypes from "prop-types";
import TranomdomGame from "./presenter";
import Hammer from 'hammerjs';
import axios from 'axios';
Object.defineProperties(Vector2.prototype, {

	"width": {

		get: function () {

			return this.x;

		},

		set: function (value) {

			this.x = value;

		}

	},

	"height": {

		get: function () {

			return this.y;

		},

		set: function (value) {

			this.y = value;

		}

	}

});


Object.assign(Vector2.prototype, {

	isVector2: true,

	set: function (x, y) {

		this.x = x;
		this.y = y;

		return this;

	},

	setScalar: function (scalar) {

		this.x = scalar;
		this.y = scalar;

		return this;

	},

	setX: function (x) {

		this.x = x;

		return this;

	},

	setY: function (y) {

		this.y = y;

		return this;

	},

	setComponent: function (index, value) {

		switch (index) {

			case 0:
				this.x = value;
				break;
			case 1:
				this.y = value;
				break;
			default:
				throw new Error('index is out of range: ' + index);

		}

		return this;

	},

	getComponent: function (index) {

		switch (index) {

			case 0:
				return this.x;
			case 1:
				return this.y;
			default:
				throw new Error('index is out of range: ' + index);

		}

	},

	clone: function () {

		return new this.constructor(this.x, this.y);

	},

	copy: function (v) {

		this.x = v.x;
		this.y = v.y;

		return this;

	},

	add: function (v, w) {

		if (w !== undefined) {

			console.warn('THREE.Vector2: .add() now only accepts one argument. Use .addVectors( a, b ) instead.');
			return this.addVectors(v, w);

		}

		this.x += v.x;
		this.y += v.y;

		return this;

	},

	addScalar: function (s) {

		this.x += s;
		this.y += s;

		return this;

	},

	addVectors: function (a, b) {

		this.x = a.x + b.x;
		this.y = a.y + b.y;

		return this;

	},

	addScaledVector: function (v, s) {

		this.x += v.x * s;
		this.y += v.y * s;

		return this;

	},

	sub: function (v, w) {

		if (w !== undefined) {

			console.warn('THREE.Vector2: .sub() now only accepts one argument. Use .subVectors( a, b ) instead.');
			return this.subVectors(v, w);

		}

		this.x -= v.x;
		this.y -= v.y;

		return this;

	},

	subScalar: function (s) {

		this.x -= s;
		this.y -= s;

		return this;

	},

	subVectors: function (a, b) {

		this.x = a.x - b.x;
		this.y = a.y - b.y;

		return this;

	},

	multiply: function (v) {

		this.x *= v.x;
		this.y *= v.y;

		return this;

	},

	multiplyScalar: function (scalar) {

		if (isFinite(scalar)) {

			this.x *= scalar;
			this.y *= scalar;

		} else {

			this.x = 0;
			this.y = 0;

		}

		return this;

	},

	divide: function (v) {

		this.x /= v.x;
		this.y /= v.y;

		return this;

	},

	divideScalar: function (scalar) {

		return this.multiplyScalar(1 / scalar);

	},

	min: function (v) {

		this.x = Math.min(this.x, v.x);
		this.y = Math.min(this.y, v.y);

		return this;

	},

	max: function (v) {

		this.x = Math.max(this.x, v.x);
		this.y = Math.max(this.y, v.y);

		return this;

	},

	clamp: function (min, max) {

		// This function assumes min < max, if this assumption isn't true it will not operate correctly

		this.x = Math.max(min.x, Math.min(max.x, this.x));
		this.y = Math.max(min.y, Math.min(max.y, this.y));

		return this;

	},

	clampScalar: function () {

		var min = new Vector2();
		var max = new Vector2();

		return function clampScalar (minVal, maxVal) {

			min.set(minVal, minVal);
			max.set(maxVal, maxVal);

			return this.clamp(min, max);

		};

	}(),

	clampLength: function (min, max) {

		var length = this.length();

		return this.multiplyScalar(Math.max(min, Math.min(max, length)) / length);

	},

	floor: function () {

		this.x = Math.floor(this.x);
		this.y = Math.floor(this.y);

		return this;

	},

	ceil: function () {

		this.x = Math.ceil(this.x);
		this.y = Math.ceil(this.y);

		return this;

	},

	round: function () {

		this.x = Math.round(this.x);
		this.y = Math.round(this.y);

		return this;

	},

	roundToZero: function () {

		this.x = ( this.x < 0 ) ? Math.ceil(this.x) : Math.floor(this.x);
		this.y = ( this.y < 0 ) ? Math.ceil(this.y) : Math.floor(this.y);

		return this;

	},

	negate: function () {

		this.x = -this.x;
		this.y = -this.y;

		return this;

	},

	dot: function (v) {

		return this.x * v.x + this.y * v.y;

	},

	lengthSq: function () {

		return this.x * this.x + this.y * this.y;

	},

	length: function () {

		return Math.sqrt(this.x * this.x + this.y * this.y);

	},

	lengthManhattan: function () {

		return Math.abs(this.x) + Math.abs(this.y);

	},

	normalize: function () {

		return this.divideScalar(this.length());

	},

	angle: function () {

		// computes the angle in radians with respect to the positive x-axis

		var angle = Math.atan2(this.y, this.x);

		if (angle < 0) angle += 2 * Math.PI;

		return angle;

	},

	distanceTo: function (v) {

		return Math.sqrt(this.distanceToSquared(v));

	},

	distanceToSquared: function (v) {

		var dx = this.x - v.x, dy = this.y - v.y;
		return dx * dx + dy * dy;

	},

	distanceToManhattan: function (v) {

		return Math.abs(this.x - v.x) + Math.abs(this.y - v.y);

	},

	setLength: function (length) {

		return this.multiplyScalar(length / this.length());

	},

	lerp: function (v, alpha) {

		this.x += ( v.x - this.x ) * alpha;
		this.y += ( v.y - this.y ) * alpha;

		return this;

	},

	lerpVectors: function (v1, v2, alpha) {

		return this.subVectors(v2, v1).multiplyScalar(alpha).add(v1);

	},

	equals: function (v) {

		return ( ( v.x === this.x ) && ( v.y === this.y ) );

	},

	fromArray: function (array, offset) {

		if (offset === undefined) offset = 0;

		this.x = array[offset];
		this.y = array[offset + 1];

		return this;

	},

	toArray: function (array, offset) {

		if (array === undefined) array = [];
		if (offset === undefined) offset = 0;

		array[offset] = this.x;
		array[offset + 1] = this.y;

		return array;

	},

	fromBufferAttribute: function (attribute, index, offset) {

		if (offset !== undefined) {

			console.warn('THREE.Vector2: offset has been removed from .fromBufferAttribute().');

		}

		this.x = attribute.getX(index);
		this.y = attribute.getY(index);

		return this;

	},

	rotateAround: function (center, angle) {

		var c = Math.cos(angle), s = Math.sin(angle);

		var x = this.x - center.x;
		var y = this.y - center.y;

		this.x = x * c - y * s + center.x;
		this.y = x * s + y * c + center.y;

		return this;

	}

});
Object.assign(Box2.prototype, {

	set: function (min, max) {

		this.min.copy(min);
		this.max.copy(max);

		return this;

	},

	setFromPoints: function (points) {

		this.makeEmpty();

		for (var i = 0, il = points.length; i < il; i++) {

			this.expandByPoint(points[i]);

		}

		return this;

	},

	setFromCenterAndSize: function () {

		var v1 = new Vector2();

		return function setFromCenterAndSize (center, size) {

			var halfSize = v1.copy(size).multiplyScalar(0.5);
			this.min.copy(center).sub(halfSize);
			this.max.copy(center).add(halfSize);

			return this;

		};

	}(),

	clone: function () {

		return new this.constructor().copy(this);

	},

	copy: function (box) {

		this.min.copy(box.min);
		this.max.copy(box.max);

		return this;

	},

	makeEmpty: function () {

		this.min.x = this.min.y = +Infinity;
		this.max.x = this.max.y = -Infinity;

		return this;

	},

	isEmpty: function () {

		// this is a more robust check for empty than ( volume <= 0 ) because volume can get positive with two negative axes

		return ( this.max.x < this.min.x ) || ( this.max.y < this.min.y );

	},

	getCenter: function (optionalTarget) {

		var result = optionalTarget || new Vector2();
		return this.isEmpty() ? result.set(0, 0) : result.addVectors(this.min, this.max).multiplyScalar(0.5);

	},

	getSize: function (optionalTarget) {

		var result = optionalTarget || new Vector2();
		return this.isEmpty() ? result.set(0, 0) : result.subVectors(this.max, this.min);

	},

	expandByPoint: function (point) {

		this.min.min(point);
		this.max.max(point);

		return this;

	},

	expandByVector: function (vector) {

		this.min.sub(vector);
		this.max.add(vector);

		return this;

	},

	expandByScalar: function (scalar) {

		this.min.addScalar(-scalar);
		this.max.addScalar(scalar);

		return this;

	},

	containsPoint: function (point) {

		return point.x < this.min.x || point.x > this.max.x ||
		point.y < this.min.y || point.y > this.max.y ? false : true;

	},

	containsBox: function (box) {

		return this.min.x <= box.min.x && box.max.x <= this.max.x &&
			this.min.y <= box.min.y && box.max.y <= this.max.y;

	},

	getParameter: function (point, optionalTarget) {

		// This can potentially have a divide by zero if the box
		// has a size dimension of 0.

		var result = optionalTarget || new Vector2();

		return result.set(
			( point.x - this.min.x ) / ( this.max.x - this.min.x ),
			( point.y - this.min.y ) / ( this.max.y - this.min.y )
		);

	},

	intersectsBox: function (box) {

		// using 6 splitting planes to rule out intersections.
		return box.max.x < this.min.x || box.min.x > this.max.x ||
		box.max.y < this.min.y || box.min.y > this.max.y ? false : true;

	},

	clampPoint: function (point, optionalTarget) {

		var result = optionalTarget || new Vector2();
		return result.copy(point).clamp(this.min, this.max);

	},

	distanceToPoint: function () {

		var v1 = new Vector2();

		return function distanceToPoint (point) {

			var clampedPoint = v1.copy(point).clamp(this.min, this.max);
			return clampedPoint.sub(point).length();

		};

	}(),

	intersect: function (box) {

		this.min.max(box.min);
		this.max.min(box.max);

		return this;

	},

	union: function (box) {

		this.min.min(box.min);
		this.max.max(box.max);

		return this;

	},

	translate: function (offset) {

		this.min.add(offset);
		this.max.add(offset);

		return this;

	},

	equals: function (box) {

		return box.min.equals(this.min) && box.max.equals(this.max);

	}

});
var Singletonify = function (cons) {
	'use strict';

	var INSTANCE;

	var c = function () {
		if (INSTANCE === undefined) {

			var F = function () {
			};
			F.prototype = cons.prototype;

			var t = new F();
			var ret = cons.apply(t, Array.prototype.slice.call(arguments));

			INSTANCE = (typeof ret === 'object') ? ret : t;
		}

		return INSTANCE;
	};

	c.getInstance = function () {
		return c.apply(null, Array.prototype.slice.call(arguments));
	};

	return c;
};
var domElementInfo = function () {
  this.domElement = document.getElementById("test");
  this.width = 680;
  this.height = 604;
  this.aspect =  1;
  this.frustumSize = this.height;
  this.canvas = document.createElementNS('http://www.w3.org/1999/xhtml', 'canvas');
  this.domElement.appendChild(this.canvas);
  this.context = this.canvas.getContext('2d');
  this.canvas.style.position = 'absolute';
  this.canvas.style.display = 'block';
  this.canvas.width = 680;
  this.canvas.height = 604;
  
  this.areaCanvas = document.createElementNS('http://www.w3.org/1999/xhtml', 'canvas');
  this.domElement.appendChild(this.areaCanvas);
  this.areaContext = this.areaCanvas.getContext('2d');
  this.areaCanvas.style.position = 'absolute';
  this.areaCanvas.width = this.width;
  this.areaCanvas.height = this.height;
  this.areaCanvas.style.zIndex = 4;
  this.areaCanvas.style.display = 'block';
  this.status = "AREA";
  this.selectBlock = "";
  this.selectSeat = "";
  new TLViewController(this.domElement);
};

domElementInfo.prototype.updateDomElement = function () {
//console.log(this);
//console.log(this.domElement);
	this.width = this.domElement.clientWidth;
	this.height = this.domElement.clientHeight;
	this.aspect = this.width / this.height;
	this.frustumSize = this.height;

	this.canvas.width = this.width;
	this.canvas.height = this.height;

	this.areaCanvas.width = this.width;
	this.areaCanvas.height = this.height;

};

domElementInfo.prototype.getDomElement = function () {
  return this.domElement;
};

domElementInfo.prototype.getWidth = function () {
  return this.width;
};

domElementInfo.prototype.getHeight = function () {
  return this.height;
};

domElementInfo.prototype.getAspect = function () {
  this.aspect = this.width / this.height;
  return this.aspect;
};

domElementInfo.prototype.getFrustumSize = function () {
  return this.frustumSize;
};

domElementInfo.prototype.getHeaderAreaHeight = function () {
  return document.querySelector('#header').offsetHeight + document.querySelector('.reserve_prdt_info').offsetHeight;
}

var TLDomInfo = Singletonify(domElementInfo);
var TLAreaBackgroundLayerBase = function () {
	this.areaMapScale = 0.25;
	this.mapSize = 256;
	this.center = {
		"x": 1024.0,
		"y": 1024.0
	};
	this.imageUrl = '';
	this.image = new Image();
};

TLAreaBackgroundLayerBase.prototype.updatedSelectedBlockEvent = function () {
	//TLEventManager.getInstance().signals.updateRender.dispatch();
};
var blockBgInfo = {
	"center": {
		"x": 4096.0,
		"y": 4096.0
	},
	//"mapSize": 2048,
	"mapSize": 8192,
	"imageUrl": "",
	"imageUrlThumnail": "//image.toast.com/aaaaab/ticketlink/TKL_CONCERT/23_kia_area_230330.png?160x160",
	"imageTileUrl": "",
	"imageTileSize": 512,
	"empty": false
}
var blockInfo = []
var seatInfo = []
var gradeMap = {}
TLAreaBackgroundLayerBase.prototype.setLayerInfo = function (blockBgInfo) {
	this.mapSize = blockBgInfo.mapSize;
	this.center = blockBgInfo.center;
	var thumnailSize = 2048;
	if (this.mapSize > thumnailSize) {
		this.imageUrl = blockBgInfo.imageUrlThumnail;
		//console.log(this.imageUrl);
		this.mapSize = thumnailSize;
	} else {
		this.imageUrl = blockBgInfo.imageUrl;
	}
	this.areaMapScale = this.mapSize / blockBgInfo.mapSize;
	this.center.x *= this.areaMapScale;
	this.center.y *= this.areaMapScale;
	this.image.src = this.imageUrl;
};
TLAreaBackgroundLayerBase.prototype.setBlockInfo = function (blockMap) {
	if (!Object.keys(blockMap).length) {
		return;
	}
	// 충돌처리 블럭 blockMap
};

//-------------------------------------------------------
//  Desc : 영역 구역 활성화.
//-------------------------------------------------------
TLAreaBackgroundLayerBase.prototype.activateBlock = function (blockList) {

};

//-------------------------------------------------------
//  Desc : 이미지 로드 실패한 경우 재시도 과정 시작
//-------------------------------------------------------
TLAreaBackgroundLayerBase.prototype.failedToLoadImage = function () {
	//if (TLG.COUNT_IMAGE_LOAD_AREA === 0) {
	//	this.retryImageloadArea();
	//}
	//TLEventManager.getInstance().signals.updateRender.dispatch();
};

TLAreaBackgroundLayerBase.prototype.loadedImage = function () {
	//TLEventManager.getInstance().signals.updateRender.dispatch();
};

// TLAreaBackgroundLayerBase.prototype.failedToLoadImage = function () {
// 	console.log(this.image.complete, this.image.naturalHeight, "failed to load image");
// };

//-------------------------------------------------------
//  Desc :
//-------------------------------------------------------
TLAreaBackgroundLayerBase.prototype.updateLayer = function (state) {
	TLSVGMatrixInfo.getInstance().setChangeLayer("NORMAL", state);
	TLSVGMatrixInfo.getInstance().setMapSize("NORMAL", this.mapSize);
	TLSVGMatrixInfo.getInstance().fullScreenSizeMap();
};

//-------------------------------------------------------
//  Desc :
//-------------------------------------------------------
TLAreaBackgroundLayerBase.prototype.updateLayerByBack = function (state) {
	TLSVGMatrixInfo.getInstance().setChangeLayer("BACK", state);
	TLSVGMatrixInfo.getInstance().setMapSize("BACK", this.mapSize);
	TLSVGMatrixInfo.getInstance().fullScreenSizeMapByBack();
};

//-------------------------------------------------------
//  Desc  :
//-------------------------------------------------------
TLAreaBackgroundLayerBase.prototype.setInitMatrix = function () {

};
//-------------------------------------------------------
//  Desc :
//-------------------------------------------------------
TLAreaBackgroundLayerBase.prototype.render = function (context) {
	context.drawImage(this.image, 0, 0);
	// 선택한 등급
	this.showBlockNoImage(context, 'fill');
	// 나머지 등급
	this.showBlockNoImage(context, 'stroke');
};


//-------------------------------------------------------
//  Desc  :  이미지 로드 여부
//-------------------------------------------------------
TLAreaBackgroundLayerBase.prototype.isImageReady = function () {
	return (this.image.complete && this.image.naturalHeight > 0);
};

//-------------------------------------------------------
//  Desc  :  전체 등급 블록
//-------------------------------------------------------
TLAreaBackgroundLayerBase.prototype.getAllBlocks = function () {
	var blockMap = [];//tk.state.plan.blockMap;
	var fullBlockArray = new Array();
	for (var key in blockMap) {
		var blockObject = [];//tk.state.plan.blockMap[key];
		fullBlockArray.push(blockObject);
	}
	return fullBlockArray;
};
TLAreaBackgroundLayerBase.prototype.showBlockNoImage = function (context, drawType) {
	var blockArray = drawType === 'stroke' ? this.getAllBlocks() : [];//tk.state.select.getSelectedBlocks().blocks;
	var selectedGrade = []; //tk.state.select.selectedGrade;
	var hasSelection = selectedGrade !== null && selectedGrade.hasOwnProperty('zones') && selectedGrade.zones.length > 0;
	if (!blockArray.length) {
		context.globalAlpha = 1.0;
		return;
	}

	context.save();
	context.globalAlpha = 1.0;
	context.beginPath();
	context.strokeStyle = '#000000';
	context.lineWidth = 5;
	context.lineCap = 'round';
	context.lineJoin = 'round';

	for (var idx = 0; idx < blockArray.length; idx++) {
		var blockObject = blockArray[idx];
		if (!TLSVGMatrixInfo.getInstance().isContainsPointInMap(this.mapSize,
			{
				x: blockObject.linkedPoint.x * this.areaMapScale,
				y: blockObject.linkedPoint.y * this.areaMapScale
			})) {
			continue;
		}
		//---------------------------------------------------------
		for (var i = 0; i < blockObject.cornerPoints.length; i++) {
			var point = blockObject.cornerPoints[i];
			if (i == 0) {
				context.moveTo(point.x * this.areaMapScale, point.y * this.areaMapScale);
			} else {
				context.lineTo(point.x * this.areaMapScale, point.y * this.areaMapScale);
				if (blockObject.cornerPoints.length - 1 === i) {
					context.lineTo(
						blockObject.cornerPoints[0].x * this.areaMapScale,
						blockObject.cornerPoints[0].y * this.areaMapScale);
				}
			}
		}
		//---------------------------------------------------------
	}
	if (hasSelection && drawType === 'fill') {
		context.fillStyle = selectedGrade.color;
		context.fill();
	}
	context.stroke();
	context.clip();
	context.restore();
	context.globalAlpha = 0.2;
};

TLAreaBackgroundLayerBase.prototype.showBlockLine = function (context) {
	var blockArray = [];//tk.state.select.getSelectedBlocks().blocks;
			// [예매대기] 신청가능한 block이 없는 경우는 전체 dimmed처리 되도록
	if (!blockArray.length) {
		context.globalAlpha = 1.0;
		return;
	}

	context.save();
	context.globalAlpha = 1.0;
	context.beginPath();
	context.strokeStyle = '#000000';
	context.lineWidth = 5;
	context.lineCap = 'round';
	context.lineJoin = 'round';

	for (var idx = 0; idx < blockArray.length; idx++) {
		var blockObject = blockArray[idx];
		if (!TLSVGMatrixInfo.getInstance().isContainsPointInMap(this.mapSize,
			{
				x: blockObject.linkedPoint.x * this.areaMapScale,
				y: blockObject.linkedPoint.y * this.areaMapScale
			})) {
			continue;
		}
		//---------------------------------------------------------
		for (var i = 0; i < blockObject.cornerPoints.length; i++) {
			var point = blockObject.cornerPoints[i];
			if (i == 0) {
				context.moveTo(point.x * this.areaMapScale, point.y * this.areaMapScale);
			} else {
				context.lineTo(point.x * this.areaMapScale, point.y * this.areaMapScale);
				if (blockObject.cornerPoints.length - 1 === i) {
					context.lineTo(
						blockObject.cornerPoints[0].x * this.areaMapScale,
						blockObject.cornerPoints[0].y * this.areaMapScale);
				}
			}
		}
		//---------------------------------------------------------
	}
	context.stroke();
	context.clip();
	context.drawImage(this.image, 0, 0);
	context.restore();
	context.globalAlpha = 0.2;
};

// [예매대기전용] 선택영역 색칠
TLAreaBackgroundLayerBase.prototype.showBlockFill = function (context) {
	var blockInfo = [];//tk.state.plan.blockInfo;
	var sectionInGrade = [];//tk.state.select.selectedSectionInBlockMap;
	var sectionArray = [];
	sectionInGrade.map(function (grade) {
		sectionArray = sectionArray.concat(grade.sections);
	});

	context.save();
	context.globalAlpha = 1.0;
	context.beginPath();
	context.strokeStyle = '#FFFFFF';
	context.lineWidth = 3;
	context.lineCap = 'round';
	context.lineJoin = 'round';

	for (var idx = 0; idx < sectionArray.length; idx++) {
		var blockObject = blockInfo.find(function(curBlock) {
			return curBlock.blockId === sectionArray[idx].blockId;
		});
		// if (!TLSVGMatrixInfo.getInstance().isContainsPointInMap(this.mapSize,
		// 	{
		// 		x: blockObject.linkedPoint.x * this.areaMapScale,
		// 		y: blockObject.linkedPoint.y * this.areaMapScale
		// 	})) {
		// 	continue;
		// }
		//---------------------------------------------------------

		var max = {x: -1, y: -1};
		var min = {x: 99999999, y: 99999999};

		for (var i = 0; i < blockObject.cornerPoints.length; i++) {
			var point = blockObject.cornerPoints[i];
			if (point.x > max.x) {
				max.x = point.x;
			}
			if (point.x < min.x) {
				min.x = point.x;
			}
			if (point.y > max.y) {
				max.y = point.y;
			}
			if (point.y < min.y) {
				min.y = point.y;
			}

			if (i == 0) {
				context.moveTo(point.x * this.areaMapScale, point.y * this.areaMapScale);
			} else {
				context.lineTo(point.x * this.areaMapScale, point.y * this.areaMapScale);
				if (blockObject.cornerPoints.length - 1 === i) {
					context.lineTo(
						blockObject.cornerPoints[0].x * this.areaMapScale,
						blockObject.cornerPoints[0].y * this.areaMapScale);
				}
			}
		}
	}

	context.fillStyle = '#ff8700';
	context.globalAlpha = 1;
	context.fill();
	context.stroke();
	context.restore();
};
var TLToolTipLayerBase = function () {
    this.toolTipCanvas = document.createElementNS('http://www.w3.org/1999/xhtml', 'canvas');
    TLDomInfo.getInstance().getDomElement().appendChild(this.toolTipCanvas);
    this.toolTipContext = this.toolTipCanvas.getContext('2d');
    this.toolTipCanvas.style.position = 'absolute';
    this.toolTipCanvas.width = TLDomInfo.getInstance().getWidth();
    this.toolTipCanvas.height = TLDomInfo.getInstance().getHeight();
    this.toolTipCanvas.style.zIndex = 5;
    //this.toolTipCanvas.style.display = 'none';
    this.textArray = null;
    this.mousePoint = new Vector2();

    this.toolTipContext.font = "bold 15px Dotum";
    this.toolTipContext.fillStyle = "rgba(0,0,0,0.7)";
};

TLToolTipLayerBase.prototype.setToolTip = function (textObj, evnet) {
    if (textObj === undefined) {
        this.textArray = null;
        this.toolTipCanvas.style.display = 'none';
        return;
    }
	//console.log(textObj,"textobj");
    this.toolTipCanvas.style.display = 'block';
    this.textArray = textObj;
    this.mousePoint.x = evnet.offsetX || (evnet.pageX - this.toolTipCanvas.offsetLeft);
    this.mousePoint.y = evnet.offsetY || (evnet.pageY - this.toolTipCanvas.offsetTop);
};

TLToolTipLayerBase.prototype.getTextArrayMaxSize = function (textArray) {
    var maxTextWidth = 0;
    for (var idx = 0; idx < textArray.length; idx++) {
        var text = textArray[idx];
        maxTextWidth = Math.max(maxTextWidth, this.toolTipContext.measureText(text).width);
    }
    return maxTextWidth;
};

TLToolTipLayerBase.prototype.render = function () {
    this.toolTipContext.clearRect(0, 0,
        this.toolTipCanvas.width, this.toolTipCanvas.height);
    this.drawToolTip();
};

TLToolTipLayerBase.prototype.drawToolTip = function () {
	//console.log(this.textArray)
    if (this.textArray === null) {
        return;
    }

    var widthTerm = 20;
    var heightTerm = 10;
    var textWidth = this.getTextArrayMaxSize(this.textArray) + widthTerm;
    var textHeight = 22;

    var width = Math.max(100, textWidth);
    var height = this.textArray.length * textHeight + heightTerm;
    var isRightOver = this.mousePoint.x + width > this.toolTipCanvas.width;
    var isTopOver = this.mousePoint.y - height < 0;
    var originX = this.mousePoint.x;
    var originY = this.mousePoint.y;
    var right = this.mousePoint.x + (isRightOver ? -1 * width : width);
    var top = this.mousePoint.y + (isTopOver ? height : -1 * height);
    var tailX = this.mousePoint.x + (isRightOver ? -10 : 10);
    var tailY = this.mousePoint.y + (isTopOver ? 7 : -7);
    var textLeft = isRightOver ? right + 10 : originX + 10;
    var textTop = top + (isTopOver ? -1 * 10 : 15);

    // Tooltip 박스
    this.toolTipContext.fillStyle = "rgba(0,0,0,0.7)";
    this.toolTipContext.beginPath();
    this.toolTipContext.moveTo(originX, originY);
    this.toolTipContext.lineTo(originX, top);
    this.toolTipContext.lineTo(right, top);
    this.toolTipContext.lineTo(right, tailY);
    this.toolTipContext.lineTo(tailX, tailY);
    //this.toolTipContext.closePath();
    this.toolTipContext.fill();

    // Tooltip 텍스트
    this.toolTipContext.fillStyle = "rgba(255,255,255, 1.0)";
    for (var idx = 0; idx < this.textArray.length; idx++) {
        var text = this.textArray[idx];
        var x = textLeft;
        var y = textTop + idx * (isTopOver ? -1 * textHeight : textHeight);
        this.toolTipContext.fillText(text, x, y);
    }
};
var TLLogicalSeatLayerBase = function () {
	
	var logical_tile_size = 256;
	var logigal_tile_intersect_space = 10;
	this.offScreenCanvas = document.createElementNS('http://www.w3.org/1999/xhtml', 'canvas');
	//this.offScreenCanvas.style.position = 'absolute';
	//TLDomInfo.getInstance().getDomElement().appendChild(this.offScreenCanvas);
	this.offScreenCanvas.width = logical_tile_size + logigal_tile_intersect_space * 2;
	this.offScreenCanvas.height = logical_tile_size + logigal_tile_intersect_space * 2;
	this.offScreenContext = this.offScreenCanvas.getContext('2d');

	this.tileImage = {};
	// 사석 이벤트
	this.defaultGradeColor = "rgba(255,255,0,1.0)";

	this.deadSeatIntervalID = null;
	this.deadSeatIntervalCount = 0;
};
TLLogicalSeatLayerBase.prototype.processSeats = async function (seatInfo, color) {
    var prevx = 0;
    var prevy = 0;

    // Clearing the off-screen canvas.
    this.offScreenContext.clearRect(0, 0, this.offScreenCanvas.width, this.offScreenCanvas.height);
    
    // Iterate through seats.
    for (var idx = seatInfo.length - 1; idx >= 0; idx--) {
        var seat = seatInfo[idx];

        var x = seat.area.virtualX * 256 - 10;
        var y = seat.area.virtualY * 256 - 10;

        if (prevx !== x || prevy !== y) {

            var tileImage = new Image();
            tileImage.src = this.offScreenCanvas.toDataURL();

            try {
                await new Promise((resolve, reject) => {
                    tileImage.onload = function () {
                        TLDomInfo.getInstance().context.drawImage(tileImage, prevx, prevy);
                        resolve();
                    };
                    tileImage.onerror = reject;  // Error handling
                });

                // Drawing logic...
                // Note: Ensure 'selectSeats' and 'gradeMap' are defined in your scope.
                var context = TLDomInfo.getInstance().context;
                context.fillStyle = '#000000';
                for (var key in selectSeats) {
                    context.beginPath();
                    var sss = selectSeats[key];
                    context.arc(sss.position.x, sss.position.y, 7, 0, 2 * Math.PI, false);
                    context.fill();
                }

                for (var key in selectSeats) {
                    var sss = selectSeats[key];
                    var gi = gradeMap[sss.gradeId];
                    context.beginPath();
                    context.fillStyle = gi ? gi.color : this.defaultGradeColor;
                    context.arc(sss.position.x, sss.position.y, 4, 0, 2 * Math.PI, false);
                    context.fill();
                }

            } catch (error) {
                console.error("Error loading or drawing image:", error);
            }

            prevx = x;
            prevy = y;
            this.offScreenContext.clearRect(0, 0, this.offScreenCanvas.width, this.offScreenCanvas.height);
        }

        // ... Drawing seat shapes.
        this.offScreenContext.beginPath();
        this.offScreenContext.moveTo(seat.cornerPoints.ne.x - x, seat.cornerPoints.ne.y - y);
        this.offScreenContext.lineTo(seat.cornerPoints.se.x - x, seat.cornerPoints.se.y - y);
        this.offScreenContext.lineTo(seat.cornerPoints.nw.x - x, seat.cornerPoints.nw.y - y);
        this.offScreenContext.lineTo(seat.cornerPoints.sw.x - x, seat.cornerPoints.sw.y - y);
        this.offScreenContext.lineTo(seat.cornerPoints.ne.x - x, seat.cornerPoints.ne.y - y);

        this.offScreenContext.fillStyle = color;
        this.offScreenContext.fill();
    }
    
    // Handle the final tile image after the loop.
    var tileImage = new Image();
    tileImage.src = this.offScreenCanvas.toDataURL();

    try {
        await new Promise((resolve, reject) => {
            tileImage.onload = function () {
                TLDomInfo.getInstance().context.drawImage(tileImage, prevx, prevy);
                resolve();
            };
            tileImage.onerror = reject;  // Error handling
        });
    } catch (error) {
        console.error("Error loading or drawing final image:", error);
    }
};
var TLToolTipLayer = Singletonify(TLToolTipLayerBase);
var TLAreaBackgroundLayer = Singletonify(TLAreaBackgroundLayerBase);
var TLLogicalSeatLayer = Singletonify(TLLogicalSeatLayerBase);
var TLSeatBackgroundLayerBase = function () {
	this.mapSize = 8192;
	this.center = {x: 4096, y: 4096}
	this.tileSize = 512;
	this.tileRadius = 363;
	this.imageUrl = '//seat_230330_{level}_{x}_{y}.png';
	this.lowLevelImage = null;
	this.singleImage = null;
	this.tileImage = {};
	this.currentTileImage = {};
	this.tileBGLoadedMap = {};
	for (var row = 0; row < 16; row++) {
		for (var col = 0; col < 16; col++) {
			var key = row.toString() + ':' + col.toString();
			this.tileBGLoadedMap[key] = false;
		}
	}
};
var setPlanState = function (state) {
	switch (state) {
		case "AREA":
			TLDomInfo.getInstance().status = "AREA";
			TLDomInfo.getInstance().areaCanvas.style.display = 'block';
			TLDomInfo.getInstance().canvas.style.display = 'none';
			TLSVGMatrixInfo.getInstance().setMoveBoundary();
			var center = TLAreaBackgroundLayer.getInstance().center;
			TLSVGMatrixInfo.getInstance().setWarpWorld("NORMAL", center.x, center.y);
			break;
		case "SEAT":
			TLDomInfo.getInstance().status = "SEAT";
			TLDomInfo.getInstance().areaCanvas.style.display = 'none';
			TLDomInfo.getInstance().canvas.style.display = 'block';
			TLSVGMatrixInfo.getInstance().setMoveBoundary();
			var center = TLSeatBackgroundLayer.getInstance().center;
			//console.log(center,"cc");
			TLSVGMatrixInfo.getInstance().setWarpWorld("NORMAL", center.x, center.y);
			
			break;
	}
};
async function  gotoSeatPlan (blockObj,seat,color) {
	seatInfo = seat;
	if(seatInfo.length>0){
		
	var vPos = {
		x: blockObj.linkedPoint.x,
		y: blockObj.linkedPoint.y,
	};

    var tlmatrix = TLSVGMatrixInfo.getInstance();
    tlmatrix.setChangeLayer("seat");
    tlmatrix.mapSize = 8192;
	tlmatrix.scale = 1;
	tlmatrix.fullScreenSizeMap2();

    tlmatrix.saveScaleAndPosition();
    TLDomInfo.getInstance().canvas.width = 680;
    TLDomInfo.getInstance().canvas.height = 604;
	TLDomInfo.getInstance().width = 680;
    TLDomInfo.getInstance().height = 604;
	setPlanState("SEAT");
	TLSVGMatrixInfo.getInstance().setMoveBoundary(blockObj.cornerPoints);
	TLSVGMatrixInfo.getInstance().setWarpSectionWorld(vPos, blockObj.vectorPoint);
	TLSeatBackgroundLayer.getInstance().pagingSectorDetectionBG();
	processTiles(seatInfo,color);
	
	var s2wBox = TLSVGMatrixInfo.getInstance().updateScreenToWorldBox();
	TLSVGMatrixInfo.getInstance().setMoveS2W_Boundary(s2wBox);
	}
	else{
		alert("예약 연습이 불가능한 좌석입니다.")
	}
};
function onResize () {
	TLDomInfo.getInstance().updateDomElement();
	var matrixInfo = TLSVGMatrixInfo.getInstance();
	matrixInfo.setKeepPosition(matrixInfo.getMatrix().e, matrixInfo.getMatrix().f);
	var termSize = 2;
	matrixInfo.mapBoundary.max.x = matrixInfo.mapBoundary.max.y = matrixInfo.mapSize + termSize;
	matrixInfo.updateSquareBoundary();

}
TLSeatBackgroundLayerBase.prototype.render = function (context) {
	processTiles(seatInfo);
};
TLSeatBackgroundLayerBase.prototype.pagingSectorDetectionBG = async function () {
	
};
function Vector2 (x, y) {

	this.x = x || 0;
	this.y = y || 0;

}
function Box2 (min, max) {

	this.min = ( min !== undefined ) ? min : new Vector2(+Infinity, +Infinity);
	this.max = ( max !== undefined ) ? max : new Vector2(-Infinity, -Infinity);

}
//-------------------------------------------------------
function render () {
	var p1 = TLSVGMatrixInfo.getInstance().transformedPoint(0, 0);
	var p2 = TLSVGMatrixInfo.getInstance().transformedPoint(
		TLDomInfo.getInstance().getWidth(),
		TLDomInfo.getInstance().getHeight());
	var PLAN_STATE = TLDomInfo.getInstance().status;
	switch (PLAN_STATE) {
		case "AREA":
			TLDomInfo.getInstance().areaContext.globalCompositeOperation = "source-over";
			TLDomInfo.getInstance().areaContext.clearRect(
				p1.x, p1.y, p2.x - p1.x, p2.y - p1.y);
			TLAreaBackgroundLayer.getInstance().render(TLDomInfo.getInstance().areaContext);
			break;
		case "SEAT":
			TLDomInfo.getInstance().context.globalCompositeOperation = "source-over";
			TLDomInfo.getInstance().context.clearRect(
				p1.x, p1.y, p2.x - p1.x, p2.y - p1.y);
			TLSeatBackgroundLayer.getInstance().render(TLDomInfo.getInstance().context);
			break;
	}

	var s2wBox = TLSVGMatrixInfo.getInstance().updateScreenToWorldBox();
};
var TLViewController = function (domElement) {
	var domElement = domElement;
	this.beforePoint = null;
	this.minDistance = 10;
	this.beforePinchTime = 0;
	this.minPinchTime = 30;
	var mc = new Hammer.Manager(domElement);
	mc.options.domEvents = true;
	var hmrPan = new Hammer.Pan({threshold: 0, direction: Hammer.DIRECTION_ALL});
	mc.add(hmrPan);
  domElement.addEventListener('mousewheel', this.handelMouseWheel.bind(this));
  domElement.addEventListener('mousemove', this.handelMouseMove.bind(this));
  domElement.addEventListener('click', this.onTap.bind(this));
	var scope = this;
	
	mc.on("press pressup", this.onTap.bind(this));
	mc.on("panstart panmove panend", this.onPan.bind(this));
};
TLViewController.prototype.onPan = function (ev) {
	if (TLSVGMatrixInfo.getInstance().defaultAction) {
		return;
	}
	if (ev.type === "panstart") {
		TLSVGMatrixInfo.getInstance().panStart(ev);
		this.setBeforePointWhenPanStart(ev);
	} else if (ev.type === "panmove") {

		//TLSVGMatrixInfo.getInstance().updateScreenToWorldBox();
		TLSVGMatrixInfo.getInstance().panMove(ev);
		//
	} else if (ev.type === "panend") {
		TLSVGMatrixInfo.getInstance().panEnd(ev);
		this.onTapAfterPanEnd(ev);
	}
};
var selectSeats = [];
TLLogicalSeatLayerBase.prototype.drawSelectedSeat = function (context) {
	//tk.state.select.selectedSeatMap = {}; // 선택된 좌석
	//tk.state.select.selectedZoneMap = {}; // 선택된 비지정석
	//console.log(selectSeats);
	context.fillStyle = '#000000';
	for (var key in selectSeats) {
		
		context.beginPath();
		var sss = selectSeats[key];
		context.arc(sss.position.x, sss.position.y, 7, 0, 2 * Math.PI, false);
		context.fill();
	}
	for (var key in selectSeats) {
		var sss = selectSeats[key];
		var gi = gradeMap[sss.gradeId];
		context.beginPath();
		context.fillStyle = gi ? gi.color : this.defaultGradeColor;
		context.arc(sss.position.x, sss.position.y, 4, 0, 2 * Math.PI, false);
		context.fill();
	}

};
TLViewController.prototype.onTap = function (event) {
	var state = TLDomInfo.getInstance().status;
	if(popupclickEnabled == true){
		stateChange("popup",false);
	}
	switch (state) {
		case "AREA":
			var blockObj = TLSVGMatrixInfo.getInstance().selectAreaDetection(
				TLAreaBackgroundLayer.getInstance().areaMapScale);
			if(blockObj)
			{
				stateChange("selectGradeMap",blockObj.grade);
				stateChange("selectBlock",blockObj);
				op();
				//stateChange("popup",true);
				//gotoSeatPlan(blockObj);
			}

			break;
		case "SEAT":
			var seatObj = TLSVGMatrixInfo.getInstance().selectSeatDetection();
			if(seatObj){
				if(selectSeats.length>0){
					if (selectSeats.includes(seatObj)) {
					selectSeats = selectSeats.filter(s => s !== seatObj);
					} else {
						selectSeats.push(seatObj);
					}
				}
				else{
					selectSeats.push(seatObj);
				}
				ss(selectSeats);
				processTiles(seatInfo);
			}
			//var seatInfo = TLSVGMatrixInfo.getInstance().selectSeatDetection();
			//var zoneInfo = TLSVGMatrixInfo.getInstance().selectZoneDetection();
			break;
	}
};

TLViewController.prototype.onPress = function (ev) {
	//console.log(ev)
	// console.log("press")
};

//-------------------------------------------------------
//  Desc : LG 최신 단말기 민감도로 인한 문제 때문에 추가 로직
//
//  Pan Start 때 이전 포인트를 저장(단, Pinch End 직후에는 저장하지 않는다.)
//-------------------------------------------------------
TLViewController.prototype.setBeforePointWhenPanStart = function (ev) {
	if (new Date().getTime() - this.beforePinchTime > this.minPinchTime) {
		this.beforePoint = ev.center;
	}
};

//-------------------------------------------------------
//  Desc : touchstart와 touchend Event에 대한 클릭이벤트 처리 로직
//  Pan Start 와 Pan End 의 거리차가 최소 거리차보다 작으면 Tap 으로 인지
//-------------------------------------------------------
TLViewController.prototype.onTapAfterPanEnd = function (ev) {
	
	if (!this.beforePoint) {
		return;
	}

	var dx = ev.center.x - this.beforePoint.x;
	var dy = ev.center.y - this.beforePoint.y;
	var distance = dx * dx + dy * dy;

	if (distance < this.minDistance) {
		TLViewController.prototype.onTap(ev);
	}
	this.beforePoint = null;
};
TLViewController.prototype.handelMouseWheel = function (event) {
	if (TLSVGMatrixInfo.getInstance().defaultAction) {
		return;
	}
	if (event.altKey) {
		
	} else {
		TLSVGMatrixInfo.getInstance().onZoom(event);
		//TLSeatBackgroundLayer.getInstance().pagingSectorDetectionBG();
    //TLSVGMatrixInfo.getInstance().pagingSectorDetection();
	}
	TLAreaBackgroundLayer.getInstance().setLayerInfo(blockBgInfo);
	//render();
	//processAreas();
};
function gradeSort(grades, isByGradeId) {
    if (!Array.isArray(grades)) {
      return [];
    }

    isByGradeId = isByGradeId === undefined ? false : isByGradeId;

    var sort = !isByGradeId ? compareForSort : compareForSortByGradeId;

    return grades.sort(sort);

    function compareForSort(first, second) {
      // 우선순위 순 정렬
      if (first.priority === second.priority) {
        // 이름 순 정렬
        if (first.name < second.name) return -1;
        if (second.name < first.name) return 1;
        return 0;
      } else if (first.priority < second.priority) {
        return -1;
      } else {
        return 1;
      }
    }

    function compareForSortByGradeId(first, second) {
      // 우선순위 순 정렬
      var firstGrade = gradeMap[first.gradeId];
      var secondGrade = gradeMap[second.gradeId];

      if (firstGrade === undefined) {
        return -1;
      }

      if (secondGrade === undefined) {
        return 1;
      }

      if (firstGrade.priority === secondGrade.priority) {
        // 이름 순 정렬
        if (firstGrade.name < secondGrade.name) return -1;
        if (secondGrade.name < firstGrade.name) return 1;
        return 0;
      } else if (firstGrade.priority < secondGrade.priority) {
        return -1;
      } else {
        return 1;
      }
    }
  }
function getBlockTooltip (block) {
	var tooltip = [block.blockName];
	var grades = block.grade;

	if (!Array.isArray(grades)) {
		return null;
	}

	grades = gradeSort(grades, true);
	//console.log(grades,"ss",gradeMap);
	for (var idx = 0; idx < grades.length; idx++) {
		var grade = grades[idx];
		var gradeInMap = gradeMap[grade.gradeId];
		//console.log(gradeInMap,"grmap")
		if (gradeInMap === undefined || gradeInMap.restriction) {
			continue;
		}

		var text = '';

		
		text = "[ " + gradeMap[grade.gradeId].name + "] ";
		tooltip.push(text);
	}

	if (tooltip.length === 1) {
		tooltip = null;
	}
	return tooltip;
}
function getSeatTooltip (seat) {
	var tooltip = ["[" + blockInfo.grade[0].name+ "]"];
	tooltip.push(seat.mapInfo)
	return tooltip;
}

//-------------------------------------------------------

TLViewController.prototype.handelMouseMove = function (event) {
	var PLAN_STATE = TLDomInfo.getInstance().status;
	if (TLSVGMatrixInfo.getInstance().defaultAction) {
		return;
	}

	TLSVGMatrixInfo.getInstance().mouseMove(event);
	switch (PLAN_STATE) {
		case "AREA":
			var blockObj = TLSVGMatrixInfo.getInstance().selectAreaDetection(
				TLAreaBackgroundLayer.getInstance().areaMapScale);
			//console.log(blockObj)
			TLToolTipLayer.getInstance().setToolTip(
				(blockObj ? getBlockTooltip(blockObj) : null), event);
				TLToolTipLayer.getInstance().render();
			break;
		case "SEAT":
			var seat= TLSVGMatrixInfo.getInstance().selectSeatDetection();
			
			TLToolTipLayer.getInstance().setToolTip(
				(seat ? getSeatTooltip(seat) : null), event);
				TLToolTipLayer.getInstance().render();
			//var zoneInfo = TLSVGMatrixInfo.getInstance().selectZoneDetection();
			//TLToolTipLayer.getInstance().setToolTip(
			//	(zoneInfo ? tk.controller.view.getZoneTooltip(zoneInfo) : null), event);
			break;
	}
};


var TLSVGMatrixInfoBase = function () {
	this.canvas = TLDomInfo.getInstance().canvas;
	this.context = TLDomInfo.getInstance().context;

	this.svg = document.createElementNS("http://www.w3.org/2000/svg", 'svg');
	this.svgMatrix = this.svg.createSVGMatrix();
	this.checkSvgMatrix = this.svg.createSVGMatrix();
	this.sectionWorldMatrix = this.svg.createSVGMatrix();
	this.pt = this.svg.createSVGPoint();

	this.svgMatrixScale = this.svg.createSVGMatrix();
	this.svgMatrixRotate = this.svg.createSVGMatrix();
	this.svgMatrixTransrate = this.svg.createSVGMatrix();

	this.wheelTime = null;
	this.worldScreenRadius = 0;
	this.worldCenterPosition = new Vector2();
	this.oldWorldCenterPosition = new Vector2();
	this.worldMousePosition = new Vector2();
	this.pickWorldPosition = new Vector2();
	this.basePosition = new Vector2();
	this.pickTermSpace = new Vector2();
	this.baseRotateDegree = 0;
	this.pickingPoint = new Vector2();
	this.position = new Vector2();

	this.baseScreenPosition = new Vector2();
	this.screenToWorldBox = {LT: 0, LB: 0, RT: 0, RB: 0};  //스크린box를 월드좌표로 변환한 박스.
	this.moveScreenToWorldBoundary = {
		LT: new Vector2(),
		LB: new Vector2(),
		RT: new Vector2(),
		RB: new Vector2()
	};

	//this.radian = 1.0471848490249274;
	this.radian = 0;
	this.baseScale = 0.33203125;
	//this.scale = 1.0;
	this.scale = 0.33203125;
	this.scaleMin = 0.5;
	this.scaleStaticMin = 0.166015625;
	this.scaleMax = 5.0;
	this.scaleStaticMax = 10.0;

	this.savedScale = 0.33203125;
	this.savedX = 0;
	this.savedY = 	0;

	this.startPan = false;
	this.outAccelerValue = -1.0;
	this.moveVector = new Vector2();
	this.moveBoundaryCenter = new Vector2();
	this.moveBoundary = new Box2();
	this.moveBoundaryRadius = 1024;
	this.screenBox = new Box2();
	this.screenBoundary = new Box2();
	this.screenBoundaryArray = [
		new Vector2(this.screenBoundary.min.x, this.screenBoundary.min.y), // LT
		new Vector2(this.screenBoundary.min.x, this.screenBoundary.max.y), // LB
		new Vector2(this.screenBoundary.max.x, this.screenBoundary.min.y), // RT
		new Vector2(this.screenBoundary.max.x, this.screenBoundary.max.y)  // RB
	];

	this.screenMinSize = 680;
	this.mapSize = 2048;
	this.mapBoundary = new Box2();
	this.mapBoundary.min.x = this.mapBoundary.min.y = 0;
	this.mapBoundary.max.x = this.mapBoundary.max.y = this.mapSize;
	this.cullingBoundary = {left: 0, top: 0, right: 0, bottom: 0};
	this.cullingBox = new Box2();

	this.defaultActionTime = 100;
	this.defaultAction = null;
	this.ticking = false;
	this.defaultTransform = {
		a: 1, b: 0, c: 0,
		d: 1, e: 0, f: 0
	};

	this.animationRenderFlag = false;

	var scope = this;

	document.addEventListener('keydown', onKeyDown);
	document.addEventListener('keyup', onKeyUp);

	function onKeyDown (event) {
		switch (event.keyCode) {
			case 32:	// Space
				break;
		}
	}

	function onKeyUp (event) {

	}
};
TLSVGMatrixInfoBase.prototype.gotoDefault = function() {
	this.wheelTime = null;
	this.worldScreenRadius = 0;
	this.worldCenterPosition = new Vector2();
	this.oldWorldCenterPosition = new Vector2();
	this.worldMousePosition = new Vector2();
	this.pickWorldPosition = new Vector2();
	this.basePosition = new Vector2();
	this.pickTermSpace = new Vector2();
	this.baseRotateDegree = 0;
	this.pickingPoint = new Vector2();
	this.position = new Vector2();

	this.baseScreenPosition = new Vector2();
	this.screenToWorldBox = {LT: 0, LB: 0, RT: 0, RB: 0};  //스크린box를 월드좌표로 변환한 박스.
	this.moveScreenToWorldBoundary = {
		LT: new Vector2(),
		LB: new Vector2(),
		RT: new Vector2(),
		RB: new Vector2()
	};

	//this.radian = 1.0471848490249274;
	this.radian = 0;
	this.baseScale = 0.33203125;
	//this.scale = 1.0;
	this.scale = 0.33203125;
	this.scaleMin = 0.5;
	this.scaleStaticMin = 0.166015625;
	this.scaleMax = 5.0;
	this.scaleStaticMax = 10.0;

	this.savedScale = 0.33203125;
	this.savedX = 0;
	this.savedY = 	0;

	this.startPan = false;
	this.outAccelerValue = -1.0;
	this.moveVector = new Vector2();
	this.moveBoundaryCenter = new Vector2();
	this.moveBoundary = new Box2();
	this.moveBoundaryRadius = 1024;
	this.screenBox = new Box2();
	this.screenBoundary = new Box2();
	this.screenBoundaryArray = [
		new Vector2(this.screenBoundary.min.x, this.screenBoundary.min.y), // LT
		new Vector2(this.screenBoundary.min.x, this.screenBoundary.max.y), // LB
		new Vector2(this.screenBoundary.max.x, this.screenBoundary.min.y), // RT
		new Vector2(this.screenBoundary.max.x, this.screenBoundary.max.y)  // RB
	];

	this.screenMinSize = 680;
	this.mapSize = 2048;
	this.mapBoundary = new Box2();
	this.mapBoundary.min.x = this.mapBoundary.min.y = 0;
	this.mapBoundary.max.x = this.mapBoundary.max.y = this.mapSize;
	this.cullingBoundary = {left: 0, top: 0, right: 0, bottom: 0};
	this.cullingBox = new Box2();

	this.defaultActionTime = 100;
	this.defaultAction = null;
	this.ticking = false;
	this.defaultTransform = {
		a: 1, b: 0, c: 0,
		d: 1, e: 0, f: 0
	};

	this.animationRenderFlag = false;

	var scope = this;
}
TLSVGMatrixInfoBase.prototype.selectSeatDetection = function (ev) {
	
	
	var row = parseInt(this.worldMousePosition.x / 256);
	var col = parseInt(this.worldMousePosition.y / 256);
	var key = row + ':' + col;
	for (var i = seatInfo.length - 1; i >= 0; i--) {
		var squaredLength = this.worldMousePosition.distanceToSquared(seatInfo[i].position);
		if (squaredLength < 64) {
			//console.log( seatInfo[i]);
			return seatInfo[i];
		}
	} 
	return null;
};
TLSVGMatrixInfoBase.prototype.setKeepPosition = function (x, y) {
	this.svgMatrix.e = x;
	this.svgMatrix.f = y;
	return this.context.setTransform(
		this.svgMatrix.a,
		this.svgMatrix.b,
		this.svgMatrix.c,
		this.svgMatrix.d,
		this.svgMatrix.e,
		this.svgMatrix.f);
};

TLSVGMatrixInfoBase.prototype.setMoveS2W_Boundary = function (boundary) {
	this.moveScreenToWorldBoundary = {
		LT: new Vector2(),
		LB: new Vector2(),
		RT: new Vector2(),
		RB: new Vector2()
	};

	this.moveScreenToWorldBoundary.LT.copy(boundary.LT);
	this.moveScreenToWorldBoundary.LB.copy(boundary.LB);
	this.moveScreenToWorldBoundary.RT.copy(boundary.RT);
	this.moveScreenToWorldBoundary.RB.copy(boundary.RB);
};
TLSVGMatrixInfoBase.prototype.updateSquareBoundary = function () {
	this.screenMinSize = TLDomInfo.getInstance().getWidth();
	//scale 의 min 값 도출.
	//this.screenMinSize = Math.min(TLDomInfo.getInstance().getWidth(),
	//    TLDomInfo.getInstance().getHeight());

	// 화면보다 mapSize 가 작을 경우 scaleMin의 범위는 0.5 ~ 1.0 사이.

	if (TLDomInfo.getInstance().canvas.style.display === "block") {
		this.scaleMin = Math.max(0.5, Math.min(1.0, this.screenMinSize / this.mapSize));
	} else {
		
			this.screenMinSize = TLDomInfo.getInstance().getWidth();
			if (this.scale < this.screenMinSize / this.mapSize) {
				this.scaleMin = this.scale;
			} else {
				this.scaleMin = this.screenMinSize / this.mapSize;
			}
	}
};
var getNormal2Radian = function (normal) {

	var normalVector = {x: normal.x, y: normal.y};
	//노멀벡터 검증은 패스
	//var normalVector = new THREE.Vector2(normal.x, normal.y);
	//normalVector.normalize();
	//normalVector.x = normalVector.x.toFixed(4);
	//normalVector.y = normalVector.y.toFixed(4);

	var zeroPoint = {x: 0, y: 0};
	var dx = normalVector.x - zeroPoint.x;
	var dy = normalVector.y - zeroPoint.y;

	var startRadian = Math.PI * 0.5; // 90도 기준
	var radian = Math.atan2(dy, dx) - startRadian;
	//var degree = radian*180/Math.PI ;
	//console.log("degree : %f", degree);

	// 라디안은 절대 건드리지 않는다 만약 건드린다면 노멀벡터가 변형된다.
	// 아래처럼 사용하면 X
	// radian = radian.toFixed(4);

	return radian;
};

TLSVGMatrixInfoBase.prototype.setWarpSectionWorld = function (vPos, vNormal) {
	var domWidth = TLDomInfo.getInstance().getWidth();
	var domHeight = TLDomInfo.getInstance().getHeight();
	//console.log(domWidth,domHeight);
	var vPivot = {
		x: domWidth,
		y: domHeight,
	};

	
	vPivot.x = domWidth * 0.5;
	vPivot.y = domHeight * 0.5;
	this.radian = getNormal2Radian(vNormal);
	this.setAffineTransform(this.scale, this.radian, vPos, vPivot);

	this.worldCenterPosition.copy(this.transformedPoint(
		this.canvas.width * 0.5,
		this.canvas.height * 0.5));
	this.worldScreenRadius = this.worldCenterPosition.distanceTo(this.transformedPoint(0, 0));
	//console.log(this.worldCenterPosition,this.worldScreenRadius,"dd")
	this.updateScreenToWorldBox();
	//console.log(this,"DD")
};
var ptInPolygon = function (cornerArray, point) {
	var polygonCorners = cornerArray.length;
	var j = polygonCorners - 1;
	var oddNodes = false;

	for (var i = 0; i < polygonCorners; i++) {
		if ((cornerArray[i].y < point.y && cornerArray[j].y >= point.y
			|| cornerArray[j].y < point.y && cornerArray[i].y >= point.y)
			&& (cornerArray[i].x <= point.x || cornerArray[j].x <= point.x)) {
			if (cornerArray[i].x + (point.y - cornerArray[i].y) /
				(cornerArray[j].y - cornerArray[i].y) *
				(cornerArray[j].x - cornerArray[i].x) < point.x) {
				oddNodes = !oddNodes;
			}
		}
		j = i;
	}
	return oddNodes;
};
//----------------------------------------------
TLSVGMatrixInfoBase.prototype.isContainsPointInMap = function (mapSize, point) {
	return point.x < 0 || point.x > mapSize ||
	point.y < 0 || point.y > mapSize ? false : true;
};
TLSVGMatrixInfoBase.prototype.selectAreaDetection = function (scale, ev) {
	// [예매대기전용] 구역형일때 선택 불가능하게 prefix
	// if (tk.utils.isWaitingReservation()) {
	// 	if (tk.state.waitingDetail.useGradeSelect) {
	// 		// return;
	// 	}
	// }

	if (ev != undefined) {
		// 모바일 일때.
		this.worldMousePosition = this.transformedPoint(ev.center.x,
			ev.center.y - TLDomInfo.getInstance().getDomElement().offsetTop);
	}
	// 영역 겹침 처리를 위해서 역순으로 확인
	// 나중에 생긴 영역의 Id 값이 먼저 생긴 영역의 Id 보다 작다.
	var blocks = blockInfo;
	for (var blockIdx = blocks.length - 1; blockIdx > -1; blockIdx--) {
		var blockObj = blocks[blockIdx];
		// 맵영역 안쪽 영역 오브젝트만 체킹한다.------------------
		if (!this.isContainsPointInMap(this.mapSize,
			{
				x: blockObj.linkedPoint.x * scale,
				y: blockObj.linkedPoint.y * scale
			})) {
			continue;
		}
		//-------------------------------------------
		if (ptInPolygon(blockObj.cornerPoints, {
			x: this.worldMousePosition.x / scale,
			y: this.worldMousePosition.y / scale
		})) {
			
			//console.log(blockObj);
			return blockObj;
		}
	}
	return null;
};
TLSVGMatrixInfoBase.prototype.setChangeLayer = function ( state) {
	switch (state) {
		case "area":
			this.canvas = TLDomInfo.getInstance().areaCanvas;
			this.context = TLDomInfo.getInstance().areaContext;
			break;
		case "seat":
			this.canvas = TLDomInfo.getInstance().canvas;
			this.context = TLDomInfo.getInstance().context;
			break;
	}
}
TLSVGMatrixInfoBase.prototype.translate = function (dx, dy) {
	this.svgMatrix = this.svgMatrix.translate(dx, dy);
	return this.context.translate(dx, dy);
};
TLSVGMatrixInfoBase.prototype.onZoom = function (ev) {
	var delta = 0;
	if (ev.wheelDelta !== undefined) {
		// WebKit / Opera / Explorer 9
		delta = ev.wheelDelta;

	} else if (ev.detail !== undefined) {
		// Firefox
		delta = -ev.detail * 2;
	}

	if (new Date() - this.wheelTime > 100) {
		//console.log(ev.pageX,"EVPAGEX")
		var lastX = ev.offsetX || (ev.pageX - this.canvas.offsetLeft);
		var lastY = ev.offsetY || (ev.pageY - this.canvas.offsetTop);
		this.baseScale = this.scale;
		this.basePosition = this.transformedPoint(lastX, lastY);

		this.pickTermSpace.x = lastX;
		this.pickTermSpace.y = lastY;
		this.pickWorldPosition.copy(this.worldMousePosition);

	}

	this.scale = Math.max(this.scaleMin, Math.min(this.scaleMax, this.baseScale + (this.baseScale * delta * 0.0002)));
	this.setAffineTransform(this.scale, this.radian, {x: this.pickWorldPosition.x, y: this.pickWorldPosition.y}, this.pickTermSpace);
	//this.translate(this.pickWorldPosition.x, this.pickWorldPosition.y);


	//this.updateSquareBoundary();
	//this.updateWorldMatrix();
	this.baseScale = this.scale;
	this.wheelTime = new Date();
	this.worldCenterPosition.x = this.pickTermSpace.x;
	this.worldCenterPosition.y = this.pickTermSpace.y;
	this.worldCenterPosition.copy(this.transformedPoint(
		this.canvas.width * 0.5,
		this.canvas.height * 0.5));
	//this.worldScreenRadius =  454.7570746033647; //this.worldCenterPosition.distanceTo(this.transformedPoint(0, 0));
	render();
};
TLSVGMatrixInfoBase.prototype.panStart = function (ev, isDomEvent) {
	this.startPan = true;
	if (isDomEvent) {
		this.wheelTime = 0;
		var lastX = ev.offsetX || (ev.srcEvent.pageX - this.canvas.offsetLeft);
		var lastY = ev.offsetY || (ev.srcEvent.pageY - this.canvas.offsetTop);
		this.baseScreenPosition.set(lastX, lastY);
		this.basePosition = this.transformedPoint(lastX, lastY);
		//TLCheckBoundary.getInstance().isPanStart(lastX, lastY);
	} else {
		//console.log("xx")
		//console.log(ev);
		this.baseScreenPosition.set(ev.deltaX, ev.deltaY);
		this.basePosition = this.transformedPoint(ev.deltaX, ev.deltaY);
		//TLCheckBoundary.getInstance().isPanStart(ev.deltaX, ev.deltaY);
	}
};

TLSVGMatrixInfoBase.prototype.panMove = function (ev, isDomEvent) {
	if (!this.startPan) {
		//var lastX = ev.offsetX || (ev.pageX - this.canvas.offsetLeft);
		//var lastY = ev.offsetY || (ev.pageY - this.canvas.offsetTop);
		//this.worldMousePosition.copy(this.transformedPoint(lastX, lastY));
		return false;
	}
	if (isDomEvent) {
		//console.log("pt mvoe")
		var pt = this.transformedPoint(ev.srcEvent.pageX, ev.srcEvent.pageX);
		var moveVector = {x: pt.x - this.basePosition.x, y: pt.y - this.basePosition.y};
		//console.log(this.updateMoveBoundary(moveVector.x, moveVector.y));
		if (!this.updateMoveBoundary(moveVector.x, moveVector.y)) {
			var accelerValue = this.outAccelerValue > 0 ? 50 / this.outAccelerValue : 1;
			this.translate(moveVector.x * accelerValue, moveVector.y * accelerValue);
			//return;
		} else {
			//console.log("hihi")
			this.translate(moveVector.x, moveVector.y);
		}
		//this.updateSquareBoundary();
		//this.updateWorldMatrix();
	} else {
		var pt = this.transformedPoint(ev.deltaX, ev.deltaY);
		//console.log(ev);
		var moveVector = {x: pt.x - this.basePosition.x, y: pt.y - this.basePosition.y};
		//console.log(pt,"sec")
		//console.log(this.basePosition.x,this.basePosition.y,"base")
		//console.log(moveVector)
		//TLCheckBoundary.getInstance().isPanMove(lastX, lastY);
		//TLCheckBoundary.getInstance().isPanMove(ev.deltaX, ev.deltaY);
		if (!this.updateMoveBoundary(moveVector.x, moveVector.y)) {
			var accelerValue = this.outAccelerValue > 0 ? 50 / this.outAccelerValue : 1;
			this.translate(moveVector.x * accelerValue, moveVector.y * accelerValue);
			//return;
		} else {
			this.translate(moveVector.x, moveVector.y);
		}
		//this.updateSquareBoundary();
		//this.updateWorldMatrix();
	}
	this.worldCenterPosition.copy(this.transformedPoint(
		this.canvas.width * 0.5,
		this.canvas.height * 0.5));
	this.worldScreenRadius = this.worldCenterPosition.distanceTo(this.transformedPoint(0, 0));
	var PLAN_STATE = TLDomInfo.getInstance().status;
	if (blockBgInfo && blockBgInfo.center ) {
		
		//console.log(blockBgInfo.center,"center")
		//console.log(this.basePosition,"base")
        //blockBgInfo.center.x = this.basePosition.x + moveVector.x;
        //blockBgInfo.center.y = this.basePosition.y + moveVector.y;
        render();
    }
};

TLSVGMatrixInfoBase.prototype.panEnd = function (ev, isDomEvent) {
	this.basePosition.copy(this.position);
	this.startPan = false;

	if (this.outAccelerValue > 0) {
		this.setDefaultAction({
			target: this.oldWorldCenterPosition,
			startTime: new Date()
		});
		
	}

};
TLSVGMatrixInfoBase.prototype.setDefaultAction = function (param) {
	this.defaultAction = requestAnimationFrame(function () {
		TLSVGMatrixInfo.getInstance().setDefaultAction(param);
	});

	// 위치 보간,
	if (typeof (param.target) === 'object') {
		var t = (new Date() - param.startTime) / this.defaultActionTime;
		//var vOri = new Vector2(this.getMatrix().e, this.getMatrix().f);
		var vOri = this.worldCenterPosition;
		var vPos = this.lerpVector2(vOri, param.target, t);
		if (t > 1.0) {
			vPos = param.target;
			cancelAnimationFrame(this.defaultAction);
			this.defaultAction = null;
		}
		this.setWarpWorld("NORMAL", vPos.x, vPos.y);
		//this.translate(pt.x - this.basePosition.x, pt.y - this.basePosition.y);
		//this.updateSquareBoundary();
		//this.updateWorldMatrix();
		this.updateScreenToWorldBox();
		TLSVGMatrixInfo.getInstance().updateScreenToWorldBox();
		//blockBgInfo.center = vOri;
		///alert(vOri.x,vOri.y,"ff");
	}
	// scale 보간.
	else {
		var t = (new Date() - param.startTime) / this.defaultActionTime;
		var scale = this.lerpScale(this.scale, param.target, t);
		if (t > 1.0) {
			scale = param.target;
			this.scale = param.target;
			cancelAnimationFrame(this.defaultAction);
			this.defaultAction = null;
		}
		this.translate(this.basePosition.x, this.basePosition.y);
		this.setScale(scale, scale);
		this.translate(-this.basePosition.x, -this.basePosition.y);
		//this.updateWorldMatr	ix();
		TLSVGMatrixInfo.getInstance().updateScreenToWorldBox();
		//alert(vPos.x,vPos.y);
		
	}
};

TLSVGMatrixInfoBase.prototype.setWarpWorld = function (eventType, x, y) {
	var vPosition = {
		x: x,
		y: y,
	};
	var vPivot = {
		x: 0,
		y: 0,
	};
	var domWidth = TLDomInfo.getInstance().getWidth();
	var domHeight = TLDomInfo.getInstance().getHeight();

	if (eventType === "NORMAL") {
		vPivot.x = domWidth * 0.5;
		vPivot.y = domHeight * 0.5;
	} else if (eventType === "BACK") {
		vPosition.x = this.savedX;
		vPosition.y = this.savedY;
	}

	this.setAffineTransform(this.scale, this.radian, vPosition, vPivot);
	this.worldCenterPosition.copy(this.transformedPoint(
		this.canvas.width * 0.5,
		this.canvas.height * 0.5));
	this.worldScreenRadius = this.worldCenterPosition.distanceTo(this.transformedPoint(0, 0));
	this.updateScreenToWorldBox();
};
TLSVGMatrixInfoBase.prototype.setScale = function (sx, sy) {
	this.svgMatrix.a = Math.cos(this.radian) * sx;
	this.svgMatrix.b = Math.sin(this.radian) * sy;
	this.svgMatrix.c = -Math.sin(this.radian) * sx;
	this.svgMatrix.d = Math.cos(this.radian) * sy;

	//this.svgMatrixScale.a = Math.cos(this.radian) * sx;
	//this.svgMatrixScale.b = Math.sin(this.radian) * sy;
	//this.svgMatrixScale.c = -Math.sin(this.radian) * sx;
	//this.svgMatrixScale.d = Math.cos(this.radian) * sy;
	//this.svgMatrix = this.svgMatrixScale.multiply(this.svgMatrix);

	this.context.setTransform(
		this.svgMatrix.a, this.svgMatrix.b, this.svgMatrix.c,
		this.svgMatrix.d, this.svgMatrix.e, this.svgMatrix.f);
};
TLSVGMatrixInfoBase.prototype.setTransform = function (a, b, c, d, e, f) {
	this.svgMatrix.a = a;
	this.svgMatrix.b = b;
	this.svgMatrix.c = c;
	this.svgMatrix.d = d;
	this.svgMatrix.e = e;
	this.svgMatrix.f = f;
	return this.context.setTransform(a, b, c, d, e, f);
};
var TLCheckBoundaryBase = function () {
	this.canvas = TLDomInfo.getInstance().checkCanvas;
	this.context = TLDomInfo.getInstance().checkContext;

	this.svg = document.createElementNS("http://www.w3.org/2000/svg", 'svg');
	this.checkMatrix = this.svg.createSVGMatrix();
	this.scaleMatrix = this.svg.createSVGMatrix();
	this.translateMatrix = this.svg.createSVGMatrix();

	this.baseScreenPosition = new Vector2(0, 0);
	this.worldMousePos = new Vector2();
	this.pickingPos = new Vector2();
	this.checkAABB = new Box2();
	this.pt = this.svg.createSVGPoint();
	this.scale = 1.0;
	this.position = new Vector2();
	this.movePos = new Vector2();
};

TLCheckBoundaryBase.prototype.setPickingPos = function (x, y) {
	this.pickingPos.copy(this.transformedPoint(x, y));
};

TLCheckBoundaryBase.prototype.setWorldMousePos = function (x, y) {
	this.worldMousePos.copy(this.transformedPoint(x, y));
};

TLCheckBoundaryBase.prototype.transformedPoint = function (x, y) {
	if (this.checkMatrix.a === 0 || this.checkMatrix.d === 0) {
		return new Vector2();
	}
	this.pt.x = x;
	this.pt.y = y;

	var vResult = this.pt.matrixTransform(this.checkMatrix.inverse());
	return new Vector2(vResult.x, vResult.y);
};

TLCheckBoundaryBase.prototype.setAffineTransform = function (scale, vPivot) {
	this.scaleMatrix.a = scale;
	this.scaleMatrix.d = scale;

	this.translateMatrix.e = -this.pickingPos.x;
	this.translateMatrix.f = -this.pickingPos.y;

	this.checkMatrix = this.scaleMatrix.multiply(this.translateMatrix);

	// 결국 pivot은 스크린 이동.
	this.checkMatrix.e += vPivot.x;
	this.checkMatrix.f += vPivot.y;

	return this.context.setTransform(
		this.checkMatrix.a,
		this.checkMatrix.b,
		this.checkMatrix.c,
		this.checkMatrix.d,
		this.checkMatrix.e,
		this.checkMatrix.f);
};


TLCheckBoundaryBase.prototype.updateAABB = function (box, radius, radian) {
	//console.log(Math.cos(radian))
	var size = box.getSize();
	var x = Math.max(size.x, size.y);
	var y = Math.min(size.x, size.y);

	this.checkAABB.setFromCenterAndSize(new Vector2(x, y), box.getSize());
	// console.log(this.checkAABB)
	//this.checkAABB
};

TLCheckBoundaryBase.prototype.isPanStart = function (x, y) {
	this.baseScreenPosition = this.transformedPoint(x, y);
};


TLCheckBoundaryBase.prototype.render = function () {

	this.context.strokeStyle = '#00FF00';
	this.context.lineWidth = 4;
	this.context.lineCap = 'round';
	this.context.lineJoin = 'round';

	var p1 = this.transformedPoint(0, 0);
	var p2 = this.transformedPoint(
		TLDomInfo.getInstance().getWidth(),
		TLDomInfo.getInstance().getHeight());
	this.context.clearRect(p1.x, p1.y, p2.x - p1.x, p2.y - p1.y);

	var vSize = this.checkAABB.getSize();
	this.context.strokeRect(this.checkAABB.min.x, this.checkAABB.min.y,
		vSize.y, vSize.x);

	//this.context.strokeRect(0, 0, this.canvas.width, this.canvas.height);
};

var TLCheckBoundary = Singletonify(TLCheckBoundaryBase);

TLSVGMatrixInfoBase.prototype.transformedPoint = function (x, y) {
	if (this.svgMatrix.a === 0 || this.svgMatrix.d === 0) {
		return new Vector2();
	}
	this.pt.x = x;
	this.pt.y = y;

	var vResult = this.pt.matrixTransform(this.svgMatrix.inverse());
	return new Vector2(vResult.x, vResult.y);
};

TLSVGMatrixInfoBase.prototype.mouseMove = function (event) {
	var lastX = event.offsetX || (event.pageX - this.canvas.offsetLeft);
	var lastY = event.offsetY || (event.pageY - this.canvas.offsetTop);
	this.worldMousePosition = this.transformedPoint(lastX, lastY);
  //console.log(this.worldMousePosition);
  //console.log(this);
	//TLCheckBoundary.getInstance().setWorldMousePos(lastX, lastY);
	return this.worldMousePosition;
};
TLSVGMatrixInfoBase.prototype.updateScreenToWorldBox = function () {

	var domInfo = TLDomInfo.getInstance();
	this.screenToWorldBox.LT = this.transformedPoint(0, 0);
	this.screenToWorldBox.LB = this.transformedPoint(0, domInfo.getHeight());
	this.screenToWorldBox.RT = this.transformedPoint(domInfo.getWidth(), 0);
	this.screenToWorldBox.RB = this.transformedPoint(domInfo.getWidth(), domInfo.getHeight());

	return this.screenToWorldBox;
};
TLSVGMatrixInfoBase.prototype.lerpScale = function (ori, dest, t) {
	var result = ori + t * (dest - ori);
	return result;
};

TLSVGMatrixInfoBase.prototype.lerpVector2 = function (vOri, vDest, t) {
	//vOri + t*(vDest-vOri)
	var vResult = new Vector2(0, 0);
	vResult.x = vOri.x + t * (vDest.x - vOri.x);
	vResult.y = vOri.y + t * (vDest.y - vOri.y);
	return vResult;
};

TLSVGMatrixInfoBase.prototype.setAffineTransform = function (scale, radian, vPosition, vPivot) {
	//console.log(scale,radian,vPosition,vPivot)
	//this.scale = scale;
	//this.radian = radian;
	//this.position = vPosition;

//	this.svgMatrixScale.a = scale;
//	this.svgMatrixScale.d = scale;

	this.svgMatrixScale.a = scale;
	this.svgMatrixScale.d = scale;

	this.svgMatrixRotate.a = Math.cos(radian);
	this.svgMatrixRotate.b = Math.sin(radian);
	this.svgMatrixRotate.c = -Math.sin(radian);
	this.svgMatrixRotate.d = Math.cos(radian);

	this.svgMatrix = this.svgMatrixScale.multiply(this.svgMatrixRotate);

	this.svgMatrixTransrate.e = -vPosition.x;
	this.svgMatrixTransrate.f = -vPosition.y;

	// 시행착오를 격지 않도록 해당부분 주석으로 처리 ------------------------------------------------------------
	//this.svgMatrixTransrate.e = -vPosition.x + vPivot.x / scale;
	//this.svgMatrixTransrate.f = -vPosition.y + vPivot.y / scale;

	//this.svgMatrixTransrate.e = vPosition.x + (vPosition.x * Math.cos(radian) + vPosition.y * Math.sin(radian));
	//this.svgMatrixTransrate.f = vPosition.y + (vPosition.x * Math.sin(radian) - vPosition.y * Math.cos(radian));

	//var termX = -(-vPivot.x * Math.cos(radian) + vPivot.y * Math.sin(radian) ) / scale;
	//var termY = -(-vPivot.x * Math.sin(radian) - vPivot.y * Math.cos(radian) ) / scale;
	//console.log("vPivot : %d, %d", vPivot.x/scale, vPivot.y/scale)
	//console.log("term : %d, %d", termX, termY)
	//this.svgMatrixTransrate.e = -vPosition.x + termX;
	//this.svgMatrixTransrate.f = -vPosition.y + termY;
	//-------------------------------------------------------------------------------------------------

	this.svgMatrix = this.svgMatrix.multiply(this.svgMatrixTransrate);

	// 결국 pivot은 스크린 이동.
	this.svgMatrix.e += vPivot.x;
	this.svgMatrix.f += vPivot.y;

	return this.context.setTransform(
		this.svgMatrix.a,
		this.svgMatrix.b,
		this.svgMatrix.c,
		this.svgMatrix.d,
		this.svgMatrix.e,
		this.svgMatrix.f);
};
TLSVGMatrixInfoBase.prototype.setMapSize = function (eventType, mapSize) {
	var termSize = 0;
	this.mapSize = mapSize;
	this.mapBoundary.min.x = this.mapBoundary.min.y = -termSize;
	this.mapBoundary.max.x = this.mapBoundary.max.y = this.mapSize + termSize;
};
TLSVGMatrixInfoBase.prototype.fullScreenSizeMap = function () {
  this.screenMinSize = 680;
  this.scaleMin = 0.33203125;
  this.scaleStaticMin = this.scaleMin * 0.5;
  var vCenter = new Vector2(
    TLDomInfo.getInstance().getWidth() * 0.5,
    TLDomInfo.getInstance().getHeight() * 0.5);
  this.setAffineTransform(this.scale, this.radian, this.worldCenterPosition, vCenter);
  this.worldScreenRadius = this.worldCenterPosition.distanceTo(this.transformedPoint(0, 0));
  this.updateScreenToWorldBox();
  //console.log(this);
};
TLSVGMatrixInfoBase.prototype.fullScreenSizeMap2 = function () {
	this.screenMinSize = 680;
	this.scaleMin = 0.33203125;
	this.scaleStaticMin = this.scaleMin * 0.5;
	var vCenter = new Vector2(
	  TLDomInfo.getInstance().getWidth() * 0.5,
	  TLDomInfo.getInstance().getHeight() * 0.5);
	this.setAffineTransform(this.scale, this.radian, this.worldCenterPosition, vCenter);
	this.worldScreenRadius = this.worldCenterPosition.distanceTo(this.transformedPoint(0,0));
	this.updateScreenToWorldBox();
	//console.log(this);
  };
TLSVGMatrixInfoBase.prototype.getMatrix = function () {
	return this.svgMatrix;
};
TLSVGMatrixInfoBase.prototype.setMoveBoundary = function (cornerPoints) {
	this.outAccelerValue = -1.0;
	if (cornerPoints === undefined) {
		this.moveBoundary.min = new Vector2(0, 0);
		this.moveBoundary.max = new Vector2(this.mapSize, this.mapSize);
		//console.log(this.mapSize,"mapsize")
		//this.moveBoundaryRadius = this.moveBoundary.getCenter().distanceTo(this.moveBoundary.min);
		this.moveBoundaryRadius = this.mapSize * 0.5;
		this.moveBoundaryCenter.copy(this.moveBoundary.getCenter());
		return;
	}

	var length = cornerPoints.length;
	if (!length) {
		return;
	}
	this.moveBoundary.min.x = cornerPoints[0].x;
	this.moveBoundary.min.y = cornerPoints[0].y;
	this.moveBoundary.max.x = cornerPoints[0].x;
	this.moveBoundary.max.y = cornerPoints[0].y;
	for (var idx = 0; idx < cornerPoints.length; idx++) {
		var point = cornerPoints[idx];
		this.moveBoundary.min.x = Math.min(this.moveBoundary.min.x, point.x);
		this.moveBoundary.min.y = Math.min(this.moveBoundary.min.y, point.y);
		this.moveBoundary.max.x = Math.max(this.moveBoundary.max.x, point.x);
		this.moveBoundary.max.y = Math.max(this.moveBoundary.max.y, point.y);
	}
	// radius 도출.
	this.moveBoundaryRadius = 1.0;
	for (var idx = 0; idx < cornerPoints.length; idx++) {
		var point = cornerPoints[idx];
		this.moveBoundaryRadius = Math.max(this.moveBoundaryRadius,
			this.moveBoundary.getCenter().distanceTo(new Vector2(point.x, point.y)));
	}
	//this.moveBoundaryRadius *= 1.2;
	this.moveBoundaryCenter.copy(this.moveBoundary.getCenter());
};
//-------------------------------------------------------
//  Desc  : 이동가능한 바운더리 감지.
//-------------------------------------------------------
TLSVGMatrixInfoBase.prototype.updateMoveBoundary = function (x, y) {
	//console.log("%x, %y", x, y);
	var PLAN_STATE = TLDomInfo.getInstance().status;
	var BACKGROUND_TYPE = "BG_SECTION_TILE"
	//console.log(this.moveBoundaryCenter);
	//console.log(this.worldCenterPosition);
	var squaredLength = this.moveBoundaryCenter.distanceToSquared(this.worldCenterPosition);
	//console.log(squaredLength,this.moveBoundaryRadius,"sL")
	this.outAccelerValue = squaredLength - (this.moveBoundaryRadius * this.moveBoundaryRadius);
	//console.log(this.outAccelerValue);
	if (this.outAccelerValue >= 0) {
		return false;
	}
	if (PLAN_STATE === "SEAT" && BACKGROUND_TYPE === "BG_SECTION_TILE") {
		this.oldWorldCenterPosition.copy(this.worldCenterPosition);
		this.moveVector.set(x, y);
		this.sectionWorldMatrix.e = x;
		this.sectionWorldMatrix.f = y;
	} else {
		this.oldWorldCenterPosition.copy(this.worldCenterPosition);
	}

	return true;
};

//-------------------------------------------------------
//  Desc  : 화면에 꽉차게 만들고 센터정렬한다.
//-------------------------------------------------------
TLSVGMatrixInfoBase.prototype.saveScaleAndPosition = function () {
	var pt = this.transformedPoint(this.canvas.offsetWidth, this.canvas.offsetHeight);
	this.savedX = pt.x;
	this.savedY = pt.y;
	this.savedScale = this.scale;
};

var TLSeatBackgroundLayer = Singletonify(TLSeatBackgroundLayerBase);
var TLSVGMatrixInfo = Singletonify(TLSVGMatrixInfoBase);
function stateChange(){

}
function op(){

}
function ss(){

}
function st(){

}
async function getSeatInfo(blockId,gradeId) {
  try {
    const response = await axios.get(`/ticketing/api/seat/?blockId=${blockId}&gradeId=${gradeId}`); // API 엔드포인트 및 매개변수에 맞게 수정
    return response.data;
  } catch (error) {
    console.error('Error fetching seat info:', error);
    throw error; // 오류 처리를 원하는 방식으로 수정
  }
}
function setjsToReact(rstateChange){
	//console.log(rstateChange);
	stateChange = rstateChange;
}
function setop(func){
	op = func;
}
function setss(func){
	ss = func;
}
function setst(func){
	st = func;
}
async function processAreas() {
	selectSeats = [];
	var tlmatrix = TLSVGMatrixInfo.getInstance();
	tlmatrix.gotoDefault();
    tlmatrix.setChangeLayer("area");
	var p1 = TLSVGMatrixInfo.getInstance().transformedPoint(0, 0);
	var p2 = TLSVGMatrixInfo.getInstance().transformedPoint(
		TLDomInfo.getInstance().getWidth(),
		TLDomInfo.getInstance().getHeight());
	TLDomInfo.getInstance().areaContext.globalCompositeOperation = "source-over";
		TLDomInfo.getInstance().areaContext.clearRect(
			p1.x, p1.y, p2.x - p1.x, p2.y - p1.y);
	
	var center = TLAreaBackgroundLayer.getInstance().center;
	//console.log(center);
	tlmatrix.worldCenterPosition.x = 1024;
    tlmatrix.worldCenterPosition.y = 1024;
    tlmatrix.fullScreenSizeMap();
	
	TLAreaBackgroundLayer.getInstance().setLayerInfo(blockBgInfo);
	
	await new Promise((resolve, reject) => {
		TLAreaBackgroundLayer.getInstance().image.onload = function() {
			TLAreaBackgroundLayer.getInstance().render(TLDomInfo.getInstance().areaContext);
			resolve();
		};
		TLAreaBackgroundLayer.getInstance().image.onerror = reject;  // Error handling
	});
	TLDomInfo.getInstance().areaCanvas.style.display = 'block';
	TLDomInfo.getInstance().canvas.style.display = 'none';
	TLAreaBackgroundLayer.getInstance().updateLayer();
}
async function processTiles(seatInfo,color) {
	var tsbl = TLSeatBackgroundLayer.getInstance();
	var tlmatrix = TLSVGMatrixInfo.getInstance();
	//console.log(tsbl,"tsbl");
	//console.log(tlmatrix,"tlmatrix");
	//console.log(tlmatrix.worldCenterPosition);
    const keys = Object.keys(tsbl.tileBGLoadedMap);
    for (const key of keys) {
        tsbl.tileImage[key] = new Image();
        var rowColArray = key.split(':', 2);
        var row = parseInt(rowColArray[0]);
        var col = parseInt(rowColArray[1]);
        var x = row * tsbl.tileSize + tsbl.tileSize * 0.5;
        var y = col * tsbl.tileSize + tsbl.tileSize * 0.5;
        var sumRadiusSquared = (tlmatrix.worldScreenRadius + tsbl.tileRadius);
        sumRadiusSquared *= sumRadiusSquared;
        var squaredLength = tlmatrix.worldCenterPosition.distanceToSquared({x: x, y: y});
        if (squaredLength < sumRadiusSquared) {
            //console.log(key)
            tsbl.tileBGLoadedMap[key] = true;
            var replaceTileNumber =  row + '_' + col;
            var tileImageUrl = tsbl.imageUrl.replace("{x}_{y}", replaceTileNumber);
            tsbl.tileImage[key].src = tileImageUrl;
            tsbl.currentTileImage[key] = tsbl.tileImage[key];
            tsbl.tileImage[key].tilePosition = {x: row * tsbl.tileSize, y: col * tsbl.tileSize};

            await new Promise((resolve, reject) => {
                tsbl.tileImage[key].onload = function() {
                    TLDomInfo.getInstance().context.drawImage(this, this.tilePosition.x, this.tilePosition.y);
                    resolve();
                };
                tsbl.tileImage[key].onerror = reject;  // Error handling
            });
        }
    }
	TLLogicalSeatLayer.getInstance().processSeats(seatInfo,color);
	TLDomInfo.getInstance().areaCanvas.style.display = 'none';
	TLDomInfo.getInstance().canvas.style.display = 'block';
	st();
}
var popupclickEnabled = false;
class Container extends Component {
  constructor(props) {
    super(props);
    this.timerInterval = null;
  }
  state = {
	score : 1,
    randomobj : [],
    canvasRef : React.createRef(),
	state : "area",
	gradeMap : [],
	selectGradeId : 0, 
	selectBlockMap : [],
	selectGradeMap : [],
	popup : false,
	selectBlock : [],
	selectSeat : [],
	time : 1000,
	istimer : false,
	scale : 1.0,
	isEnd : false,
  };

  static propTypes = {
    getRandomTicketLink : PropTypes.func.isRequired,
    randomobj : PropTypes.array.isRequired,
  };
   filterBlocksByGrade(jsonData, gradeId) {
	const filteredBlocks = jsonData.filter(block => {
	  return block.grade.some(grade => grade.gradeId == gradeId);
	});
  
	const result = filteredBlocks.map(block => {
	  return {
		block
	  };
	});
  
	return result;
  }
  seatSelect = (selectseat) => {
	this.setState({ selectSeat : selectseat });
  }
  allView = (e) =>{
	setPlanState("AREA");
    processAreas();
	TLSVGMatrixInfo.getInstance().setMoveBoundary();
  }
  selectGrade = (e,gradeId) => {
	if(this.state.selectGradeId!=gradeId){
		this.setState({
			selectBlockMap : [],
		})
	}
	this.setState({
		selectGradeId : gradeId
	})
  }
  componentWillReceiveProps = nextProps => {
    if(nextProps.randomobj ){
        this.setState({
			randomobj : nextProps.randomobj.random_seat.block
        })
		blockInfo = nextProps.randomobj.random_seat.block;
		blockBgInfo.imageUrlThumnail = nextProps.randomobj.random_seat.img;
		TLSeatBackgroundLayer.getInstance().imageUrl = nextProps.randomobj.random_seat.img.split("images/")[0] + "images/" +  nextProps.randomobj.random_seat.eng + "/seat_{x}_{y}.png";
		setjsToReact(this.stateChange);
		setop(this.openPopup);
		setss(this.seatSelect);
		setst(this.startTimer);
		gotoSeatPlan(nextProps.randomobj.random_seat.block,nextProps.randomobj.random_seat.seat,nextProps.randomobj.random_seat.block.grade[0].color);
		//processTiles()
		TLSVGMatrixInfo.getInstance().setMoveBoundary();
  	}
  };
  tileBGLoadedMap = {

  }
  startTimer = () => {
	if(!this.state.istimer){
		this.timerInterval = setInterval(this.updateElapsedTime, 10);
		this.setState({istimer: true});
	}
  }
  stopTimer = () => {
	if (this.state.istimer) {
		//console.log(this.timerInterval);
	  clearInterval(this.timerInterval);
	  this.setState({ istimer: false });
	}
  }
  updateElapsedTime = () => {
	if(this.state.time>=0){
		this.setState({ time : this.state.time - 1});
	}
	else{
		clearInterval(this.timerInterval);
		this.setState({ istimer: false });
		alert("[게임 오버]\n 최종 LV "+ this.state.score+" 단계");
		window.location = "/physical"
	}
  };
  popupClose = () => {
    popupclickEnabled = false;
	this.setState({
		popup: false,
	})
  }
  openPopup = () => {
    this.setState({ popup: true });
    setTimeout(() => {
		popupclickEnabled = true;
    }, 50);
  };
  clickStart = () => {
	this.startTimer();
  }
  clickNext = () => {
	if(this.state.selectSeat.length==seatInfo.length){
		this.stopTimer();
		this.setState({
			time : this.state.time + (this.state.selectSeat.length * 100),
			selectSeat : [],
			score : this.state.score + 1,
		})
		selectSeats = [];
		const {getRandomTicketLink } = this.props;
		getRandomTicketLink();
	}
	else{
		alert("모든 좌석을 선택해야 합니다.")
	}
  }
  clickReplay = () => {
	
	this.setState({
		canvasRef : React.createRef(),
		state : "area",
		selectGradeId : 0, 
		selectBlockMap : [],
		selectGradeMap : [],
		popup : false,
		selectBlock : [],
		selectSeat : [],
		time : 0,
		isEnd : false,
	})
	setPlanState("AREA");
    processAreas();
	TLSVGMatrixInfo.getInstance().setMoveBoundary();
  }
   handleResize = () => {
	var updatedScale = window.innerHeight / 990;
	if(updatedScale<1.0){
		this.setState({
			scale : updatedScale
		})
	}
	else{
		this.setState({
			scale : 1.0,
		})
	}
};
  //https://image.toast.com/aaaaab/ticketlink/TKL_CONCERT/new_twins_seat_23(0512)_4
  componentWillUnmount() {
	window.removeEventListener('resize', this.handleResize);
  }
  componentDidMount() {
	const {getRandomTicketLink } = this.props;
	getRandomTicketLink();
	document.title = 'T사 피지컬 연습';
	
  
	this.handleResize(); // 컴포넌트가 마운트되었을 때 초기 크기 계산을 합니다.
  
	window.addEventListener('resize', this.handleResize); // 리사이즈 이벤트 리스너를 추가합니다.
	
  };
  render() {
    return (
      <TranomdomGame startTimer={this.startTimer} clickStart={this.clickStart} clickReplay={this.clickReplay} clickNext={this.clickNext} allView={this.allView} {...this.state} {...this.props} popupClose={this.popupClose} btnBlockClick={this.btnBlockClick} selectGrade={this.selectGrade} btnGradeClick={this.btnGradeClick} />
    );
  }
}

export default Container;