module.exports = {
  publicPath: './',
  outputDir: '../app/templates',
  assetsDir: process.env.NODE_ENV === 'production' ? '../app/static' : ''
}