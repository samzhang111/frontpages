var jsdom = require("jsdom");

jsdom.env({
   url: 'http://www.newseum.org/todaysfrontpages/',
   done: function(err, window){
       console.log(JSON.stringify(window.TFP_DATA));
       window.close();
   },
   features: {
       FetchExternalResources: ['script'],
       ProcessExternalResources: ['script'],
       SkipExternalResources: false}
   }
);
