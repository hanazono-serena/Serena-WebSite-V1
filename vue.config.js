module.exports = {
    productionSourceMap: process.env.NODE_ENV !== 'production',
    chainWebpack: config => {
        config.plugin('html').tap(options => {
            if (process.env.NODE_ENV === 'production') {
                options[0].minify.removeComments = false;
                options[0].minify.collapseWhitespace = false;
            }
            return options
        })
    }
}