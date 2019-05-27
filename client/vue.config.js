module.exports = {
  publicPath: './',
  outputDir: '../aita/templates',
  assetsDir: process.env.NODE_ENV === 'production' ? '../static' : ''
}