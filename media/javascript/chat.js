function entsub(myform) {
	if (window.event.keyCode == 13)
		{
		sendmessage();
		return false;
		}
}
var MyWebSocket = {
	ws : null,
	timer : null,
	init: function(){
		var that = this;
		var resource = document.getElementsByName('resource')[0].value;
		that.connect(resource);		
	},
	
	connect : function(resource) {
		if(this.ws)
			this.ws.close();		
		this.ws = new WebSocket("ws://109.74.198.181:4000/"+resource);

		var that = this;
		
		this.ws.onopen = function(e) {
			//document.getElementById('board').innerHTML = '<b>connect succeed : '+resource+'</b><br/>';
			document.getElementsByName('send')[0].disabled = false;
			document.getElementsByName('message')[0].disabled = false;
			document.getElementsByName('disconnect')[0].disabled = false;
			document.getElementsByName('connect')[0].disabled = true;
			document.getElementsByName('resource')[0].disabled = true;
			document.getElementsByName('username')[0].disabled = true;
		}
		
		this.ws.onmessage = function(e) {
			var nd = document.createElement('div');
			nd.setAttribute('class', 'messbody');
			nd.innerHTML = e.origin + decodeURIComponent(e.data);
			document.getElementById('board').insertBefore(nd);
			document.getElementById('board').scrollTop = document.getElementById('board').scrollHeight;
		};
		this.ws.onclose = function(e) {
			if(that.timer) {
				clearInterval(that.timer);
				that.timer = null;
			}
			var nd = document.createElement('div');
			nd.innerHTML = 'closed';
			document.getElementById('board').insertBefore(nd, document.getElementById('board').firstChild);
			document.getElementsByName('send')[0].disabled = true;
			document.getElementsByName('message')[0].disabled = true;
			document.getElementsByName('connect')[0].disabled = false;
			document.getElementsByName('disconnect')[0].disabled = true;
			document.getElementsByName('resource')[0].disabled = false;
		};
				
		this.timer = setInterval(function(){
			that.ws.send('Heartbeat');
		}, 60000);

	},
	
	send: function(message){
		if(!this.ws) return;
				
		if(typeof(message) == 'undefined' || message =='') {
			alert('not found Message...');
			return;
		}
		
		// this.ws.send(encodeURIComponent(message));
		this.ws.send(message);
		///////////////////////////////////////////////////
		// 2010/01/08 prevent encodeURLComponent
		// since websocket is designed to communicate
		// with utf-8.
		// text-frame = (%x00) *( UTF8-char ) %xFF
		//  
		// http://tools.ietf.org/html/
		//             draft-hixie-thewebsocketprotocol-68#page-6
		//
		// URLencode encodes UTF8-char to ascii character.
		// for example, 'あ' is encoded to '%E3%81%82'.
		// in this case, these encoded string consume 9 byetes.
		// however, 'あ' is 3 bytes in native utf-8 (%xe3%x81%x82).
		// therefore, sending messages in utf-8 ( don't use
		// encodeURIComponent ) may be reasonable to keep
		// network traffic lower and make shortage of messaging
		// delay.
		///////////////////////////////////////////////////
		document.getElementsByName('message')[0].value = '';
	},
	
	close : function() {
		if(this.ws) {
			this.ws.close();
		}
	}
};
	window.addEventListener('load', function(e){
	MyWebSocket.init();
}, false);
	function sendmessage() {
	message = document.getElementsByName('message')[0].value;
	name = document.getElementsByName('username')[0].value;
	MyWebSocket.send('<strong>' + name + ': '+ '</strong>' + message);
}

window.addEventListener('unload', function(e) {
	MyWebSocket.close();
}, false);

