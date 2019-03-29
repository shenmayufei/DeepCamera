var request = require('request')

var object_detection_task_url = 'http://127.0.0.1:3000/api/post?url='

//var test_urls = ['/data/data/com.termux/files/home/sharpai/src/yolo_detector/frame_18012019_010702_639.jpg']

var	test_urls = ['/data/data/com.termux/files/home/sharpai/src/yolo_detector/frame_18012019_011011_296.jpg']

test_urls.forEach(function(item){
	request({
	    url: object_detection_task_url+item,
	    method: "GET"
	}, function (error, response, body){
	    //console.log(response)
	    if(error) {
	        console.log(error)
	    } else {
	        console.log(body)
      }
	})
})