// vue.config.js
module.exports = {
  chainWebpack: config => {
    config.plugin('define').tap(definitions => {
      definitions[0]['process.env']['__VUE_OPTIONS_API__'] = true;
      definitions[0]['process.env']['__VUE_PROD_DEVTOOLS__'] = false;
      return definitions;
    });
  }
}