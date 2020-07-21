const phantom = require('phantom');

(async function() {
    const instance = await phantom.create();
    const page = await instance.createPage();

    await page.open("https://www.newseum.org/todaysfrontpages/")
    const tfpData = await page.evaluate(function() {
        return JSON.stringify(window.TFP_DATA)
    })
    console.log(tfpData)

    await instance.exit();
})();
