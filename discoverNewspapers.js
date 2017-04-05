var jsdom = require("jsdom");

jsdom.env({
   url: 'http://www.newseum.org/todaysfrontpages/',
   done: function(err, window){
       window.TFP_DATA.papers.map(function(paper) {
           console.log(paper.links.pdf);
       });
       window.close();
   },
   features: {
       FetchExternalResources: ['script'],
       ProcessExternalResources: ['script'],
       SkipExternalResources: false}
   }
);
