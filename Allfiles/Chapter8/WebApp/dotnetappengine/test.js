

var system = require('system');
var host = system.env['CASPERJS11_URL'];

casper.test.begin('Hello World home page returns 200.', 1, function suite(test) {
    casper.start(host + '/', function (response) {
        test.assertEquals(200, response.status);
    });
    
    casper.run(function () {
        test.done();
    });
});